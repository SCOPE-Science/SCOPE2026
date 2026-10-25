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

# Mathematical verification

The statement and complete proof are in `RESULT.md`. The positive and negative Gaussian exceedance processes are treated jointly; their asymptotic independence follows from disjoint rare-event multinomial factors, rather than from assuming the same finite sample is independent. The top-two Gaussian comparison and chi-dimensional radius estimates establish the needed first moments, so the displayed deficit is a proven asymptotic statement conditional only on the explicitly stated ratio limit.

Run `python CHECK.py` with NumPy available. The executable independently computes the permitted pair vertices, checks 840 direct support/width evaluations, exhaustively enumerates 15 small ranking configurations to establish the finite exposure probability, and tests 15 analytic CDF evaluations against seeded independent exponential samples. It terminates with `CHECK_OK` after successful comparisons. These are finite checks and diagnostics only; the general Gaussian Poisson and tail arguments are mathematical, not computer-certified.

The full result treats every integer \(p\ge1\), \(q\ge2\) and the finite-ratio sequences \(q\to\infty\), \(p/q\to c\in[0,\infty)\). It does not claim an infinite-ratio limit, several parallel classes, or independent formal certification.
