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

Run `python3 verify_hypercube_p_lip.py` with the standard Python library. The script constructs the full cube graph from bit flips rather than relying solely on shell multiplicities, exactly solves grounded rational Laplace systems at \(p=2\) for dimensions two through five, checks individual vertices/edges against the formula, and independently evaluates all full-graph nonlinear Euler equations and edge gradients for dimensions three through eight and exponents \(1.5,3,5,11\).

Recorded output from the actual verifier execution:

```
exact p=2 2 norm 1
exact p=2 3 norm 6/5
exact p=2 4 norm 3/2
exact p=2 5 norm 15/8
critical scaling 0.5 finite 2.46733172 limit 2.51620862
critical scaling 1.0 finite 1.60079919 limit 1.61857611
critical scaling 2.0 finite 1.27076458 limit 1.27826369
PASS: exact-rational full-graph interior vertices 52
PASS: exact-rational full-graph edges 128
PASS: nonlinear full-graph interior Euler equations 1968
PASS: nonlinear full-graph edge values 7152
```

For the nonlinear checks the program tests zero p-Laplacian residual for every unlabeled vertex (absolute tolerance \(2\cdot10^{-11}\)) and graph-edge amplitude against the claimed sharp formula. For the entropy comparisons at dimension \(300\), it uses a numerical Riemann integral to check agreement within \(0.06\), **not** to establish convergence. The analytical chain reduction, Hölder equality, and uniform Stirling bounds are required to prove the theorem for every dimension and exponent. No independent external mathematical validation is asserted.
