#!/usr/bin/env python3
"""Exact checks for near-complete cyclic de Bruijn words.
All arithmetic is integral. No external dependencies.
"""
from itertools import product, combinations
from math import factorial, comb
from fractions import Fraction


def bareiss(matrix):
    a=[list(map(int,row)) for row in matrix]
    n=len(a)
    if n==0: return 1
    sign=1
    denom=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((i for i in range(k+1,n) if a[i][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                t=a[i][j]*p-a[i][k]*a[k][j]
                assert t%denom==0
                a[i][j]=t//denom
            a[i][k]=0
        denom=p
    return sign*a[-1][-1]


def arborescence(q,n,removed):
    m=n-1
    V=list(product(range(q),repeat=m))
    idx={v:i for i,v in enumerate(V)}
    A=[[0]*len(V) for _ in V]
    removed=set(removed)
    for w in product(range(q),repeat=n):
        if w in removed:continue
        u=idx[w[:m]];v=idx[w[1:]]
        A[u][u]+=1;A[u][v]-=1
    return bareiss([row[1:] for row in A[1:]])


def best_count(q,n,removed):
    m=n-1
    outdeg={v:q for v in product(range(q),repeat=m)}
    for w in removed:outdeg[w[:m]]-=1
    if min(outdeg.values())<=0:return 0
    return arborescence(q,n,removed)*__import__('math').prod(factorial(d-1) for d in outdeg.values())


def formula(q,n):
    b=factorial(q)**(q**(n-1))//(q**n)
    base=Fraction(b,(q-1)**2)
    r=Fraction(q-1,q+1)+Fraction(2,q+1)*Fraction((-1)**(n-1),q**(n-1))
    return b,base,base*r,base*comb(q,2)*(1+r)


def rotation(w):
    return min(w[i:]+w[:i] for i in range(len(w)))


def exact_necklaces(q,n):
    L=q**n-2
    if L<1:return {},{}
    accepted={}
    for w in product(range(q),repeat=L):
        windows={tuple(w[(i+j)%L] for j in range(n)) for i in range(L)}
        if len(windows)!=L:continue
        key=rotation(w)
        missing=set(product(range(q),repeat=n))-windows
        assert len(missing)==2
        accepted[key]=tuple(sorted(missing))
        for m in range(1,L+1):
            mult={z:0 for z in product(range(q),repeat=m)} if m<=n else {}
            for i in range(L):
                z=tuple(w[(i+j)%L] for j in range(m))
                mult[z]=mult.get(z,0)+1
            lo=L//q**m;hi=(L+q**m-1)//q**m
            assert all(lo<=v<=hi for v in mult.values())
    t={'loops':0,'alternating':0}
    for missing in accepted.values():
        w1,w2=missing
        if len(set(w1))==len(set(w2))==1:t['loops']+=1
        else:t['alternating']+=1
    return accepted,t


def run():
    checks=0
    for q,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(4,2),(4,3)]:
        b,loops,alt,total=formula(q,n)
        assert loops.denominator==alt.denominator==total.denominator==1
        a,b_sym=0,1
        loopmiss={(a,)*n,(b_sym,)*n}
        altmiss={tuple((a if i%2==0 else b_sym) for i in range(n)),tuple((b_sym if i%2==0 else a) for i in range(n))}
        c1=best_count(q,n,loopmiss)
        c2=best_count(q,n,altmiss)
        assert (c1,c2)==(int(loops),int(alt)),(q,n,c1,c2,loops,alt)
        print('EXACT_TREE',q,n,'loop_per_pair',c1,'alt_per_pair',c2,'total',int(total))
        checks+=1
    for q,n in [(2,2),(2,3),(2,4),(3,2)]:
        seqs,t=exact_necklaces(q,n)
        _,loop,alt,total=formula(q,n)
        assert (t['loops'],t['alternating'],len(seqs))==(comb(q,2)*loop,comb(q,2)*alt,total)
        print('EXHAUSTIVE',q,n,'total',len(seqs),'split',t)
        checks+=1
    print('VERIFY_OK tree_cases=9 exhaustive_cases=4 total_checks='+str(checks))

if __name__=='__main__':run()
