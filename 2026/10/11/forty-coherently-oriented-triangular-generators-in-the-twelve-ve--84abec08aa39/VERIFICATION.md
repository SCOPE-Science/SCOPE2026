---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Read the exact 48 four-simplex facets from frozen verify.py. An independently written JS combinatorial enumeration rebuilt f=(12,60,120,120,48), all six antipodal nonedges, and 40 nonfacial triangles. The specified integer cocycle has 15 positive increasingly oriented edges, evaluates zero on ALL 120 triangular facets and +1 on EACH of the 40 nonfacial triangles. Published topology identifies H1≅Z, hence unit evaluation proves each triangle is a common primitive generator, not just nonzero mod2. Exhausted ALL 2^6×6! permutations preserving the mandatory nonedge matching and found exactly 24 simplicial automorphisms, and carrier orbits 4,12,24 with representatives (1,5,9),(1,3,8),(1,4,8); each vertex occurs ten times. Exhaustion is complete because any automorphism must preserve missing edges.

## originality

PASS

Lutz’s exact-object census already supplies the 12-vertex S³×S¹ triangulation, crosspolytope one-skeleton, 48 facets, f-vector and dihedral presentation. These are not claimed original. The checked published source does NOT classify the integral homology of all 40 nonfacial triangles, coherent sign, or full carrier-orbit decomposition. Resultary’s other triangular-systole findings concern nonisomorphic manifolds, including a 12-vertex twisted S³ bundle with 76 triangles, 14-vertex S4×S1 with 70, and S²×S² H2 cycles; these do not imply this result.

## value

PASS

The shortest nontrivial integral H1 carriers of a canonical small vertex-transitive triangulated S³×S¹ are a natural discrete systolic invariant. Unit cocycle pairings simultaneously settle primitivity and coherent orientation of the complete shortest layer, beyond the raw f-vector, mod2 rank, or enumeration of nonfaces. Their full symmetry orbit profile is an exact natural finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
