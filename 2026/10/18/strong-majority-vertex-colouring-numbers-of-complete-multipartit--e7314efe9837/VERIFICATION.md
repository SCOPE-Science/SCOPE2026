---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For complete multipartite K_(n_1,...,n_r) with all parts nonempty, r>=2 and minimum degree>=2, every colour appears in at most half each open neighbourhood. With two colours, each part sign sum S_i must equal global S, hence all S_i=0 and all n_i even. K4 and K_(1,1,2) force four distinct colours. Adding two differently coloured vertices to any fixed part increases each other open neighbourhood count by <=1 while degree grows by 2; preserves 3-colour validity. Reducing each part modulo 2 to size1 or2, plus handling parity core K4/K112 by first restoring one pair, gives explicitly coloured n=3,5,6,7, n>=8 and three enlarged n=6 cores, exhausting all cases. Independent brute force checked exact 2- and 3-colour minima for all 51 admissible unlabeled profiles of orders 3..8; official 9246 profiles through 25 checked constructively, neither finite set used to establish general proof.

## originality

PASS

The prior paper introducing the invariant already supplies the K4 obstruction; two-colour parity for complete multipartite neighborhoods precedes it. Our exact 3-vs-4 classification adds K_(1,1,2) and a uniform pair-extension construction, neither obtained from generic maximum-degree estimates, game variants, or two-colour neighborhood balance.

## value

PASS

This gives a complete all-order classification on a canonical highly structured graph family for a recent invariant unbounded over arbitrary graphs, strengthening existing Delta-dependent bounds to a sharp universal threshold and isolating non-complete K_(1,1,2) exception. Pair augmentation is a reusable structural extension method, not merely a finite graph table; known 2-colour balance is correctly credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
