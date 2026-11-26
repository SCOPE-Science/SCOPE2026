---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An independent full computation represented Petersen as KG(5,2) (indices mod 5, u_i={i,i+2}, v_i={i+3,i+4}) and represented a colour class by a nonempty matching of the 15 edges. It enumerated all matching masks and recursively partitioned the remaining edges by adding the unique class containing the least uncovered edge. This exhausts unordered partitions into at most four classes without duplicates. No cover with fewer than four classes occurred. For each union of two classes, it closed a seed edge's endpoints under incident union edges to recover one component at a time, XORed the component into each class, sorted the class masks and removed loops. Bitset distance fronts from every state reached all states; a front contains exactly the vertices at its current distance. The automorphisms used were the S5 action on the pairs: the size-four independent sets in KG(5,2) are exactly the five stars (checked over all four-subsets), and each vertex is determined by the two stars containing it, so the action is the full Petersen automorphism group. Orbit computation on matching masks gives (size,eccentricity):multiplicity (20,6):1, (40,6):1, (40,7):1, (60,5):1, (60,6):2, (120,6):14, (120,7):1. Output confirms 2080 states, 12600 undirected edges, degrees 12:1840 and 13:240, eccentricities 5:60, 6:1860 and 7:160, radius 5, diameter 7, group order 120 and 21 orbits. Both the independent reconstruction and the supplied algorithm address all states, not a sample.

## originality

PASS

Credit is for the complete Kempe metric and symmetry strata, not the previously proved connectivity or the underlying colouring count alone. The nearest indexed variants change the move or the object. The bounded evidence does not identify a prior statement or table entailing these profiles.

## value

PASS

Petersen is the classical small cubic obstruction to three-edge-colourability, so its four-colour reconfiguration graph is a natural benchmark in the palette where Kempe connectivity is guaranteed. Exact radius and diameter specify the best-base and worst-pair numbers of component moves, and the orbit census establishes the sharp distinction between a single central Petersen orbit and two peripheral orbits. These are natural finite invariants for comparison with other cubic reconfiguration graphs, not just a known connectivity test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
