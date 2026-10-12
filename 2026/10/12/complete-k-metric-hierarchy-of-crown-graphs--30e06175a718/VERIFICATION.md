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

The proof is symbolic and applies to every \(n\ge3\). The bundled `verify.py` is a finite corroboration of its two critical ingredients.

First, for each \(3\le n\le9\), the script constructs the crown graph from its adjacency rule and computes shortest-path distances by breadth-first search. It checks that each same-side pair with indices \(i\ne j\) is distinguished by exactly the four vertices in \(P_i\cup P_j\), while every opposite-side pair is distinguished by all \(2n\) vertices. It therefore confirms that the minimum distinctive-set size is \(4\).

Second, the script exhausts all \(2^{2n}\) vertex subsets. For each \(k\in\{1,2,3,4\}\), it independently tests the generator condition against the verified distinctive sets, finds the minimum size, counts all minimum bases, and checks their pair-occupancy profiles. The expected outputs are \(n-1,n,2n-1,2n\) and \(n2^{n-1},2^n,2n,1\).

A successful run prints one line beginning `VERIFY_OK`. Exhaustive verification through \(n=9\) does not replace the infinite proof; it is intended to detect indexing, boundary, and counting errors in the closed formulas.
