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

# Reproducible checks and proof boundary

Run the included `verify.py` with Python 3 and NumPy. It checks coordinate products of unit pairs, performs constructive inverse factorizations of random feasible complex coefficient vectors, and verifies the exact three-phase sharpness witness for several interior overlap parameters. It also tests that the affine phase-rank test is nondegenerate in the three-site witness.

The checker is supplementary finite evidence. It does not establish the result for all dimensions, phases, compact domains, or function families. The mathematical proof is the four-step argument in `RESULT.md`. No independent audit has been performed.
