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

Conditioning on the center spin gives the two products; dividing by ∏q_i gives F(z)=∏(z+a_i)+z∏(1+a_i z). It is reciprocal, has degree m+1 and F(0)>0. For positive angles the lifted phase of B_m(z)/z is strictly convex, starts at zero, ends at (m−1)π, and is strictly greater than −π before the endpoint. Each positive odd level below the terminal value is crossed once with positive derivative, by convexity and the positive secant slope from zero. Conjugate symmetry and the single endpoint −1 when m is even give exactly m−1 simple unit roots, also for m=1. On (0,min a_i), B_m(−x) is positive strictly decreasing from P_m to zero, hence meets x once and transversely; reciprocity yields the distinct exterior root. The total exhausts the degree. At the inner root x/P_m=∏(1−t_i) with t_i=x(1−a_i²)/[a_i(1−a_i x)]∈(0,1). The union bound for this product, x<P_m and P_m/a_i≤a_*^(m−1) give the claimed uniform estimate. For m c_*>1 the phase of B_m(z)/z is increasing on the whole lifted interval. Counting the odd-phase lattice on a half-open interval incurs error at most 1. After dividing by m+1, subtracting the angular-length term and changing m+1 to m each incur at most 1/(m+1), giving the stated 3/(m+1). The averaged arc kernel is continuous and bounded in a∈[0,a_*], and the limiting circle measure has no atoms; the escaping pair contributes only 2/(m+1) against bounded continuous tests. The finite polynomial example also checks independently: division by z² and y=z+z⁻¹ give y²+40y+60, with exactly one y in (−2,2) and the other below −2.

## originality

PASS

Credit classical Blaschke theory for the qualitative fixed-point count and the boundary Poisson-kernel derivative, and credit the prior ferromagnetic-star record for the same explicit bulk-density form. The supported distinct claim is the quantitative heterogeneous antiferromagnetic-star result, especially the negative pair's uniform product-relative escape estimate, with an explicit arc bound for the complementary spectrum. Neither the fixed-point count nor the bulk kernel alone is a novelty basis.

## value

PASS

A star is a natural high-degree tree where uniform-field antiferromagnetism allows violations of the circle theorem. Arbitrary bond heterogeneity could in principle complicate the zero geometry; the result isolates the exceptions and gives a uniform, explicit multiplicative estimate depending on the full interaction product. Together with the finite bulk discrepancy this is a useful quantitative local model, not a claim about a bulk phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
