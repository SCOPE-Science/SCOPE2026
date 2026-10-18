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
# Verification and bounds

The script `check.py` is a standalone Python 3 program using only the standard library. It independently enumerates every simple labeled graph on three through six vertices and evaluates expectations and cross-covariances by exact weighted integer sums at two rational edge probabilities. It compares each with the closed covariance identity using `fractions.Fraction`, checks strict coefficient inequalities through 69 vertices, and checks the seven-vertex threshold reversal by a rational-power comparison.

Observed execution: `PASS: 52475 exact checks; full graph enumeration through six vertices.` This verifies finitely many cases only. The all-size result is justified by the conditional edge-independence proof and exact binomial identities in `RESULT.md`; the asymptotic follows from fixed-parameter polynomial growth, not from finite simulation. No independent third-party validation was performed.
