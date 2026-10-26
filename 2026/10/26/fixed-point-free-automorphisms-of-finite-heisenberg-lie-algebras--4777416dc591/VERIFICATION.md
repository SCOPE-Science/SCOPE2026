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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and only the standard library. It exhaustively enumerates all 2-by-2 similitudes over the prime fields of orders 2, 3, and 5 and enumerates a symplectic basis model for the multiplier-2 coset of \(\operatorname{GSp}_4(3)\). It checks the corresponding exact counts against the formula in `RESULT.md` and prints `VERIFY_OK_HEISENBERG_FPF` on success.

These are finite consistency checks, not the proof for arbitrary dimension or every prime power. The all-parameter proof is the isotropic-subspace Möbius inversion in `RESULT.md`. The full text of one plausible 1998 source was inaccessible; this access limitation is preserved in the review and structured audit.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
