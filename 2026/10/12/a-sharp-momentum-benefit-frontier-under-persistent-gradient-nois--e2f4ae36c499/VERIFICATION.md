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
# Reproducible mathematical checks

Run `python3 checker.py` with a standard Python 3 interpreter. No third-party packages are needed. The program independently constructs the three-state linear update for normalized curvature \(a=1\), computes all six stationary covariance unknowns by exact-rational Gaussian elimination, and checks the explicit variance formula and its signed difference against zero-momentum SGD.

It executes 270 combinations with \(r\in\{0,1/4,1/2,3/4,9/10\}\), \(t\in\{1/5,1/2,4/5,1,6/5,7/5,3/2,9/5,19/10\}\), and \(\beta\in\{0,1/10,1/4,1/2,3/4,9/10\}\). It also checks exact stationary-variance sign reversal at fixed \(t=6/5\), \(\beta=1/10\), comparing \(r=0\) against \(r=1/2\).

Observed run output:

```
VERIFY_OK 270 exact covariance and difference cases, 2 contrasting rational witnesses
```

The full universal parameter domain is established by the exact analytic proof in `RESULT.md`, **not** by finite rational sampling. No stochastic simulation, Gaussian assumption, Lean proof, or independent external verification is asserted. Independent audit is not yet performed.
