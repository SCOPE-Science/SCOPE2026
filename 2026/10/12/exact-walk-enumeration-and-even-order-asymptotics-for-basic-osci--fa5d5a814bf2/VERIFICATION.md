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
The proof in `RESULT.md` is symbolic and applies in every order. The finite checker `verify.py` is a regression aid only.

Checks performed by the packaged script:

- enumerate every positive vector satisfying Xie's three profile conditions for orders \(2\) through \(9\);
- independently compute the weighted-walk formulas for the same orders and compare exact counts;
- compute the recurrence through order \(15\) and compare the displayed sequence;
- numerically cross-check the algebraic dominant constant \(3\sqrt{2-\sqrt3}\) against the logarithmic integral used in the proof.

A successful replay prints `CHECK_OK`. No finite enumeration is used to infer the all-order theorem or the asymptotic.
