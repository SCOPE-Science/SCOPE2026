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

For L,H>0, check the full even/odd deck-orbit minimization D^2=min{A^2+V^2,B^2+(H−V)^2}; the determinant-2 horizontal torus map preserves product Haar, so A and B are independent Unif[0,L/2], independent of triangular V. The injected geodesic disk range gives F(r)=pi*r^2/(LH) for r<min(L,H)/2. Both min terms reach (L^2+H^2)/4 exactly when A=B=L/2,V=H/2, proving the support diameter. With alpha=L/2−A,beta=L/2−B,delta=V−H/2, the rescaled inequalities for s=rho^2−r^2 are 0<u<(1+Hz)/L,0<w<(1−Hz)/L, |z|<1/H; the density is 4/(L^2 H). The integral (4/(L^4 H))*integral_{−1/H}^{1/H}(1−H^2 z^2)dz equals 16/(3L^4 H^2), a full all-aspect ratio dominated-convergence proof. Small-ball area LH and endpoint coefficient reconstruct L and H uniquely. Independent pointwise deck-reduction checks and rescaled numerical quadrature for (L,H)=(1,2),(2,1),(3,2) found near-tail ratios 1.009102,1.006044,1.007620 at small positive s; these only corroborate the proved limit.

## originality

PASS

Best-of-knowledge PASS: the exact nonorientable flat-Klein two-point law, cubic rather than torus quadratic tail, and injective reconstruction of the labeled translation/glide periods were not identified as consequences of the inspected published distance-distribution theory or flat-Klein geometric papers. The broad Mémoli–Needham primary source was accessible here only as abstract, and authorized full-text retrieval returned vpn_disconnected, so entire-document noncoverage is NOT claimed. This limitation and equivalent-coordinate priority risks remain explicit.

## value

PASS

The complete smooth-flat Klein-bottle isometry class is a natural two-parameter space. A cubic endpoint law distinguishing it from a rectangular torus and resolving the equal-area/equal-diameter swapped-period ambiguity is a motivated inverse geometry theorem, not an isolated tail constant or numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
