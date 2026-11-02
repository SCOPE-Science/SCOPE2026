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

The standalone `verify.py` program constructs the finite nonzero partial translation maps as explicit graphs and multiplies them by direct partial-map composition. For every \(1\le n\le10\), its exact counts match the polynomial \(n(n-1)(n+1)(n+2)(n^2+n-1)/30\); the number of commuting ordered pairs is independently split between zero and nonzero common products. An additional symbolic power-sum check reproduces the exact polynomial.

The finite enumeration does **not** establish the limiting theorem. The infinite proof uses the exact interval-disjointness count and a four-hyperplane upper bound on commuting nonzero products. No independent external verification or audit has been undertaken.
