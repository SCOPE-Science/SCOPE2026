---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The derivative of a stopped-Poisson row has nonterminal entries p_(k-1)-p_k and terminal entry p_(n-i-1). The absolute row sum is twice the largest retained Poisson mass by unimodality and zero row sum; the nonterminal column sum is the variation of the truncated mass sequence starting at zero, and the terminal column sum is F_(n-1). This gives both formulas, including mode ties, n=1, and the real/complex counting norms. The piecewise time-weighted mode grows strictly to n and then decays. For the absorbing-column optimizer, F_(n-1)/(t p_(n-1)) is a strictly decreasing sum of inverse powers, so it crosses one exactly once. Stirling at t=n-c sqrt(n log n) gives t p_(n-1)~n^((1-c^2)/2)/sqrt(2 pi), while F tends to 1 (even Chebyshev gives an O(1/log n) upper tail there); derivative signs bracket the optimizer for c on either side of 1. At the optimizer p_n=F/n and the tail geometric bound loses only O(sqrt(n/log n)) in the time-weighted norm. The nonterminal branch is bounded by the infinity-mode expression, hence its supremum is O(sqrt n) and cannot compete for large n. The spectrum follows from triangularity.

## originality

PASS

The supported contribution is the exact paired endpoint optimization and in particular the absorption-induced linear ℓ1 scale and its negative sqrt(n log n) time shift, not the stopped-Poisson representation or mode estimate. The closest inspected shift- and finite-chain results have different boundary dynamics and do not yield this pair.

## value

PASS

This gives a sharp absorption-driven mismatch between dual counting-norm endpoints despite the same two-point spectrum for every dimension. The quantitative time shift and the exact square-root endpoint calibration provide a useful test case for dimension-dependent semigroup estimates, not just a numerical norm calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
