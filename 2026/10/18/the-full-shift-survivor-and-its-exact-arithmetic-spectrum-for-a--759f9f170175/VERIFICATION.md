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

# Reproducibility and verification

Run `python3 check_survivor.py` using standard Python 3; no nonstandard dependencies are required. The program uses `Fraction` and integer `gcd`, computes the direct numerator map on residue classes modulo powers of the fixed modulus, and tests the inverse-branch fixed point formulas and exact rational digit itineraries. The observed completed output is:

```text
PASS: exact survivor counts, rational periodic-point formulas,
branch itineraries and independent two-cycle check
Number of direct count and periodic-point checks: 15740
Moduli: [2,3,4,5,6,7,8,9,10,11,12]
Period range: 1..4
```

For all moduli and depths, inspect the four proof steps in RESULT.md: (i) injectivity of multiplication by the modulus and unit inverses, (ii) disjoint exact contraction images, (iii) the mass-distribution argument for normalized Hausdorff measure and cylinder counting, and (iv) affine-composition algebra and strict interval inclusions for periodic points. Finite checks alone cannot establish these infinite assertions. Source comparison was carried out against Carvalho's arXiv:2605.21802v1 and Azevedo–Carvalho–Machiavelo's arXiv:1210.0042v1; the latter covers a different arithmetic transformation. Any unindexed previous statement or stronger theorem remains a novelty risk.
