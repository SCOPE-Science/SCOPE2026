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

# Reproducibility

Run `python verify.py` using Python 3.9 or later. It exhaustively generates all recursive-tree parent arrays for sizes 2 through 9 and compares the actual cross-covariance matrix and row sums with the stated exact-rational formulas. It also verifies the strict second difference and finite sign boundary through 200 vertices. The observed run completed with `VERIFY_OK 34860 exact assertions; 46233 enumerated trees`.

The universal mathematical justification is the independent-parent leaf-survival calculation, a telescoping sum over arrival times, a discrete convexity argument and a harmonic-sum limit. Finite enumeration is a reproducibility check and does not certify universal correctness or historical novelty. The claimed leaf convention is rooted outdegree zero, not undirected degree one. No independent audit has been performed.
