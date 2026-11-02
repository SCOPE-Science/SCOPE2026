---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For six distinct unit normals sum x_i=0 and sum x_i x_i^T=2I, E=M^TM/2 is a rank-three projector orthogonal to the all-ones vector, and its complement F=I-J/6-E is a rank-two constant-diagonal 1/3 projector. Six unit-modulus complex coordinates z_i obey sum z_i=sum z_i^2=0; self-inversive symmetry forces characteristic polynomial z^6-e3 z^3+e6 and partitions them into two equilateral triples. The original normals therefore split into two orthonormal triples with opposite sums; one twist phi in [0,pi/3] parametrizes all configurations. The polar unit-support hexahedron/prism has area A0=18t/(t+1)^2 per normal and volume 36t/(t+1)^2, t=2cos(pi/3-phi); scale to facet areas 2pi/3 to obtain V=4pi^(3/2)(t+1)/(9sqrt(3t)), increasing across t in [1,2]. Exact endpoint volumes 8pi^(3/2)/(9sqrt3) and (2pi/3)^(3/2) with triangular bipyramid/cube shapes. Degenerate endpoint treated; numerical convex hulls are supplementary, not universal proof.

## originality

PASS

Best-of-knowledge originality qualified by material actually accessed. The exact continuous volume equation and endpoint uniqueness require additional geometry beyond the visible prior general existence results. Relevant literature not wholly indexed or accessible; see source_inspections and residual_risks.

## value

PASS

Six is the first nonrigid cardinality for equally weighted spherical 2-designs in dimension three (four is tetrahedral and five impossible), so an exact one-modulus classification plus sharp equal-facet-area Minkowski volume interval addresses a canonical smallest-flexible design family, not an arbitrary sampled polyhedron. All twists and equality types are described.

The dated certificate retains the supplied scientific assessment, sources and limitations.
