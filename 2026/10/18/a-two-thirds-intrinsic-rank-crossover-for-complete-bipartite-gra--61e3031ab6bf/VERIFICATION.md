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

# Reproduction and limits

Execute `python3 verify.py` with a standard Python 3 interpreter. No downloaded mathematical data or additional Python packages are needed. The program enumerates forests of each \(K_{2,q}\) for \(2\le q\le7\) and checks all values of \(V_k\) against the closed expression, treating the two hub-connectivity cases separately. It also compares raw forest counts to the uniform-measure binomial formulas. It calculates all exact integral Gram determinants in the \(2\le q\le4\) subfamily by fraction-free elimination and compares them to the product-of-component-orders expression.

A successful run ends in `VERIFY_OK`. Recorded aggregate results: `forest_checks=10383`, `exact_gram_checks=258`; the six finite critical-regime diagnostics (three Gram-weighted and three uniform) at \(q=100000\) were within 0.02 of their analytical limits. The latter computations are illustrative, not proofs of the limits.

The infinite part follows independently from \(X_k/k\to1/2\) for a binomial \(X_k\), a bounded expectation argument, and the exact \(J_{q,k}/D_{q,k}\) ratio. No formal proof assistant or independent audit has been used.
