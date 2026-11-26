---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frozen Finding lines 18–21 is not scale invariant if an orthogonal eigenbasis is taken literally without normalization: H=1, u=2, x_0=2 gives c=1 and already 4≠1 at n=0. The separate corrected RESULT.md uses an orthonormal basis and gives the squared-length factors for a general orthogonal basis. Reassessed the entire repaired result: with η_i=Y_i−1 the eigenmode multiplier has orthogonal L² terms proportional to 1, η_1, η_2, η_1η_2; their squared norms 1,a−1,a−1,(a−1)² give exactly Q_b and the stated quadratic excess over Heun. Iteration independence and Parseval give the corrected all-horizon law; positive integer powers preserve strict ordering for nonzero states when a>1. Q_b−1 is z/4 times a cubic whose derivative has global minimum 4C−16/3>0 and which starts at −8. The top eigenspace establishes necessity, equality and instability. The midpoint factorization and positive quadratic factor give 2/a, matching Euler. At the Heun endpoints the cubic gives −4+4/a and 24/a. With r=az_*, 2r−8+r(r²−4r+6)/a=0, positivity of the polynomial and its derivative gives monotonicity, and its value at 4 gives r=4−12/a+O(a^(−2)). Under reuse the squared factor grows as z⁴Y⁴/4; for the Pareto example the first two moments are 1 and 4/3 and the exact Heun factor is 355/576. Inspected the frozen checker and its recorded outputs, did not run it, and used analytic proof rather than its finite tests. No source evidence changed.

## originality

PASS

Best of current knowledge, the distinct claim in the repaired version is the exact distribution-free tableau comparison under independent scalar stage multipliers and the resulting exact Heun frontier and reuse contrast. The normalization correction to the norm law does not change the class of problems or the prior comparisons. Classical tableau order and the one-gradient stability benchmark are prior, and the fixed-Heun two-point case has direct catalogue overlap.

## value

PASS

The repaired result answers a concrete design question in a quadratic benchmark: with noise drawn independently at each call, the equal-weight choice optimizes every step and horizon, and the exact stability-range comparison quantifies a possible near-doubling versus midpoint. The reuse example separates models under finite variance with an infinite fourth moment. These are stronger and more useful than a normalization correction or a single-stepsize example. The gain is per iteration, not evidence of lower cost per gradient evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
