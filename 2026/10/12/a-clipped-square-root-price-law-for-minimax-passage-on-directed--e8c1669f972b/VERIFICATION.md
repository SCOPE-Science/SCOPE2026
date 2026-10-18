---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Each directed first-passage time equals the sum of holding-time means 1/r_i along the sole directed path, so the longest paths omit precisely one edge and the objective is sum_i 1/r_i−min_j 1/r_j. For arbitrary probability q on omitted edges, max >=sum_i(1−q_i)/r_i >=(sum_i sqrt(c_i(1−q_i)))² by price-budget Cauchy–Schwarz. Maximizing the concave dual over q yields KKT q_i=(1−c_i/theta)_+, unique theta, and at least two positive q_i; equality produces all strictly positive optimal rates with clipped inverse-square-root prices. Strict equality under Cauchy–Schwarz gives uniqueness. Direct algebra checks example c=(1,3,100), theta=4,Z=12,r=(1/24,1/24,1/120), max=144, and equal-rate max=208. Independently checked the source Poisson-generator verifier, exact threshold relation, and numerical feasible comparisons; the universal claim rests on the analytic minimax lower-bound/equality proof.

## originality

PASS

Previously published surveillance optimization works focus on stationary-weighted average hitting time, cyclic observation gaps, or general discrete-time largest MFPT bounds. The closest Breen–Kirkland paper treats maximum MFPT but in a different discrete-time optimization/normalization and does not provide the arbitrary positive price clipped law in inspected sections. Resultary search located no direct equivalent result. Prior specialized priced-cycle formula could still exist.

## value

PASS

A complete analytic solution to a natural continuous-time network design minimax problem with arbitrary positive linear rate prices, identifying a nontrivial clipped threshold and a sharp uniform-rate phase, provides an interpretable and practically reusable allocation law, not just a routine uniform-rate exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
