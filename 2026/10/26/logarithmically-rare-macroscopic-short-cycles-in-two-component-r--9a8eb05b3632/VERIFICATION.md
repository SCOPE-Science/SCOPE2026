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

# Verification and limits

The standalone Python program `verify.py` exhaustively enumerates all self-maps on up to six vertices and recomputes cycle lengths directly from each map. It compares every positive-probability pair of total cyclic count and shorter-cycle size with the independent exact rational law. Its output includes `EXACT_MAP_ENUMERATION_PASS` for every size from two to six and ends `VERIFY_OK`.

At three larger finite sample sizes the code evaluates conditional moments via analytic harmonic sums, checking their normalized values against the limiting constants. These numerical comparisons are diagnostics, not error bounds or substitutes for the analytic limit theorem. The proof of Gaussian domination, Riemann sums, tail integration, and the positive moment domain appears in `RESULT.md`.

No independent audit or independent validation was performed. The novelty comparison does not rule out an unlocated earlier derivation from general classical enumerations.
