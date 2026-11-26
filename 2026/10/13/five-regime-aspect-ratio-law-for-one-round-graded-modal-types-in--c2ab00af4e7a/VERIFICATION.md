---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exact type is (cell bit, row sum, column sum): interiors at depth zero have only two colors to distinguish and the named modal thresholds recover both sums. The finite algebra consists of all unions of these type classes. For a binomial sample of size t at length L, below square-root scale the expected number of coincident pairs is O(t²/√L)=o(t); at t/√L→1 the expected occupancy is the local-limit Riemann sum √L times L_v with tails bounded by the expected number of tail observations, and variance at most the mean by negative covariance. Above that scale, writing t/√L=n^(β+o(1)), the inner interval of radius (1−ε)√(2Lvβ log n) has t times each bin mass polynomially large. The expected number of samples outside the outer radius (1+ε)√(2Lvβ log n) is at most √L n^(−β(2ε+ε²)+o(1)) by Bernstein, and Markov bounds their distinct values too. The row and column samples need only be internally independent. For a<2 the column-degree interval is in the dense occupancy regime. For a fixed row, mark and degree, the success probability is the mark probability times the shifted Bin(m−1,p) mass, and trials over columns are independent before any row conditioning. The uniform polynomial lower bound on n times this probability defeats the union bound over all rows, marks and inner degrees. This establishes coverage on every row before choosing degree representatives, giving 2R|I|≤K1≤2RC. At a≥2 the row-degree sample is dense and the transposed argument gives the same result. The squeeze as ε→0 proves saturation without treating cross-axis degrees as independent. Multiplying the occupancy limits gives each frozen coefficient, including 8v at a=1, 4L_v√(3v/2) at a=1/2 and 4L_v√(3v) at a=2. The floor does not affect these limits.

## originality

PASS

The supported distinct claim is the explicit asymptotic and near-saturation of the two-mark degree-pair alphabet of iid rectangles. The available comparisons credit existing modal semantics, refinement, and degree sequence theory but do not establish this quantitative law or its critical constants.

## value

PASS

For a standard two-equivalence model, the one-round algebra size is a natural measure of the expressive gain from counting. A square-only estimate or a marginal-product upper bound would miss whether that upper bound is attained and both critical crossovers. The theorem resolves both questions over the full natural polynomial aspect family with explicit constants and a uniform coverage argument reusable in comparable occupancy problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
