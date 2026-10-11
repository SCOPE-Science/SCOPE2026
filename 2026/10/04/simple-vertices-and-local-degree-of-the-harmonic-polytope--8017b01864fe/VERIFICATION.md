---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The source dimension/order formula makes the incident-edge classification exact: a codimension-one coarsening either performs one adjacent merge while keeping K={k}, or keeps both permutations and enlarges K by one product maximum. The two possible predecessor merges fail exactly in the two stated adjacency cases, while set enlargement contributes s-1 choices, giving degree 2n+s-3-epsilon_- -epsilon_+. Setting this equal to dimension 2n-2 yields the three simple forms. A fresh independent exhaustive replay over all relative permutations through n=6 matched the direct codimension-one count for every marked right-to-left maximum and reproduced fixed-first-permutation simple counts 3,7,21,83,410 for n=2,...,6.

## originality

PASS

Originality passes. Ardila--Escobar give the full harmonic-triple face-poset encoding, global vertex/facet counts, and note that the harmonic fan is already non-simple for n=3, but they do not extract vertex degrees, classify simple maximal cones, or enumerate them. Those quantities require a nontrivial codimension-one coarsening classification and a marked right-to-left-maxima enumeration. The bipermutahedron paper concerns the related simple refinement, not local degrees in the harmonic polytope.

## value

PASS

Simplicity is a canonical local invariant of a polytope and is especially natural here because the defining paper already flags non-simplicity of the harmonic fan. The exact local formula identifies all regular maximal cones, the closed count quantifies how rare they are, and the density tends to zero. This is structural information rather than a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
