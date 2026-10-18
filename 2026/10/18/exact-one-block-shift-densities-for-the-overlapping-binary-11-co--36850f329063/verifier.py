#!/usr/bin/env python3
"""Exact rational recurrence and independent finite arithmetic checks."""
from fractions import Fraction as Q
from functools import lru_cache

# A Laurent polynomial represents (this polynomial)/(2z-1).
def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}

def scale(a, c):
    return {k: c*v for k, v in a.items() if c*v}

def shift(a, j):
    return {k+j: v for k, v in a.items()}

def sub(a, b):
    return add(a, scale(b, Q(-1)))

def mul(a, b):
    out = {}
    for k, v in a.items():
        for h, w in b.items():
            out[k+h] = out.get(k+h, Q(0)) + v*w
    return {k:v for k,v in out.items() if v}

def neg_mass(a):
    # 1/(2z-1) = sum_{h>=1} 2**(-h) z**(-h) for |z|>1/2.
    return sum((v if k < 0 else v*Q(1, 2**k)) for k, v in a.items())

def total_mass(a):
    return sum(a.values()) # evaluation z=1, denominator at z=1 equals 1

@lru_cache(None)
def ab(t):
    if t == 0:
        p = {0:Q(-1), 1:Q(2)}
        return p, p
    if t == 1:
        return {0:Q(-1,2),1:Q(1,2),2:Q(1)}, {1:Q(1,2),2:Q(1,2)}
    if t % 4 == 0:
        a,b = ab(t//2)
        u=scale(add(a,b), Q(1,2))
        return u,u
    if t % 4 == 1:
        a,b = ab((t-1)//2)
        e,f = ab((t+1)//2)
        return scale(add(a,shift(b,1)),Q(1,2)),scale(add(e,shift(f,-1)),Q(1,2))
    if t % 4 == 2:
        a,b=ab(t//2)
        return scale(add(a,b),Q(1,2)),scale(add(shift(a,1),shift(b,-1)),Q(1,2))
    a,b = ab(t//2)
    c,d = ab((t+1)//2)
    return scale(add(shift(a,1),b),Q(1,2)),scale(add(c,shift(d,-1)),Q(1,2))

def prob_nonnegative(t):
    a,b = ab(t)
    return 1-Q(1,2)*(neg_mass(a)+neg_mass(b))

def r(n):
    return (n & (n >> 1)).bit_count()

def run():
    # The exact base laws and recurrence are algebraically represented by Laurent polynomials.
    A1,B1=ab(1)
    assert A1=={0:Q(-1,2),1:Q(1,2),2:Q(1)}
    assert B1=={1:Q(1,2),2:Q(1,2)}
    for t in range(1,8192):
        a,b = ab(t)
        assert total_mass(a)==1 and total_mass(b)==1
        assert neg_mass(a)>=0 and neg_mass(b)>=0
    # This is the exact algebraic factorization of (A31-A15) after cancelling 2z-1.
    zminus1={0:Q(-1),1:Q(1)}
    zplus1={0:Q(1),1:Q(1)}
    q={0:Q(2),1:Q(1),2:Q(2)}
    K=scale(mul(mul(mul(zminus1,zminus1),zplus1),q),Q(1,64))
    denom={0:Q(-1),1:Q(2)}
    A15,B15=ab(15)
    A31,B31=ab(31)
    assert sub(A31,A15)==mul(denom,K)
    assert B15==B31
    assert min(K)>=0 and sum(K.values())==0
    assert neg_mass(A15)==Q(9,32)
    assert neg_mass(B15)==Q(27,64)
    assert prob_nonnegative(15)==Q(83,128)
    assert prob_nonnegative(30)==Q(39,64)
    expected0={1:Q(13,16),2:Q(47,64),3:Q(87,128)}
    expected1={1:Q(23,32),2:Q(43,64),3:Q(5,8)}
    algebra_checks=0
    for k in range(1,13):
        t=(1<<k)-1
        for j in range(5):
            target = (expected0.get(k,Q(83,128)) if j==0 else expected1.get(k,Q(39,64)))
            assert prob_nonnegative(t<<j)==target,(k,j,prob_nonnegative(t<<j),target)
            algebra_checks+=1
        if k>=4:
            assert ab(t)[1]==B15
            assert sub(ab(2*t+1)[0],ab(t)[0])==shift(scale(sub(ab(t)[0],ab((t-1)//2)[0]),Q(1,2)),1)
    # Independent direct finite arithmetic; the period chosen is much larger than the input shift.
    brute_cases=0
    width=1<<18
    for k in range(1,9):
        for j in range(3):
            t=((1<<k)-1)<<j
            count=sum(r(n+t)>=r(n) for n in range(width))
            target=prob_nonnegative(t)
            # Dyadic truncation can differ at its upper boundary: no claim of finite periodicity.
            assert abs(Q(count,width)-target) <= Q(1,4096),(t,Q(count,width),target)
            brute_cases+=1
    print('VERIFICATION_PASS: polynomial identities,',algebra_checks,'exact one-block pgf checks,',brute_cases,'full finite dyadic-count checks; exact matrix proof in RESULT.md.')

if __name__=='__main__':
    run()
