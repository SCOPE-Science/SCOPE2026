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
The accompanying `verify_sparse_stack.py` completed with `PASS`, checking 5,018 exhaustively enumerated small signed matrices, exact two-edge collision probabilities at five block sizes, and 40,000 simulated two-stack matrices covering densities 0.5 and 0.8, correlations -1, 0, 0.5, and 1, and block sizes 80 and 240. The scripts compare real matrix rank to the graph-derived nullity and empirical finite-size rank statistics to the predicted asymptotic Poisson means. Simulated agreement is not a proof of infinite-dimensional convergence. The proof in RESULT.md establishes the universal conclusions by factorial moments, cycle tails, and monotone coupling.
