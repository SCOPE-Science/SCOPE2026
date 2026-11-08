---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Let C0 be largest Nash coalition: a missing type i agent would strictly improve by joining it, so C0 contains all types. Bilateral deviations for an i-agent between any coalition C and C0 imply M-m_i=u-c_i; summing over represented types produces (1-p)(M-u)=H where H is the positive mass of omitted types. Hence every coalition contains every type, M=u and each type count is equal, so r divides gcd(n_i). Balanced partitions have no improving unilateral move, and multiplying multinomials/dividing by r! counts them. Summing weak-blocker friend inequalities shows size U>=s and the U=s case all indifferent; all-strict blockers require U>=s+2. Enemies preclude weak blocker size s+1, while neutrals permit a one-agent augmentation; adding two different types gives core blockers at s+2. Grand coalition has no blocking proper subset. Independent 2808 full Nash-partition/preference tests corroborate.

## originality

PASS

Best-knowledge PASS for exact characterization and labeled count of *every* Nash partition and distinct minimum core/strict-core blocking sizes under two fixed complete-multipartite preference systems. General Nash existence under symmetric friendship and grand-coalition core protection are prior; they do not state all-divisor partitions and blocking radii.

## value

PASS

Complete multipartite graphs are a canonical friendship-network family; exact equilibrium multiplicities and a sharp s+1 vs s+2 difference between neutral and enemy internal ties describe a meaningful collective-stability boundary not captured by general existence results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
