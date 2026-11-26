---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof scope

`python3 verify.py` uses only the Python standard library. For each case it enumerates all first parts of the chosen size and computes the exact support of the within-part edge totals. It tests covariance singularity by the rank of differences of these support points, without floating-point covariance calculations. It separately checks the constant-statistic conditions for regular and additive weights.

Observed output: `PASS: 66624 simple graph/size cases; 560 weighted cases.` The simple-graph cases exhaust all labeled graphs of orders four, five and six for first-part sizes from two through half the order rounded down. The weighted cases include signed additive matrices, matrices with constant row sums, and general sampled integer weights. The exchange proof in `RESULT.md`, not finite enumeration, covers arbitrary admissible sizes and real weights. The balanced Laplacian variance is derived there from published weighted permutation moments and the incidence projection.
