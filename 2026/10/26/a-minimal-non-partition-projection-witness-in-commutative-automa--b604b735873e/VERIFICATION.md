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

In the displayed complete DFA, the hidden map is the square of the visible map and hence commutes with it. The states 2,0,1 are reached by ε,a,aa; b separates 2 and 0, and ε separates 1 from both. The projected acceptance sequence is 1,1,0,1,0,…, with three distinct residuals at lengths 0,1,2 (lengths 0 and 1 are distinguished by one more a). Hidden closures are exactly {1,2},{0},{1}, so the overlap persists before minimization. For the lower bound, commute every hidden letter past the visible letters to recognize the projection on the original state set with hidden-reachability finals. Full two-state projected complexity then forces a transposition or a constant, as identity reaches only the start. For the transposition, the only commuting maps are identity and the transposition, yielding singleton closures or the whole set. For a constant with distinct start d and image c, infinitude and minimality force c projected-final and d not projected-final. Every commuting hidden map fixes c and cannot send d to c, so all hidden maps are identities. The one-state case is immediate. This covers any nonempty hidden alphabet. Independent bounded replay at /workspace/branches/993b2af2-76e4-4355-bd94-c3aa05179b8c/independent_projection_check.py (output independent_projection_check.txt) checked the witness and all 128 labeled two-state binary DFAs: 80 commute, six have infinite minimal unary projection of size two, and none of those six overlaps. This is corroboration, not the many-hidden-letter proof. The frozen checker was inspected, not run.

## originality

PASS

The closest primary example already shows that commutativity can coexist with overlapping closures, but it does not exhibit retention of full minimal complexity. Neither the upper bound for commutative projection nor the existence of an alternate state-partition representation implies the exact full-complexity witness or its minimum. No coverage of the combined claim was established in the inspected literature or catalogue.

## value

PASS

This exact minimum answers the natural equality question for commutative projection: retaining all minimal states, even for an infinite unary projection, does not require disjoint hidden closures. The smallest obstruction separates these two properties while preserving full minimal size; the proof excludes smaller obstructions for every number of hidden letters, not just the enumerated alphabet. The claim is a minimal witness, not a general classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
