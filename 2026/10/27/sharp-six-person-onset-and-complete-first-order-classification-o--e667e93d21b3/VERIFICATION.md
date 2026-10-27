---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Finite exact proof verification

The included `netflix_capacity_census.py` is an independently runnable Python 3.9+ program requiring only the standard library. Execute `python3 netflix_capacity_census.py`. The program uses integer bit sets and complete finite enumeration; no floating-point claims enter the theorem.

The executed program returned `PASS`, with connected labeled graph totals \(1,4,38,728,26704\) for orders two through six. It proved no minimum-buyer capacity reversal occurs for orders two through five and identified 1,330 labeled reversing connected graphs at order six. Each such graph had a single increase at capacity two to three with optimal buyer counts two and three. Canonicalization over all \(720\) six-vertex permutations yielded exactly eight isomorphism types and the stated labeled counts. The only five-edge type was canonical code 121.

The certificate's completeness rests on the explicit bijection between graph edge masks and all labeled simple graphs; the exhaustive buyer-set and legal nomination-subset search; the direct Nash characterization; and minimization over every relabeling. These details are explained and implemented in the proof. This is exhaustive for the finite domain, not a claim about networks of unbounded order. Source comparisons do not prove absolute uniqueness in the mathematical literature. Independent audit has not been performed.
