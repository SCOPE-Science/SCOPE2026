# Review

## Correctness

PASS. The continuous switch state and the sampled three-block factorization are explicit. Expanding the local defect gives a second-order endpoint equation that uniquely fixes the first correction to the middle amplitude, followed by an independent third-order tangent equation that uniquely fixes the time coefficient \(r(1-r)/3\). The relevant leading derivatives are nonzero for \(0<\Delta<1\), so the implicit-function argument is nondegenerate away from phase endpoints. The standalone replay solves the exact endpoint equations numerically and reproduces the predicted coefficient.

## Originality

PASS, with residual risk. The 2022/2023 source states the three-part \(-1,\omega_0,+1\) structure for most sampled optima and describes an approximate exponential trend, but it does not state a cubic grid-phase expansion. The general sampled-data PMP of Bourdin–Trélat does not supply an error coefficient. Scarinci–Veliov study a different higher-order discretization for linear-quadratic bang-bang problems and prove a generic second-order estimate, not this qubit branch or coefficient. Dedicated semantic searches returned no matching published finding.

## Value

PASS. The source explicitly highlights the unexpectedly fast convergence of sampled quantum speed limits and the numerical cloud in the one-control case. The finding gives a closed-form explanation for that cloud, identifies a phase-dependent cubic scale, and exhibits exact zero-error grid alignments. This directly sharpens the interpretation of a natural discretization effect in a basic quantum-control model.

## Closest literature and limitations

The closest primary source is Dionis–Sugny itself. The closest general numerical-control comparison found is Scarinci–Veliov's bang-bang discretization analysis; the closest general sampled-data theory is Bourdin–Trélat. The result is deliberately limited to the local three-block endpoint branch and does not certify global optimality for every sample count.

Same-model review: passed. Independent audit: not yet performed.
