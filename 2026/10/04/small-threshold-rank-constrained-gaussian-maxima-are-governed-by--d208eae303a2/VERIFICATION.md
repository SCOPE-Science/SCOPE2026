---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The final claim was checked by reconstructing the proof from the definitions rather than by numerical sampling.

For a feasible rank-at-most-\(d\) correlation matrix, choose unit Gram vectors \(u_i\in\mathbb R^d\). With \(W\sim N(0,I_d)\), the event is exactly \(W\in tK(u)\). The lower bound is uniform over all configurations because it is expressed through
\[
a_R=\min_u\operatorname{vol}_d(K(u)\cap B_R),
\]
not through a pointwise asymptotic. Compactness and dominated convergence at fixed \(R\) give existence and continuity; a convergent-minimizer subsequence proves \(a_R\uparrow V_{d,n}\). Restricting the Gaussian integral to a fixed ball yields the liminf. A single finite-volume near-minimizer and dominated convergence yield the limsup.

For the five-direction rank-three specialization, the cited classical five-face theorem gives the right equilateral triangular prism. With unit inradius, its equilateral triangular base has side \(2\sqrt3\) and area \(3\sqrt3\), while its tangent top and bottom planes are distance \(2\) apart. Hence its volume is \(6\sqrt3\), producing the coefficient \(6\sqrt3/(2\pi)^{3/2}\).

Checks do not establish a convergence rate, a fixed-positive-threshold minimizer, or uniqueness of asymptotically minimizing configurations. The historical five-face theorem is used from modern sources that report the proved result; the original nineteenth-century proof was not independently reconstructed.
