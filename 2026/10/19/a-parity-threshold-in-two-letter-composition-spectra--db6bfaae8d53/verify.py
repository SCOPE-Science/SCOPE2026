#!/usr/bin/env python3
"""Exact polynomial and independent finite checks for the pair-composition theorem.

Requires only Python 3 and its standard library. Run: python3 verify.py
"""
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial


def trim(a):
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a


def add(a,b):
    r=[0]*max(len(a),len(b))
    for j,c in enumerate(a):r[j]+=c
    for j,c in enumerate(b):r[j]+=c
    return trim(r)


def scale(a,k):
    return trim([k*v for v in a])


def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return trim(r)


def power(a,n):
    r=[1]
    for _ in range(n):r=mul(r,a)
    return r


def prod(seqs):
    r=[1]
    for a in seqs:r=mul(r,a)
    return r


def part(items):
    """Each set partition is emitted exactly once."""
    if not items:
        yield ()
    else:
        head,*tail=items
        for p in part(tail):
            yield ((head,),)+p
            for i in range(len(p)):
                z=list(p)
                z[i]=(head,)+z[i]
                yield tuple(z)


def simple_parity(s):
    """Polynomials for simple graphs with zero and two odd vertices."""
    edges=list(combinations(range(s),2))
    out={0:[0]*(len(edges)+1),2:[0]*(len(edges)+1)}
    for bits in product((0,1),repeat=len(edges)):
        odd=[0]*s
        for bit,(a,b) in zip(bits,edges):
            if bit:odd[a]^=1;odd[b]^=1
        k=sum(odd)
        if k in out:out[k][sum(bits)]+=1
    return {k:trim(p) for k,p in out.items()}


def conn_num(s):
    """Connected/parity-admissible numerator over (1-t)^s(1-t^2)^E."""
    p={d:simple_parity(d) for d in range(1,s+1)}
    total=[0]; edge_count=comb(s,2)
    for blocks in part(list(range(s))):
        sizes=[len(b) for b in blocks]
        parity0=prod([p[d][0] for d in sizes])
        parity2=[0]
        for i,d in enumerate(sizes):
            parity2=add(parity2,prod([p[v][2] if j==i else p[v][0]
                                       for j,v in enumerate(sizes)]))
        term=add(parity0,parity2)
        cross=edge_count-sum(comb(d,2) for d in sizes)
        term=mul(term,power([1,0,-1],cross))
        mu=(-1)**(len(sizes)-1)*factorial(len(sizes)-1)
        total=add(total,scale(term,mu))
    return total


def rational_check():
    t=[0,1];one_minus_t=[1,-1];one_plus_t=[1,1]
    Cnums={1:[1],2:[0,1],3:[0,0,3,-2],
           4:mul([0,0,0,1],[12,27,0,-47,-2,30,0,-6])}
    Cdens={1:power(one_minus_t,1),2:power(one_minus_t,3),
           3:power(one_minus_t,6),
           4:mul(power(one_minus_t,10),power(one_plus_t,4))}
    for s in range(1,5):
        generic_den=mul(power(one_minus_t,s),power([1,0,-1],comb(s,2)))
        assert mul(conn_num(s),Cdens[s])==mul(Cnums[s],generic_den),s
    common=Cdens[4]
    numerator=scale(common,-4)
    for s in range(1,5):
        factor=prod([power(one_minus_t,10-(1 if s==1 else 3 if s==2 else 6 if s==3 else 10)),
                     power(one_plus_t,4-(4 if s==4 else 0))])
        numerator=add(numerator,scale(mul(Cnums[s],factor),comb(4,s)))
    Q=[10,-26,22,85,-120,-23,178,-126,-70,128,-30,-30,20,-4]
    assert numerator==mul(t,Q), (numerator,mul(t,Q))
    assert sum(Q)==14
    return Q


def euler_profile_count(q,m):
    pairs=list(combinations_with_replacement(range(q),2))
    c=0
    def gen(j,rem,weights):
        nonlocal c
        if j==len(pairs)-1:
            weights=weights+(rem,)
            parity=[0]*q; seen=set();adj=[set() for _ in range(q)]
            for (a,b),w in zip(pairs,weights):
                if w:
                    seen.update((a,b))
                    if a!=b:
                        parity[a]^=w%2;parity[b]^=w%2
                        adj[a].add(b);adj[b].add(a)
            if sum(parity)>2:return
            marked={min(seen)};stack=list(marked)
            for v in stack:
                for w in adj[v]:
                    if w not in marked:
                        marked.add(w);stack.append(w)
            if marked==seen:c+=1
            return
        for w in range(rem+1):gen(j+1,rem-w,weights+(w,))
    gen(0,m,())
    return c


def word_profile_count(q,n):
    types=list(combinations_with_replacement(range(q),2))
    index={e:j for j,e in enumerate(types)}
    seen=set()
    for word in product(range(q),repeat=n):
        v=[0]*len(types)
        for a,b in zip(word,word[1:]):v[index[tuple(sorted((a,b)))]]+=1
        seen.add(tuple(v))
    return len(seen)


def from_rational(Q,m_max):
    den=mul(power([1,-1],10),power([1,1],4))
    num=mul([0,1],Q)
    ar=[0]*(m_max+1)
    for m in range(1,m_max+1):
        ar[m]=(num[m] if m<len(num) else 0)-sum(
            den[j]*ar[m-j] for j in range(1,min(m,len(den)-1)+1))
    return ar


def main():
    Q=rational_check()
    got=from_rational(Q,12)
    expected=[10,34,116,367,1060,2782,6704,14963,31276,61738,116020]
    assert got[1:12]==expected,(got[1:12],expected)
    for q in range(2,5):
        for m in range(1,9):
            independent=euler_profile_count(q,m)
            if q==4:assert independent==got[m],(q,m,independent,got[m])
            if q**(m+1)<=65536:
                observed=word_profile_count(q,m+1)
                assert observed==independent,(q,m,observed,independent)
    print('ALL EXACT POLYNOMIAL AND INDEPENDENT FINITE CHECKS PASSED')
    print('Quaternary profile counts for m=1,...,11:',expected)
    print('All-q asymptotic follows from the proved parity-map and connectivity lemmas.')


if __name__=='__main__':main()
