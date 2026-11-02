---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Rotation symmetry and direct edge second-moment integration yield K_n(x,y)=1+[6/(2+cos(2π/n))]x·y. Convexity of its L1 norm in the evaluation point bounds all perimeter points by vertex values; strict sign disagreement between adjacent vertex kernels on a positive-measure arc excludes edge interiors. At a vertex the kernel values change sign between integer indices J−1 and J, J=ceil(n/3); exact negative edge integrals consist of a full negative-vertex cosine sum minus two fractional crossing-edge triangular deficits amounting to ab/(a+b). This gives the closed finite-n expression. Taylor expansion in h=2π/n with d=J−n/3 in {0,2/3,1/3} produces the stated common positive n^-2 term and n mod 3 cubic correction. Fresh high-precision independent direct edge integration for every n=3..100, rational n=3,4,6, and n≈30000 across all congruence classes corroborated the formula and cubic sign.

## originality

PASS

The indexed three-frequency Fourier norm problem has a different measure (uniform vertex counting), hence different kernel coefficient and even the opposite sign of the n^-2 defect for some classes. Hangelbroek–Narcowich–Sun–Ward bound L∞ norms of general smooth-manifold kernel projectors, not the exact continuous perimeter-affine polynomial kernel and its n mod 3 asymptotic. The Resultary simplex-affine norm uses volume measure on simplices and cannot imply the polygonal perimeter exact formula without new integration. Possible older numerical-analysis Lebesgue constant calculations remain a qualified priority risk.

## value

PASS

The exact endpoint operator norm is a natural stability and positivity-defect invariant for least-squares approximation on polygonal meshes. The arithmetic n mod 3 term distinguishes discrete polygon boundaries from their smooth circle limit and from vertex-only sampling, and the explicit sharp norm is applicable across every n≥3 rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
