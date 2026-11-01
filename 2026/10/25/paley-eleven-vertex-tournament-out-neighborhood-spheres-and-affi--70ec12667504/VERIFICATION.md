---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Each five-vertex out-neighborhood is x+R, R={1,3,4,5,9} modulo 11. Exhaustive independent face construction found (11,55,110,55,11), 242 nonempty faces. Independent reproducible elementary-collapse matching yielded exactly 110 face-coface pairs and 22 critical cells (one vertex, 21 triangles); reversing match edges in all 715 Hasse incidences gave acyclic directed graph with all 242 nodes topologically sorted. This gives the integral wedge of 21 two-spheres. Signed Lefschetz checks of all 55 affine symmetries yield (21,-1,1), the character of 1+2 Aug(Q[11]); quotient rational H2 rank 1 follows by averaging.

## originality

PASS

Dochtermann–Singh directly define directed out-neighborhood complexes as the Hom of an oriented edge and study general topology and tournament examples, including five-vertex tables and realizability constructions. The accessible full manuscript does not provide the 11-vertex quadratic-residue tournament’s exact wedge decomposition or its affine rational character.

## value

PASS

A complete integral homotopy and symmetry calculation for the canonical order-11 Paley tournament is a concrete, independently reusable benchmark for directed Hom/neighborhood topology, distinct from small-order census and general existence results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
