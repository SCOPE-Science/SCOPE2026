#!/usr/bin/env python3
"""Exact reproducibility checks for average-distance Schelling equilibria on stars.

Uses only the Python standard library.  Finite checks test stated algebraic
identities and examples; the all-size and limit assertions require the proof.
"""
from itertools import combinations_with_replacement
from fractions import Fraction
from decimal import Decimal, localcontext
from math import sqrt


def payoff_star(values, center, agent):
    n = len(values)
    if agent == center:
        return Fraction(sum(abs(values[center]-values[j]) for j in range(n)), n-1)
    return Fraction(abs(values[agent]-values[center]))


def stable_direct(values, center):
    n = len(values)
    for leaf in range(n):
        if leaf == center:
            continue
        before_c = payoff_star(values, center, center)
        before_l = payoff_star(values, center, leaf)
        # Swapping positions changes center identity; agents remain distinct.
        after_c = Fraction(abs(values[center]-values[leaf]))
        after_l = Fraction(sum(abs(values[leaf]-values[j]) for j in range(n) if j != leaf), n-1)
        if after_c < before_c and after_l < before_l:
            return False
    return True


def stable_sum(values, center):
    n=len(values)
    T=[sum(abs(values[i]-values[j]) for j in range(n)) for i in range(n)]
    return not any(T[j]<(n-1)*abs(values[j]-values[center])<T[center]
                   for j in range(n) if j!=center)


def stable_lattice_formula(n, center):
    m=n-1
    a=min(center,m-center)
    if 2*a >= n-2:
        return True
    with localcontext() as ctx:
        ctx.prec=75
        M=Decimal(m)
        aa=Decimal(a)
        L=M-(M*(Decimal(n-2)/2-aa)).sqrt()
        U=Decimal(n)/2+aa*aa/M
        return not any(L<j<U for j in range(n))


def main():
    count=0
    for n in range(2,9):
        for vals in combinations_with_replacement(range(6),n):
            for c in range(n):
                assert stable_direct(vals,c)==stable_sum(vals,c),(vals,c)
                count+=1
    print('Exact direct-swap vs. center certificate:',count,'profiles/centers passed')
    lattice_count=0
    for n in range(3,401):
        m=n-1
        vals=range(n)
        T=[j*j-m*j+n*m//2 for j in range(n)]
        for c in range(n):
            direct=not any(T[j]<m*abs(j-c)<T[c] for j in range(n) if j!=c)
            assert direct==stable_lattice_formula(n,c),(n,c)
            lattice_count+=1
    print('Exact lattice certificates vs. radical intervals:',lattice_count,'passed')
    vals=(0,1,4,5,6)
    centers=[c for c in range(5) if stable_direct(vals,c)]
    assert centers==[0,2,3,4],centers
    print('Disconnected equilibrium-center example:',vals,centers)
    for n in (100,200,400,800,1600):
        K=sum(stable_lattice_formula(n,c) for c in range(n))
        assert abs(K-n*(2-sqrt(3)))<12,(n,K)
        print('Grid size:',n,'stable centers:',K,'fraction:',round(K/n,9))
    print('ALL CHECKS PASSED (finite tests do not prove asymptotics)')

if __name__=='__main__':
    main()
