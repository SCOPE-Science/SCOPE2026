---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed the analytic proof from RESULT.md blob 11cbbd9e649066560233055c60f5cba5e4e3b940. For a product base K, replacing arbitrary test bodies L,M by Cartesian products of their factor projections weakly increases the mixed two-body numerator by monotonicity; their first mixed-volume denominators remain exactly equal because the first area measure of K is carried by factor-normal subspaces and h_L restricted to each is the projected support function. Expanding vol(K+t product(L_i)+s product(M_i))=product_i vol(K_i+t L_i+s M_i) gives normalized coefficients sum a_i, sum b_i and sum_{i≠j}a_i b_j+sum c_i. Each c_i≤[(d_i-1)/d_i] beta_i a_i b_i and all a_i,b_i≥0. Dividing yields upper beta_n≤n/(n-1) Gamma. Tests supported in different factor subspaces attain cross coefficient 1; tests in one factor approximate its beta_i, proving each lower-bound term even if sup is unattained. Symmetric affine invariance holds via determinant normalization. Theorem 6.1 of Soprunov–Zvavitch establishes beta_2(D)≤2, supplying the planar corollary. Inspected the bundled exact polynomial-product and zonotope determinant checker and separately checked the combinatorial coefficient expansion; bounded finite checks are corroboration, not the arbitrary-body proof.

## originality

PASS

Closest indexed and primary theorems distinguish PSD mixed discriminants, arbitrary-body inequalities, zonoid-limited estimates, and planar sharp constants; none of their inspected statements implies the exact max-of-factor-coefficients product formula for all convex tests.

## value

PASS

The optimal two-body Bézout coefficient is a standard geometric invariant, and the exact functorial Cartesian-product law reduces a general higher-dimensional optimization to factor invariants plus one cross-factor witness. It gives a new sharp all-dimension consequence for products of planar sets and segments; such a tensorization statement is mathematically useful even though its proof uses classical mixed-volume tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
