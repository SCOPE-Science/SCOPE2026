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

# Verification and boundaries

The source file `verify.py` uses only standard Python 3. Running `python verify.py` builds the cycle-plus-rung graphs afresh with vertices represented as two-coordinate tuples, checks undirected cubic adjacency, constructs the two witnesses, and verifies nonempty open-neighborhood intersection for *all* vertices and pairwise uniqueness for all vertices outside each witness. It asserts witness sizes \(7\) and \(9\), the exact cubic lower bound, and the inconsistent \(8\) and \(10\) conjectural values. It tests all vertex subsets smaller than seven for the \(16\)-vertex prism, exactly \(14{,}893\) candidate subsets.

The captured successful run is in `verification_output.txt`. The general lower bound is proved by incidence inequalities independently of enumeration. No brute-force search over all \(22\)-vertex-graph subsets is necessary to establish the \(11\)-cycle minimum; the sharp lower bound excludes smaller sets. Neither computation nor a search-result absence is offered as proof of originality against unknown papers.
