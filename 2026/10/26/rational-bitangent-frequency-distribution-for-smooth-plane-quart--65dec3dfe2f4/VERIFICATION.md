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

# Verification

Install Python 3 with SymPy (validated with SymPy 1.14.0). In a directory containing all packaged artifacts execute:

```bash
python3 census.py
python3 crosscheck.py
```

The first command exhausts the 15-bit polynomial space using projective generators and exact three-chart Gröbner basis computations. It writes `all_orbits.csv` and `smooth_orbits.csv`, with 279 and 78 data records. The second independently enumerates all 168 invertible matrices, confirms that their 279 orbits are pairwise disjoint and cover all 32,767 nonzero forms, repeats Gröbner smoothness checks with a different monomial representation and order, and explicitly computes bitangent counts for all 10,920 smooth forms. Its success line begins `CROSSCHECK_OK`.

Both programs were executed and yielded the embedded reference outputs. The distribution must be `(0,3072),(1,5278),(2,2352),(3,105),(4,112),(7,1)` with 10,920 smooth forms. The checks are complete for the stated finite universe, not a proof about arbitrary fields or degrees. The independent execution and independent human mathematical audit remain unperformed.
