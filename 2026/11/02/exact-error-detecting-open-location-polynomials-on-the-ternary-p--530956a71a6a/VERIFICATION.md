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

# Finite verification

Execute `python3 verify.py` with Python 3.8 or later. The script has no third-party dependencies.

For \(\operatorname{PG}(2,3)\), the script generates all normalized projective point and line coordinates, independently assembles incidence neighborhoods, and enumerates all \(8192\) choices per bipartition side. It compares each geometrical acceptance decision to the original two-directed neighborhood definition (and separately the RED symmetric-difference definition). All classifications match.

For every pair among the \(234\) minimum-size valid point-side and \(234\) minimum-size valid line-side choices, the program checks the resulting full \(26\)-vertex detector set against the original predicate: \(54{,}756\) complete checks. It also checks \(20{,}001\) further deterministically chosen complete subsets, and confirms each polynomial coefficient.

Expected terminal summary:

```
q 2 N 7 DET_SIDE_DISTRIBUTION [(6, 7), (7, 1)] RED_SIDE_DISTRIBUTION [(6, 7), (7, 1)]
q 3 N 13 DET_SIDE_DISTRIBUTION [(10, 234), (11, 78), (12, 13), (13, 1)] RED_SIDE_DISTRIBUTION [(9, 234), (10, 234), (11, 78), (12, 13), (13, 1)]
DET_FULL_POLYNOMIAL [(20, 54756), (21, 36504), (22, 12168), (23, 2496), (24, 325), (25, 26), (26, 1)] min_direct_checks 54756
RED_FULL_POLYNOMIAL [(18, 54756), (19, 109512), (20, 91260), (21, 42588), (22, 12636), (23, 2496), (24, 325), (25, 26), (26, 1)]
VERIFY_OK
```

This finite verification is exhaustive for each one-side selection and for all optimum full sets, but not for all \(2^{26}\) full detector selections. The infinite/general claim is not inferred from finite tests: the result concerns the specified finite plane and has an independent structural proof. Scientific literature priority is assessed separately, not certified by computation.
