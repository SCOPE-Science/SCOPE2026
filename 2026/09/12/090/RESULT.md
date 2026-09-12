# Unique maximizing measure for a translated degree-2 sine potential on the doubling map

## Context
Ergodic optimization asks which invariant measures maximize the integral of a given
potential. For the doubling map T(x) = 2x mod 1 on the circle S^1 = R/Z, translations
of the cosine are known (Bousch and successors) to be uniquely optimized by Sturmian
measures. Degree-2 trigonometric potentials with a genuine second harmonic lie outside
that one-parameter family, and their exact maximizing measures and maximum values are
generally unknown. The admitted target is a dichotomy between two concrete candidates:
the period-2 orbit O2 = {1/3, 2/3} averaging 1/2 and a period-7 orbit
Q = {43, 45, 53, 85, 86, 90, 106}/127 averaging about 0.4876870211, selected by an
exhaustive periodic-orbit census through period 7.

## Definitions
- T(x) = 2x mod 1 on S^1 = R/Z.
- phi(x) = sin(2 pi (x - 1/4)) + (1/2) sin(4 pi (x - 1/4))
  = -cos(2 pi x) - (1/2) sin(4 pi x), Lipschitz (indeed analytic).
- beta(phi) = max { integral of phi dmu : mu T-invariant Borel probability }.
- mu_O2 = (delta_{1/3} + delta_{2/3}) / 2, the orbit measure on O2.
- A Lipschitz function u: S^1 -> R is a calibrated subaction with value beta if
  F(x) := beta - phi(x) + u(T(x)) - u(x) >= 0 for all x, with equality exactly on
  the support of the maximizing measure.

## Result
Alternative (A) holds. For T and phi as above, beta(phi) = 1/2 and the unique
phi-maximizing measure is the period-2 orbit measure mu_O2 on O2 = {1/3, 2/3}.
Alternative (B), that the unique maximizer is the orbit measure on the period-7 orbit
Q, is false because the Q-average 0.4876870211... is strictly below 1/2.

The certificate uses the explicit rational trigonometric polynomial u of degree 12
with coefficients a_1,b_1,...,a_12,b_12 in artifacts/u_coeffs.txt, beta = 1/2, and
F(x) = 1/2 - phi(x) + u(2x mod 1) - u(x), a trigonometric polynomial of degree 24.
F >= 0 on S^1 with equality exactly on {1/3, 2/3}, and F >= 3/1000 =: eta off the
0.02 circular neighbourhood U of O2 (with F >= 0.2355 on the strip |x - 1/2| <= 0.001).

## Proof / evidence
Elementary values: phi(1/3) = 1/2 + sqrt(3)/4, phi(2/3) = 1/2 - sqrt(3)/4, so O2
averages exactly 1/2; phi(0) = -1; global max 3 sqrt(3)/4 at x = 5/12. The Q average
is 0.4876870211 < 1/2. The function u satisfies three exact interpolation constraints
(C1), (C2a), (C2b) forcing F = F' = 0 at 1/3 and 2/3, verified in exact rationals.

Algebraization with t = tan(pi x) gives F(x(t)) = R(t)/(1+t^2)^24 with R a degree-48
rational polynomial (artifacts/R_coeffs.txt), rebuilt from u coefficient-by-coefficient
in exact arithmetic. The exact identity R(t) = (t^2 - 3)^2 S(t) holds with S of degree
44 (artifacts/S_coeffs.txt). A PARI-free exact Sturm engine shows S has no real root
and S(0) = 1/6, hence S > 0 everywhere, in fact S >= 3/200; R has exactly two distinct
real roots, which by the factorization are t = +- sqrt(3), i.e. x = 1/3, 2/3; and
F(1/2) = 599383/1425000 > 0. Thus F >= 0 with zeros exactly on O2.

The uniform gap: with Fourier data S1 = 1511419981/51300000 and Lipschitz constant
L1 = 2 pi S1 <= 185.12, F >= F(1/2) - L1 * 0.001 >= 0.2355 on the strip. Elsewhere t
ranges over compact pieces covered by rational intervals [0,1.506], [2.014,319],
[-319,-2.014], [-1.506,0], whose containment follows from rigorous tan enclosures with
margins ~1e-3 or better. Critical points of F in t are roots of
D(t) = R'(1+t^2) - 48 t R (degree 48); exact Sturm counts per piece are 9, 5, 3, 12,
and bisection with Sturm recounts isolates every root in a box of width <= 1e-9
(artifacts/critical_boxes.json; box-count sums match Sturm totals so none is missed).
Exact Fraction-interval Horner evaluation gives all critical values >= 0.00307055 and
all piece endpoints >= 0.0041, hence min over the complement cover exceeds 3/1000.

Ergodic conclusion: for any invariant mu, integral of (u o T - u) vanishes, so
integral phi dmu = 1/2 - integral F dmu <= 1/2, i.e. beta(phi) <= 1/2; O2 attains 1/2
so beta(phi) = 1/2. Writing phi - 1/2 = (u o T - u) + r with r = -F <= 0 continuous
vanishing exactly on O2, any maximizing mu has integral r dmu = 0 hence support in O2;
the only invariant measure supported on the period-2 orbit is mu_O2. Uniqueness follows.

## Limitations
The certificate is computer-verified exact rational arithmetic (Sturm sequences,
interval Horner evaluation) rather than hand-checkable; float optimization and PARI
were discovery-only and are not part of the proof. Uniqueness uses continuity of r and
invariance. No claim is made about zero-temperature limits, Sturm optimality beyond
this potential, or a completed census above period 7.

## Reproducibility
Run `python3 artifacts/verify_certificate.py` (stdlib only, exact Fractions,
PARI-free Sturm engine). It checks [C1] constraints, [C2] full R-from-u rebuild
(all 49 coefficients), [C3] factorization, [C4] positivity S >= 3/200, [C5]
exactly-two-roots, [C6] gap > 3/1000 with Sturm recounts. Expected output:
ALL CHECKS PASSED. Re-verified independently by the auditor in the audit workspace.

## References
- O. Jenkinson, Ergodic optimization in dynamical systems, Ergodic Theory Dynam. Systems (survey).
- T. Bousch, cosine-translation Sturmian optimization line for the doubling map.
- R. Gao, Regularity of calibrated sub-actions for circle expanding maps and Sturmian optimization, Ergod. Th. Dynam. Sys. 43 (2023), doi:10.1017/etds.2022.32.
- Generic typical periodic optimization results for expanding/unimodal/Thurston/beta maps (existential background only).
