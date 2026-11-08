---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For rows (1,0),(1,0),(0,sqrt(2q/(1−q))) and targets (0,d,0), paired affine reflections are exactly three types: horizontal-horizontal with ±d or zero increments, vertical-vertical identity, and mixed pair with probability θ=2q(1−q) resetting X to 0 or d and Y to 0. This Doeblin coalescence yields TV distance ≤(1−θ)^n and a unique invariant geometric lattice law; its generating/characteristic function gives geometric ratio (sqrt(1+q)−sqrt(2q))/(sqrt(1+q)+sqrt(2q)), mean d/2 and variance d²/(4q). Conditional first and squared-error recurrences yield the exact finite-time formulas for arbitrary deterministic Z0; matched single-reflection projection gives floor d²/4. Characteristic-function scaling yields Laplace(0,1/(2sqrt2)). Independent rational enumeration verified all nine ordered pairs and first/second moments for q=1/4,1/2,3/4 and three starting vectors (9 exact cases).

## originality

PASS

Best-knowledge originality applies to the precise claimed combination, not generic background results: The general randomized DR construction and Markov invariant-measure theory are prior. This exact three-row inconsistent algorithm with independent-with-replacement double draws has a different regenerative transition kernel and stationary discrete-Laplace output. Neither implies a nonzero stationary residual for an inconsistent instance, let alone its factor 1/q. The renewal kernel can be analyzed with standard reset-walk tools; that tool itself is not new, but application with exact DR comparison is.

## value

PASS

The specific three-row inconsistent linear system is natural as a minimal full-column-rank noise-floor stress test of a genuine randomized splitting algorithm. Its exact stationary law, sharp convergence and arbitrarily bad 1/q error inflation versus Kaczmarz quantify a real algorithmic boundary that convergence theorems for consistent systems do not address; not a generic resetting-random-walk novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
