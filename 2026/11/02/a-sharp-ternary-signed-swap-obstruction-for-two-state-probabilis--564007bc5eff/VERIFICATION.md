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

Run `python3 verify.py` with Python 3.10 or newer and compare with `verification_output.txt`. The checker enumerates all \(2,538\) surjective ternary words of lengths \(3\) to \(7\), both by sign/rank testing and by cycle detection, and verifies the canonical representatives. The six inequalities for `0120102` and the general affine commutator are proved in RESULT.md rather than inferred from the checker. The finite script does not classify all two-state realizable words and does not prove exhaustive publication priority.
