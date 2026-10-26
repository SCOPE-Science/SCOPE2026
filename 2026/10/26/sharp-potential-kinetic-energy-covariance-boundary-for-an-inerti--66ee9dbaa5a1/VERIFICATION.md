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

# Reproducible mathematical checks

Run `python CHECK.py` with Python 3, SymPy and mpmath available. The checker reconstructs moment equations for both spin sectors at polynomial degrees one through four and checks their exact closed forms. It factors the connected fourth mixed moment, verifies endpoint factorizations and checks strict polynomial derivative coefficient positivity. A separate frequency-domain/response-kernel computation integrates the stationary four-time telegraph correlation (with ordered independent spacings) and matches the covariance for four parameter pairs spanning both sign phases and both damping regimes. The completed checker reports 25 passed assertions.

The algebraic phase classification is proved symbolically in `RESULT.md`; numerical integrations only corroborate finite test points. There are no unproved extrapolations from experiments. The model excludes zero damping, zero flipping, additive thermal diffusion, and nonlinear traps. This package has not undergone independent external scientific validation or priority adjudication.
