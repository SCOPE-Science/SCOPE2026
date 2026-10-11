# Review of Sharp power-weight phase diagram for Cauchy-pole Bergman commutators

## Correctness

PASS. The power-weight Békolle--Bonami range is reconstructed exactly from the defining Carleson-box integrals. After normalizing the lower-half-plane pole, the weighted oscillation quotient is estimated in two exhaustive geometric regimes.

For boxes shorter than their distance scale from the pole, the derivative estimate gives
\[
\mathcal O_s(I)
\lesssim
L^{1-s}R^{-r-1}.
\]
For boxes comparable to that scale, direct integration of
\[
|z+i|^{-r}
\]
gives the required bound. Together these prove weighted BMO membership for
\[
-r\le s\le1.
\]

Necessity is not inferred from those upper bounds. Shrinking boxes give the positive asymptotic
\[
\mathcal O_s(I_L)
\sim
cL^{1-s},
\]
while translated expanding boxes give
\[
\mathcal O_s(I_L)
\sim
c'L^{-r-s}.
\]
These same asymptotics prove failure of the two VMO conditions at the endpoints. Hence
\[
\operatorname{BMOA}_{y^s}
\]
holds exactly on the closed strip and
\[
\operatorname{VMOA}_{y^s}
\]
exactly on its open interior. Applying the source theorems then gives the claimed boundedness and compactness equivalences for both commutators.

## Originality

PASS. The lead source proves a general two-weight characterization for analytic symbols, but its statement remains in abstract weighted BMOA/VMOA form. Full-text inspection found no explicit power-weight/Cauchy-pole specialization and no formula equivalent to
\[
-2r\le u-v\le2
\]
with compactness given by the strict inequalities.

The closest earlier analytic literature characterizes Bergman Hankel operators through BMO, VMO, or Bloch-type spaces in unweighted or structurally different settings. Those results do not dominate this two-weight phase diagram: the lower threshold depends on the decay exponent
\[
r,
\]
whereas the upper threshold is a local first-order boundary effect independent of
\[
r.
\]

Searches using the source title, power-weight aliases, weighted BMOA/VMOA terminology, Cauchy-pole symbols, and equivalent boundedness/compactness formulations did not identify an implication-equivalent published result. A residual risk remains from older weighted Bergman literature using different normalizations.

## Value

PASS. Power weights are the canonical scale-homogeneous test family for the Békolle--Bonami theory, and lower-half-plane Cauchy poles are natural bounded holomorphic symbols with tunable algebraic decay.

The classification exposes a genuine two-scale phenomenon hidden by the abstract theorem. The sharp upper wall
\[
u-v=2
\]
is local and comes from boundary regularity, while the lower wall
\[
u-v=-2r
\]
is global and records decay at infinity. The endpoints are bounded but noncompact, so the result also gives an exact compactness gap rather than only a boundedness test.

This supplies a reusable model for understanding how source/target weight imbalance interacts with symbol regularity and decay in two-weight complex commutator theory.

Same-model review: passed. Independent audit: not yet performed.
