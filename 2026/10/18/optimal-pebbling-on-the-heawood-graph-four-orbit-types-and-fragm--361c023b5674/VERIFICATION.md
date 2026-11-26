---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently reconstructed full reachability for a binary dot-product model of the Fano plane, reversing moves from distributions already occupying each target, in increasing weight. Every reverse step removes one at an occupied recipient and adds two at a neighbor; each such parent has a legal forward move. An explicit point-line relabeling to the cyclic model gives exact agreement with all 38,760 frozen mask rows, 161 optima, and 42 slide and jump edges (21 three-vertex paths and 98 isolated vertices). Counting every permutation of the seven points preserving the lines and composing with the dot-product duality gives all 336 automorphisms, because the connected bipartition is unique and a side-preserving permutation is determined by its point permutation. The four geometric class orbits have sizes 21,42,56,42. The repaired proof uses the known profile restriction, but determines geometry without counting solutions: target weight strictly excludes misplaced same-side two piles and noncollinear triples, and at weight exactly one the two opposite singleton lines must each receive a delivery from the heavy point and then can only send to distinct points on the target line. Nonincident 3+3 piles cannot interact after either first move. Explicit routes establish each case of sufficiency, including splitting two deliveries through the intersection of the two-pebble line and a remote target line in the 4+2 case. Basis changes and duality give transitivity in each geometrically distinguished family. This reconstructs necessity, sufficiency and the orbit partition in the repair.

## originality

PASS

The frozen package's scalar optimum, total census, three pile-size profiles, and both optimal relocation graphs have exact coverage in the broader Heawood slack-threshold record. They are now credited as background rather than claimed. The surviving distinct finding identifies the four full orbits by a necessary-and-sufficient Fano incidence rule, and proves the incidence mechanism. The compared source's weight profiles do not specify which supports with those profiles work; its transfer edge and component counts do not supply that rule. This is a scope assessment, not a finding of chronological priority.

## value

PASS

The repair turns an optimum size and unordered pile-profile census into a local, geometry-based test for exactly which configurations work. This makes all optimum states describable by four representatives with explicit transitivity and provides a route or an obstruction for each configuration type, including the sharp target-potential equality case. It is a natural finite classification useful for studying solvable configurations on this incidence graph, not just retabulating the covered minimum or transfer counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
