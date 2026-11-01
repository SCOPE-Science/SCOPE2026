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

# Reproduction and verification

From the directory containing this file, run `python verify.py` after installing the dependencies listed in `requirements.txt`. The checker performs exact symbolic identities for the one-variable reduction, stationarity polynomial, radical coefficients, and maximizing-ratio displacement, together with deterministic high-precision numerical checks of unit norms, Birkhoff orthogonality, direct fourth-norm evaluations and finite-ratio comparisons. It reports the number of checks completed or exits with an assertion on failure.

The full quantified statement rests on the analytical proof in `RESULT.md`: the smooth support-functional characterization, global one-variable reduction including both signs, strict uniqueness of the interior leading maximum, uniform fourth-root expansion, and a local implicit-function argument. Neither a numerical grid nor a symbolic evaluation at finitely many parameter values establishes the infinite quantifiers. The result has not been independently audited, and older equivalent priority remains possible.
