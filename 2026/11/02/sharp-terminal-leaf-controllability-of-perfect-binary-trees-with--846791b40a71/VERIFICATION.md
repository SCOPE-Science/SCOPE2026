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

Run `python3 verify_binary_tree.py` using Python 3 and only its standard library. The checker computes unit-eigenspace nullspaces in finite fields and selects exact independent terminal-leaf pivots. It then directly computes the corresponding Kalman Krylov-column rank for all perfect binary trees of heights one through six (3 through 127 vertices) over the two different prime fields of orders 1000003 and 1000033. It confirms the exact dimension formula, verifies the selected number of leaf controls and checks that the rank equals the number of graph vertices. Height-three baseline underactuation is also checked.

Both sets of six tests pass and the program prints `ALL_FINITE_CHECKS_PASSED`. A finite-field test cannot prove a universal real-field spectral statement and does not constitute a substitute for the all-height Jacobi/PBH proof. It is an exact reproducibility and arithmetic check at the specified finite heights. No external audit has been performed.
