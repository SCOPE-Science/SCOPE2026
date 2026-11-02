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
# Verification and scientific boundaries

Run `python verify.py` (Python 3.10+, standard library only). Executed tests passed: 3,000 seeded finite-difference comparisons against independently reconstructed survivor-weighted hazards; representative instances of all strict phase regimes; exact fold and endpoint algebraic identities; both witness critical coordinates; asymptotic scaling at both boundaries. Numerical rounding limits are explicitly confined to these checks.

The infinite continuum theorem is proved in RESULT.md by direct differentiation, the strictly increasing auxiliary function \((u+k)\tanh(u/2)\), exact endpoint signs, and the local double-root Taylor expansion. The code is a reproducibility aid rather than a proof by enumeration. The statement is limited to two equal birth-weight frailty atoms and a common positive Gompertz slope. No external independent audit has been performed.
