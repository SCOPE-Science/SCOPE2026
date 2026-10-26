"""Independent finite-state checks for dimer adsorption on matching-bridged cliques.
Requires Python >=3.9, standard library only. Run: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp


def plus(p, q):
    out = list(p) + [Fraction(0)] * max(0, len(q)-len(p))
    for k, val in enumerate(q):
        out[k] += val
    while len(out)>1 and not out[-1]:
        out.pop()
    return tuple(out)


def scale(p, s):
    return tuple(s*x for x in p)


def poly_aggregated(n, weight):
    @lru_cache(None)
    def rec(a, b, c):
        A = comb(a, 2)
        B = comb(b, 2)
        C = weight*c
        D = A+B+C
        if D==0:
            return (Fraction(1),)
        val=(Fraction(0),)
        if A:
            for t in range(3):
                if 0 <= t <= c and 0 <= 2-t <= a-c:
                    val=plus(val,scale(rec(a-2,b,c-t),Fraction(comb(c,t)*comb(a-c,2-t),1)/D))
        if B:
            for t in range(3):
                if 0 <= t <= c and 0 <= 2-t <= b-c:
                    val=plus(val,scale(rec(a,b-2,c-t),Fraction(comb(c,t)*comb(b-c,2-t),1)/D))
        if C:
            val=plus(val,scale((Fraction(0),)+rec(a-1,b-1,c-1),C/D))
        return val
    return rec(n,n,n)


def poly_full_graph(n, weight):
    edges = [(i,j,Fraction(1),False) for base in (0,n) for i in range(base,base+n) for j in range(i+1,base+n)]
    edges += [(i,i+n,weight,True) for i in range(n)]
    @lru_cache(None)
    def rec(mask):
        avail=[(i,j,w,vertical) for i,j,w,vertical in edges if mask&(1<<i) and mask&(1<<j)]
        rate=sum((w for i,j,w,vertical in avail),Fraction(0))
        if not rate: return (Fraction(1),)
        value=(Fraction(0),)
        for i,j,w,vertical in avail:
            child=rec(mask^(1<<i)^(1<<j))
            if vertical: child=(Fraction(0),)+child
            value=plus(value,scale(child,w/rate))
        return value
    return rec((1<<(2*n))-1)


def phi(a,b,c):
    if c==0:return Fraction(0)
    return Fraction(c,a)+Fraction(c,b)


def generator_phi(a,b,c,weight):
    A=comb(a,2); B=comb(b,2); out=Fraction(0)
    if A:
        for t in range(3):
            if 0<=t<=c and 0<=2-t<=a-c:
                out += Fraction(comb(c,t)*comb(a-c,2-t),1)*(phi(a-2,b,c-t)-phi(a,b,c))
    if B:
        for t in range(3):
            if 0<=t<=c and 0<=2-t<=b-c:
                out += Fraction(comb(c,t)*comb(b-c,2-t),1)*(phi(a,b-2,c-t)-phi(a,b,c))
    if c:
        out += weight*c*(phi(a-1,b-1,c-1)-phi(a,b,c))
    return out


def main():
    cnt=0
    for weight in (Fraction(1,3), Fraction(1), Fraction(3)):
        for n in range(2,6):
            p=poly_aggregated(n,weight)
            q=poly_full_graph(n,weight)
            assert p==q,(n,weight,p,q)
            assert sum(p)==1
            # Parity: a terminal defect is equivalent to an odd cross-count when n even, and vice versa.
            p_def=sum(v for m,v in enumerate(p) if (m-n)%2)
            assert Fraction(0)<=p_def<=1
            cnt+=3
        for a in range(1,12):
            for b in range(1,12):
                for c in range(min(a,b)+1):
                    drift=generator_phi(a,b,c,weight)
                    factor=max(Fraction(1),weight)
                    assert factor*drift <= -weight*c, (a,b,c,weight,drift)
                    cnt+=1
    # Numerical distributional trend, exact rational recursion with no stochastic simulation:
    for n in (6,8,10):
        p=poly_aggregated(n,Fraction(1))
        assert sum(p)==1
        defect=float(sum(v for m,v in enumerate(p) if (m-n)%2))
        assert abs(defect-(1-exp(-2))/2)<0.2
        cnt+=2
    print('PASS',cnt,'exact transition, full-graph comparison, and Lyapunov assertions')
    for n in (2,3,4,6,8,10):
        p=poly_aggregated(n,Fraction(1))
        print('n=',n,'cross mean=',float(sum(i*v for i,v in enumerate(p))),
              'P(two uncovered)=',float(sum(v for m,v in enumerate(p) if (m-n)%2)))

if __name__=='__main__':
    main()
