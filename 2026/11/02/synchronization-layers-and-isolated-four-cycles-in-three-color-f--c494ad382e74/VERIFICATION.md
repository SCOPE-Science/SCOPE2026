---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Exact 49-state support-pair quotient follows from the fact that all vertices in a shore share the same blink-neighbor indicator. Independent enumeration of all 7×7 states under q0=(0→1,1→2,2→0), q1=(0→1,1→2,2→2) confirmed the full transition table, recurrent support cycles and maximum transient length six. Recurrent supports yield only synchronized 3-cycle, nonsynchronous 3-cycles at (4,7),(7,4), and nonsynchronous 4-cycles at (5,6),(6,5), with no transient basins. Weighting each support by U_j(m) surjection count proves the exact T0...T6,T∞ formulas for all a,b≥2; independent computations checked (a,b)=(2,2),(2,3),(3,3),(4,5). In particular T∞=u+v+2xy; T2→probability 1 and balanced T∞~2(4/9)^n. Finite 49-support exhaustion is complete because the quotient is exact for all shore sizes.

## originality

PASS

Lyu original 3-color inhibitory rule and tree/path synchronization criteria precede this. Thick bicliques have cycles and are outside the tree theorems; known complete-multipartite binary parity automaton results use a different transition operator. No same-model exact 49-state/layer census found in inspected sources.

## value

PASS

Complete first-synchronization distribution and exact isolated asynchronous cycles for a natural dense graph family exhibit a sharp six-step cutoff and asymptotic rarity of non-synchronizing states; the finite 49-support reduction lifts to an unrestricted two-parameter family, a motivated structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
