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
The proof's universal steps are scalar Minkowski equality, trace-dual polar-support rigidity, a full-rank pairing argument in the matrix domain, and finite-dimensional compactness. They do not depend on numerical experiments.

Run `python checker.py` with NumPy installed. Its deterministic checks cover the explicit diagonal isometries, all pairwise cycle distances for sizes 4 through 24, scalar Hilbert Fourier witnesses and randomly generated complex matrices. The observed run passed 5,018 finite assertions.

The checker does not enumerate all possible matrices or decide exact subthreshold constants. Its finite tests alone cannot establish a universal theorem, and independent verification has not occurred.
