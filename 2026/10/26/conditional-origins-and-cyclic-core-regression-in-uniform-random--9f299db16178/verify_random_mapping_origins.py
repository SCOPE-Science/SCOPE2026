"""Independent exact checks for origins and cyclic vertices in uniform random mappings.

Run: python verify_random_mapping_origins.py
Python standard library only. Finite checks supplement, not replace, the proof.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import product
from math import factorial, comb, sqrt, pi, e


def cyc_count(f):
    n=len(f)
    cyclic=set()
    for v in range(n):
        seen={}
        w=v
        while w not in seen:
            seen[w]=len(seen)
            w=f[w]
        cyc=list(seen.keys())[seen[w]:]
        cyclic.update(cyc)
    return len(cyclic)


def falling(x,t):
    y=1
    for j in range(t): y*=x-j
    return y


def Pk(n,k):
    return Fraction(k*falling(n,k),n**(k+1))


def condfac(n,k,t):
    if t>n-k: return Fraction(0)
    return Fraction(falling(n-k,t))*Fraction(n-t,n)**(n-k-1)


def expectedK(n):
    return sum(Fraction(k)*Pk(n,k) for k in range(1,n+1))


def expectedL(n):
    return n*Fraction(n-1,n)**n


def exact_exhaustive(n):
    counts=Counter()
    selected_origin_cycle=defaultdict(Counter)
    for f in product(range(n),repeat=n):
        degree=[0]*n
        for w in f: degree[w]+=1
        leaves={v for v,x in enumerate(degree) if x==0}
        K=cyc_count(f)
        L=len(leaves)
        counts[(K,L)]+=1
        for t in range(min(3,n-1)+1):
            if all(v in leaves for v in range(t)):
                selected_origin_cycle[t][K]+=1
    checks=0
    assert sum(counts.values())==n**n;checks+=1
    for k in range(1,n+1):
        N=sum(c for (j,l),c in counts.items() if j==k)
        assert Fraction(N,n**n)==Pk(n,k);checks+=1
        for t in range(n-k+1):
            v=sum(falling(l,t)*c for (j,l),c in counts.items() if j==k)
            assert Fraction(v,N)==condfac(n,k,t), (n,k,t,Fraction(v,N),condfac(n,k,t))
            checks+=1
        if k<n:
            A=sum(l*c for (j,l),c in counts.items() if j==k)
            assert Fraction(A,N)==Fraction(n-k)*Fraction(n-1,n)**(n-k-1);checks+=1
    for t in range(min(3,n-1)+1):
        prob=Fraction(n-t,n)**n
        for k in range(1,n-t+1):
            got=Fraction(selected_origin_cycle[t][k],n**n)
            assert got==prob*Pk(n-t,k), (n,t,k,got,prob*Pk(n-t,k))
            checks+=1
    cov=(sum(Fraction(k*l*c,n**n) for (k,l),c in counts.items())-
         expectedK(n)*expectedL(n))
    nsub=expectedK(n-1)
    assert cov==n*Fraction(n-1,n)**n*(nsub-expectedK(n));checks+=1
    assert cov<0;checks+=1
    return checks


def exact_formula_checks(n):
    checks=0
    assert sum(Pk(n,k) for k in range(1,n+1))==1;checks+=1
    for k in range(1,n):
        m=condfac(n,k,1)
        if k+1<n: nxt=condfac(n,k+1,1)
        else: nxt=Fraction(0)
        assert m-nxt==Fraction(k,n)*Fraction(n-1,n)**(n-k-2)
        checks+=1
    out=sum(Pk(n,k)*condfac(n,k,1) for k in range(1,n+1))
    assert out==expectedL(n);checks+=1
    return checks


def main():
    checks=0
    for n in range(2,8):
        count=exact_exhaustive(n);checks+=count
        print('Exhaustive',n,'mappings',n**n,'checks',count)
    for n in range(2,41): checks+=exact_formula_checks(n)
    for n in (500,2000,10000):
        # Uniformly accurate asymptotic test by finite exact recurrence for expectation of K.
        # P(K=k) = (k/n) prod_{i<k}(1-i/n), computed as floats.
        p=1.0; EK=0.0; second=0.0
        q=(1.0-1.0/n)**n; EL=n*q
        ekl=0.0
        for k in range(1,n+1):
            p*=1-(k-1)/n
            pr=k*p/n
            EK+=k*pr
            m=(n-k)*(1-1/n)**(n-k-1) if k<n else 0
            ekl+=k*m*pr
            second+=pr
        cov=ekl-EK*EL
        constant=cov/sqrt(n)
        target=-sqrt(pi/2)/(2*e)
        assert abs(second-1)<1e-9,(n,second)
        assert abs(constant-target)<0.05,(n,constant,target)
        checks+=2
        print('n',n,'Cov/sqrt(n)',constant,'limit',target)
    print('PASS',checks,'checks')

if __name__=='__main__': main()
