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

# Reproducibility and verification

Run `python checks/check.py` from the extracted package root with Python 3 and SymPy installed. The checker generates the normal cones for all \(4\le n\le7\) directly from the braid-order description, without loading any precomputed polytope, tests the unique primitive four-ray relations and unimodular bases, and verifies the complete maximal-cone and singular-component counts. It returns `VERIFY_OK` after exact-arithmetic assertions. Reproduced counts are described in `RESULT.md`.

The checker is a finite consistency test. The all-parameter mathematical argument consists of the hyperplane-deletion chamber classification, explicit saturated lattice basis and semigroup computation, identification of all minimal singular cones, and integral description of their star fans. No symbolic-algebra log is treated as a substitute for those mathematical steps. The theorem concerns reduced singular support and generic transverse local rings; it makes no claim about the full Jacobian singular scheme. Independent audit has not been performed.
