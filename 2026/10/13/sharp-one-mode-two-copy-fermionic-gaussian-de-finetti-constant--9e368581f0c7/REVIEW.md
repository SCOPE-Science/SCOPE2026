# Self-review

## Correctness
**PASS.** The one-mode covariance space is one-dimensional, so the source's exchangeability criterion becomes the exact box \(u,v\in[-1,1]\). The retained two-copy covariance is diagonalized by a physical copy rotation, reducing both states to commuting Bernoulli products. The four probability differences are computed explicitly, and their absolute values give \(2|h|+2h^2\) for \(|h|\le1/2\). The maximum and equality cases therefore follow without numerical extrapolation. The source's extremal covariance family proves attainability.

Risk: the proof depends on the same Majorana sign and graded-copy convention as arXiv:2610.01860v1. Those conventions, Proposition IV.3, and Remark IV.5 were checked directly in the full text. The finite checker is corroborative only.

## Originality
**PASS.** The closest source, arXiv:2610.01860v1, gives the general state bound \(4m_A(k-1)/n\) and separately proves sharpness of the covariance suppression constant, but does not state a sharp state-level one-mode two-copy value. arXiv:2409.17953v3 gives the generic mixed-Gaussian perturbation inequality used in that proof; it does not optimize the constrained exchangeable family. arXiv:2508.18532v2, arXiv:2607.25779v1, and arXiv:1708.01266v1 concern different extension symmetries or approximation targets.

Residual risk: because the anchor is very recent, an independently derived equivalent formula may not yet be indexed. The searches and implication comparisons are recorded in `AUDIT.json`.

## Value
**PASS.** The constant measures the exact state-level cost of finite exchangeability in the minimal nontrivial Gaussian setting. It exposes a genuine factor-of-two asymptotic loss in the anchor theorem's general covariance-to-state conversion and identifies exactly which extensions are extremal. This is a natural sharpness question for the new finite Gaussian de Finetti theorem, not a recomputation of a known table or an arbitrary small parameter slice.

## Closest literature and limitations
The result is restricted to one mode per copy and \(k=2\); it does not settle the sharp constants for more retained copies, higher local mode number, non-Gaussian states, or alternative fermionic exchangeability notions. It also does not improve the already-sharp covariance suppression bound.

Self-review: passed. Independent audit: not yet performed.
