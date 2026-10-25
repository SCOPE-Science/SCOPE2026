---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Two-round EF pointed type determined by predecessor, current, successor colours and the set of colours among all other vertices; equality of sets of pointed types is necessary and sufficient for rank-two sentences. Far colours require counts truncated at four and the set of cyclic length-three factors. Append-state automaton has four seeds, 758 reachable states, and closing into a cycle yields exactly 48 signature classes, with BFS least-length distribution (4,6,6,9,10,9,4) for lengths 3..9. Independently reconstructed this closure and checked direct cyclic pair profiles for every binary word length 3..12, 8184 words, including all four sharp length-nine witnesses. Completeness for all n depends on the finite-state transfer proof, not cutoff enumeration.

## originality

PASS

Brown–Hoshino 2007 provides uncoloured undirected graph path/cycle EF thresholds, not oriented binary-labelled cyclic words. Weis–Immerman includes linear order and endpoints, unlike these cycles. Classical two-round EF theorem is prior art; the exact 48 class census, 758-state closure and 9 bound are the inspected quantitative addition.

## value

PASS

Complete finite-rank logical classification for all binary-coloured oriented cycles is a natural finite-model invariant; the sharp model-length spectrum and exact local signature are independently useful and more than applying a known count mechanically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
