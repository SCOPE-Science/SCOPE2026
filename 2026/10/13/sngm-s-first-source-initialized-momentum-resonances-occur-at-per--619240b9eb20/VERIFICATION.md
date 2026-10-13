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
The package reconstructs deterministic source-form SNGM on the scalar quadratic \(f(x)=a x^2/2\).

`verify.py` exhaustively forms the momentum and cumulative-displacement polynomials for every sign word through period six using exact rational arithmetic. It checks the absence of admissible shorter return factors, isolates the two period-six candidate factors, and verifies their sign words.

It then replays both resonance families for multiple initial points and checks the six-step state return and the exact average-gradient formulas.

The finite enumeration is exhaustive only through period six. No longer-period claim is made.
