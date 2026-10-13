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

# Verification notes

Run `python3 verify.py` in the extracted package. The verifier constructs endomorphism matrices and their multiplication explicitly, tests all generator fixed domains \(D_{g,h}\) through products \(gh\), closes these domains under intersection, and compares them with independently constructed image/kernel rectangles over binary fields. It also generates the complete partial inner automorphism monoid in the smallest nontrivial binary case, rather than assuming its idempotents arise only from generator-domain intersections.

Observed results:

- \(n=2,q=2\): \(16\) matrices; \(11\) idempotent domains (one of size \(1\), nine of size \(2\), one of size \(16\)); exactly \(4\) domains have zero multiplication. The full partial inner monoid has \(52\) maps and \(11\) idempotents.
- \(n=3,q=2\): \(512\) matrices; \(198\) idempotent domains (one of size \(1\), \(49\) of size \(2\), \(98\) of size \(4\), \(49\) of size \(16\), one of size \(512\)); exactly \(36\) domains have zero multiplication.
- \(n=2,q=3\): \(81\) matrices; \(18\) idempotent domains (one of size \(1\), sixteen of size \(3\), one of size \(81\)).

Execution from the extracted package terminates with `VERIFY_OK`. This finite enumeration checks examples, not all dimensions, all fields, or the general proof. There is no independent review or certification.
