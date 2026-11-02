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

# Reproducibility record

Run `python3 verify.py` with standard Python 3. The program enumerates normalized points and dual lines over the prime fields of size two and three; it checks exact line cardinalities and unique connecting lines, enumerates every nonempty point subset, and derives the signed avoidance coefficients. No external packages or input files are required.

The program then verifies the symbolic tail-gap values at four, five, and six draws, the positive uniform bound at seven draws, and an exact rational sample of later times. It independently checks selected completion probabilities using a covered-subset recurrence. Finally it reproduces four published expected times as consistency checks. The output records 250 exact assertions passed.

**Limit:** These finite assertions are not an infinite-time proof. Infinite-time strict positivity follows from the analytical lower-envelope monotonicity and the closed Fano formula displayed in `RESULT.md`. The code does not test larger projective planes or establish historical priority. Independent audit has not been performed.
