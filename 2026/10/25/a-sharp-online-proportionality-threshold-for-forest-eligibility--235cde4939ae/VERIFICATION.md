---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For greedy assignment to the larger prearrival deficit, proved by induction that every vertex with signed deficit B_v=r>0 belongs to a current tree component of size >=2^r: the newly losing endpoint has pre-deficit r-1, while the distinct receiving component has endpoint deficit >=r-1, and their union doubles the bound. Every forest component at prefix s has at most s+1 vertices, proving floor(log2(s+1)) for all prefixes. Opposite lower bound is an adaptive binary merge of two independently constructed 2^(r-1)-vertex trees whose marked vertices both have deficit r-1: the loser of one joining good receives deficit r; no cycle, and padding to exactly t edges preserves earlier prefix witness. At r=3 the construction needs 8 agents and 7 edges, and Prop1 is exactly B<=2 (eligibility-aware unit share). Independent minimax enumeration for all n<=5 and admissible t agreed, but the induction is the infinite proof.

## originality

PASS

Best-knowledge PASS for the exact sharp signed-deficit prefix minimax and the seven/eight eligibility-aware Prop1 boundary, not for a generic logarithmic forest-orientation upper bound. Bender et al previously use a doubling argument for logarithmic maximum outdegree, which is a related upper bound and is expressly credited. Biburger et al define the relevant 2026 fair-division model and study approximate Prop1 for unrestricted eligibility, not a forest exact cutoff. Gupta et al allow recourse, which fundamentally changes the online problem; offline orientation existence is also not the prefix game.

## value

PASS

A sharp, fully parameterized online fairness guarantee on the natural acyclic pair-eligibility family, with an explicit first unavoidable adaptive obstruction at 8 agents, gives a meaningful finite cutoff and universal all-n minimax theorem. It isolates the cost of irrevocability from offline or recourse-based solutions, useful for designing sequential allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
