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

# Reproducibility

Run `python3 verify.py` with any supported Python 3 standard-library installation. Recorded output:

`VERIFY_OK finite_identities=4317 spectrum_levels=101 exceptional_level=1`

This reproduces exact integer coin-count calculations, five distinct pairwise-coprime parameter examples, the period shift, parity bijection, and the 84-index sharp classification for (6,7,8). The finite test checks many instances but the infinite theorem rests on the generating-function pole analysis and the exact shift identity in RESULT.md. The 84 cases are exhaustively certified by the finite table and a direct closed counting formula, not guessed from a finite initial sequence.

The general finite onset need not be minimal; the (6,7,8) onset is separately sharpened. No external mathematical validation or independent audit has been performed.
