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

The standalone program `verify.py` uses direct neighbor counts, not the quotient transition formula, and exhaustively enumerates all \(4^k\) labelled initial configurations for each integer \(1\le k\le8\). It checks the full first-entry distribution, primitive periods, orbit multiplicities, exact period-two basin, and the asserted time-two cutoff. The saved stdout in `verification_output.txt` ends in `MAJORITY_MINOR_CONSTELLATION_ALL_CHECKS_PASSED`.

The proof for every positive integer \(k\) is the explicit three-case update identity and its forward consequences in `RESULT.md`. The program is finite corroboration, not an infinite certificate. The Gaussian scaling step invokes the standard central-binomial Stirling estimate. Completeness of the historical literature comparison is not certified; Cannings's 2009 full text remained unavailable for a section-by-section comparison.
