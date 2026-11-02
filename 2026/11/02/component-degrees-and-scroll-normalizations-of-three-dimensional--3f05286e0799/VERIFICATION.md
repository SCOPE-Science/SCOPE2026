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
The checker `check_degree_profile.py` uses exact integers and SymPy rational matrix rank, verifies pairwise orthogonality, and computes full Jacobian ranks at explicit general points on each component family for \(4\le h\le12\). The run printed `VERIFY_OK`. It also checks \(4\cdot8+4\cdot8=64\) at \(h=4\) and the closed-form degree arithmetic. General \(h\) is established by the rank arguments and projective bundle/Chern-class calculation in `RESULT.md`, not by bounded tests.

The original Gram ideal may contain embedded nilpotents when \(h\ge5\); no global radicality claim is made. The independent mathematical audit is not performed. The scientific priority comparison is qualified as described in `REVIEW.md`.
