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

Conditioned on cell count X=x, selected labels in its row outside the specified column form a uniform subset, so a same-row Y is H(N-b_j,b_l,a_i−x); inversion of the permutation gives the corresponding same-column law. Distinct row and column: K=|pi(A_i) cap B_l| is H(N-b_j,b_l,a_i−x), then Y|K=k is H(N-a_i,b_l−k,a_k). Nested-population and nested-sample hypergeometric couplings give K down and therefore Y up when x rises. Condition on admissible supports avoids improper hypergeometric parameters. Symmetrization of Cov(f(X),E[g(Y)|X]) gives signs for nondecreasing transforms, including negatives of empty indicators; elementary permutation indicator expansion yields exact standard count covariances. This proves the full all-N result beyond enumeration.

## originality

PASS

Fisher–Yates mass formula, covariance and sampling without replacement are classical; tested claim is stronger direction-dependent conditional stochastic regression for every cell pair and zero-event signs. Three inspected primary papers address distribution, asymptotics, and double-coset Markov dynamics, not that complete regression theorem. Older negative-regression literature is genuine residual risk.

## value

PASS

Pairwise dependence of sparse and zero cells is a natural question in exact conditional inference for fixed-margin categorical data. The all-threshold signs strictly strengthen linear covariance and distinguish adjacent versus opposite cells, supplying a reusable monotonicity principle with explicit support and finite-sample scope; it does not claim global table association.

The dated certificate retains the supplied scientific assessment, sources and limitations.
