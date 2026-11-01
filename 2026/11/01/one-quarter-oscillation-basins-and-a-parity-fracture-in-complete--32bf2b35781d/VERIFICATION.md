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

Run `python3 verify_split_majority.py` using Python 3 and no external dependencies. The script computes each vertex's next state by its actual open neighborhood, with deterministic tie retention, and verifies \(F_n^4=F_n^2\) for all \(349{,}524\) labelled initial configurations across \(1\le n\le9\). It independently counts periodic two-cycle states, the complete two-cycle attraction basin and sharp first-periodic-entry times. For \(1\le n\le150\), it also compares population-map weighted counts to the closed binomial formulas.

The recorded output in `verification_output.txt` terminates with `SPLIT_MAJORITY_VERIFY_OK`. The mathematical proof, not finite enumeration, supplies quantification over every positive \(n\). The asymptotic expansions use standard central-binomial Stirling estimates. No external independent audit has been carried out.
