---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For SPD 3x3 C and unit y, every orthonormal frame with constant positive barycentric dot product 1/sqrt(3) is a rotating equilateral triple in y-perpendicular tangent plane. Expanding u_j^TCu_j-tr(C)/3 yields the j-th real harmonic of √2(b1−ib2)e^{iθ}+(p+iq)e^{−2iθ}; all three vanish iff e^{3iθ}√2(b1−ib2)=−(p+iq), so p²+q²=2||PCy||², i.e. Δ=2sqrt(2)||PCy||. Direct coordinate-free trace algebra shows Δ²−8||PCy||² = 9a²+2Tr(C)a−12y^TC²y+2Tr(C²)−Tr(C)²; nonnegative sides avoid squaring spurious roots. Independent symbolic check in tangent block exactly reproduced 4(p²+q²)−8(b1²+b2²), and diag(1,2,3), y=(1,2,1)/√6 satisfies the criterion. When b != 0, three θ solutions differ only by cyclic column permutation; when b=0, the compression is scalar and every θ works. Kania geometric theorem maps this frame criterion to the ellipsoid maximum for every prescribed vertex, while the global maximum formula is correctly attributed to Kania.

## originality

PASS

Qualified PASS: a nontrivial exact answer in dimension three to Kania’s published prescribed-vertex barycentric Schur–Horn problem, with complete quartic criterion and equality family; Kania owns the general extremal geometry and principal-axis subcase.

## value

PASS

Kania’s explicit prescribed-point maximizer question motivates solving the restricted 3x3 Schur–Horn existence problem; intrinsic quartic and generic uniqueness versus rotational degeneracy answer all boundary points rather than just eigenvectors. The nonprincipal triaxial witness shows this is not a substitution of Kania’s principal-axis result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
