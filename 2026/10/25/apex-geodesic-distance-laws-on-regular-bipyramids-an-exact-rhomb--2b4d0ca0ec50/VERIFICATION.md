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

Reconstructed the paired upper/lower triangle isometric unfolding into convex equal-edge rhombi. The Euclidean source-distance potential agrees across upper, equatorial and lower seams and is facewise 1-Lipschitz, so is a lower bound on every intrinsic path, while the straight rhombus segment attains it; this establishes exact distance rather than an assumed unfolding. Uniform rhombus coordinates yield the U,V law; independently checked its second/fourth moments for four angles and evaluated both the 1D polar CDF and each closed piece for angles 0.55,π/2,1.73,2.04 at multiple thresholds (agreement to <2e-7 including numerical integration tolerance). The tangential contact expands quadratically at α=π/2 and at interior minimum for α>π/2, establishing ε^(3/2); transverse acute contact gives ε². Formula for α and h/R confirms only n=3 can yield obtuse angle and right case is h/R=1/sqrt2. Finite numerical checks corroborate full symbolic geometric argument, not exhaustive quantifiers.

## originality

PASS

Qualified PASS for the exact all-parameter intrinsic bipyramid reduction and sharp onset law. Li–Qiu gives planar triangle/rhombus area integrals and moments but not the intrinsic polyhedron-to-rhombus identity; Itoh–O’Rourke–Vîlcu gives general quasigeodesic star unfolding, not the evaluated stochastic law. A later skeletal-cut-loci paper is abstract-only and remains a material equivalence risk.

## value

PASS

A full intrinsic distance law over an entire natural polyhedral family is reduced to one rhombus, with a sharp geometry-controlled transition from ε² to ε^(3/2), and explicitly identifies which dimensions permit the obtuse regime. The onset singularity and stochastic order plus shape-invariance answer motivated surface sampling and geodesic questions rather than a gratuitous parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
