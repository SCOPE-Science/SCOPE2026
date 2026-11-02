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

# Exact verification and limits

The included `verify_induced_motifs.py` uses only the Python standard library and does **not** use the analytic argument to enumerate graph outcomes. It independently constructs each labeled graph via edge subsets; computes the isolate count from incident-edge masks; computes induced wedges from all vertex triples; computes induced four-cycles and four-vertex paths from the six edges and four degrees on every vertex quadruple; and groups the sample exactly by the number of edges.

For \(n=4,5,6\), all \(G(n,m)\) wedge samples were enumerated. For \(n=5\), every graph was also separately checked for induced four-cycles and four-vertex paths. Three independent expected-value/mixed-moment identities were verified in every model and edge-count case using `fractions.Fraction`. **168 exact assertions passed over 34,880 enumerated labeled graphs** (including repeated small graphs across different motif tests). Reproduce with `python3 verify_induced_motifs.py`.

The infinite-family proof is the uniform hypergeometric conditional expectation calculation and strict monotonicity product in `RESULT.md`. Finite enumeration alone cannot establish the infinite theorem. The final numerical density at the equality boundary is not determined by the first-order limit. Originality involves residual historical-priority risk and has not undergone independent external verification.
