---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Each rank-(n-a) partial injection has exactly a! full permutation extensions, hence μ_a is uniform Π restricted outside an independent uniform a-deletion set. In composing independent factors, pull deletion D_i backwards through independent prefix permutations P_{i-1}, obtaining independent uniform A_i that are independent of final uniform P_k; the product equals P_k restricted outside their union. Inclusion-exclusion gives p_s and individual-map probability p_s s!/n!. Rank conditioned product is uniform; μ_a span a commutative convolution subalgebra with normalized uniform permutation μ_0 as identity, not δ_id. For fixed a, surviving-rank chain is a deletion hypergeometric process; (r)_j are an eigenbasis with λ_j=C(n-j,a)/C(n,a); factorial moments give fixed-a Poisson and Gumbel coupon limits, with a=1 Stirling/harmonic laws classical. Checked rank fibers exactly at n≤4 for mixed profiles and hundreds of eigenfunction cases; universal coupling proof is separate.

## originality

PASS

Ganyushkin–Mazorchuk 2006 §§6–7 **already prove** products of independent uniformly sampled elements of the whole IS_n have law constant on each rank and derive a rank transition matrix/eigenvectors (Lemma 8, Theorem 11); these substantial prior parts are fully credited, not claimed new. The current theorem instead fixes arbitrary rank strata μ_{a_i}, identifies the full semigroup-valued product with a random permutation restricted by independent fixed-cardinality deletion sets, gives explicit multivariate convolution constants for all deletion profiles and a fixed-batch coupon hitting-time law. The prior unconditional uniform-whole-monoid product law neither states nor directly determines the conditional multirank convolution coefficients, and its transition matrix corresponds to a mixture of deletion sizes. Best-of-knowledge PASS qualified by possible older conditioning arguments.

## value

PASS

The rank-stratum probability measures form a natural (n+1)-dimensional commutative convolution algebra inside a noncommutative inverse semigroup. The full labeled-map coupling gives its exact structure constants and a tractable spectral stochastic model for repeated products; it is more informative than the classical scalar coupon-collector limit alone. It links semigroup multiplication, hypergeometric thinning, and occupancy in an exact natural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
