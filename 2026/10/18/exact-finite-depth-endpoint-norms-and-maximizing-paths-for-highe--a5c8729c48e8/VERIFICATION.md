---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For each source leaf, off-diagonal target shells at first divergence j yield coefficient b^{j-1-d}(y_{j-1}-e_j) and diagonal y_d, y_0=1, y_j=(y_{j-1}+(b-1)e_j)/b. Counting (b-1)b^{d-j} targets yields exact L1 column sum (b-1)/b sum_j(1-e_j y_{j-1})+|y_d|. For b>=3, each y_j has sign e_j strictly; eliminate signs to rewrite as (b-1)d-(b-1)sum_{j<d}|y_j|-(b-2)|y_d|. The future optimal absolute-state cost is even with Lipschitz bound (b-1)sum_{k=1}^{m-1}b^{-k}+(b-2)b^{-m}=1-2b^{-m}<1. Thus minimizing next-state magnitude strictly forces the opposite sign, including final weight b-2>0. Since y0=1, unique maximizing path signs are (-1)^j, and all off-path signs never affect that column. Solving y recurrence gives the claimed exact depth-dependent norm and equality iff some root-leaf path alternates. Independently enumerated all sign paths for b=3,4,5 and depths 1..6 with exact fractions; matches closed form; source checker independently constructs conditional expectation matrices. Analytical Bellman argument supports arbitrary finite b>=3,d>=1.

## originality

PASS

Dragičević–Petermichl–Volberg arXiv:math/0606006 sharp nonendpoint Lp (p>1) transforms; Osękowski dyadic weak-type/distributional estimates; Astashkin–Huang–Pliev–Sukochev–Zanin arXiv:2202.07154 studies a specified DYADIC Haar martingale transform and optimal symmetric ranges, not optimization over all predictable signs for uniform b>=3 at finite depth. Compared finite stochastic matrix, cancellative b-ary Haar transform and tree filtration; the exact alternating path extremal representation appears distinct from dyadic weak estimates. No inspected general result implies the full exact b,d and unique alternating path classification; historical finite-filtration results remain a residual risk.

## value

PASS

A natural finite-filtration strong L1 martingale-transform optimization is determined exactly for all branching arities >=3 and depths, including the nontrivial equality geometry of predictable sign families; the sharp linear slope and oscillatory bounded correction quantify amplification, not a routine endpoint norm bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
