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

The exact formulas and genus-four proof are in `RESULT.md`. Run the following commands from the directory containing these files:

```sh
python verify_cartier.py
python verify_stable_rank.py
python verify_finite_fields.py
```

The first requires SymPy and independently compares a multinomial expansion and polynomial expansion for the relevant \(f^2\), \(f^4\) coefficients, with a symbolic discriminant/determinant identity. It reports `CARTIER_DISCRIMINANT_OK`.

The second uses the Python standard library only and performs exact polynomial arithmetic over \(\mathbb F_7[A]\). It checks the full \(3\)-by-\(3\) Frobenius products, the gcd of all nine second-iterate minors and all third-iterate entries, and the stable rank limits. It reports `FROBENIUS_STABLE_RANK_OK`.

The third independently tests all normalized coefficient pairs over \(\mathbb F_7\) and \(\mathbb F_{49}\) by direct polynomial gcd of the quintic and its derivative. It reports `FINITE_FIELD_CENSUS_OK`. These finite enumerations do not prove the classification over the algebraic closure; the symbolic algebra and the Cartier argument supply that proof.

These checks were rerun on actual distributed file paths. No external mathematical validation has been performed. Historical-priority risk from unindexed or differently parameterized treatments remains.
