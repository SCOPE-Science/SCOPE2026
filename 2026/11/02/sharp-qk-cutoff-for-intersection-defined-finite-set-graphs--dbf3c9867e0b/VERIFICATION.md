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

# Verification and limits

The proof was checked symbolically for \(q\ge2\), \(k\ge1\), \(n,m\ge qk\). The central inequality at move \(t<q\) is \(n-tk\ge(q-t)k\ge k\); the same inequality holds on the opposite side. Any new \(k\)-subset needs at most \(k\) fresh points, while existing selected points are transported by the maintained bijection. Thus the game result is unconditional. A clique in the disjointness graph requires and is implied by \(q\) disjoint \(k\)-sets, using \(qk\) underlying points. The clique formula contains \(q\) nested existential quantifiers. These are exhaustive analytic arguments, not numerical experiments. The result does not address the exact equivalence partition among parameters below the cutoff. Independent audit: not performed.
