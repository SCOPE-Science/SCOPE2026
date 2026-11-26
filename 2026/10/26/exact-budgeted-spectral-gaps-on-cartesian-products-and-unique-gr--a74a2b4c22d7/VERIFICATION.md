---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For each direction i, testing on centered vectors constant in the other coordinates gives the factor Rayleigh quotient with rates averaged over the N/n_i fibers. By budget homogeneity this bounds the product gap by α_i B_i/(N/n_i), also when B_i=0. Summing the budget inequalities gives the sharp upper bound. Each factor's unit-budget optimizer exists by compactness and has positive gap by using all edges. Repeating these designs with equal gaps gives a Kronecker sum attaining the bound. On a path with w_k=ℓ k(n−k)/2, the order-r finite-difference terms contribute leading coefficient ℓ[r+binom(r,2)] to L(k^r), with no term of higher degree; the boundary weights are zero, so this holds at the endpoints. The polynomial flag then gives the full path spectrum, and tensor products add the eigenvalues with multiplicity. For a grid the centered coordinate k_i−(n_i+1)/2 has squared norm D_i=N(n_i²−1)/12 and energy B_i. Equality at the optimum forces each coordinate to be a gap eigenvector, regardless of multiplicity. The difference equation on each separate fiber with w_0=0 has the unique parabolic solution, so asymmetric allocations cannot tie it. The spectrum has exactly d occurrences of its smallest positive value. Dividing by the uniform gap using d(n−1)n^(d−1) edges yields the given ratio and the cosine expansion gives its limit, also consistent with equality at n=2. No graph symmetry of a competitor or hidden normalized-Laplacian convention is used.

## originality

PASS

The supported distinction is the unrestricted fixed-total-conductance formula for arbitrary connected factors and the all-edge uniqueness result for rectangular grids. Single-path parabolic optimality and uniqueness, the geometric dual, and fixed-weight product spectral addition are prior ingredients, not new findings. The closest comparisons do not supply the unrestricted optimization theorem and grid equality classification in this model.

## value

PASS

The result resolves the full budgeted optimization on a natural graph product by reducing it to factor optima despite allowing variations across every fiber. On rectangular grids it also determines the unique design, multiplicities and quantitative cost of uniform weighting. The equality argument excludes ties outside the repeated-fiber family, a mathematical conclusion not available merely from selecting directional multipliers or plugging prior path optima into the product spectral identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
