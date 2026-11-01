---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

On Q=Z/kZ x {0,1}, hidden a toggles lanes; b swaps pair indices 0,1; c:i->-i; d:i->1-i; visible e swaps (0,0) and (1,0). Each map squares to identity. The visible c,d product rotates indices, with b conjugates generating S_k on hidden pairs. Nonempty pair unions are closed under hidden epsilon closure; conjugating the e split adds an arbitrary missing pair to any nonempty subset, inductively reaching all 2^k-1 subsets. A pair permutation sends a symmetric-difference index to the unique accepting pair 0, distinguishing any two; the original transition group is transitive and singleton final ensures its 2k states minimal. Both {P0} and {P1} map via e to {P0,P1}, so projected minimal transition not injective, hence non-permutation. Independent BFS of closures confirmed all subsets for k=2..8 (finite corroboration). The 2^k-1 upper bound holds for any permutation automaton with this erased matching.

## originality

PASS

Hoffmann 2021 establishes the numerical hidden-orbit upper bound and a seven-letter lower-bound construction on a parameter regime 0<2m+1<n, excluding full hidden matching. Those facts are prior. Here the construction attains full-matching endpoint using only five involutive letters and a minimal input, not implied by arbitrary permutation witnesses; his Remark 1 asks whether seven letters can be reduced. Kutrib et al DUFA operations do not give this erasure witness. Residual possible unindexed all-involution endpoint construction.

## value

PASS

Exponential deterministic blowup under erasure is a canonical automata complexity question. An explicit all-even-size extremal witness with a constant five-letter involution alphabet and fixed-point-free hidden matching is a motivated sharp boundary, not a tiny improvement or generic finite example; nonclosure of undirected class is an additional structural consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
