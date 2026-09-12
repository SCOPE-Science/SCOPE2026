# Exact ordinary-line ledger for the pinned two-circle 21-point set D21

## Context

The Dirac–Motzkin theorem (Dirac 1951, Motzkin 1951; proved for large n by Green–Tao 2013) states that every non-collinear set of n points in the Euclidean plane spans at least n/2 ordinary lines (lines containing exactly two of the points) once n is large. The unconditional Csima–Sawyer bound gives only 6n/13, i.e. about 9.7 at n = 21. Sharp and near-sharp examples for large n live on cubics and one-circle Boróczky families, leaving symmetric multi-component supports essentially untested at fixed small n. The natural next test object is a pinned two-circle competitor: two concentric decagons plus the center.

## Definitions

Let zeta = zeta_20 = exp(2*pi*i/20) and identify R^2 with C. Define D21 as:

- inner decagon I_k = zeta^{2k} for k = 0,...,9 (10 points on the unit circle at angles 2k*pi/10);
- outer decagon O_k = 2*zeta^{2k+1} for k = 0,...,9 (10 points on the circle of radius 2 at offset angles 2k*pi/10 + pi/10);
- center C = 0.

So |D21| = 21, no three of the defining circles coincide, and the offset pi/10 is pinned. A line is ordinary if it contains exactly two points of D21. The Dirac–Motzkin threshold at n = 21 is ceil(21/2) = 11. The support polynomial Q(x,y) = (x^2+y^2-1)(x^2+y^2-4) is the degree-4 polynomial vanishing exactly on the two circle components carrying 20 of the 21 points.

## Result

D21 consists of 21 distinct non-collinear Euclidean points and spans exactly 180 ordinary lines, hence in particular at least 11. Precisely:

- 190 distinct spanned lines in total;
- 180 ordinary (2-point) lines: 40 inner–inner (II), 100 inner–outer (IO), 40 outer–outer (OO);
- 10 rich (3-point) lines, each an antipodal diameter through the origin: 5 of type {I_k, I_{k+5}, C} and 5 of type {O_k, O_{k+5}, C};
- no other collinearities: the only collinear triples are those 10.

## Proof / evidence

Exact computation in the cyclotomic field Q(zeta_20) with basis 1, zeta, ..., zeta^7, minimal polynomial z^8 - z^6 + z^4 - z^2 + 1, and exact rational (Fraction) coefficients. Inner points are zeta^{2k}, outer points are 2*zeta^{2k+1}, center is 0. Conjugation is the Galois automorphism zeta -> zeta^{-1} = zeta^{19}. Collinearity of complex points a, b, c is tested by exact vanishing of (a-b)*conj(a-c) - conj(a-b)*(a-c).

1. Distinctness: all 21 field elements are pairwise distinct; the circles are disjoint and the center is off both.
2. Enumeration: of all C(21,3) = 1330 triples, exactly 10 are collinear, namely {I_k, I_{k+5}, C} for k = 0,...,4 and {O_k, O_{k+5}, C} for k = 0,...,4.
3. Grouping: grouping the C(21,2) = 210 pairs by shared collinear triples (union-find) yields 190 spanned lines; each grouped line's full point set is re-verified collinear triple by triple.
4. Count: 180 lines have exactly 2 points; 10 have exactly 3 (all through the center). Since 10 rich lines consume 10*3 = 30 pairs and 180 ordinary lines consume 180 pairs, 30 + 180 = 210 = C(21,2), closing the ledger.
5. Self-checks: the script asserts z^20 = 1, i^2 = -1 with i = zeta^5, |zeta^k|^2 = 1 for all k, and the final count identities before printing VERIFY_OK.

Replay: `python3 output/artifacts/verify.py` (stdlib only) prints VERIFY_OK and writes `output/artifacts/ledger.json` with the full type census.

## Limitations

The certificate applies only to the pinned offset pi/10 definition of D21 and counts ordinary lines under exact algebraic equality (no floating point). It does not classify other two-circle offsets, prove a general degree-4 partitioning theorem, or address ordinary-line counts for larger two-circle families. The degree-4 polynomial Q is used as the support/cell ledger for this instance (vanishing on 20/21 points; cells: open disk, open annulus, exterior), not as a general incidence theorem.

## Reproducibility

Stdlib-only Python 3 script `output/artifacts/verify.py` performs the exact enumeration and writes `output/artifacts/ledger.json`. Independent re-run in this audit reproduced VERIFY_OK with 190 spanned lines, 180 ordinary, and 10 rich lines with the 40/100/40 II/IO/OO split.

## References

- B. Green, T. Tao, On sets defining few ordinary lines, Discrete Comput. Geom. 50 (2013), 409–468; arXiv:1208.4714.
- J. Csima, E. Sawyer, There exist 6n/13 ordinary points, Discrete Comput. Geom. 9 (1993), 187–202.
- G. A. Dirac, Collinearity properties of sets of points, Quart. J. Math. 2 (1951), 221–227.
- T. Motzkin, The lines and planes connecting the points of a finite set, Trans. Amer. Math. Soc. 70 (1951), 451–463.
- E. W. Weisstein, Ordinary Line, MathWorld, https://mathworld.wolfram.com/OrdinaryLine.html.
- Orchard-planting problem, https://en.wikipedia.org/wiki/Orchard-planting_problem.
