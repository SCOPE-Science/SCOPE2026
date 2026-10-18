---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed the six halfspaces s>=0,t>=0,v>=0, Al-s-dt-Delta_A v>=0, bl-t-Delta_b v>=0, l-v>=0 with normal lengths 1,1,1,N_A,N_b,1. A radius rho ball is feasible only if all shifted facet margins hold. Since d,Delta_A,Delta_b>=0 and coordinate lower bounds require s,t,v>=rho, pushing to (rho,rho,rho) can only improve all three upper clearances. Feasibility reduces exactly to 2rho<=l, (1+Delta_b+N_b)rho<=bl, (1+d+Delta_A+N_A)rho<=Al. Gives the claimed min of three normalized barriers and the complete all-incenter six-inequality description. Verified allowed d=0 and equality/tie cases logically; an independent scipy linprog implementation sampled 250 integer parameter cases with zero observed discrepancy. Sampling corroborates, does not prove the all-integer symbolic theorem.

## originality

PASS

Best-of-knowledge statement-level comparison against directly inspected mathematical texts supports originality of the precise claim, not the source construction or standard lemmas. Each comparison and reading limit is distinguished; inaccessible work is recorded as risk, not proof of uniqueness. Resultary semantic search failed internally and supplies no negative evidence.

## value

PASS

The exact Euclidean Chebyshev radius and complete center locus form a natural geometric metric invariant of a published nontrivial family of lattice prismatoids, with three distinct contact regimes and ties. The proof identifies why six facets collapse to three active normalized barriers and gives exact parameter-dependent centers; the invariant is not supplied by rational linear precision itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
