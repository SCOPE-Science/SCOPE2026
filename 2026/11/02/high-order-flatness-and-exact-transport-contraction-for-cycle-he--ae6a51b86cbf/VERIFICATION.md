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

# Reproducibility checks

Run `python checker.py` with NumPy and SciPy installed. The script uses direct matrix exponentiation, a separately implemented Kantorovich dual linear program with edge-Lipschitz constraints and pinned potential, and integer matrix-power computations of Taylor coefficients. It prints:

```
Separate cycle Kantorovich dual LP comparisons: 140
Exact-integer Taylor checks: 589
All finite checks passed
```

For the analytic argument, check the Dirac-edge reduction, the shift-difference cumulative identity, the signed cycle flow/median equality, the radial heat-kernel Metzler system including distinct odd/even boundary diagonals, shell counting, and the first nonzero Taylor coefficient. Numerical LP solvers use floating arithmetic and the declared absolute comparison tolerance \(3\times10^{-6}\); exact-integer coefficients avoid this rounding issue. Finite checks are evidence only, not exhaustive verification of an infinite theorem. No independent mathematical audit has been carried out.
