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

Run the supplied standalone Python 3 standard-library script with `python3 verify.py`. It exhaustively enumerates all involutions on \(n=2,\ldots,10\), verifies \(45{,}612\) pair-insertion increments, verifies the exact conditional means, all adjacent-class inversion-tail inequalities, and exact negative covariances for four positive fugacities at each of nine orders. It also evaluates finite exact weighted expectations at \(n=5{,}000\) for the fugacity crossover, numerically checking four interior and two endpoint cases.

The successful output ends with `VERIFY_OK`. Finite enumeration and numerical limit comparisons cannot prove statements for all \(n\); the proof in RESULT.md derives the exact insertion identity, uniform matching coupling, tilted fixed-point ratio concentration and conditional variance bound. No independent audit or external mathematical certification has been conducted.
