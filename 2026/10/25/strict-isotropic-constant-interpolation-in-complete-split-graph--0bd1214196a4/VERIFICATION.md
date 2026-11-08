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

For p>=1, stable-set hull equals {x_i>=0, y_j>=0, T+y_j<=1}; slicing at T=sum x_i yields coarea density T^(p-1)/(p-1)! and beta(p,q+1) law. Direct q-cube integration gives Vol=q!/N!, conditional Dirichlet p-simplex and conditional independent U[0,1-T] variables give raw means and the stated unsheared covariance. The determinant-one shear W_j=Y_j+T/2 eliminates clique/independent cross covariance and all independent off-diagonals, with Var(W_j)=(q+1)(q+2)/[12(N+1)(N+2)]. Cov(X) has p-1 equal eigenvalues 1/[(N+1)(N+2)] and sum-direction eigenvalue (q+1)/[(N+1)^2(N+2)], yielding the claimed determinant. p=0 reduces to the cube. The explicit B_N(q+1)/B_N(q) expression equals (1+1/s)^2(1+2/s)^s/12, s=q+1>=2; s=2,3 checked rationally and for s>=4 the bounds (5/4)^2 e^2 < (5/4)^2(11/4)^2 <12 establish strictness. Uniform Stirling including q=1 and q=N yields log L=-p/N-q log 12/(2N)+O(log(N+2)/N); alpha limit follows. Independent Fraction/sympy implementation independently derived conditional second moments and checked full covariance determinants and shear for 66 (p,q) pairs (p=0..8,q=1..9,N<=12), 149 exact rational adjacent ratios for q=1..149 and asymptotic errors for N=25,100,500,2500. These checks corroborate but are not used as infinite proofs. No claim for q=0, p=N, general split graphs or vertex-uniform measure.

## originality

PASS

Best-of-knowledge claim-level comparison: graph stable-set literature gives the body and clique facets, and the known chain-polytope volume yields q!/N!, but no inspected primary full theorem yields the normalized continuous covariance determinant together with strict p-step ordering and uniform macroscopic interpolation. The closest published exact Hanner isotropic formula applies to centrally symmetric ℓ1 sums rather than these generally nonsymmetric positive stable-set bodies. A reported 2026 global simplex maximum entails at most the final endpoint upper bound, not the strict full chain. Closely related unindexed simplex-cube join or beta-Dirichlet moment recursions remain priority risks, not mathematical disproof.

## value

PASS

For a natural complete split-graph edge-completion chain that genuinely interpolates from the hypercube to the simplex, the affine-invariant isotropic constant measures global uniform-volume concentration, not a merely cosmetic edge/volume statistic. A complete closed determinant, strict all-dimension monotonicity under this specific inclusion (not true for arbitrary convex inclusions), and a uniform limiting density curve separating macroscopic clique fractions form a motivated and independently useful geometric classification. Although beta slicing and the classical endpoint constants are standard, the strict ordered family and uniform interpolation are not simply another small finite instance or restatement of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
