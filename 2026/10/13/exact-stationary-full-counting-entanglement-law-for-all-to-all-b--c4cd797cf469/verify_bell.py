#!/usr/bin/env python3
"""Exact verification of the complete-graph Bell-pair matching stationary entropy law.
Python >= 3.9, standard library only. No external data or dependencies.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial, log, exp, sqrt, lgamma

@lru_cache(None)
def states(n):
    def rec(free):
        if not free:
            yield ()
            return
        a=free[0]
        for e in rec(free[1:]):
            yield e
        for b in free[1:]:
            rest=tuple(x for x in free[1:] if x!=b)
            for e in rec(rest):
                yield ((a,b),)+e
    return tuple(tuple(sorted(t)) for t in rec(tuple(range(n))))

def partner(n,edges):
    v=[-1]*n
    for a,b in edges:
        assert v[a]<0 and v[b]<0
        v[a]=b; v[b]=a
    return v

def z_update(n,edges,x):
    v=partner(n,edges)
    b=v[x]
    if b<0:
        return edges
    return tuple(sorted(t for t in edges if t!=tuple(sorted((x,b)))))

def bell_update(n,edges,a,b):
    v=partner(n,edges)
    if v[a]==b:
        return edges
    old=[t for t in edges if a not in t and b not in t]
    if v[a]>=0 and v[b]>=0:
        old.append(tuple(sorted((v[a],v[b]))))
    old.append((a,b))
    return tuple(sorted(old))

def partition(n,z):
    return sum(Fraction(factorial(n),factorial(n-2*r)*2**r*factorial(r))*z**r for r in range(n//2+1))

def check(n,p):
    sts=states(n); N=len(sts); idx={m:i for i,m in enumerate(sts)}
    assert len(idx)==N
    z=Fraction(1-p,p*(n-1))
    weights=[z**len(m) for m in sts]
    assert sum(weights)==partition(n,z)
    W=partition(n,z)
    # exact detailed balance on every state-pair transition
    rows=[]
    for i,m in enumerate(sts):
        moves=Counter()
        for x in range(n):
            moves[idx[z_update(n,m,x)]]+=p/Fraction(n)
        for a,b in combinations(range(n),2):
            moves[idx[bell_update(n,m,a,b)]]+=(1-p)/Fraction(comb(n,2))
        assert sum(moves.values())==1
        rows.append(moves)
    for i,move in enumerate(rows):
        for j,rate in move.items():
            assert weights[i]*rate==weights[j]*rows[j][i], (n,p,i,j,rate)
    for k in range(1,n):
        hist=Counter()
        for m,w in zip(sts,weights):
            crossings=sum(int(a<k<=b) for a,b in m)
            hist[crossings]+=w
        predicted=Counter()
        for j in range(min(k,n-k)+1):
            predicted[j]=(Fraction(comb(k,j)*comb(n-k,j)*factorial(j))*z**j*partition(k-j,z)*partition(n-k-j,z))
        assert hist==predicted,(n,p,k,hist,predicted)
        r1=z*partition(n-2,z)/W
        r2=z*z*partition(n-4,z)/W if n>=4 else Fraction(0)
        E=Fraction(k*(n-k))*r1
        V=E+Fraction(k*(k-1)*(n-k)*(n-k-1))*r2-E*E
        e2=sum(Fraction(j*j)*w for j,w in hist.items())/W
        assert sum(Fraction(j)*w for j,w in hist.items())/W==E
        assert e2-E*E==V
    return N,sum(map(len,rows)),sum(len(m) for m in sts)

def asymptotic(n,p,a):
    z=(1-p)/p/(n-1)
    ms=range(n%2,n+1,2)
    ll=[lgamma(n+1)-lgamma(m+1)-(n-m)/2*log(2)-lgamma((n-m)/2+1)+(n-m)/2*log(z) for m in ms]
    ma=max(ll); ww=[exp(v-ma) for v in ll]; tot=sum(ww)
    em=sum(m*w for m,w in zip(ms,ww))/tot
    vm=sum((m-em)**2*w for m,w in zip(ms,ww))/tot
    k=round(a*n); l=n-k
    q1=(n-em)/(n*(n-1))
    q2=sum((n-m)*(n-m-2)*w for m,w in zip(ms,ww))/tot/(n*(n-1)*(n-2)*(n-3))
    ex=k*l*q1
    var=ex+k*(k-1)*l*(l-1)*q2-ex**2
    theta=(1-p)/p
    u=2/(sqrt(1+4*theta)+1)
    sig=2*u*(1-u)/(2-u)
    v=a*(1-a)*(1-u)*(u+2*a*(1-a)*(1-2*u))+(a*(1-a))**2*sig
    return em/n,vm/n,ex/n,var/n,u,sig,a*(1-a)*(1-u),v

def main():
    configurations=0; transitions=0; matched_bonds=0; cases=0
    for n in range(2,9):
        for p in (Fraction(1,3),Fraction(2,5),Fraction(3,4)):
            x,y,z=check(n,p)
            configurations+=x;transitions+=y;matched_bonds+=z; cases+=1
    assert len(states(8))==764
    for p in (0.1,0.4,0.85):
        for a in (0.25,0.4,0.5):
            em,vm,ex,var,u,sig,e,v=asymptotic(4000,p,a)
            assert abs(em-u)<0.001
            assert abs(vm-sig)<0.002
            assert abs(ex-e)<0.001
            assert abs(var-v)<0.001
    print(f'VERIFY_OK: {cases} exact weighted matching chains; {configurations} state instances; {transitions} transition pairs; generating distributions and first two moments for every bipartition; 9 thermodynamic variance checks')

if __name__=='__main__':
    main()
