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

# Reproducible checks and limitations

Run `python check.py` with the Python standard library. This checker evaluates the specified rational-height and rational-gain instances directly from \(f_H\) and the controller formula, constructs the full two-branch return cylinders, and compares exact rational interval lengths to the predicted survival law. It separately subdivides the endpoint map into exact affine pieces through eight iterates and checks the finite-time capture tail.

The executed checker reported 980 passing exact-rational assertions. These finite checks verify representative calculations but do not establish all-real-parameter correctness, global novelty, independence, or external certification. The general proof is the explicit branch/cylinder argument in `RESULT.md`. No independent audit has been conducted.
