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

# Reproduction and checks

Run `python3 verify_bipartite_flow_sis.py` in the same directory. Only Python 3's standard library is required.

The checker independently evaluates the vertexwise infection and receiver-health load equations on \(K_{m,n}\). It tests the closed forms at 128 exactly rational supercritical parameter combinations, 972 further floating-point supercritical combinations with maximum residual \(4.885\times10^{-15}\), and 363 disease-free combinations. The exact tests additionally check strict infection/load ranking reversal and total-load conservation.

The theorem for every positive integer community size and every positive recovery and load follows from the edge-square identity and the two-class algebra in `RESULT.md`. Numerical sampling is not an infinite-case proof. Global attraction, stochastic behavior and directed or weighted network extensions were not checked.
