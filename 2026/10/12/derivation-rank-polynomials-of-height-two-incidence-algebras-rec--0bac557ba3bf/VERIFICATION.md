---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: For a height-two bipartite incidence algebra, derivations have one inner idempotent-arrow coefficient b_e and one scalar arrow coefficient λ_e per edge; idempotent Leibniz identities rule out other terms. The operator arrow-row block is [diag(b)∂ | diag(λ)]. Rows with λ!=0 pivot independently; remaining nonzero rows form a scaled incidence matrix with rank v−c(U) over any field. Counting per-edge zero/L/U states yields the polynomial. Its generating-subset expansion yields the printed Tutte substitution term by term. A rank deficit arises only from cycles in U, with first correction c_g(q−1)^g at degree g−1, and the unicyclic formula follows by moving the unique all-U cycle state down one degree. Independent state enumeration gave C4 q=2: (1,12,54,109,80); q=3: (1,32,384,2064,4080), and K2,3 q=2: (1,18,135,543,1231,1464,704). Finite cases corroborate; proof covers all finite simple bipartite graphs and all prime-power q.

## originality

PASS

Best-of-knowledge original as precise final theorem, after distinguishing stronger priors and genuine access limitations. Failed search is not proof of novelty; see mathematical implication checks and source inspections.

## value

PASS

PASS: Operator rank is a natural nontrivial invariant of an algebra derivation beyond dimension of the derivation space. One exact polynomial simultaneously enumerates every derivation rank for infinitely many algebras and recovers girth and the number of shortest cycles, a meaningful structural bridge to matroid theory. It does not claim complete graph reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
