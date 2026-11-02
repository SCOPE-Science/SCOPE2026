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

# Verification of the finite and limiting laws

The analytic proof uses the exact exponential race cut sizes \(k(m+1-k)\), the independence and uniformity of the hub rank, the telescoping exponential moment at the repeated endpoint rate, and standard extreme-value tail integration for convergence of means. These determine the infinite-parameter assertions.

For reproducibility, run `python3 verify_windmill.py` using Python 3.9 or newer. The checker independently computes full-graph infection-state expected flooding times with rational arithmetic and compares them with the petal decompositions for small instances; tests uniform-rank expectations and the telescoped factor; checks phase-type survival values by uniformization; and checks seeded Dijkstra simulations on static independent exponential edge weights. The checked program terminates with `PASS 187 exact/numerical tests`.

Exact finite tests are not an exhaustive proof for all \(n,m\), and numerical simulation cannot prove an asymptotic distribution. Inference about historical priority and generalizations to variable petal size is not certified. Independent mathematical validation has not been performed.
