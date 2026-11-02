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

# Reproducibility and scope

Run `python3 verify.py` with Python 3 and no third-party packages. The file uses exact rational arithmetic. It checks the displayed stage-factor rational identity symbolically, the scalar negative-axis factorization, the sign-controlling discriminants and endpoint rational identities, the derivative at the common three-state witness, and an independent exact rational matrix-function evaluation.

The observed local execution returned `VERIFY_OK 24 exact-rational assertions`. The analytic proof in RESULT.md supplies all continuous-parameter, arbitrary-step, and all-generator quantifiers. The computation is only a second exact certificate for the algebra and finite witness, not an exhaustive enumeration of all generators or step sizes.

No independent mathematical audit has been performed, and the proof does not cover nonlinear stages, approximated spatial derivative closures, finite-precision errors, or the minimum *irreducible* CTMC dimension.
