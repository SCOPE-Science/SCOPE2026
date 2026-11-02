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

The finite base at nine vertices is proved by enumerating every unlabelled tree via leaf-adjoining and exact canonical rooted-parenthesis codes. Every vertex subset is tested by the defining condition: an outside vertex has at most one selected neighbor. The nine-vertex output is 47 isomorphism types and a unique nonstar maximum of 208, attained by the one-edge-subdivided star. Other finite checks verify the rooted inclusion base, the rooted one-neighbor lower bound on nonstar trees of orders 6 through 9, all corresponding leaf-extension identities, broom formulas to order 13, and the star-plus-one-edge formula to order 13.

Run `python3 verify.py`. Successful final output is `ONE_PASS`.

The bound for all larger orders is not inferred from finite data. It follows by the stated induction using the rooted one-neighbor lemma and the strict edge-monotonicity argument. The test of nine-vertex trees is exhaustive in that finite domain, but is not an independent audit of the inductive proof. Independent mathematical and historical-priority audits have not been performed.
