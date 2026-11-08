---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Conditioning on the observed comparison pattern splits independent underlying variables into L/M/R blocks. The two tested bits reduce to a decreasing endpoint response f(X_{i+1}) and increasing g(X_j); a missing intermediate edge disconnects endpoints conditionally, proving exact independence. If every intervening edge observed, each strict-order kernel 1{x<y} or 1{x>y} is TP2, products with arbitrary positive one-variable densities and consecutive Cauchy-Binet integrations remain TP2. Positive-density strict interlacing produces a positive determinant on a positive-measure set, forcing Cov(f(T),g(U))<0. Adjacent case uses Chebyshev antitonicity. Direct independent uniform-permutation counts checked n=4,5: for n=4 conditioned middle bit covariance -1/36, unconditional 0; n=5 cases negative/zero as predicted. This is all-n proof, not enumeration extrapolation.

## originality

PASS

Best-of-knowledge PASS for exact all-conditioning sign criterion, strictness and heterogeneous independent marginals. Unconditional one-dependence and determinantal descents are established prior, not the new claim. Strong-Rayleigh/conditional negative association does not directly cover uniform descents because its generating polynomial violates a necessary Rayleigh inequality at n=5.

## value

PASS

Conditional dependence between retained adjacent rank comparisons is a standard natural statistic in permutation/comparative ranking probability. Identifying precisely which observed edges transmit strict anticorrelation and proving the path criterion for all heterogeneous independent absolutely continuous inputs is a nontrivial structural classification, not a finite table or renaming of unconditional one-dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
