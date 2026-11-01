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

The exact statement is proved by exhaustive classification of possible edge-pair routes, triangle-area integration for the exceptional pair, and direct differentiation of the resulting finite positive-part quadratic. These steps apply to arbitrary finite connected simple factors with positive geodesic edge lengths.

For reproducible finite consistency checks, place `check_product_detour.py` and `check_product_multifactor.py` in the same folder and run `python check_product_detour.py` and `python check_product_multifactor.py` with standard Python. The first program compares intrinsic metric-product edge-point shortest routes with separately calculated ambient factor distances for 14 weighted two-factor products and 86,336 point pairs. The second performs the same exact-rational check for five products with three or four factors, totaling 51,728 point pairs. Both finished successfully with 138,064 exact-rational pair comparisons in total.

The programs use finitely many rational edge coordinates and do not constitute exhaustive computational proof across all graphs or real edge lengths. No independent human or external mathematical audit has been performed. The historical originality assessment remains limited by older full-text availability.
