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

Independently enumerated all spoke subsets and completed each exact cover on the remaining outer decagon and two inner pentagons. The spoke choice and three residual cycle choices are exhaustive and determine the matching. This yielded 36 perfect matchings. Tabulating all 36×1024 submasks globally makes a submask forcing precisely when its incidence multiplicity is one. The resulting coefficient vectors in degrees 0–10 were (0,0,0,20,110,202,200,120,45,10,1) six times and (0,0,0,24,122,216,204,120,45,10,1) thirty times. Separately enumerated simple length-eight cycles by starting at their least vertex and choosing a traversal orientation; exchanging alternating edge masks when contained in a matching gives all and only the stipulated flips. The graph has 120 unordered edges and all 36 eccentricities equal three. The joint counts (forcing triples, degree, degree-ten neighbors) are (20,10,0) six times and (24,6,2) thirty times, proving the precise cross-neighbor assertion. The separate four-cycle enumeration is empty, also validating the frozen symmetric-difference shortcut.

## originality

PASS

Pass for both distinct complete all-forcing-subset profiles, the exact eight-cycle perfect-matching flip statistics, and their class correspondence. No originality is assigned to the 36 matchings, the 30+6 structural split, forcing number 3, or the concept of an alternating-cycle move. The closest inspected sources study the same invariant on a different graph, the same graph with a different invariant, or the same graph with different configurations; none of their results implies the exact profiles or flip statistics checked here.

## value

PASS

The dodecahedron is the smallest fullerene and a natural symmetric test case. The ordinary forcing number cannot distinguish any of its matchings, while the all-subsets invariant measures the number of certificates at every observation size. The flip census identifies the same two classes by exact local mobility and gives the higher-degree class's entire cross-type incidence, not just a second list of counts. These are useful exact benchmarks for forcing and reconfiguration on a canonical graph, not a claimed general correlation law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
