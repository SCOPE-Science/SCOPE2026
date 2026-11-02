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

Run `python3 verify.py` in a standard Python 3 environment. The script builds all objects afresh and reports five assertion-guarded statuses: TRITANGENTS_OK, CUBIC_OK, QUARTIC_OK, LIFTS_OK and WEYL_OK. It performs exact exhaustive signature enumeration for all multisets of 45 tritangents of sizes two, three and four, with no omitted cases. All 540 minimal quartic fibers are checked individually, as is their orbit closure. No floating-point computation, external library or downloaded dataset is needed.

These finite checks concern an explicitly finite incidence configuration common to all smooth characteristic-zero cubic surfaces. Their application across that family rests on the classical blowup description and its exhaustive 27-line and 45-tritangent classification. They do not settle generators of degree five or higher, or establish independent priority review.
