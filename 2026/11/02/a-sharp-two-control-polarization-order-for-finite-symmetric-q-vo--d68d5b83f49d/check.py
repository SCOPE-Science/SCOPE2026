"""Exact and sampled checks for the two-control polarization-order theorem.

Run: python3 check.py (Python 3 standard library only).
All stochastic-chain, likelihood-ratio, and certificate tests use integer
cross-multiplication. Finite tests supplement the universal paper proof.
"""
from fractions import Fraction
from math import comb, log


def rising(z, n):
    p = 1
    for i in range(n):
        p *= z + i
    return p


def stationary_weights(s, z, q):
    return [comb(s, k) * (rising(z, k)*rising(z, s-k))**q
            for k in range(s+1)]


def radial_mass(s, z, q):
    w = stationary_weights(s, z, q)
    return [sum(w[k] for k in range(s+1) if abs(2*k-s)==d)
            for d in range(s%2, s+1, 2)]


def sign(x):
    return (x>0)-(x<0)


def main():
    chain = 0
    for s in range(4, 31):
        for z in range(1, 15):
            for q in range(2, 8):
                w = stationary_weights(s, z, q)
                assert w == w[::-1]
                for k in range(s):
                    lhs = Fraction(w[k+1], w[k])
                    rhs = Fraction(s-k,k+1)*Fraction(z+k,z+s-k-1)**q
                    assert lhs == rhs
                    chain += 1
    print('PASS detailed balance/symmetry:', chain)

    shapes = comparisons = turns = 0
    for s in range(4, 36):
        m=(s-1)/2
        for z1 in range(1, 8):
            for z2 in range(z1+1, 12):
                a1, a2 = m+z1, m+z2
                ds=[m-k for k in range((s-1)//2+1)]
                ds=[d for d in ds if d>0]
                F=[log((a1+d)/(a1-d))/log((a2+d)/(a2-d)) for d in ds]
                assert F[0] > F[-1] > 1
                assert all(F[i]>F[i+1]+1e-10 for i in range(len(F)-1))
                shapes += 1
                for q1 in range(2,9):
                    for q2 in range(q1+1,14):
                        signs=[]
                        for k in range((s-1)//2+1):
                            left=Fraction(z1+k,z1+s-k-1)**q1
                            right=Fraction(z2+k,z2+s-k-1)**q2
                            if left==right==1: continue
                            signs.append(sign(right-left))
                        # Inward sequence is nonincreasing: one-turn relative density.
                        assert signs==sorted(signs,reverse=True),(s,z1,z2,q1,q2,signs)
                        r=q2/q1
                        if r < F[-1]-1e-12: assert all(v>0 for v in signs)
                        if r > F[0]+1e-12: assert all(v<0 for v in signs)
                        if F[-1]+1e-12 < r < F[0]-1e-12:
                            assert signs[0]>0 and signs[-1]<0
                        comparisons += 1
                        turns += sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))
    print('PASS critical-ratio shape grids (numeric corroboration):',shapes)
    print('PASS exact adjacent-likelihood phase tests:', comparisons)
    print('PASS observed sign transitions:', turns)

    # An independent exact full-law/MLR test for all three bands.
    s,z1,z2,q1=20,2,5,5
    base=radial_mass(s,z1,q1)
    for q2,expected in [(6,'depolarizing'),(7,'intermediate'),(8,'polarizing')]:
        alt=radial_mass(s,z2,q2)
        diffs=[sign(alt[i+1]*base[i] - alt[i]*base[i+1])
               for i in range(len(base)-1)]
        if expected=='depolarizing':assert all(v<0 for v in diffs)
        elif expected=='polarizing':assert all(v>0 for v in diffs)
        else:assert diffs[0]>0 and diffs[-1]<0
        if expected!='intermediate':
            for i in range(1,len(base)):
                a=Fraction(sum(base[i:]),sum(base))
                b=Fraction(sum(alt[i:]),sum(alt))
                assert (b<a) if expected=='depolarizing' else (b>a)
    print('PASS integer exact three-band certificate and every strict radial tail')

if __name__=='__main__':main()
