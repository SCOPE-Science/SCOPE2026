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

# Verification details

Running `python3 verify.py` uses only Python standard-library arithmetic. It compares Burnside/derangement and transfer formula against independent canonical orbit counting for all \(1\le q\le8\), \(3\le n\le9\) (56 cases). It independently enumerates all labeled partial assignments for \(1\le q\le5\), \(3\le n\le6\) (20 cases). The output is `VERIFIED 76 exact independent checks`.

The theorem for unbounded \(n\) uses the mathematical transfer matrix, finite-group Euler formula and strict dominant-root comparison, not extrapolation from these checks. There is no independent external audit or general homotopy certificate.
