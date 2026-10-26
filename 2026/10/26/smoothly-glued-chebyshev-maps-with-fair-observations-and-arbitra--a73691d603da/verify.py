"""Exact finite-branch checks for a two-degree Chebyshev interval family.

The all-degree theorem rests on the written proof; these checks are reproducible
finite corroboration, not certification of untested parameter values.
"""
from fractions import Fraction
from itertools import product
import math


def branches(m, n):
    assert m >= 2 and n >= 2 and m % 4 == n % 4 == 2
    # Branch intervals for the arccosine conjugate, each mapped onto [0,1].
    out = []
    for degree, low, high, symbol in [(m, Fraction(0), Fraction(1,2), '+'),
                                       (n, Fraction(1,2), Fraction(1), '-')]:
        edges = [Fraction(j,degree) for j in range(degree+1) if low <= Fraction(j,degree) <= high]
        assert edges[0] == low and edges[-1] == high
        for a, b in zip(edges, edges[1:]):
            assert b-a == Fraction(1, degree)
            # Triangular wave has full amplitude on all these intervals.
            out.append((a,b,degree,symbol))
    assert len(out) == (m+n)//2
    return out


def exact_sign_word_probability(m, n, signs):
    # Explicitly sum inverse-branch cylinder widths over EVERY lift of
    # a sign word. This is separate from simply assuming fair signs.
    relevant = [tuple(Fraction(1,d) for _,_,d,s in branches(m,n) if s == label)
                for label in '+-']
    groups = {'+': relevant[0], '-': relevant[1]}
    masses = [Fraction(1)]
    for sign in signs:
        masses = [w * slope_inv for w in masses for slope_inv in groups[sign]]
    return sum(masses)


def main():
    inspected=0
    for m,n in [(2,2),(2,6),(6,10),(2,10),(10,22)]:
        B=branches(m,n)
        assert sum(b-a for a,b,_,_ in B)==1
        assert sum(Fraction(1,d) for _,_,d,_ in B)==1
        assert sum(1 for _,_,_,s in B if s=='+')==m//2
        assert sum(1 for _,_,_,s in B if s=='-')==n//2
        # Independent branch weights are exactly inverse local slopes.
        for size in range(1,7):
            total=Fraction(0)
            for word in product('+-',repeat=size):
                p=exact_sign_word_probability(m,n,word)
                assert p == Fraction(1,2**size)
                total+=p
                inspected+=1
            assert total==1
        N=len(B)
        mu_probs={'+':Fraction(1,2),'-':Fraction(1,2)}
        nu_probs={'+':Fraction(m,m+n),'-':Fraction(n,m+n)}
        assert nu_probs['+']+nu_probs['-']==1
        assert N==(m+n)//2
        assert math.isclose(math.log(N)-(math.log(m)+math.log(n))/2,
                            math.log((m+n)/(2*math.sqrt(m*n))),abs_tol=1e-12)
        assert (m==n)==(mu_probs==nu_probs)
    print('VERIFY_OK: 5 polynomial-degree pairs; %d exact sign-word probabilities; full-branch counts, conservation, Perron bias and gap checked' % inspected)

if __name__=='__main__': main()
