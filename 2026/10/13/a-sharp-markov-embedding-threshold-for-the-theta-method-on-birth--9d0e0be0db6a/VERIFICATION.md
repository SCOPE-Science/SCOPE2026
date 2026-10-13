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

Use Python 3 with the standard library and run `python3 artifacts/verify_embedding.py` in this folder. The check was run on the included code and produced exactly:

`VERIFY_OK exact checks: 336`

The program uses exact `fractions.Fraction` arithmetic to verify the rational Crank–Nicolson witness, its three spectral projectors and determinant/eigenvalue relationships, finite path-sign identities, the coefficient signs in the effective-generator series, the resolvent positivity identities for several sample chains, and the exact two-state formulas.

## Analytical certification boundaries

The infinite families are established analytically in RESULT.md by simple-spectrum logarithm uniqueness, the sign-coherent path-expansion lemma, the convergent logarithm power series, and a stochastic-resolvent integral. Finite checking is not an exhaustive proof of unbounded dimension or uncountably many stepsizes. No external or independent audit was performed. In particular, numerical sampling alone cannot rule out earlier equivalent formulations of the same statement.
