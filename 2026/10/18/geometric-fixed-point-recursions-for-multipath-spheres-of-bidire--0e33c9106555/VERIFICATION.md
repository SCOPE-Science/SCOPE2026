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

# Verification summary

The symbolic proof identifies fixed orbit simplices and derives every all-parameter action. The independent finite checker `verify_bidirected_linear_fixed_points.py` enumerates allowed arrow subsets, tests both orbit identifications exhaustively for widths up to twelve, compares the signed reduced Lefschetz characters for all three involutions up to twelve, and performs exact mod-two boundary-rank calculations for the first six widths.

Run: `python verify_bidirected_linear_fixed_points.py` from a directory containing the program. Recorded output: `verification_output.txt`.

The finite checks are not an exhaustive check for arbitrarily many edges and do not verify literature novelty. The known nonequivariant homotopy statement and the signed Lefschetz argument are separately reconstructed in `RESULT.md`. No independent audit has been performed.
