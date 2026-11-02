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

Execute `python verify_residual.py` with a Python 3 interpreter. Only the Python standard library is used. The script constructs the exact characteristic-two quotient by multivariate polynomial long division and checks the original product identity.

It then enumerates rational curve points over \(\mathbb F_8,\mathbb F_{16},\mathbb F_{32}\), candidate singular supports over the corresponding geometric subfields \(\mathbb F_4,\mathbb F_8,\mathbb F_{16}\), and the distinct smooth tangency points on all three diagonal lines. It checks that no defining-field rational point is singular and that the computed counts match the theorem.

The script also verifies, in the polynomial ring \(\mathbb F_2[A,D,S]\), the exact identity
\[
A^4(D+S)^3+D^4(A+S)^3+S^4(A+D)^3
=(A+D)(A+S)(D+S)(AD+AS+DS)^2.
\]
This identity guarantees the critical nonzero cubic coefficient along the unique quadratic tangent in the symbolic proof.

Expected output includes the checked rational-point counts 24, 168, 840; geometric candidate cusp counts 0, 24, 168; and three-line tangency counts 2, 6, 14.

Finite enumeration is a check only: the all-\(r\) assertions rest on the equations, inclusion–exclusion, local cusp argument, and Bézout supplied in `RESULT.md`. Independent external mathematical validation has not been performed.
