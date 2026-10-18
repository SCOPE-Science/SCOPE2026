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

The analytic argument establishes exact finite-height orthogonal block decomposition, Hilbert--Schmidt convergence of each normalized block to rank one, separation of all deeper blocks by compression monotonicity, and thus the complete fixed-rank singular-value limit. Perron--Frobenius positivity proves finite-height simplicity of the largest singular value.

Run `python checker.py` in a Python environment with NumPy. The script constructs the original vertex-ancestor averaging matrix without using the predicted decomposition, calculates its singular values, compares them with those of all reduced blocks for small finite regular trees, and compares several normalized blocks with their limiting values. It passed 133 assertions in the recorded execution. Finite checks do not certify the infinite-height theorem; the proof supplies that step.

Scientific limitations: branching number and target rank are fixed; the theorem does not include height-dependent ranks, nonregular trees or continuous metric trees. There is no independent mathematical validation or priority certification.
