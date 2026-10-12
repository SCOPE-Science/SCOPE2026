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

# Reproducibility

From the containing directory, execute `python3 verify.py`. The checker uses only the Python standard library. The graph and the predicted coefficients are implemented separately: the graph uses bitset adjacency and directly tests both independence and domination, whereas the formula uses exact integer binomial coefficients.

Executed command: `python3 verify.py`.

Observed output:

`VERIFY_OK exhaustive_n=3..10 masks=1398080 formula_and_OEIS_n=3..200 parity_extremal=passed`

The checker visits every one of \(2^{2n}\) possible subsets for every integer \(3\le n\le10\), totaling \(1{,}398{,}080\) subsets. It compares the complete cardinality histograms, verifies equality with the known Lucas-number total through \(n=200\), and checks the claimed extremal and parity features in that range.

The infinite statement follows instead from the explicit isolated-empty-rung/alternation bijection and counting with a marked occupied rung, proved in the result. Computation over finite orders cannot establish universality or historical originality.
