# Sharp Bogomolov dichotomy on the monomial line L = {(z^d, c z^d)}

## Context
The relative dynamical Bogomolov program for split maps studies common
preperiodic points of pairs (f, g) as preperiodic points of Phi = (f, g) on
the diagonal Delta in (P^1)^2, with fiber powers X_k = Delta^k, and asks for
the special locus carrying dense small points plus uniformity outside it.
The target singles out the monomial stratum and the line
L = {(z^d, c z^d)} with the locus {c in mu_infinity} as its motivating
example. This record certifies the sharp all-k classification on L.

## Definitions
Let d >= 2, f(z) = z^d, g_c(z) = c z^d with c in Qbar^*. Let
Phi = (f, g_c) act on (P^1)^2, Delta the diagonal, X_k = Delta^k with the
fiberwise product action. Prep denotes preperiodic points; mu_infinity the
roots of unity. Let lambda satisfy lambda^{d-1} c = 1, phi(z) = lambda z,
and S(z) = h_f(z) + h_{g_c}(z) the summed canonical height (h = Weil height,
which equals the canonical height for z^d).

## Result
(a) Prep(f) = {0} union mu_infinity affinely (plus infinity projectively)
and Prep(g_c) = {0} union lambda mu_infinity.
(b) lambda in mu_infinity iff c in mu_infinity. Hence affinely
Prep(f) cap Prep(g_c) = {0} union mu_infinity if c in mu_infinity
(infinite), and = {0} if c not in mu_infinity (exactly one point; two
projectively with infinity). Outside {c in mu_infinity} the uniform bound
1 affine / 2 projective holds independently of d.
(c) h_{g_c}(z) = h(z/lambda) and S(z) = h(z) + h(z/lambda) >= h(lambda) =
h(c)/(d-1) for z != 0. If c not in mu_infinity then h(c) > 0 and every
nonzero root of unity has S = h(c)/(d-1) > 0; for
0 < eps < h(c)/(d-1) the only eps-small point is z = 0. If c in mu_infinity
the gap is 0 and S = 0 on mu_infinity.
(d) For every k >= 1, X_k carries a Zariski-dense set of Phi-preperiodic
points iff c in mu_infinity iff each diagonal factor Delta is
Phi-preperiodic. Phi^n(Delta) is the line of slope s_n = c^{e_n} with
e_n = (d^n-1)/(d-1); slopes cycle finitely iff c in mu_infinity and are
pairwise distinct otherwise. A tuple in X_k is Phi-preperiodic iff every
coordinate is a common preperiodic point, so for c not in mu_infinity the
only affine Phi-preperiodic point of X_k is the origin.

## Proof / evidence
Lemma 1 (conjugacy): phi^{-1} o g_c o phi = z^d since
c lambda^{d-1} = 1; conjugacy preserves (pre)periodicity, giving (a) from
Prep(z^d) = {0} union mu_infinity (z != 0 satisfies
z^{d^{n+k}} = z^{d^n} iff z is a root of unity).
Lemma 2 (torsion): from lambda^{d-1} c = 1, torsion passes both ways;
nonzero z is common preperiodic iff z, lambda z in mu_infinity iff
lambda in mu_infinity, giving (b); infinity is fixed by both maps.
Lemma 3 (height gap): canonical height of z^d is h; by conjugacy
h_{g_c}(z) = h(z/lambda); then h(lambda) <= h(z) + h(lambda/z) = S(z) for
z != 0 via h(ab) <= h(a)+h(b), and h(c) = (d-1) h(lambda); Kronecker
gives the dichotomy in (c). Slopes: g_c^n(z) = c^{e_n} z^{d^n} by
induction, so Phi^n(Delta) has slope s_n = c^{e_n}; torsion criterion on
exponents gives (d). Machine spot-checks verify the conjugacy identity
and gap values on rational instances; the proof is deductive, not
experimental. Green-current translation T_Phi^{wedge r} wedge [X_k] != 0
is recorded as a consequence via cited special-curve characterizations,
not proved analytically here.

## Limitations
Covers only the one-parameter line L = {(z^d, c z^d)}, not arbitrary
second factor or higher-dimensional base. The Green-current wedge
identity relies on cited characterizations. No full-target uniform bound
outside L is claimed.

## Reproducibility
Run output/artifacts/line_L_intersection.py and height_gap.py to
regenerate the certificates; all proof steps are in DRAFT.md Lemmas 1-3
and the slope computation.

## References
Baker-DeMarco 2011 (unlikely intersections); Medvedev-Scanlon 2014
(invariant varieties); DeMarco-Mavraki 2023 (pairwise stability, Sec.7
monomials); Mavraki-Schmidt 2024 (relative Bogomolov for split maps).
