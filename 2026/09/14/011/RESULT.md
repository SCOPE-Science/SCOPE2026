# Disproof of the uniform cusp-modulus band for diagonal double fillings of the magic manifold

## Context

Let M = s776 be the magic manifold, the complement of the minimally twisted
3-component chain link, with cusps (E0, E1, E2) in standard
meridian-longitude framing. For integer n with |n| >= 6, let N_n be the
simultaneous filling of slope 1/n on E1 and 1/n on E2, leaving E0 unfilled.
The N_n are one-cusped manifolds containing two short core geodesics whose
lengths tend to 0 as |n| -> infinity, with geometric limit M. Normalize the
remaining cusp E0 at its maximal horoball so its meridian has length 1 and
let theta_n in the upper half-plane be its cusp modulus. The target claim
asserted every N_n is hyperbolic and satisfies 1.30 <= Im(theta_n) <= 2.00
and |Re(theta_n)| <= 0.35. Either a proof of the band for all |n| >= 6 or an
explicit certified counterexample decides the target; numerics alone do not
count.

## Definitions

- s776: SnapPy census triangulation of the magic manifold (volume
  approximately 5.33348956690).
- (1,n) filling: SnapPy Dehn-filling coefficients (p,q) = (1,n) on each of
  cusps 1 and 2, i.e. slope 1/n in the topic language; cusp 0 left at
  (0,0). The alternative (n,1) sequence is a different family.
- theta: meridian-normalized cusp modulus L/M, a scale-invariant ratio, so
  any horoball size gives the same value.
- Hyperbolic: existence of a positively oriented solution of the complete
  logarithmic gluing system (edge, completeness, and filling equations).

## Result

The uniform band is FALSE. The manifold N_6, the simultaneous (1,6)
filling on E1 and E2 with E0 unfilled, is hyperbolic, and its cusp modulus
satisfies Re(theta_6) in [0.465477568846, 0.465477568850] and
Im(theta_6) in [1.193992809179, 1.193992809183]. Hence
Re(theta_6) >= 0.4654 > 0.35 and Im(theta_6) <= 1.1940 < 1.30, each with
margin exceeding 0.1, violating both claimed bounds. Consistently, the
geometric limit M itself has Re = 0.5 > 0.35.

## Proof / evidence

Hyperbolicity: N_6 uses 6 tetrahedra. SnapPy's enough_gluing_equations
selects 6 independent rectangular equations. At the SnapPy float shapes
(all Im > 0.34) the log-form Jacobian has condition number approximately
58.3 and log residuals at most 5e-15. A Krawczyk test in mpmath.iv interval
arithmetic at 50 decimal digits with outward rounding on every operation
and integer powers by repeated interval multiplication certifies a box of
half-width 1e-8: K(X) is strictly inside X in all 6 components (existence
and uniqueness of a zero of the independent system in X); inf Im > 0 on
every box (minimum 0.3496); log-lift validity holds (|log| <= 1e-5 < 0.1 on
X for each independent equation); and a full log-system audit over all 10
SnapPy log rows (6 edges and 2 fillings within 2.2e-6 of 2 pi i, cusp-0
rows within 3.1e-7 of 0) holds far below the 0.1 branch-ambiguity
threshold. The audit independently re-executed the interval Krawczyk stage
from the recorded equations and float shapes and confirmed strict inclusion
in all components, positivity, and log-lift bounds. Hence the box contains
genuine positively oriented shapes solving the complete hyperbolic gluing
system.

Cusp modulus: replaying SnapPy's ComplexCuspCrossSection accumulation
(horotriangle side propagation with exact kernel peripheral-curve integers
and face pairings, seed convention validated by matching SnapPy float
translations to 10 digits) with interval shapes over the certified boxes
encloses theta_6 in a box of width approximately 3e-12 containing the float
value 0.465477568848 + 1.193992809181i. The certified box lies strictly
outside the band in both coordinates, with margin over 1e10 times the
interval width.

Slope identification: (1,n) is the slope-1/n sequence, confirmed by volume
convergence to the parent volume as |n| grows (4.9949 at n=6, 5.3016 at
n=20, 5.3335 limit). The Martelli-Petronio classification is consistent:
(1/6,1/6) is not among exceptional slopes, so N_6 is hyperbolic; that
classification states no cusp modulus and no band.

## Limitations

Slope identification rests on the standard SnapPy (p,q) framing plus
convergence behavior, not on a from-diagram framing proof; scale invariance
makes the maximal-horoball normalization immaterial to the ratio. Interval
rigor depends on mpmath.iv outward rounding for the used operations
(+,-,*,/,log,abs) with integer powers by repeated multiplication; no
second interval library cross-check was performed. Only n=6 is certified;
no claim is made about other n or about any sub-band for larger |n|.

## Reproducibility

Requires SnapPy (topology and float seeds only), numpy, mpmath. Run
python3 output/artifacts/lane1841_krawczyk.py (asserts CERTIFIED: True) and
python3 output/artifacts/lane1841_cusp.py (asserts CERTIFIED OUTSIDE BAND:
True). Certificates: output/artifacts/lane1841_krawczyk.json,
output/artifacts/lane1841_cusp.json; topology snapshot:
output/artifacts/lane1841_n6_snapshot.json.

## References

- B. Martelli, C. Petronio, Dehn filling of the magic 3-manifold,
  arXiv:math/0204228.
- J. S. Purcell, Cusp shapes under cone deformation, arXiv:math/0410233.
- SnapPy census manifold s776; SnapPy enough_gluing_equations and
  ComplexCuspCrossSection machinery (float seeds and combinatorics only).
