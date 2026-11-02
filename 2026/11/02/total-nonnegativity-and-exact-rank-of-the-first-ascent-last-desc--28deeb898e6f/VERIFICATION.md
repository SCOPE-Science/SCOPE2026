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

The accompanying standalone Python 3 program `verify_dyck_boundary.py` was executed from the packaged source tree using the standard library alone. It reported `PASSED 227640 exact checks; exhaustive Dyck paths n<=11, all minors n<=8, 2x2 n<=21`. Explicitly, it compares independent Dyck enumeration against the midpoint Gram formula and closed reflection count, checks row sums and determinant-one rank witnesses, computes all integer minors through semilength eight and all two-by-two minors through semilength 21. All-size claims rely on the stated proof (reflection, midpoint decomposition, path intersection, LGV, Cauchy–Binet), not on finite enumeration. Independent audit has not been performed.
