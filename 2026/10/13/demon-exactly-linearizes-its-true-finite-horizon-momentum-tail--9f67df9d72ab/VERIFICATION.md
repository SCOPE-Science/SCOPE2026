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
The package reconstructs the DEMON momentum schedule
\[
\beta_t=\frac{b(T-t)}{T-bt}.
\]

`verify.py` evaluates the finite varying-product tail directly with exact rational arithmetic and checks
\[
E_t=\frac{b(T-t)}{T(1-b)+b}
\]
for multiple horizons and initial momenta.

It also checks the source proxy, the constant ratio between exact and proxy tails, the shifted tail for a newly injected gradient, and the numerical relative-error examples.

The checker is a transcription guard. The identity is proved by finite backward induction in `RESULT.md`.
