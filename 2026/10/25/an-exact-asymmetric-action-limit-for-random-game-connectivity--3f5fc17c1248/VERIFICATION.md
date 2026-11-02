---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

A profile (i,j) is a pure Nash equilibrium precisely when j=C(i) and F(i)=R(C(i))=i. For k>=3, constant two-state F yields a single reachable equilibrium, the swap gives none, and identity F yields two distinct equilibria with a third column giving a unilateral-response trap. Thus connectivity iff F constant. The independent response map law gives Pr(constant)=(k+1)/(2k), Pr(at least one fixed point)=(3k+1)/(4k). Direct fresh directed-graph exhaustive tests for k=3,4,5,6 checked all 72,256,800,2304 response-map pairs and agree with fractions 4/5,10/13,3/4,14/19. The proof, not this finite testing, establishes all k>=3.

## originality

PASS

The closest primary game-connectivity theorem explicitly fixes equal action counts for all players, whereas the present limit fixes one action count at two. The other inspected literature concerns sequential convergence or correlated payoffs, different events/ensembles. No directly dominating rectangular-action formula was found; historical exact 2 by k enumeration is the remaining priority risk.

## value

PASS

The exact conditional probability and nonzero 2/3 limit expose a genuine asymptotic regime change relative to published equal-action two-player connectivity. It is an exact natural game-graph statistic for a common asymmetric action-space model, not a renaming of the equal-action parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
