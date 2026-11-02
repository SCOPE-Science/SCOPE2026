---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The all-parameter result is established by the symbolic classification of optimum induced matchings and their pairwise intersections in `RESULT.md`. These included finite programs provide independent implementation checks, not infinite certificates.

Run in this extracted directory:

```
python3 verify.py
python3 verify_alt.py
```

The first independently constructs the subdivided \(K_{m,n}\), enumerates every size-\(m+n-2\) edge subset, tests inducedness from the underlying adjacency relation, and checks all optimum configurations and exchange components for each budget. It completed successfully for \((m,n)=(3,3),(3,4),(4,3),(3,5),(4,4)\) with `INDEPENDENT_FINITE_CERTIFICATE_OK`.

The second independently builds the edge-compatibility graph and enumerates its maximal cliques, then calculates replacement-cost multiplicities from pairwise set differences. It completed for the same parameters with `ALT_INDEPENDENT_CERTIFICATE_OK`. The respective maximum-optimum counts were \(9,12,12,15,16\). The pairwise cost multiplicities agreed with \(m\binom n2\) at cost \(m\), \(n\binom m2\) at cost \(n\), and \(2\binom m2\binom n2\) at cost \(m+n-2\), with costs combined when equal.

Boundaries: these scripts do not establish novelty, do not constitute external independent validation, and do not enumerate arbitrarily large parameter values. Those limits are reflected in the mathematical proof and literature comparison.
