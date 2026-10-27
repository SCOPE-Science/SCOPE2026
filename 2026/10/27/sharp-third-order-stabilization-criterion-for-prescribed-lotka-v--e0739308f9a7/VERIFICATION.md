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

Execute `python3 verify.py` with Python 3 and its standard library. The program uses `fractions.Fraction` and a deterministic seed, with no external dependencies or network access. The reproducible terminal message starts `EXACT_REPLAY_OK 1190 rational cases` and reports the constructed/obstructed cases.

For every tested coefficient tuple it directly checks the equilibrium equation, computes the Jacobian of the actual unnormalized vector field, verifies its positive-diagonal similarity to the constructed target matrix, verifies the mandatory Euler row-sum identity, and checks the rank-one nilpotent structure that places every constructed nonconstant-row-sum eigenvalue at \(-1\). It separately checks two fully explicit two-species examples and a fourth-order rescue.

These are **finite exact-rational consistency checks**. The general proof is the algebraic argument in `RESULT.md`, particularly the homogeneous quadratic identity and the nilpotent matrix construction. There is no computational claim of exhaustive verification of the real parameter domain, or of global nonlinear stability. Independent audit has not been performed.
