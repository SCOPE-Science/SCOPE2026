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

# Reproducibility and limits

The proof of the universal trace identity uses cyclicity after trace-class approximation, and the moment inequality uses Schatten Hölder plus the Hilbert–Schmidt parallelogram law. The finite-dimensional equality criterion follows from equality forcing \(XY=-YX\), Sylvester's determinant identity, and an explicit eigenvalue-pairing involution. These analytic arguments are necessary; numerical tests cannot establish the theorem.

The standalone program `verify_commutator.py` checks complex matrix samples, paired normal targets and the skewed diagonal example. Its tests are deterministic and require NumPy. The normal-target spectral criterion is proved only for finite matrices, not for all compact normal operators. The cubic gap coefficient has not been optimized.

Scientific review of the displayed result addressed correctness, priority relative to inspected primary sources, and mathematical value. Independent audit is not yet performed.
