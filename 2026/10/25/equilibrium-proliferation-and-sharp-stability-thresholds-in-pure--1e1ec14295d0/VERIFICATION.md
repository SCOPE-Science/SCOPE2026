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

# Verification procedure and limitations

Run `python3 verify.py` with Python 3.10+ and SymPy available. The script recomputes, from the displayed equations, the symbolic determinant reduction, its branch-crossing identity, the cubic maximum and threshold monotonicity. It tests exact-rational equilibria and differential identities, and evaluates both endemic branches for 88 \((m,\lambda)\) combinations with \(1\le m\le8\), totaling 536 nonzero ODE steady-state representatives. The reported execution was:

```text
PASS: 5 symbolic identities, 88 parameter cases, 536 evaluated nonzero endemic configurations, 34 exact-rational cases/identities.
```

These calculations are finite checks, not a computer-assisted proof for unbounded graph size or real infection rates. The general all-equilibrium count is proved by the exact per-petal difference identity and one-variable calculus; the Jacobian block decomposition proves the stated linear stability. The fold is explicitly excluded from any claim of exponential stability. The deterministic approximation should not be confused with an exact finite stochastic-contagion law. Independent external review or validation has not occurred.
