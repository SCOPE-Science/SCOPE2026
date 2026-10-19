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

# Exact reproducibility and mathematical scope

Run `python3 verify.py`. The program uses the standard library `fractions.Fraction` and checks the exact stationary equations, both two-by-two invasion matrices, the sign of the exact determinants and trace, and the rational positivity identities in the displayed example. The universal result instead depends on the proof of the scalar equilibrium uniqueness, the strict sign of the eigenvalue determinants and the two-case stationary-state contradiction in RESULT.md. Finite verification cannot prove arbitrary real-parameter statements. This file records self-review only; independent audit has not been performed.
