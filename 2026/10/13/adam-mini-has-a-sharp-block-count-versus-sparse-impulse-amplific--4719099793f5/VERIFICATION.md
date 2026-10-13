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
The package verifies the Adam-mini sparse-impulse formulas and the block-count minimax frontier.

`verify.py` reconstructs the bias-corrected Adam-mini and coordinatewise Adam impulse updates from zero history, checks the exact formulas for several moment parameters and impulse times, verifies the \(\sqrt{d/k}\) support-size limit, and exhaustively enumerates integer block-size compositions for small \(N\) and \(B\).

Finite computation is used only as a transcription and combinatorial guard. The sharp coordinate inequality and all-\(N,B\) minimax theorem are proved analytically in `RESULT.md`.
