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

The accompanying standard-library `verify.py` implements the temporal matching updates directly, then independently implements the interval-block criterion and the rational-series coefficient recurrence. It exhaustively compares every initial subset for \(2\le n\le14\), \(1\le T\le10\) (130 parameter instances, 327,640 initial subsets), with polynomial, minimum-cardinality, and optimum-count checks. It also tests the \(n=2T\) parity statement through \(T=12\).

Command: `python3 verify.py`.

Expected ending: `VERIFY_OK`.

The infinite claims are proved by superposition and exact interval/offset enumeration. Finite checks alone would not establish them. Historical priority for the generating-function statement is provisional because the full manuscript of a relevant earlier research archive was not accessible. Independent audit has not been performed.
