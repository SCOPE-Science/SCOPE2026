#!/usr/bin/env python3
"""Exact cut-distance certificates and high-precision center-locus checks."""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import floor


def cuts(p, q):
    n = p + q
    for a in range(p + 1):
        for b in range(q + 1):
            k = a + b
            if 0 < k < n:
                d = a * (q-b) + b * (p-a)
                yield a, b, k, d


def root(x):
    return Decimal(x.numerator).sqrt()/Decimal(x.denominator).sqrt()


def test_radii():
    cases = tested = 0
    for p in range(2, 25):
        for q in range(p, 28):
            n = p + q
            wanted = Fraction(1) if (p,q)==(2,2) else Fraction(p*p*n, 4*(n-1))
            touches = []
            for a,b,k,d in cuts(p,q):
                squared = Fraction(d*d*n,4*k*(n-k))
                assert squared >= wanted, (p,q,a,b,squared,wanted)
                if squared == wanted: touches.append((a,b))
                tested += 1
            if (p,q)==(2,2): expected=[(1,1)]
            elif p==q: expected=[(0,1),(1,0),(p-1,q),(p,q-1)]
            else: expected=[(0,1),(p,q-1)]
            assert sorted(touches)==sorted(set(expected)), (p,q,touches,expected)
            cases += 1
    return cases,tested


def test_center_intervals():
    checked = 0
    with localcontext() as ctx:
        ctx.prec = 75
        for q in range(3, 71):
            p=2;n=q+2
            r=(Decimal(n)/Decimal(n-1)).sqrt()
            cap=Decimal(q)/2-(Decimal(n*n//4)/Decimal(n-1)).sqrt()
            assert cap>0
            # Center vector (t,-t,0,...,0); checking cuts by class sizes
            for a,b,k,d in cuts(p,q):
                slack=Decimal(d)/2-r*(Decimal(k*(n-k))/Decimal(n)).sqrt()
                if a==1:
                    assert slack>=cap-Decimal('1e-61'), (q,a,b,slack,cap)
                else:
                    assert slack >= -Decimal('1e-61'), (q,a,b,slack)
                checked+=1
            # A nearest-half cut, with one first-class vertex, reaches the bound.
            k=n//2
            b=k-1
            d=q
            slack=Decimal(d)/2-r*(Decimal(k*(n-k))/Decimal(n)).sqrt()
            assert abs(slack-cap)<Decimal('1e-60')
        # K(2,2) radius one and center (t,t,-t,-t):
        cap=Decimal(1)-Decimal(3).sqrt()/2
        for a,b,k,d in cuts(2,2):
            slack=Decimal(d)/2-(Decimal(k*(4-k))/Decimal(4)).sqrt()
            if a==1 and b==1:
                assert abs(slack)<Decimal('1e-60')
            elif k==1 or k==3:
                assert abs(slack-cap)<Decimal('1e-60')
            checked+=1
    return checked

if __name__ == '__main__':
    a,b=test_radii()
    c=test_center_intervals()
    print(f'EXACT_OK bipartite_pairs={a} cut_types={b}; CENTER_OK high_precision_constraints={c}; q=3..70 and C4')
