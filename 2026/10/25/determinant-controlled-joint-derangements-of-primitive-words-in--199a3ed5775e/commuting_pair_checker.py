"""Exact small-size checks for primitive-word fixed-point exclusions in commuting pairs.

Run: python3 commuting_pair_checker.py
Only Python standard library is needed. This exhausts every ordered commuting pair
through degree six and independently evaluates rational generating functions.
"""
from itertools import permutations
from fractions import Fraction
from math import factorial

def parts(N):
    p = [0]*(N+1)
    p[0] = 1
    for m in range(1,N+1):
        for n in range(m,N+1):
            p[n] += p[n-m]
    return p

def coefficient_joint_zero(n, D, p):
    # E(z) = exp(sum_{d|D} z^d/d), coefficients by z E'=E sum z^d.
    ds = [d for d in range(1,D+1) if D % d == 0]
    e = [Fraction(0) for _ in range(n+1)]
    e[0] = 1
    for k in range(1,n+1):
        e[k] = sum((e[k-d] for d in ds if d<=k), Fraction(0))/k
    pe = [sum((p[k-j]*e[j] for j in range(k+1)),Fraction(0)) for k in range(n+1)]
    return pe[n] - 2*(pe[n-1] if n>=1 else 0) + (pe[n-2] if n>=2 else 0)

def compose(f,g):
    return tuple(f[g[i]] for i in range(len(f)))

def fixed_points_word(sig,tau,D):
    # (sig * tau**D), cyclic permutation exponent D, commuting hypothesis.
    t = tuple(range(len(tau)))
    for _ in range(D):
        t = compose(tau,t)
    f = compose(sig,t)
    return any(f[i] == i for i in range(len(f)))

def main():
    p=parts(6)
    checked=0
    for n in range(1,7):
        pp=list(permutations(range(n)))
        totals=0
        none_v=0
        none_vw={d:0 for d in (1,2,3,4,5)}
        for s in pp:
            for t in pp:
                if compose(s,t)!=compose(t,s):
                    continue
                totals+=1
                bv=all(s[i]!=i for i in range(n))
                none_v+=bv
                if bv:
                    for d in none_vw:
                        if not fixed_points_word(s,t,d):
                            none_vw[d]+=1
                checked+=1
        assert totals==factorial(n)*p[n], (n,totals,p[n])
        assert none_v==factorial(n)*(p[n]-p[n-1]), (n,none_v)
        for d,num in none_vw.items():
            expected=factorial(n)*coefficient_joint_zero(n,d,p)
            assert expected.denominator==1 and num==expected.numerator,(n,d,num,expected)
        print('DEGREE',n,'PAIRS',totals,'NO_SINGLE',none_v,'DOUBLE',none_vw)
    print('COMMUTING_PRIMITIVE_EXCLUSION_OK',checked,5*6)

if __name__ == '__main__':
    main()
