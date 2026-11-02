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

# Verification

The reproducibility file `verify.py` uses only the Python standard library and rational arithmetic. Run `python verify.py` from the directory containing this document and the script. It independently enumerates all 5,913 uniform increasing-parent trees of orders 2 through 8, checks the displayed marginal Wiener mean and mixed covariance, the deterministic degree-transmission identity, the tree Wiener upper bound, and the conditional leaf-attachment increment covariance. It also checks the harmonic covariance recurrence and strict sign for orders 2 through 300.

Observed output on the supplied script: `PASS trees=5913 exact_assertions=24271 exhaustive_orders=2..8 recurrence_orders=2..300`. These computations check examples and exact formulas, not the all-size proof. The all-size proof uses a deterministic tree identity, a graph extremal inequality, a conditional covariance recurrence, and harmonic summation. The two published marginal variance asymptotics enter only the displayed correlation limit. No external or independent validation has been performed.
