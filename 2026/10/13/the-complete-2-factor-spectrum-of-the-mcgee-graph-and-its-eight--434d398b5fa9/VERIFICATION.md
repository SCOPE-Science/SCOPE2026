---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the exact 24-vertex 36-edge LCF [-12,7,-7]^8 model, complement in a cubic graph bijects each perfect matching with one 2-factor. Independent perfect-matching recursion branching on the least unused vertex produces 60 perfect matchings, and cycle tracing on each complement yields 42 type (24), 6 type (12,12), and 12 type (8,8,8). Exhaustive distance-preserving vertex permutation backtracking obtains exactly 32 graph automorphisms; their actions on the 60 matchings split into eight disjoint orbit sizes by type: (24): 2,8,16,16; (12,12): 2,4; (8,8,8): 4,8. For each choice of first named edge color, the even complementary cycles have 2^number_of_cycles alternate colorings, yielding 42*2+6*4+12*8=204 distinct named proper three-edge colorings and 34 modulo the free 3! color action. The independently written checker reconstructs the graph, full matchings, cycle profiles, automorphisms, orbits and coloring sum; enumeration covers *all* matchings by a complete recursion, not a random sample.

## originality

PASS

McGee's four-page 1960 construction proves graph existence and gives a Hamiltonian circuit, while MathWorld contains the standard LCF notation and full automorphism-group order 32. The inspected exact Tutte polynomial appendix is not a cycle-type distribution, and generic cubic 2-factor bounds cannot determine the McGee 60-by-type matching census. Distinguishes new complete spectrum/orbits from known graph, single Hamilton cycle, and known group size. An inaccessible dissertation remains a named originality risk.

## value

PASS

A canonical unique smallest cubic girth-seven cage is intrinsically motivated. Its entire 2-factor cycle-partition spectrum, exact Hamiltonian count, full matching symmetry orbits and edge-coloring number are natural graph invariants that may be reused in coloring, cycle-cover and extremal studies; the exact classification is independently useful even without an infinite-family theorem. The computation is complete rather than a partial count or arbitrary induced slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
