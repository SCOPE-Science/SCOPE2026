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

PASS. Independently enumerated every Paley-17 clique (17 vertices, 68 edges, 68 triangles, zero tetrahedra), with Q={1,2,4,8,9,13,15,16}. No nontrivial 17-translation stabilizes a face of cardinality <=3, so the action on |X| is free. Enumerated orbit partitions: one vertex, four edge orbits (steps 1,2,4,8), four triangle orbits represented by (0,1,2),(0,2,4),(0,4,8),(0,1,9). Their oriented attaching words are x1*x1*x2^-1, x2*x2*x4^-1, x4*x4*x8^-1 and x1*x8*x8. These nonabelian presentation relators permit actual CW one-/two-cell cancellations to one loop x1 and one degree-17 2-cell, giving X/C17 homotopy equivalent to M(Z/17,1), not merely equal homology. The quotient has π1=C17. The original action cover X->X/C17 has degree17 and maps edge x1 to generator, hence is universal cover. The universal cover of the Moore CW model has R=Z[C17] chain 0→R --N=1+...+t^16→R --(t-1)→R→0; kernel N is exactly augmentation ideal I and no other positive reduced homology. This establishes the integral C17 module action, not just rational Betti ranks.

## originality

PASS

PASS, best-of-knowledge. Rinaldo–Romeo explicitly establish Paley-17 circulant independence-complex vertex decomposability; Paley self-complementarity covers original clique-complex nonequivariant sphere topology, which is excluded from novelty. The published Paley-17 Lovász open-neighborhood complex has unrelated three-torsion and different facets. None of those statements computes this ordinary translation orbit-space attaching map or integral augmentation-ideal deck module. Potential unindexed equivalent quotient computations remain a residual risk.

## value

PASS

PASS. A natural free order-17 symmetry on the smallest pertinent Paley clique complex produces an explicit Moore-space quotient with torsion fundamental group and a nontrivial integral deck homology module. This exact symmetry-refined topological invariant is not supplied by the known vertex-decomposable classification and is a useful canonical finite example distinguishing orbit topology from original homology and from Borel quotients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
