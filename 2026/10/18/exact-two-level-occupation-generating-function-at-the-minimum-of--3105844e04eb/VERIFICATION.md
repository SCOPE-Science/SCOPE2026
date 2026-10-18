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

# Reproducibility and limits

Execute `python3 verify.py` using the standard library. The script exhaustively enumerates all \(2^n\) fair walks through \(n=10\), checks every exact joint law coefficient against an independent decomposition into two strictly positive meanders and marked positive excursions, and verifies both closed generating-function factors for the rational level-one weights \(v\in\{0,1/2,1,2,3\}\). It verifies the rare-event cell by exact fractions. These finite checks corroborate algebra but are not the infinite proof; the complete proof is the bijective path decomposition in `RESULT.md`.

No third-party executable resources are needed. The generating functions are formal about \(z=0\); the asymptotic uses the elementary binomial reflection formula and Stirling's theorem. Independent audit: not performed.
