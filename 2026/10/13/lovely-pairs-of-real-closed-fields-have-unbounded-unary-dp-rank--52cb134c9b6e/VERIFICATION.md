---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Fix r and choose t outside the proper elementary subfield P. If t were algebraic over P, its minimal polynomial over P would have a root in P by elementarity, forcing it to be linear. Therefore 1,t,…,t^(r−1) are P-linearly independent. The map P^r→R that sends (p_i) to Σ_i p_i t^i is definable with parameters and injective. Requiring its unique i-th coefficient to equal a specified element of an infinite sequence in P gives the stated definable cosets, with row-disjointness and explicit simultaneous realization of every selection. In fact, row-disjointness also witnesses the negations required by a depth-r ICT pattern. Thus the finite unary lower bounds hold, without assuming any infinite-depth pattern or an infinite-rank complete type. RCF is o-minimal and geometric (in particular it eliminates ∃∞), and has unary dp-rank 1. For any k≥1 take r=k+1 in the pair, which is NIP by the established preservation result. RCF is then in C_k and its pair is not. Theorem 10.33 of Kim would preserve membership if C_k belonged to the larger indicated class, yielding the contradiction. The frozen verification was inspected; the audit is analytic.

## originality

PASS

The supported distinction is the explicit obstruction at every fixed finite unary cutoff using the proper lovely RCF pair. Parameter coding by a finite set of field elements and Kim's preservation theorem are not claimed new. The inspected results do not establish this rank jump or these exclusions, nor did the broader finite-dp-rank field comparison locate a theorem already supplying the rank jump.

## value

PASS

This is a motivated obstruction to preservation of an entire family of finite cutoffs, not a rank calculation for an arbitrary small example. It shows how adding a predicate can encode arbitrarily many independent coordinates into one variable while staying NIP, and supplies a uniform witness against placing bounded unary dp-rank among Kim's pair-preserved dividing lines. The result answers this boundary question even though the field-pair witness and the final preservation application are short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
