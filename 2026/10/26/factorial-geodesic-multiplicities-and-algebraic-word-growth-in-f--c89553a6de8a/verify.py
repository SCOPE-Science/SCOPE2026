#!/usr/bin/env python3
"""Exact, independently generated bounded-word check of Green-geodesic multiplicities."""
from collections import defaultdict, deque
from itertools import product
from math import factorial
from random import Random

ALPH=(-2,-1,1,2)

def mul(v,w):
    t=list(v)
    for a in w:
        if t and t[-1]==-a:t.pop()
        else:t.append(a)
    return tuple(t)

def inv(v):return tuple(-a for a in reversed(v))

def transl(T,s):return tuple(sorted(mul(inv(s),v) for v in T))

def neighbors(T):
    S=set(T)
    return {v:[mul(v,(a,)) for a in ALPH if mul(v,(a,)) in S] for v in S}

def distances(adj,s):
    q=deque([s]);d={s:0};parents={s:None}
    while q:
        v=q.popleft()
        for u in adj[v]:
            if u not in d:d[u]=d[v]+1;parents[u]=v;q.append(u)
    return d,parents

def path(adj,s,t):
    d,par=distances(adj,s)
    assert t in d
    P={t};v=t
    while v!=s:v=par[v];P.add(v)
    return P,d[t]

def weight(T,s,t):
    adj=neighbors(T)
    P,d=path(adj,s,t)
    prod=1
    for v in adj:
        if v in P:
            on=sum(u in P for u in adj[v])
            # Tree intersections of path at a vertex have degree 0, 1 or 2.
            assert 0<=on<=2
            prod*=factorial(len(adj[v])-on)
        else:prod*=factorial(len(adj[v])-1)
    return prod

def predict_r(T):
    adj=neighbors(T); d,_=distances(adj,());rad=max(d.values())
    return sum(weight(T,(),t) for t in T if d[t]==rad)

def predict_d(T):
    adj=neighbors(T)
    diameter=max(distances(adj,s)[0][t] for s in T for t in T)
    return sum(weight(T,s,t) for s in T for t in T if distances(adj,s)[0][t]==diameter)

def class_keys(T,end):
    T=tuple(sorted(T))
    return ( (T,end), T, transl(T,end), min(transl(T,s) for s in T) )

def check_all_words(max_length=8):
    assert max_length>=0
    counts=[defaultdict(int) for _ in range(4)]
    shortest=[{} for _ in range(4)]
    witness=[{} for _ in range(4)]
    cases=0
    # Direct word construction; no invocation of weight/DFS to determine counts.
    for n in range(max_length+1):
        for w in product(ALPH,repeat=n):
            p=(); T={p}
            for a in w:p=mul(p,(a,));T.add(p)
            keys=class_keys(T,p);cases+=1
            for i,key in enumerate(keys):
                if key not in shortest[i]:shortest[i][key]=n;witness[i][key]=tuple(sorted(T))
                if shortest[i][key]==n:counts[i][key]+=1
    checked=[]
    for i in range(4):
        for key,number in counts[i].items():
            T = (key[0] if i==0 else key if i==1 else key if i in (2,3) else ())
            if i==0:
                T,end=key
                pred=weight(T,(),end)
                shortest_length=2*(len(T)-1)-path(neighbors(T),(),end)[1]
            elif i==1:
                pred=predict_r(T)
                shortest_length=2*(len(T)-1)-max(distances(neighbors(T),())[0].values())
            elif i==2:
                # The L-class can be represented with its terminal vertex at identity.
                # Inversion gives equality with the R-class of the normalized tree.
                pred=predict_r(T)
                shortest_length=2*(len(T)-1)-max(distances(neighbors(T),())[0].values())
            else:
                pred=predict_d(T)
                adj=neighbors(T)
                diam=max(distances(adj,s)[0][t] for s in T for t in T)
                shortest_length=2*(len(T)-1)-diam
            if number != pred or shortest[i][key]!=shortest_length:
                raise AssertionError(('H','R','L','D')[i],T,key,number,pred,shortest[i][key],shortest_length)
        checked.append(len(counts[i]))
    by_length=[sum(v for key,v in counts[0].items() if shortest[0][key]==n) for n in range(max_length+1)]
    return cases,checked,by_length

def geodesic_series(rank, cutoff):
    """Independently expand the formal rooted-excursion equations."""
    q=2*rank; p=q-1; N=cutoff
    def mulpoly(a,b):
        out=[0]*(N+1)
        for i,x in enumerate(a[:N+1]):
            if x:
                for j,y in enumerate(b[:N+1-i]):out[i+j]+=x*y
        return out
    def polyadd(a,b):return [x+y for x,y in zip(a,b)]
    def scale(a,x):return [x*v for v in a]
    one=[1]+[0]*N
    def expbranch(cap, zF):
        out=[0]*(N+1);power=one;factor=1
        for j in range(cap+1):
            if j: power=mulpoly(power,zF);factor*=cap-j+1
            out=polyadd(out,scale(power,factor))
        return out
    F=one
    for i in range(N+1):
        zF=[0]+F[:-1]
        F=expbranch(p,zF)
    zF=[0]+F[:-1]
    def lift(a):
        out=[0]*(N+1)
        for i,v in enumerate(a):
            if 2*i<=N:out[2*i]=v
        return out
    B=lift(expbranch(p,zF));C=lift(expbranch(p-1,zF));A=lift(expbranch(q,zF))
    numerator=scale(mulpoly(B,B),q)
    numerator=[0]+numerator[:-1]
    denominator=[1]+[-p*C[i-1] for i in range(1,N+1)]
    out=[0]*(N+1)
    for k in range(N+1):
        out[k]=numerator[k]-sum(denominator[j]*out[k-j] for j in range(1,k+1))
    return polyadd(A,out)

def auxiliary_rank_checks():
    """Directly enumerate independent words in boundary rank 1 and rank 3."""
    for rank,cutoff in ((1,12),(3,6)):
        alphabet=tuple(letter for k in range(1,rank+1) for letter in (-k,k))
        actual=[]
        for n in range(cutoff+1):
            count=0
            for word in product(alphabet,repeat=n):
                vertex=();seen={vertex}
                for a in word:
                    vertex=mul(vertex,(a,));seen.add(vertex)
                if n==2*(len(seen)-1)-len(vertex):count+=1
            actual.append(count)
        expected=geodesic_series(rank,cutoff)
        assert actual==expected,(rank,actual,expected)
        print('AUXILIARY_VERIFY_OK',rank,cutoff,actual)

if __name__=='__main__':
    n,c,actual=check_all_words(8)
    expected=geodesic_series(2,8)
    assert actual==expected,('series-vs-enumeration',actual,expected)
    assert expected==[1,4,16,60,228,840,3132,11496,42528],expected
    print(f'VERIFY_OK enumerated_words={n} H={c[0]} R={c[1]} L={c[2]} D={c[3]} rank=2 max_length=8')
    print('RANK2_GEODESIC_SERIES',expected)
    auxiliary_rank_checks()
