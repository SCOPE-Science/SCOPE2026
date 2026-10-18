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

# Reproduction and check boundaries

Run `python3 verify.py` from the extracted package. Only Python's standard library is required. The code checks all \(2^{\binom n2}\) labelled simple graphs for each \(1\le n\le6\), reduces to exact isomorphism orbits under generating adjacent transpositions, identifies connected block graphs by biconnected edge blocks, and computes 1-WL signatures using joint colour names across all graphs of the same order. Asserted graph totals are \(1,2,4,11,34,156\), connected block totals \(1,1,2,4,9,22\), and connected block graphs having a nonisomorphic 1-WL mate \(0,0,0,0,0,1\). At order six the exact global 1-WL class containing the exceptional block graph has two members.

The verifier terminates with `VERIFIED_FIRST_FAILURE_ORDER_6_AND_UNIQUE_PAIR` and was executed successfully before packaging. This is exhaustive **only through six vertices**. The source-literature comparisons were assessed with the self-review; no independent external validation or proof assistant certification has been performed. The 2015 general classification is cited because it potentially subsumes individual membership claims, not as external verification of the new block-graph census.
