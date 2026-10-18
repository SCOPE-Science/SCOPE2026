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

The accompanying `certificate.json` contains every admissible conjugation orbit, face count, ordered elementary-collapse pair and residual graph for each integer parameter from 1 through 22. The standard-library command `python3 verify.py certificate.json` reconstructs the entire partition-transfer graph and its conjugation action, checks the classification of admissible orbits via off-diagonal transposed addable corners, enumerates every simplex of the fixed-orbit flag complex, and verifies uniqueness of the coface at every prescribed collapse. It also computes the complete mod-two homology independently, without using the listed collapses.

The exact execution output `verification_output.txt` ends with `FIRST_FIXED_H1_NONZERO=18; H1_RANK_AT_18=1; H1_RANK_AT_22=2`. The reconstructed surviving component signatures, together with full free-face certificates, establish integral graph homotopy types for every listed parameter. The finite computation is exhaustive **within the stated range** and does not imply homotopy information for any size above 22. The all-size orbit model and the rational Lefschetz identity are proved mathematically in `RESULT.md`, rather than extrapolated from those calculations.

The verifier uses only the Python 3 standard library and requires no third-party code, downloads or external datasets. Independent mathematical audit has not been performed.
