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

# Verification and reproducibility

Run `python3 verification/check_rrk.py` with Python 3 (standard library only) from the extracted files. The verifier uses exact rational projection matrices for unit normals \(u=(1,0)\) and \(v=(3/5,4/5)\), with \(x=9/25\). It checks all positions of the unique row for 1 through 8 repeated rows, both preceding endpoint-line types, transfer-matrix coefficients, characteristic polynomial identities, and all position strings up to five epochs for repeat counts 1 through 4. A separate finite floating-point comparison checks the strict order of the formula-derived rates at representative angles and repeat counts.

Actual verification output: `PASS: 11752 deterministic exact-arithmetic and floating-point consistency assertions`. The pathwise formula, limits for all epoch counts, and strict parameter-uniform inequalities are proved analytically in RESULT.md, not deduced from finite verification. Source comparison covers the full accessible source arXiv:2410.01140v1, a complete public related-result proof, and limited accessible bibliographic material of older related work. The self-review has passed; independent scientific audit has not been performed.
