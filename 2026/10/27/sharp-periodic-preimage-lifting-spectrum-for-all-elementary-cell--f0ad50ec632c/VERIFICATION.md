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

A bi-infinite predecessor segmented at word boundaries gives a walk in the word relation and hence a directed cycle. A closed walk of length k concatenates to a legal periodic predecessor with period dividing k|w|; conversely such a predecessor gives a closed walk of length k. The shortest closed walk is a simple cycle, so the least multiplier is at most four whenever one exists. This also works for words whose least period divides their length. Closing the two generators on the right from the identity captures all words; the identity, of girth one, cannot inflate any rule's index. An independent edge-set implementation propagated distances to find first returns at each of the four vertices and traversed every reachable relation in breadth-first order. It matched all 256 CSV rows, counts (156,82,16,2), maximum closure size 2375, both exception classes and their orbit partitions, and precisely the ten rules with first witness length three. Direct periodic evaluation gives outputs 001001, 1111 and 0000 for the three stated examples. Replay: python3 /workspace/branches/replay_eca.py <frozen record directory>/classification.csv. This did not execute the supplied verifier or reproduce its auxiliary n≤7 ring sweep. Symmetry follows from commuting reflection and bit flip with all period constraints (output flip complements the target). The proof is a spatial one-step result on the bilateral shift, not a statement about temporal cycles or continuous right inverses.

## originality

PASS

The supported distinct claim is the complete target-dependent lifting-index census with exact short-witness cutoff. The closure-graph method, the weak same-period condition, and individual obstructions are established work, not credited as new. Closely overlapping catalogue claims were compared on their actual multipliers and quantifiers.

## value

PASS

Among periodic points already known to be attainable, the index measures the least extra ring length one must permit when a lift is unavailable at the target period. The exact spectrum separates cases not distinguished by the common-multiplier table, and the sharp length-three cutoff gives useful minimal obstruction tests despite the all-period quantifier. This is a motivated finite classification with a verified cutoff, not merely an enumeration of rule codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
