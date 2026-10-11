#!/usr/bin/env python3
"""Exact Clebsch--Gordan and high-weight packet fourth-moment checks.

Runs with the Python standard library only. A finite check is not an
infinite proof; the general theorem follows from fusion orthogonality.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def coeff_moment_direct(S, m, c):
    out = {}
    for i, a in enumerate(S):
        for j, b in enumerate(S):
            low, high = abs(a-b), 2*m+a+b
            for k in range(low, high+1, 2):
                out[k] = out.get(k, 0) + c[i]*c[j]
    return sum(x.real*x.real+x.imag*x.imag for x in out.values())


def coeff_moment_formula(S, m, c):
    even = sum(v for s,v in zip(S,c) if s%2==0)
    odd = sum(v for s,v in zip(S,c) if s%2==1)
    leading = ((even**2+odd**2).real**2+(even**2+odd**2).imag**2) + 4*((even*odd).real**2+(even*odd).imag**2)
    b = 0
    for i,j,k,l in product(range(len(S)),repeat=4):
        a,s,t,u = (S[i],S[j],S[k],S[l])
        if (a+s-t-u)%2:
            continue
        correction = Fraction(2+min(a+s,t+u)-max(abs(a-s),abs(t-u)),2)
        b += correction*c[i]*c[j]*c[k].conjugate()*c[l].conjugate()
    return m*leading+b


def best_constant(E,O):
    if E>=3*O:
        return Fraction(E*E), Fraction(1)
    if O>=3*E:
        return Fraction(O*O),Fraction(0)
    d=6*E*O-E*E-O*O
    return Fraction(8*E*E*O*O,d), Fraction(O*(3*E-O),d)


def main():
    support_sets=[(0,),(0,1),(0,2),(0,2,4,1),(0,2,4,6,1),(0,1,2),(0,1,2,3),(0,1,3,5,8)]
    cases = 0
    for S in support_sets:
        E=sum(s%2==0 for s in S); O=len(S)-E
        C,x=best_constant(E,O)
        assert 0<=x<=1
        lhs=E*E*x*x+6*E*O*x*(1-x)+O*O*(1-x)*(1-x)
        assert lhs==C
        for m in (max(S), max(S)+1, max(S)+7):
            for z in range(9):
                c = [complex(((i+3*z)%5)-2,((2*i+z)%7)-3) for i in range(len(S))]
                assert coeff_moment_direct(S,m,c)==coeff_moment_formula(S,m,c), (S,m,z)
                cases += 1
    print(f'VERIFY_OK supports={len(support_sets)} exact_fusion_matches={cases} sharp_piecewise_rationals=PASS')
if __name__=='__main__':
    main()
