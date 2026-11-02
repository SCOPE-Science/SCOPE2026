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

# Reproducible calculations

Run `python checks/resonant_negativity_check.py` using Python 3 with SymPy, NumPy and SciPy installed. The checker was executed with all assertions passing. Its exact symbolic computations construct the four polynomial spectral projectors, verify their completeness and reconstruction of the generator, compute the partial-transpose determinant at both resonances, and evaluate the second-order perturbation coefficient as \(4c^2-1/4\).

For the two angles, exact algebra yields the same determinant, \(-p^2(1-p)^3/[16(2-p)(1+(1-p)^2)^2]\). The stationary limiting partial transpose has eigenvalues \(0,1/4,1/4,1/2\). The symbolic first-order kernel expectation is zero. The second-order direct term is \(8c^2\), while the positive-spectrum mixing term equals \(4c^2+1/4\). These identities reproduce the proof's critical finite algebra.

Finite-precision checks additionally cover five scaled detunings and three reset probabilities at each resonance. The scaled smallest-eigenvalue discrepancy from its limiting expression is below the specified numerical tolerance in all tested cases. A separate channel-iteration computation at reset probability \(0.12\) converges to the spectral-resolvent stationary state within Frobenius norm \(10^{-12}\).

The analytic extension, compact-uniform asymptotics, and local uniqueness of the zero-eigenvalue curves follow from the written proof rather than any finite numerical scan. This verification does not independently confirm originality, publication priority, broad physical applicability, or third-party certification.
