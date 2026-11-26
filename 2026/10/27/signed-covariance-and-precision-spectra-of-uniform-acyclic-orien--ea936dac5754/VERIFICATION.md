---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently reconstructed the second moments using S_i=X_ai+X_bi−1 and D_i=X_ai−X_bi. Any nonzero D_i fixes the sign of every other nonzero D_j, since opposite mixed columns form a directed four-cycle and K_{2,n} has no longer simple cycles. This gives E[D_i²]=2·3^(n−1)/Z and E[D_i D_j]=2·3^(n−2)/Z for i≠j. When a column is unmixed, its two choices give opposite S_i and can be toggled independently; hence cross moments with S_i vanish and E[S_i²]=1−E[D_i²]. In normalized pair coordinates the two blocks are s I and 4d I+2d J. Their inverses are s⁻¹ I and (4d)⁻¹[I−J/(n+2)], giving the four claimed entries. The diagonal of the inverse difference block exceeds 1/(1/4−c) by strict convexity and hence exceeds 1/s; this establishes the same-column sign. The limits follow from d→1/36, c→1/12 and Q_ee→6. At n=2 the sum modes and the constant difference mode share eigenvalue 2/7, of total multiplicity 3; the table counts the listed orthogonal modes separately (the other eigenvalue is 1/7). The frozen finite checker tests rational entries/signs against topological sorting, not a substitute for the proof.

## originality

PASS

Prior orientation counts and representations are credited. The closest earlier precision law uses a different graph and probability measure; the strongest same-law transform is a later result and its actual derivational overlap is explicit below. No earlier equivalent coverage of the exact dependence law was established.

## value

PASS

This is a canonical uniform law on a complete bipartite family with an unbounded exchangeable side. The finding gives exact benchmarks for dependence and inverse dependence: in particular, cross-column marginal correlations stay macroscopically nonzero whereas full-order linear partial correlations vanish at a known signed 1/n rate. Orientation counts or path-length frequencies do not answer that question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
