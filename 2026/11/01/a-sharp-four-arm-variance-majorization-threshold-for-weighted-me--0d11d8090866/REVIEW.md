# Scientific review: four-arm majorization transition on weighted metric stars

## Correctness

**PASS.** Distances are exactly \(|x-y|\) on one arm and \(x+y\) on distinct arms. Their first and second double integrals yield the stated normalized moments without edge-sampling ambiguities. Exact differentiation gives a positive Schur–Ostrowski quotient for both raw moments whenever there is at least one other positive arm. For three arms, the variance quotient is exactly \(2z(1+12xyz)/3>0\). The four-arm witness has strictly positive coordinates, exact rational negative variance change, and a valid reverse Robin Hood transfer. Continuity extends the reversal to every larger number of arms, while positive local curvature at equal lengths refutes Schur-concavity. The supplied exact-arithmetic checker passed 237 tests; universal conclusions are supported by the displayed symbolic proof.

## Originality

**PASS, best of accessible knowledge.** Dahl (2007) concerns vertex-root distance-vector majorization rather than random continuous two-point distances. Garijo–Márquez–Silveira (2021, inspected full preprint) gives continuous mean-distance algorithms, not the centered second moment or four-arm transition. Mălin–Rovența (2015, accessible full text inspected) study convexity inequalities and flow-function extrema on metric spiders, not two-point uniform-distance moments. Related public records on equiradial metric-star persistence, star Lipschitz norms, and tree graphical zonotope widths address different invariants. A known sharp four-petal threshold for *metric circles sharing a hub* is not a stronger claim about *tree arms*. Full historical priority remains uncertain: Dahl's full article and certain pre-2000 mean-distance references were not available for complete inspection.

## Value

**PASS.** Mean travel distance and travel-time dispersion are natural but different invariants on compact transportation networks. This is a complete sharp parameter-count classification over all positive arm-length vectors, not a numerical slice. It shows that making a star's arms more unequal necessarily increases both raw moments but can *decrease* centered variability, even while retaining a fixed simple tree topology. The specific four-arm threshold is structurally meaningful, especially in contrast with the analogous but topologically distinct result for flowers of circles.

## Scope and limitations

The comparison fixes the number of arms and total length; no generalized tree or nonuniform sampling result is claimed. For four or more arms, the result does not characterize global variance minima. A relevant older paper was accessible only through its abstract, so priority is assessed with a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
