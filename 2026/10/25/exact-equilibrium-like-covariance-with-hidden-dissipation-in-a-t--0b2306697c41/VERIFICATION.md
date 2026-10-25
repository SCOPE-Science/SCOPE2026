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

# Verification record

The complete stationary covariance and moment relations were derived from the joint generator and the explicitly stated hypotheses. The companion `checks/check.py` was executed successfully with `sympy`, `numpy`, and `scipy`, producing the exact output preserved in `checks/results.txt`. Reproduced identities include the unconditional stationary fourth cumulant, the polynomial cancellation factor, the geometric-mean equality criterion, the joint entropy formula and the inverse kurtosis–entropy relation. The checker also evaluates 30 matrix-exponential correlation lag cases across five nonidentical traps, four off-threshold counterchecks, and the exact rational example.

The infinite-parameter and all-lag theorem rests on the analytic stationary-generator/Feynman–Kac proof in `RESULT.md`, not on numerical sample size. Tests do not establish independent scholarly priority, experimental validity, or extensions beyond stationary symmetric two-state positive stiffness and common diffusion. No independent audit has been conducted.
