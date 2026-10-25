"""Reproducibility checks for weighted Möbius-ladder Max-Cut SDP formulas.

All computations use the Python standard library. These checks verify finite
instances; the family-wide assertions require the proof in RESULT.md.
"""
from fractions import Fraction
from math import cos, sin, pi, isclose
import random

rng = random.Random(20261024)
brute_checks = 0
spectrum_checks = 0
rounding_checks = 0
bound_checks = 0


def edges(n):
    N = 2 * n
    cyc = [(i, (i+1) % N) for i in range(N)]
    rungs = [(i, i+n) for i in range(n)]
    return cyc, rungs


def exact_cut(n, t):
    N = 2 * n
    cycle, chords = edges(n)
    best = Fraction(-1)
    for code in range(1 << (N-1)):
        s = [0] + [(code >> i) & 1 for i in range(N-1)]
        c = sum(s[i] != s[j] for i,j in cycle)
        d = sum(s[i] != s[j] for i,j in chords)
        val = Fraction(c) + t*d
        if val > best:
            best = val
    return best


def cut_formula(n,t):
    return Fraction(2*n)+n*t if n%2 else max(Fraction(2*n),Fraction(2*n-2)+n*t)


def sdp_formula(n,t):
    if n%2:
        return 2*n+n*t
    c=cos(pi/n)
    return 2*n if t <= 1-c else n*(1+c+t)


for n in range(3,10):
    for t in [Fraction(0),Fraction(1,8),Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(3)]:
        assert exact_cut(n,t) == cut_formula(n,t), (n,t)
        brute_checks += 1

for n in range(3,29):
    N=2*n
    cyc,chords=edges(n)
    for t in [0.0,0.05,0.25,0.5,1.0,3.0]:
        e=[2*cos(pi*k/n)+t*(-1)**k for k in range(N)]
        spectral_bound = N*(2+t -min(e))/4
        assert isclose(spectral_bound,sdp_formula(n,t),rel_tol=1e-12,abs_tol=1e-10)
        spectrum_checks += 1
        k=n if (n%2 or t<1-cos(pi/n)) else n-1
        theta=pi*k/n
        X=lambda i,j: cos(theta*(i-j))
        gram_obj=sum((1-X(i,j))/2 for i,j in cyc)+t*sum((1-X(i,j))/2 for i,j in chords)
        assert isclose(gram_obj,sdp_formula(n,t),rel_tol=1e-11,abs_tol=1e-9)
        bound_checks += 1

for n in range(4,31,2):
    theta=pi*(n-1)/n
    cyc,chords=edges(n)
    for j in range(160):
        phi=2*pi*(j+0.27182818284)/160
        spins=[cos(theta*i-phi)>0 for i in range(2*n)]
        no_rim=sum(spins[a]==spins[b] for a,b in cyc)
        cut_chords=sum(spins[a]!=spins[b] for a,b in chords)
        assert (no_rim,cut_chords)==(2,n),(n,j,no_rim,cut_chords)
        rounding_checks += 1

print('VERIFY_OK')
print('exact_integer_cut_cases:',brute_checks)
print('Fourier_extreme_eigenvalue_cases:',spectrum_checks)
print('explicit_unit_vector_SDP_cases:',bound_checks)
print('nondegenerate_hyperplane_cases:',rounding_checks)
print('finite_checks_are_not_a_proof_of_the_infinite_family')
