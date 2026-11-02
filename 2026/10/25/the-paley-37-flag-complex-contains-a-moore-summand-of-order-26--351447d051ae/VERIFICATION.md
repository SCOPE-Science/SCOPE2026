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

The exact difference-of-quadratic-residues graph P37 yields 37 vertices, 333 edges, 888 triangles, 555 tetrahedra (1813 nonempty faces), no larger cliques and χ=37. Independent staged bit-mask face pairing produces 841 pairs; inspection of all 5,550 face incidences plus a complete Hasse-DAG topological sort verifies acyclicity. The only critical cells are one 0-cell, 83 2-cells and 47 3-cells. Independently reconstructed signed Morse boundary B:Z^47→Z^83 has Smith factors 1 repeated46 and final 26. Stronger exact determinantal witnesses independently recomputed: specified 46×46 minor determinant +1, 47×47 minor determinant −26, agreeing with mod-2 and mod-13 rank drop and excluding any further factors. With one 0-cell and no critical 1-cells, Morse CW 2-skeleton is wedge of 83 2-spheres. The 3-cell attaching classes are integral degree vectors in π2=Z^83; Smith row/column changes are realized by sphere basis maps and CW cell slides. Canceling 46 unit pairs leaves 36 free 2-spheres and one degree-26 3-cell, exactly M(Z/26,2). Finite complete computation, not asymptotic theorem or extrapolation to other primes.

## originality

PASS

Knill records the Paley-37 clique Euler characteristic 37, which cannot imply torsion. A published analogous Paley-29 Moore summand has order 2, not the order-26 summand of P37. Published strongly regular graph clique-homology results establish first homology vanishing and a different Latin-square family rank formula but not this integral second-homology and homotopy classification.

## value

PASS

The natural Paley(37) graph supplies a canonical finite flag complex with rare odd-primary (13) torsion simultaneously with 2-torsion. The exact integral homotopy type is mathematically stronger than Euler characteristic and Betti ranks; detecting a nontrivial 26-attachment requires meaningful integral Smith computation rather than routine arithmetic. This precise finite complex and invariant are directly reusable in topological graph theory and test conjectures about torsion of strongly regular graph clique complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
