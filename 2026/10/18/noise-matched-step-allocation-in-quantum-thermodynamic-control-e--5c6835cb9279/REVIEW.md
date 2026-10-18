# Scientific review

## Correctness

PASS. Square completion gives an exact nonnegative deficit for the continuous cost. The monotone change of variables fixes the unique equality case and the optimal real duration. Strict comparison with metric-speed allocation is an equality-characterized Cauchy–Schwarz inequality. The qubit prefactor follows from direct Gibbs curvature and elementary hyperbolic integrals. For the discrete objective, compactness plus a linear-in-count lower bound establishes minimizer existence; the uniform-grid trial, exact square identity and Lipschitz quadrature inequality establish the claimed uniform asymptotics. A standalone standard-library checker passed 236 finite assertions but is not used in place of proof.

## Originality

PASS under the available primary-literature and indexed-result comparison, with stated residual uncertainty. McKeever–Miller–Nazir (arXiv:2605.04681v1, especially equations (4), (7), (9)–(11)) establish the quadratic noise cost and finite-duration/thermodynamic-length protocol. The new claim is *joint* schedule-and-count optimization, its strict advantage over metric-speed scheduling, and the rigorous small-noise integer-grid allocation law. Large–Chetrite–Sivak (arXiv:1802.02670v2) discuss classical stochastic control and may suggest the scalar matching principle in uniform-friction settings; Large–Sivak (arXiv:1812.08216v2) treat discrete deterministic placement, not the same stochastic integer-count minimization. Broad elementary variational or thermodynamic-speed theory could implicitly cover a specialization; absence from the inspected sources does not prove global novelty.

## Value

PASS. In systems with nonconstant thermal susceptibility, distributing steps uniformly in thermodynamic length can fail to minimize the very stochastic quadratic cost used to motivate it. The explicit qubit comparison quantifies a finite control penalty, while the integer-step theorem establishes that the competing allocation is not merely an artifact of replacing a finite sum with an integral. This gives a concrete design criterion and a falsifiable boundary for weak-noise step-equilibration schedules.

## Limits

Results concern the quadratic response functional rather than full untruncated mean work; high-temperature and low-temperature physical response validity must be independently checked. The real optimal step count need not be an integer, and the discrete equal-step law is asymptotic only. Implicit coverage by general variational inequalities remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
