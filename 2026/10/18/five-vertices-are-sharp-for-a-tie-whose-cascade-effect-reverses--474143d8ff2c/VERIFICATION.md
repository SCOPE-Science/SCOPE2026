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

Every inactive activation test at order n has denominator at most n−1, so the synchronous closure and response are constant on each cell (a,b] between consecutive positive critical values (starting with a=0). The right boundary uses inclusion at equality. An independent exact census /workspace/branches/replay_5.py uses least stable supersets rather than round-by-round updates: a set containing the fixed seed is stable when all outside active fractions are strictly less than the test threshold, and the actual closure lies in every such set and is one of them. It found connected counts 1,4,38,728 and reversal counts 0,0,0,420 at n=2,3,4,5. The complete relabeling orbits of the five reported representatives are disjoint, have sizes 60,120,60,120,60 in table order, and exhaust the 420 marked triples. Their common response at the six right endpoints (1/4,1/3,1/2,2/3,3/4,1) is (0,0,3,−1,−1,−1). For the all-order family, seed 1 first activates 2 (a leaf in the base), but base vertex 0 has only one active neighbor of three, so the base reaches all n by propagation only at phi≤1/3, otherwise it stops at two. After adding 02, vertex 2 activates iff phi≤1/2 at the first round, then 0 has two active neighbors of four, and the remaining branches of degree at most two adopt at these thresholds. Above 1/2 neither susceptible vertex activates, so only the seed remains. This verifies the unbounded family and both threshold boundaries analytically. The frozen verifier was inspected, not run.

## originality

PASS

The relevant distinction is a sign reversal for the same marked graph, added edge and seed over a varied threshold, with the exact minimum-order census and all-order law. Fractional-neighbor dilution and adverse links were known. The strongest inspected Resultary comparators cover fixed-threshold losses, a bridge joining disconnected components, or a rewiring intervention, none of which states or implies this joint reversal theorem under the same assumptions. The bounded primary and catalogue comparisons do not prove novelty worldwide.

## value

PASS

With graph, intervention and initiator fixed, the sign of the intervention changes solely with the response threshold. The complete minimum-order classification makes this a structural benchmark rather than an arbitrary example, and the tree family separates a linear positive effect from a strict negative one. Neither the census nor the family predicts empirical adoption or gives a bound on negative effects for larger graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
