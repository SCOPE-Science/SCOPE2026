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

Run `python3 verify.py` (requires the commonly available `sympy` package) to check the universal characteristic-three polynomial reductions and the \(j\)-discriminant identity. This verifies algebraic equations for indeterminate parameters rather than isolated numerical examples. It does not by itself prove the ramification and \(3\)-rank assertions; these follow from the local expansion and the stated Deuring–Shafarevich theorem in RESULT.md.

The smoothness criterion includes the boundary chart \(X+Y+Z=0\), where a unique point occurs with intersection multiplicity \(4\). It excludes exactly the two singular parameter values. All conclusions are geometric over an algebraically closed field of characteristic \(3\).

No independent scientific audit was performed.
