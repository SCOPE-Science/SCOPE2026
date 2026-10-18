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

Reconstructed the piecewise-rational expectile equation αE(X-e)+=(1-α)E(e-X)+ for the rational three-point X and four-point Y. The complete parameter partition at 1/104,2/11,210/859 yields four exact positive differences s2_Y−s2_X, certified by positive coefficients, a negative quadratic discriminant, increasing-positive quadratic and constant 9/50. Independent exact Fraction stop-loss arithmetic gives mean/MAD standardized S_X(4/5)=1/5 and S_Y(4/5)=73441/569900, gap 40539/569900>0. Smoothing by narrow triangular kernels plus ε of uniform full-interval density converges in W1; monotone-root stability on compact α subintervals and endpoint limits at 0 and 1/2 make the full positive profile gap persist. No explicit numerical smoothing ε upper bound is asserted.

## originality

PASS

Eberl–Klar Remark 6 explicitly leaves the implication in both directions open. Later results on stronger stochastic skewness order or equivalence of positivity for a single distribution do not imply the pairwise implication under s2 and sf; this construction disproves exactly one open direction inside the motivating paper’s atomless interval-support class. No actual coverage identified in targeted Resultary/publication searches; terminology/notation changes remain priority risk.

## value

PASS

Resolves one explicit directional open question in a recently published implication diagram, including the atomless continuous-cdf interval-support class. Unlike finite-grid comparisons, the strict inequality holds for the entire continuum α∈(0,1/2) with an exact rational witness of the sf reversal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
