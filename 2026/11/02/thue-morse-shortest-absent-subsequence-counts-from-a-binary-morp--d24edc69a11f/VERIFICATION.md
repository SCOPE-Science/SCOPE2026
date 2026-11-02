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

Run `python3 checker.py` from the extracted package. It requires only Python 3 standard libraries. Checks use exhaustive binary preimages for lengths 1–8, an independent greedy-matcher state dynamic program for absent subsequences, conventional last-occurrence distinct-subsequence counting, explicit local-pair enumeration, matrix product identities, and the nonlinear recurrence for nine Thue–Morse levels.

Expected initial line: `All binary sources of lengths 1..8: 510 passed four independent checks`. The seven first Thue–Morse shortest-absent counts should be `3, 5, 12, 74, 2666, 3647090, 6476006417762`, and the final displayed growth-base approximation is close to `1.5686647891503442`.

Finite computations are not proofs of the infinite theorem; the complete logical argument is in `RESULT.md`. The limit decimal is rounded, while the logarithmic sum is the exact definition. No independent audit has been performed.
