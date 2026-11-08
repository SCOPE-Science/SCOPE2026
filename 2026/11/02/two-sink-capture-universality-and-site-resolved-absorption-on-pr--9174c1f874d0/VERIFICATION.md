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

In a primitive (v,k,lambda,mu) strongly regular graph the adjacency algebra has three orthogonal projectors E_k,E_r,E_s. Both the graph and its complement have strict nonprincipal eigenvalue moduli below their degrees; therefore each 2-by-2 sink Gram matrix U*E_theta U is positive definite for theta=r,s, while the principal part has rank one. Their direct sum yields bright rank exactly 5. Every bright eigenmode of generator -iJA-(kappa_a P_a+kappa_b P_b)/2 has strictly negative real part because zero decay requires orthogonality to both sinks and hence to the bright cyclic subspace; the dark part is unitary. Thus capture is the bright projector, giving 5/v from mixed, 3/(v-2) averaged nonsinks. Diagonal Gram inverses yield the stated site formula and lambda/mu common-neighbor class populations. Independent construction of all 10 sink pairs in C5 recovered bright rank five. Finite tests corroborate but do not prove the all-graph result.

## originality

PASS

Novo et al. establish general Krylov reduction and Razzoli et al. the single-trap strongly-regular benchmark, not a two-absorber site distribution. Li et al. consider coherent marked loops rather than irreversible absorption; its full article was not available and is not called categorically noncovering. The exact two-site projector formula follows from standard spectral projectors but the simultaneous primitive-SRG rank-five, absorption-independent and entire adjacency-class distribution is a materially stronger specialized statement than those examples. Published Resultary query yielded related but logically distinct spectral subspace results.

## value

PASS

Exact site-resolved trapping probability is a natural transport invariant, especially in nonvertex-transitive primitive strongly regular networks. The law explains why nonisomorphic Shrikhande and rook networks with identical parameters are absorption-statistically indistinguishable under matched sink adjacency, and identifies a meaningful imprimitive boundary. This is a useful infinite-family classification rather than a renaming of single-sink transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
