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

# Verification record

To reproduce the finite checks, run `python verify_diameter.py` using Python 3.10 or newer. The program requires only the Python standard library. It exhaustively enumerates all binary attachment prefixes of lengths zero through eleven, followed by deterministic first-predecessor continuation. It reconstructs the full finite tree from parent pointers, determines the infinite continuation ray, enumerates its side teeth, checks the run-to-tooth identity at every spine vertex, and independently computes its diameter by two breadth-first searches.

Observed output: `PASS: 4095 exhaustive eventual-tail finite trees, 2354 with positive excess; largest excess 6`.

These checks are exact for the finite enumerated trees, but cannot prove almost-sure uniqueness of the spine, the infinite union bound, or eventual stabilization for all attachment sequences. Those are established by the analytical arguments in `RESULT.md`. The sharp exponent is derived from matching probability bounds, not an extrapolation of the finite sample. The multiplicative tail constant and mass function of the limit remain unknown from this result.
