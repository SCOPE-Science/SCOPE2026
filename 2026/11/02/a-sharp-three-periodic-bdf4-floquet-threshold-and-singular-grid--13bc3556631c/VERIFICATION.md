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

## Reproduction

Run `python verify.py` with Python 3 and SymPy. The program reconstructs derivative weights of the degree-four interpolant from five exact nodes, the three rational companion matrices, the characteristic polynomial and the Schur–Jury sign certificates. It asserts coefficient-wise strict positivity of three exact integer polynomials, the one-sign-change degree-seven threshold polynomial, the general singular-limit coefficients, and seven independent exact rational monodromy identities.

Actual result from the packaged script:

```text
EXACT_VERIFIED: coefficient identities, all positivity certificates, unique threshold, asymptotic limit, sampled direct monodromy
critical_ratio: 59.78365454067794904098188063010340271390
degree_schur_remainder: 16
```

The decisive all-parameter statements are mathematical identities and sign arguments, not finite numerical experiments. The code uses SymPy symbolic operations and its root solver only for an approximate value of a uniquely certified positive algebraic root. No independent audit has been performed.
