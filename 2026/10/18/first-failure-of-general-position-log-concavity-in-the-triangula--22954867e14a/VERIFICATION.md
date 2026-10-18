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

# Verification record

Run `python3 verify.py` using standard-library Python 3.9 or newer. The included program checks integer component recurrences against an algebraically separate signed-rational coefficient formula at *all coefficients* for orders 0–30, tests every nonzero coefficient and each internal log-concavity determinant at orders 3–29, and checks the three exact order-30 coefficients and their negative determinant. It independently enumerates general-position subsets from adjacency/forbidden-geodesic triples for orders 3–6 (33,864 subsets total). The original reproducible output is in `verification_output.txt`.

Finite arithmetic suffices to certify the sharp **least** failure order because all smaller orders have been checked with a recurrence mathematically valid for every order. These checks do not prove a global theorem for orders greater than 30 and do not amount to independent external review.
