---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Checked semantics of μ(t)=∀v ?(v=t): true exactly when the whole team has constant t. Consequently μ(x)→μ(y) is functional dependence x→y under subteam implication, and ∃inq w(w≠z) holds precisely when some z-domain value is absent. Failure of outer implication is an FD-consistent subteam covering every z. For r(X)≤2, Boolean variables per observed (x,y) pair, 0–2-literal coverage clauses and pairwise incompatible-y exclusions yield an exact 2-SAT reduction even with unrestricted y values. The 3-SAT reduction has exactly three distinct rows in every padded clause fibre, y∈{0,1}, and identical universe shared between z,x,y; it maps satisfiability to failure of support, proving coNP hardness with polynomial certificates for the complement. Independent finite constraints and reduction comparisons covered 1,200 instances.

## originality

PASS

Kontinen–Ciardelli Theorem 3.7 already proves fixed-InqBT coNP hardness and has three free formula variables after locality (not new). Their reduction uses clause tags/unary predicates and does not give the at-most-two-fibre algorithm or equality-only exactly-three-fibre hardness. The assigned claim supplies both; established SAT and database-FD facts are ingredients rather than asserted discoveries.

## value

PASS

The maximum number of witness rows per first-column value is a natural local branching parameter in an explicit fixed-formula team-model checking problem. The tight at-most-two polynomial / exactly-three coNP-complete boundary is structurally motivated, unlike a bare reformulation of generic coNP hardness; it holds with no nonlogical relations and multi-valued y on the easy side.

The dated certificate retains the supplied scientific assessment, sources and limitations.
