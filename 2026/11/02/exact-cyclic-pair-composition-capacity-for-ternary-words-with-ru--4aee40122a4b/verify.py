#!/usr/bin/env python3
"""Independent finite checks for cyclic pair-composition profiles with triple runs forbidden.

Pure Python 3, standard library only.  Finite tests supplement, but do not replace,
the general Euler-circuit and rational generating-function proof.
"""
from collections import defaultdict
from itertools import product
import random

PAIRS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}


def mul_poly(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def rational_coefficients(max_n):
    # z^2 P(z)/((1-z)^6(1+z)^3(1+z^2)^2(1+z+z^2)^2).
    p = [3, 4, 2, -1, 1, 1, 5, 4, -1, -1, -4, 0, 1, 1, 1, -1]
    num = [0, 0] + p
    den = [1]
    for fac, exponent in [([1,-1],6), ([1,1],3), ([1,0,1],2), ([1,1,1],2)]:
        for _ in range(exponent):
            den = mul_poly(den,fac)
    assert den[0] == 1
    a = []
    for n in range(max_n+1):
        v = (num[n] if n<len(num) else 0)
        v -= sum(den[j]*a[n-j] for j in range(1, min(n,len(den)-1)+1))
        a.append(v)
    return a


def profile_of_word(w):
    n = len(w)
    if any(w[i] == w[(i+1)%n] == w[(i+2)%n] for i in range(n)):
        return None
    c = [0]*6
    for i in range(n):
        c[PAIR_INDEX[tuple(sorted((w[i],w[(i+1)%n])))]] += 1
    return tuple(c)


def brute_profile_count(n):
    return len({p for w in product(range(3), repeat=n)
                if (p := profile_of_word(w)) is not None})


def dp_profile_count(n):
    # Independent incremental word enumeration merging identical partial profiles.
    if n<2:
        return 0
    found = set()
    for a,b in product(range(3), repeat=2):
        c0 = [0]*6
        c0[PAIR_INDEX[tuple(sorted((a,b)))]] += 1
        dp = {(a,b,tuple(c0))}
        for _ in range(2,n):
            nxt = set()
            for prevprev,prev,c in dp:
                for v in range(3):
                    if prevprev == prev == v:
                        continue
                    cc = list(c)
                    cc[PAIR_INDEX[tuple(sorted((prev,v)))]]+=1
                    nxt.add((prev,v,tuple(cc)))
            dp = nxt
        for prevprev,prev,c in dp:
            if prevprev == prev == a or prev == a == b:
                continue
            cc = list(c)
            cc[PAIR_INDEX[tuple(sorted((prev,a)))]] += 1
            found.add(tuple(cc))
    return len(found)


def is_valid_histogram(q, hist):
    deg = [0]*q
    adj = {i: set() for i in range(q)}
    for i in range(q):
        for j in range(i+1,q):
            t=hist.get((i,j),0)
            deg[i]+=t
            deg[j]+=t
            if t:
                adj[i].add(j)
                adj[j].add(i)
    active = [i for i in range(q) if deg[i]>0]
    if len(active)<2 or any(deg[i]%2 for i in range(q)):
        return False
    if any(hist.get((i,i),0)>deg[i]//2 for i in range(q)):
        return False
    visited={active[0]}
    todo=[active[0]]
    while todo:
        v=todo.pop()
        for w in adj[v]-visited:
            visited.add(w)
            todo.append(w)
    return set(active)==visited


def construct_word(q, hist):
    assert is_valid_histogram(q,hist)
    # Multiedge multiplicities, implemented with a matrix for reliable edge consumption.
    counts = [[0]*q for _ in range(q)]
    for (i,j),val in hist.items():
        if i<j:
            counts[i][j]=counts[j][i]=val
    start=next(i for i in range(q) if sum(counts[i])>0)
    stack=[start]
    tour=[]
    while stack:
        v=stack[-1]
        nxt=next((w for w in range(q) if counts[v][w]),None)
        if nxt is None:
            tour.append(stack.pop())
        else:
            counts[v][nxt]-=1
            counts[nxt][v]-=1
            stack.append(nxt)
    tour=tour[::-1]
    assert tour[0]==tour[-1]
    visits={i:[] for i in range(q)}
    out=list(tour[:-1])
    for idx,i in enumerate(out):
        visits[i].append(idx)
    repeat=set()
    for i in range(q):
        repeat.update(visits[i][:hist.get((i,i),0)])
    word=tuple(v for j,x in enumerate(out) for v in ((x,x) if j in repeat else (x,)))
    assert len(word)==sum(hist.values())
    assert not any(word[k]==word[(k+1)%len(word)]==word[(k+2)%len(word)]
                   for k in range(len(word)))
    h2=defaultdict(int)
    for k in range(len(word)):
        i,j=sorted((word[k],word[(k+1)%len(word)]))
        h2[i,j]+=1
    assert all(h2.get(k,0)==hist.get(k,0) for k in set(h2)|set(hist))
    return word


def independent_formula_counts(max_n):
    # Compute the positive-coefficient parametrization via truncated generating
    # function products, independent of rational numerator/denominator arithmetic.
    result=[0]*(max_n+1)
    for eps in (0,1):
        for u in range((max_n-3*eps)//2+1):
            for v in range((max_n-3*eps-2*u)//2+1):
                for w in range((max_n-3*eps-2*u-2*v)//2+1):
                    if eps==0 and u==v==w==0:
                        continue
                    m=3*eps+2*(u+v+w)
                    poly=[1]
                    for d in (u+v+eps,u+w+eps,v+w+eps):
                        poly=mul_poly(poly,[1]*(d+1))
                    for offset,val in enumerate(poly):
                        if m+offset<=max_n:
                            result[m+offset]+=val
    return result



def histogram_set(q, n):
    pairs = [(i,j) for i in range(q) for j in range(i,q)]
    idx = {pair:k for k,pair in enumerate(pairs)}
    profiles = set()
    for w in product(range(q), repeat=n):
        if any(w[i] == w[(i+1)%n] == w[(i+2)%n] for i in range(n)):
            continue
        c=[0]*len(pairs)
        for i in range(n):
            c[idx[tuple(sorted((w[i],w[(i+1)%n])))]]+=1
        profiles.add(tuple(c))
    return profiles


def all_histograms(q, n):
    pairs = [(i,j) for i in range(q) for j in range(i,q)]
    def rec(k, left, prefix):
        if k == len(pairs)-1:
            c = prefix+[left]
            hist=dict(zip(pairs,c))
            if is_valid_histogram(q,hist):
                yield tuple(c)
            return
        for v in range(left+1):
            yield from rec(k+1,left-v,prefix+[v])
    return set(rec(0,n,[]))

def random_constructions():
    rng=random.Random(241119)
    for q in (3,4,5,7):
        for _ in range(500):
            # Connected even-degree cross multigraph by adding closed walks.
            mat=[[0]*q for _ in range(q)]
            for i in range(q):
                j=(i+1)%q
                mat[i][j]+=1
                mat[j][i]+=1
            for _ in range(rng.randint(0,15)):
                i,j=rng.sample(range(q),2)
                mat[i][j]+=2
                mat[j][i]+=2
            degree=[sum(mat[i]) for i in range(q)]
            h={(i,j):mat[i][j] for i in range(q) for j in range(i+1,q)}
            h.update({(i,i):rng.randint(0,degree[i]//2) for i in range(q)})
            construct_word(q,h)


def main():
    a=rational_coefficients(45)
    assert a[:19]==[0,0,3,7,12,21,41,63,99,149,219,309,432,582,783,1029,1332,1701,2161]
    for n in range(1,11):
        assert brute_profile_count(n)==a[n], (n,brute_profile_count(n),a[n])
    for n in range(2,19):
        assert dp_profile_count(n)==a[n],(n,dp_profile_count(n),a[n])
    # Exhaustively compare the general graph criterion against literal words.
    for q, nmax in ((2,9),(3,10),(4,7),(5,5)):
        for n in range(2,nmax+1):
            assert all_histograms(q,n)==histogram_set(q,n), (q,n)
    b=independent_formula_counts(45)
    assert b==a
    random_constructions()
    print('PASS: brute words n=1..10; independent profile DP n=2..18;')
    print('PASS: exact graph criterion q=2..5, lengths through 9/10/7/5;')
    print('PASS: positive parametric enumeration n=0..45;')
    print('PASS: 2,000 constructed general-alphabet Euler tours (q=3,4,5,7).')
    print('C_2..C_18:',a[2:19])

if __name__=='__main__':
    main()
