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

Execute `python verify.py` with Python 3 and SymPy in an environment that provides SymPy. The verifier asserts exact rational-function substitution identities for the original cubic map, a Gröbner basis for saturation by the affine coordinate \(v\), redundancy of the extra eliminated relations after \(H\) is inverted, an exact nonzero Jacobian minor at \(H=0\), and the polynomial identity underlying the formal \(A_2\) normal form. Expected last line: `VERIFY_OK`.

These checks are deterministic symbolic computations, not a finite census. The full mathematical proof is in `RESULT.md`, including the birational parameterization and the formal analytic change of variables. No independent audit or external validation is claimed.
