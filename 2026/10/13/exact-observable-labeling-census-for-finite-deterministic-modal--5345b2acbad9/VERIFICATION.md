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

Boolean closure under preimage f^{-1} and Boolean operations consists exactly of unions of equivalence classes of states with identical forward color itineraries. Injectivity of itineraries requires primitive and mutually inequivalent rotational cycle words for same-length cycles and distinct labels on all same-successor fibers; if equal itineraries ever synchronize on the same cycle vertex, tracing back to the first merger contradicts fiber uniqueness. For each length l, primitive words P_q(l)=sum_{d|l}mu(d)q^{l/d} fill labeled cycles with factors P_q(l)-j l. Each cycle vertex has one precolored predecessor, so remaining d_v-1 predecessors contribute falling(q-1,d_v-1); noncycle targets contribute falling(q,d_v). This yields the product and exact q=2^r generator rank. Partition refinement gains at least one class per depth until discrete, proving depth <=n-s, with chain-to-loop sharp. Independent enumeration of all maps of size <=4 over alphabets q=1,2,3 compared 864 complete graph/color census cases via exact itinerary traces, including examples 24 and 18.

## originality

PASS

A complete exact ordered generating-labeling census and sharp generator-rank classification for every finite single-successor modal algebra. General behavioral inequivalence and unary DFA minimality are prior, but the inspected source statements do not imply the factored all-label count.

## value

PASS

Finite Boolean modal algebras of deterministic functions are a natural unrestricted family; counting all minimal observable colorings decomposes periodic and merging obstructions and gives exact minimum generator rank and sharp modal depth. The theorem provides closed computable invariants for every finite functional digraph, not an arbitrary selected small frame.

The dated certificate retains the supplied scientific assessment, sources and limitations.
