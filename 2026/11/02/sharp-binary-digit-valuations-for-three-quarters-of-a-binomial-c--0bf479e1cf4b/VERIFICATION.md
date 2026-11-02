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

## Checks
The bundled `verify.py` uses exact unbounded integer arithmetic and tests the recurrence for every positive \(n\le1024\) in the theorem's domain. Successful replay prints `VERIFY_OK cases=768 max_n=1024`. Its tested computations are finite; the separate proof in RESULT.md establishes the universal statement.

## Limits
The calculation cannot certify originality or an infinite theorem by enumeration. Independent audit has not been performed. Values for \(n\equiv0\pmod4\) are deliberately excluded from all assertions.
