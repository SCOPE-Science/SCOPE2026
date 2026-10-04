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
The proof reduces support-aligned additive-uniform signSGD to the finite Ehrenfest birth-death chain.

`verify.py` checks exact transition probabilities, binomial detailed balance, invariant moments, statewise conditional moment recurrences, the exceptional \(M=2\) oscillation, and parity-conditioned convergence on representative finite chains.

Finite enumeration is a transcription check. The invariant law, period, and moment formulas follow analytically from detailed balance and the exact conditional recurrences in `RESULT.md`.
