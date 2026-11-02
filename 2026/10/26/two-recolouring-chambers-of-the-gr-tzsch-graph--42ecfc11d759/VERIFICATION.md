---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The source C++ uses a recursively exhaustive proper-colouring generator plus an independent complete scan of 4^11 assignments, each edge of the 20-edge Grötzsch adjacency graph, all eleven single-vertex recolouring replacements, reverse-edge checks, breadth-first components and all-roots BFS for exact diameters, and verifies all 24 palette and 10 dihedral actions. Our independent implementation regenerates all 12480 proper states, builds 45240 edges, checks two 6240 components and runs BFS from every state; checks parity/dihedral action on all states, not merely a representative. The 3-degeneracy theorem establishes connectedness for all >=5 colours. Independent check: Independent C++ implementation verified vertices=12480, edges=45240, component sizes [6240,6240], diameters [17,17], 24 palette permutations and 10 dihedral automorphisms on every colouring. Source verify.cpp control flow and full 4^11 scan were inspected; this is an exhaustive finite proof, unlike sampled simulations.

## originality

PASS

Best-of-knowledge priority qualified by primary-source comparisons and explicit antecedent/corollary limits; For the standard Mycielskian of C5, the 4-colouring single-vertex recolouring graph has 12480 labelled states and 45240 edges, exactly two 6240-state components of diameter 17 with degree counts (240,1320,1920,2160,600) at degrees 5..9 per component; odd palette permutations and reflections swap components, even permutations and rotations preserve; its mixing threshold is 5. is not supplied in the compared prior statements.

## value

PASS

The Grötzsch graph is the canonical smallest triangle-free 4-chromatic graph; a complete, nontrivial 12480-state recolouring chamber classification, symmetry obstruction and sharp diameter is a reusable finite benchmark in reconfiguration theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
