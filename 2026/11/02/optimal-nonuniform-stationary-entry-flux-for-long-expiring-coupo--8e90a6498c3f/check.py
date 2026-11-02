"""Independent finite checks for a sharp biased sliding-window coupon entry-flux law.

Usage: python check.py. Only Python stdlib is required.
"""
import itertools
import math
from fractions import Fraction


def inclusion_flux(p, m):
    """Exact stationary entrance flux for a length-m onto window."""
    n = len(p)
    total = p[0] * 0
    for i in range(n):
        other = [j for j in range(n) if j != i]
        s = p[0] * 0
        for mask in range(1 << (n-1)):
            forbidden = p[i] + sum((p[j] for t,j in enumerate(other) if mask >> t & 1), p[0]*0)
            s += (-1 if mask.bit_count() % 2 else 1) * (1 - forbidden)**(m-1)
        total += p[i] * (1-p[i]) * s
    return total


def enumeration_flux(p,m):
    n=len(p)
    total=Fraction(0)
    for word in itertools.product(range(n),repeat=m+1):
        if len(set(word[:m])) < n and len(set(word[1:])) == n:
            probability=Fraction(1)
            for j in word: probability *= p[j]
            total += probability
    return total


def cstar(k):
    lo,hi=1e-8,12.
    for _ in range(110):
        mid=(lo+hi)/2
        derivative=1/mid-1+(k-1)/math.expm1(mid)
        if derivative>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def g(cs):
    r=0.
    for i,c in enumerate(cs):
        r += c*math.exp(-c)*math.prod(-math.expm1(-d) for j,d in enumerate(cs) if j!=i)
    return r


def run():
    assertions=0
    # Fraction enumeration compares independent event definition with the subset formula.
    for n in (2,3):
        p=([Fraction(1,3),Fraction(2,3)] if n==2 else
           [Fraction(1,6),Fraction(1,3),Fraction(1,2)])
        for m in range(n,n+5):
            x=inclusion_flux(p,m)
            y=enumeration_flux(p,m)
            assert x==y,(n,m,x,y)
            assertions+=1
    # For n=2, direct sum of the two long constant runs.
    for m in range(2,42):
        for z in (Fraction(1,2),Fraction(1,4),Fraction(1,10),Fraction(3,7)):
            y=inclusion_flux([z,1-z],m)
            assert y==z*(1-z)**m+(1-z)*z**m,(m,z)
            assertions+=1
    # Normalized Poisson entrance function has a unique symmetric maximum.
    old=0.
    for k in range(1,11):
        c=cstar(k)
        C=g([c]*k)
        assert C>old and abs((1/c-1)+(k-1)/math.expm1(c))<2e-13
        assertions+=2
        for j in range(1,201):
            x=j*0.035
            assert g([x]*k) <= C+2e-11
            assertions+=1
        old=C
    # Explicit construction converges to sharp constant.
    for n in (2,3,4,5):
        k=n-1; c=cstar(k); C=g([c]*k)
        vals=[]
        for m in (200,500,1000,2000):
            p=[c/m]*k+[1-k*c/m]
            val=m*inclusion_flux(p,m)
            assert abs(val-C)<0.1, (n,m,val,C)
            vals.append(val)
            assertions+=1
        assert abs(vals[-1]-C)<0.012, (n,vals,C)
        assertions+=1
    # Coordinate perturbations of Poisson optimum cannot improve it.
    for k in range(1,8):
        c=cstar(k); optimum=g([c]*k)
        for j in range(k):
            for delta in (-0.7,-0.2,-0.02,0.02,0.2,0.7):
                args=[c]*k; args[j]=c+delta
                assert args[j]>0 and g(args)<optimum,(k,j,delta)
                assertions+=1
    print(f"PASS {assertions} checks")
    for n in (2,3,4,5):
        k=n-1;c=cstar(k)
        print(f"n={n} c={c:.12f} sharp_coefficient={g([c]*k):.12f}")

if __name__=='__main__':run()
