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

For SG_{4,2}, cyclically stable 4-subsets of Z/10 give exactly 25 vertices and 60 disjointness edges. Independent-set masks reconstruct f=(25,240,1160,3140,5079,5160,3370,1380,320,32), 19,907 faces including empty. I independently implemented the specific 16-pivot face matching from verify_homotopy.py and checked all 110,730 Hasse incidences in an acyclic topological sort (19,907 processed). Exactly 9,952 augmented pairs and three augmented critical cells remain; the empty pair yields an ordinary critical vertex, with one critical 3-cell and two 4-cells. Exact integer recursive projection of both critical 4-boundaries onto the 3-cell gives (0,0). Since each attaching map S^3→S^3 is classified by integral degree, the Morse CW complex is S^3∨S^4∨S^4. These exhaustive finite computations, not mod-two Betti numbers alone, prove the finite homotopy result.

## originality

PASS

The exact finite SG(4,2) independence-complex wedge calculation appears distinct from Braun 2009, whose SG(2,k) theorem and auxiliary E_{2n+2} theorem are not SG(4,2), and from neighborhood-complex sphere results. The Resultary search found the assigned entry and distinct finite graph examples, not direct known coverage. Priority beyond consulted literature remains uncertain.

## value

PASS

Schrijver complexes are a natural test case in topological combinatorics; this resolves a concrete 25-vertex instance in Braun’s previously unclassified SG(n,2) independence-complex family at the stronger homotopy (not only field homology) level. Exact integer attaching maps are a mathematically substantive finite invariant, not an arbitrary slice or rebranded graph parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
