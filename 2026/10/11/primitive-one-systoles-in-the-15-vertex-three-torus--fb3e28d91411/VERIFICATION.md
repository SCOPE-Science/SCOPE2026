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

The six permutations of increments {1,2,4} translated over Z15 yield exactly 90 distinct tetrahedra, f-vector (15,105,180,90), and complete graph edges. Freudenthal triangulation of R³ has deck quotient by ker(a+2b+4c mod15), so H1(K,Z)≅ker(phi)≅Z³, not merely a finite modular-rank inference. The seven representative edge lift vectors for differences 1..7 and their negatives for 8..14 vanish on all actual 180 faces. An independently written exhaustive vertex-triple census counted 455−180=275 missing triangles; every boundary maps to nonzero primitive lattice displacement. Exactly seven sign classes occur with multiplicities 45 each six times, and one multiplicity 5, whose missing triangles are {i,i+5,i+10}. Inspected verifier constructs full order-120 automorphism group from published generators and explicitly exhausts the five systolic cycle orbits and class action. No simple cycle can have fewer than three edges.

## originality

PASS

The exact 15-vertex T³, its universal-cover lattice/neighborliness, facet list, and symmetry group were published by Kühnel–Lassmann and tabulated by Köhler–Lutz (2005 table p29). The accessible full-text 2005 paper lists f-vector (105,180,90), T³, group 5:4×S3 and facet orbits, not the 275 integral primitive triangle homology-class distribution. The highly relevant 1984 Kühnel–Lassmann original could not be fully inspected; authorized Oxford retrieval was safety-blocked after OA search failed, and no override was attempted. Therefore full-paper noncoverage for 1984 is not claimed and unindexed prior explicit computations remain residual risks. Current statement-level evidence supports best-of-knowledge originality without asserting certainty.

## value

PASS

An exact complete combinatorial one-systole census of the canonical minimal 15-vertex triangulation of T³ is a natural topological invariant beyond checking f-vector or ordinary H1 rank. It distinguishes homology directions and rare exceptional 5-element orbit, and combines integral primitivity with full symmetry. It is finite but complete on a mathematically canonical triangulation and potentially useful for discrete systolic and triangulated-manifold comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
