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

# Reproduction and limits

Run `python3 verify.py`. It uses only the Python standard library and directly enumerates all zero-forcing input sets of triangular graphs of orders 3, 4, 5, 6. The direct line-graph forcing algorithm is separate from the disjoint-set check for foresthood and an isolated vertex. Coefficients are additionally checked against the exact labeled-forest recurrence and inclusion-exclusion. Expected terminal marker: `VERIFY_OK orders=3..6 all_subsets= 33864 forest_EGF_recurrence_checked=4`.

The infinite family is established by a self-contained proof in `RESULT.md`; finite enumeration alone cannot establish unbounded quantifiers. No external or independent audit is claimed.
