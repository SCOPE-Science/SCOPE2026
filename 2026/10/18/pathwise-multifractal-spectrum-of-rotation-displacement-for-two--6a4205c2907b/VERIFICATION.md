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

# Reproducibility

Execute `python check.py` with Python 3. The script tests all six inverse branches on rational target points, finite forward itineraries, exact weighted partition polynomials and finite Legendre identities. Successful output is `FINITE_IDENTITIES_OK` followed by four counts. These finite checks confirm algebraic consistency only; no finite computation verifies asymptotic frequency, the almost-sure strong law, or the Hausdorff lower bound. Those are established in the analytical proof. Independent mathematical assessment was not performed.
