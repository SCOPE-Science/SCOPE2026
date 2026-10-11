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

# Verification
The proof applies to every integer \(m\ge1\). The packaged `verify.py` checks the independent domination number and neighborhood deletion for \(1\le m\le4\), but the all-parameter conclusion is supported by the explicit disjoint-neighborhood proof, not by testing finitely many values.

For the minimal-order assertion, the script enumerates every connected labeled simple graph on \(n=3,4,5,6,7\) vertices having exactly \(n\) edges (equivalently, every connected unicyclic graph in those orders). It examines all independent subsets, all maximal independent sizes, and every relevant reduced integral homology degree after closed-neighborhood deletion. Integral chain boundaries are reduced using unit row/column pivots, proving rank and unit Smith invariants without relying on field-only homology. All residual graphs in this census have at most five vertices.

The complete labeled graph totals are `1,15,222,3660,68295`, with failure totals `0,0,0,0,2520`. The full permutation orbit of the seven-vertex template has exactly `2520` distinct members and agrees setwise with the failure set. Running `python3 verify.py` must print `VERIFY_OK` after these checks.

No general assertion about all unicyclic graphs satisfying the vanishing condition follows, and no independent scientific audit has been performed.
