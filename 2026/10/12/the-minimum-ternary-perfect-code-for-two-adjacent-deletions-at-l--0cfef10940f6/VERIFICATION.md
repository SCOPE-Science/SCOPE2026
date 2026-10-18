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

For x∈Σ⁵ its 2-adjacent deletion shadow is the set {x₃x₄x₅,x₁x₄x₅,x₁x₂x₅,x₁x₂x₃}, of size at most four. Independent direct enumeration confirms the eight exhibited shadows have sizes (4,3,4,4,3,3,2,4), are pairwise disjoint and cover all 27 triples. A seven-word cover is the only remaining possible smaller cardinality because ceil(27/4)=7. Exhaustive bitset DFS enumerates all 3⁵=243 input words; at each state chooses an uncovered received triple, branches on *every* candidate shadow containing it with necessary remaining coverage bound u−4(r−1), memoizes (uncovered mask,r). Independent reproduction visits exactly 649 cached states and rejects seven-word covers (even without enforcing disjointness, so the rejection is stronger). Branching/pruning proof establishes that no candidate cover is missed; not a timed-out solver or heuristic census. Thus eight is optimal.

## originality

PASS

The natural ternary length-five two-burst perfect-code size spectrum is introduced by Chee–Li–Zhang (2015), whose reported ternary recursive family yields sizes nine, twelve and fifteen, while its stated sharp even-alphabet size theorem does not imply this odd-alphabet eight-word optimum. Xie–Sun–Ge (2026) give broad nonbinary covering-code constructions without the same perfect-code size proof in inspected accessible material. The concrete eight-word disjoint partition and exhaustive lower bound are not in the indexed material. The highly relevant 2015 body was inaccessible through lawful inspected routes, leaving substantive priority risk rather than automatic failure.

## value

PASS

The size spectrum of perfect burst-deletion codes is a canonical synchronization-coding invariant. The first small odd-alphabet length-five/two-adjacent-deletion case has genuine overlap and packing constraints, and the exact minimum eight improves the inspected nine-word ternary construction. The exhibited eight-word perfect partition plus complete seven-word exclusion is a substantive exact finite optimum, not merely a logged example or arbitrary unmotivated slice. The fact can be useful as a benchmark and boundary even without an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
