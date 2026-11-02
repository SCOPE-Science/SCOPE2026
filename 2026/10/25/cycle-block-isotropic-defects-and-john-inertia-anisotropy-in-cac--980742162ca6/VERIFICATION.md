---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every finite connected simple cactus, choose coherent cycle edge orientations. Potential-edge map B is injective on zero-sum vertex H, and dim W=b+Σ(m_i−1)=n−1, hence an isomorphism to product W of cube central sections and bridge intervals. Its Euclidean Jacobian is sqrt(n τ(G))=sqrt(n∏m_i) by matrix-tree. Coarea for m independent uniform variables on [−1,1] gives section volume 2^m sqrt(m) f_m(0); conditional variance v_m on a coordinate and covariance operator m/(m−1) v_m I on H_m, bridge variance1/3. These yield vol_d(Q_G)=2^|E|/sqrt(n) ∏ f_m_i(0), and (12 L(Q_G)^2)^d=∏((3 m v_m/(m−1))^(m−1)/(4m f_m(0)^2)). The unique John ellipsoid of each symmetric cube section is the centered ball of radius sqrt(m/(m−1)), certified by equal facet contacts; direct-sum John contact measures certify product ellipsoid. After John normalization, covariance is ⊕v_m I ⊕(1/3) I. Since 0<v_m<1/3 for m>=3, every mixed bridge+cycle cactus has nonhomothetic John/inertia ellipsoids. Independently integrated f3=3/8, f4=1/3, v3=5/18, v4=3/10 and exact Θ3=25/27, Θ4=243/250. The result is all-cactus by block argument, not just finite tests.

## originality

PASS

Best-of-knowledge PASS for the joint cactus graph volume, exact cycle-section isotropic factors, John-normalized covariance and persistence of inertia anisotropy through bridge attachments. D’Alì–Delucchi–Michałek establishes fundamental symmetric-edge graph polytopes and gluing; a published Hanner result establishes product-isotropy recursion. Those tools/identities are credited. They do not themselves supply the stated explicit central-section moments for all cycle lengths or the mixed-cactus John/inertia conclusion. Central-slice / B-spline historical equivalence risk remains.

## value

PASS

Cactus graphs form a natural maximal class of edge-disjoint cycle systems with exact block decomposition. The explicit factor Θ3=25/27 and dimension-independent John-coordinate condition number 6/5 for triangles plus bridges show affine isotropy can approach the cube constant while inertial anisotropy remains, a motivated structural convex-geometry phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
