"""Exact independent finite-field tests for twofold sums of x^5+a*x^3.

Usage: python verify_binary_sums.py
Only Python's standard library is required.
"""
from collections import Counter


def degree(f):
    return f.bit_length() - 1


def rem(a,b):
    while a and degree(a)>=degree(b):
        a ^= b << (degree(a)-degree(b))
    return a


def gf_mul(a,b,mod,m):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a & (1<<m): a^=mod
    return r


def irreducible(pol,m):
    # Trial divisibility by all possible lower-degree monic polynomials.
    if not (pol&(1<<m) and pol&1):return False
    for d in range(1,m//2+1):
        for b in range((1<<d)+1,1<<(d+1),2):
            if rem(pol,b)==0:return False
    return True


def field_modulus(m):
    for pol in range((1<<m)+1,1<<(m+1),2):
        if irreducible(pol,m):return pol
    raise ValueError(m)


def spectrum(m,a,mod):
    q=1<<m
    def mul(x,y):return gf_mul(x,y,mod,m)
    def f(x):
        x2=mul(x,x)
        x3=mul(x2,x)
        x5=mul(x3,x2)
        return x5^mul(a,x3)
    values=[f(x) for x in range(q)]
    histogram=Counter()
    for s in range(q):
        counts=Counter((values[x]^values[x^s]) for x in range(q))
        for v in range(q):histogram[counts[v]]+=1
    return histogram


def prediction(m,a):
    q=1<<m
    if a==0:
        n4=q-1 if m%2==0 else 0
    else:
        n4=q//2-1-(m%2==0)
    n2=q-1-n4
    h=Counter({0:q*q-1-n2*q//2-n4*q//4})
    h[2]+=n2*q//2
    h[4]+=n4*q//4
    h[q]+=1
    return +h,n2,n4


def main():
    cases=0
    full=0
    for m in range(2,9):
        q=1<<m
        mod=field_modulus(m)
        # all coefficients at small sizes, spread representatives at larger sizes
        vals=range(q) if m<=6 else sorted(set([0,1,2,3,5,7,q//2,q-1]))
        for a in vals:
            actual=spectrum(m,a,mod)
            predicted,n2,n4=prediction(m,a)
            assert actual==predicted,(m,a,actual,predicted)
            assert sum(r*count for r,count in actual.items())==q*q
            if a:
                assert n4==q//2-1-(m%2==0)
                assert sum((r*r)*count for r,count in actual.items())==(4*q*q-(4 if m%2 else 6)*q)
            cases+=1
            if m<=6:full+=1
        print('FIELD_OK m=%d q=%d modulus=%s coefficients=%d'%(m,q,hex(mod),len(vals)))
    print('VERIFY_OK independent_pair_enumeration=True coefficient_cases=%d full_coefficients=%d'%(cases,full))

if __name__=='__main__':main()
