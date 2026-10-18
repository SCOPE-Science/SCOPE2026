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

# Verification record

The standalone script `check.py` is complete, uses only the Python standard library, and was executed against its delivered source code. It yielded `PASS: 340 independent exact-rational finite checks`. Cases cover every size from \(n=2\) through \(n=7\), with two geometric-ratio families and one nonhomogeneous ratio family at each size. Assertions independently enumerate permutation probabilities and compare them with the sequential exponential-race formula, exact identity ranking, each pairwise inversion marginal, overlapping-neighbor event probabilities, independence at disjoint clock pairs, and the long-inversion union bound.

The mathematical proof separately verifies the exponential race representation, the uniform \(O(n^{-1})\) probability of any nonadjacent inversion, the run-event estimate, convergence of Laplace functionals to the specified Poisson process, and all three regimes of geometric-ratio exact-ranking probability. The computation neither enumerates an infinite parameter family nor establishes weak convergence by itself. Results are a self-review only; no independent audit was performed.
