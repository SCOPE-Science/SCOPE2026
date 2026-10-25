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

The executable `check_kg3.py` uses exact integer arithmetic and the Python standard library. In the checked execution it returned:

```text
KG3_FULL_AND_ALTERNATING_SYMMETRY_QUOTIENT_RATIONAL_ACYCLICITY_CHECKED
KG3_COMPLETE_CONJUGACY_CLASS_CHARACTER_VERIFIED 253
KG3_KNOWN_WEDGE_RANKS_VERIFIED n=6..12
```

The computation exhausts conjugacy classes for \(6\le n\le12\), not all permutations and not infinitely many values of \(n\). The written support-inclusion–exclusion proof is the infinite-parameter argument. The imported sphere-wedge concentration is from arXiv:1807.11732v1, Theorem 1.3. No integral representation or independent external mathematical audit is claimed.
