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

# Reproduction of the exact algebraic certificate

Run `python3 artifacts/verify_cycle.py` using only the Python standard library. The checker multiplies the degree-two matrix denominator by eight polynomial numerator coefficients modulo the cycle relation, verifies the exact denominator identity, checks each sign-sensitive factorization, checks positivity of the other numerator-coefficient arrays and the common denominator, and uses the single-sign-change rule and rational interval evaluations to isolate the two endpoints.

Recorded successful output:
```
EXACT_POLYNOMIAL_IDENTITY_OK
DESCARTES_ONE_POSITIVE_ROOT_EACH_OK
EXACT_WINDOW_SIGN_CERTIFICATE_OK
LOWER 0.51225154437271
UPPER 3.52719746626943
```

A separate exact rational matrix multiplication checked the step matrices at \(h=1/4,1,3,4,10\), obtaining, respectively, nonnegative-status false, true, true, false, false, all with row sum one. The full real-parameter theorem follows from the symbolic polynomial identities and sign arguments; these five matrix evaluations are corroboration, not exhaustive numerical evidence.

The certificate does not verify other cycle sizes, nonuniform rates, nonlinear extensions or positivity of internal Gauss stages. Independent audit has not been performed.
