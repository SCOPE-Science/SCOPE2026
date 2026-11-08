---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For exactly two indistinguishable particles on the positive-rate four-site periodic ASEP, the six-state generator defined by rate pw_i/qw_i is irreducible. The matrix-tree stationary weights yield the two displayed exact cofactor polynomial identities: N=4abcd(p-q)(p+q)(p²+q²)(Ap+Bq)(Aq+Bp) and ND_rev+N_revD=-4abcd pq(a-c)(b-d)(p-q)²(p+q)(p²+q²)(Ap+Bq)(Aq+Bp)[α(p²+q²)+βpq]. Denominators are positive for 0<|ε|<1, and the quadratic H is affine in ε². The reflection iff follows from H identically zero, α=β=0, the positive-pair AM-GM contradictions when A!=B, and matching opposite-site sums/products when A=B. The exact witness (1,2,4,9) has α=-46 β=106, reversal ε²=7/99. The source exact SymPy cofactor checker was inspected; separately implemented six-state rational stationary solves corroborated the expressions. No inference extends to larger cycles or bias endpoints.

## originality

PASS

Best-of-knowledge PASS for the six-configuration reflection-only iff, full polarity phase diagram and unique interior bias-strength inversion, not for the known site-trap model or general disorder-induced rectification. Closest primary source analyzes general responses/particle ensembles; its inspected equations/conclusions do not state this finite classification. A stronger unlocated finite-chain stationary-current identity remains possible.

## value

PASS

A sharp nontrivial analytical polarity transition at fixed disorder and particle number, with exact necessary-and-sufficient reflection criterion and a fully explicit distinct-rate witness, is a motivated exact finite nonequilibrium transport result; it is neither a naming change nor a check of one sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
