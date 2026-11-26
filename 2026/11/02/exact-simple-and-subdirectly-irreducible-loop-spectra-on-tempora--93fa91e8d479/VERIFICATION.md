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

Alvarez's finite-transit definitions and Corollaries 3 and 4 identify simplicity and subdirect irreducibility with Z-connectivity and Z-rootedness. Here Z is the closure of B;≤, where xBw exactly when w≤x and (w,x] has no looped vertex. Every upward cover is one such step and every downward cover from an unlooped upper endpoint is one; conversely any B;≤ step is a saturated descent through unlooped upper endpoints followed by a saturated ascent. Therefore the cover digraph gives exactly Z for any finite poset. On a tree, deletion of an undirected edge separates the graph, so strong connectivity requires every downward arc and is equivalent to loops only at minima. A universal root can be moved down to any minimal vertex beneath it by using an upward path back to the original root. From a selected minimal root, every path is realizable exactly when every outward downward cover is allowed, which means avoiding precisely its Fᵣ. The Boolean families of allowed decorations have intersection enumerators (1+t)^(n−|∪Fᵣ|), giving the asserted weighted inclusion–exclusion. The one-vertex transit has a two-element algebra and two admissible decorations for each property. The independent check in /workspace/branches/frozen_math_replay.py (argument 1) tested Z directly on 2,154 oriented labeled tree/decorations through four vertices, including coefficient checks, and passed. The uploaded checker was inspected, not executed; its counting assertions evaluate the polynomials at t=1.

## originality

PASS

Pass for the explicit forbidden-set classification and weighted enumerators on arbitrary finite Hasse-tree posets. The foundational Z characterizations are Alvarez's, and earlier indexed congruence-lattice work covers a graph-incidence subclass. Neither inspected statement gives the all-Hasse-tree weighted decoration law; priority is not certified for restricted families or unexplored equivalent formulations.

## value

PASS

For a naturally specified dual-frame family, the result turns a transit test for each individual algebra into a classification of all decorations with numbers of loops tracked. Root-specific constraints distinguish simple from merely SI decorations even on small mixed-orientation Hasse trees. The useful output is the family classification and exact polynomial, not a new characterization of arbitrary temporal Heyting algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
