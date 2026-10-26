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

# Verification record

The deterministic, standalone `verify.py` recomputes the transformed generator exactly with symbolic algebra. It builds the original four-by-four weighted Laplacian, takes numerical matrix exponentials independently of the closed form, enumerates all integer-valued graph-distance-Lipschitz potentials with a fixed basepoint (these contain every vertex of the Lipschitz polytope), and compares the resulting induced norm against both formula branches on 140 explicitly enumerated weight/time pairs.

The analytic assertions for every positive real conductance and every nonnegative time are proved in `RESULT.md`; finite computations alone cannot establish them. The verification script checks representative cases on both sides of the threshold and the singular fast-edge limit. Floating-point comparisons are made only within stated tolerances. The one-edge unit metric is kept separate from conductance throughout.

Independent audit has not been performed.
