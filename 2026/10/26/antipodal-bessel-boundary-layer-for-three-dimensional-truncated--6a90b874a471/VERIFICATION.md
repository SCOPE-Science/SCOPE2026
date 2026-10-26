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

Run `python check.py` with Python 3 and `mpmath` installed. The checker reconstructs Legendre polynomial values via the three-term recurrence, evaluates the exact geometric omitted-tail integral, and tests the predicted sign for selected even degrees. It checks the finite identity and the constant \(J_0(4)\), including a rational alternating-sum bound. The mathematical proof is in `RESULT.md` and does not rely on a finite test or simulation to certify an infinite-dimensional or asymptotic statement.

The calculation uses exact mathematical real arithmetic in the theorem and arbitrary precision only for diagnostic finite examples. The tested cases do not establish bounds for all \(N\), and the displayed liminf inequalities come from a fixed-parameter argument followed by an ordinary limit.
