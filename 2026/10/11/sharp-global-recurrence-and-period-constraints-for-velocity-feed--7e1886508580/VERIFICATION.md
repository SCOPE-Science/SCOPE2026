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
# Verification and reproduction

The proof is analytic. It uses the differential identity
\[
L\bigl(\tfrac12a^2+xv-F(v)\bigr)=v^2-Aa^2,
\]
stationarity of the exact generators of \(v^2/2\), \(x^2/2\), and \(va\), and the sharp mean-zero periodic Wirtinger inequality with its equality characterization. The bounded-complete-orbit argument requires compact limit sets and shows their invariant parts are confined to the single equilibrium. The final quadratic-feedback support claim uses an exact nonnegative-integrand identity and the zero-mean velocity law.

Run the standalone Python 3/SymPy source:

```
python artifacts/verify_identities.py
```

The observed output for this package is `VERIFY_OK` (also embedded in `artifacts/verification_output.txt`). The checker verifies the vector-field and moment generators, the characteristic polynomial and critical factorization, and substitution of the equality harmonic orbit. It cannot verify the topological limit-set lemma or Wirtinger's inequality; those steps are proved or explicitly cited in `RESULT.md`. No extrapolation from a finite trajectory or timeout is made.
