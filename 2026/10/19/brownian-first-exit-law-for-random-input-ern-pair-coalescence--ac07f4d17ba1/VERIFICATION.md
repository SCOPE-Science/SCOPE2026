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

The included `verify.py` was executed with Python 3, NumPy and SciPy. It replays the exact pair-automaton transitions at all \(1736\) branch combinations \((n,d,U,V)\) for \(3\le n\le30\), and solves independent finite pair-state discounted equations for \(n=20,40,80\) at \(p=1/2,2/3\), \(x=1/4,1/2\) and Laplace parameter \(s=3/4\).

Execution summary:

`VERIFY_OK macro_branch_cases=1736 direct_full_pair_Laplace_n=20,40,80 p=1/2,2/3 x=1/4,1/2 s=3/4`

The directly computed Laplace values, listed as \(n=20,40,80\) after the theoretical limit, are:

- \(p=1/2, x=1/4\): 0.6455997; 0.6574284, 0.6514176, 0.6484854.
- \(p=1/2, x=1/2\): 0.5409601; 0.5625816, 0.5515854, 0.5462279.
- \(p=2/3, x=1/4\): 0.6827979; 0.6904193, 0.6865483, 0.6846582.
- \(p=2/3, x=1/2\): 0.5873941; 0.6012165, 0.5941905, 0.5907642.

Limits of these checks: no finite array establishes a Brownian weak limit. The mathematical proof supplies the exact cycle reduction, gambler's ruin coupling, Donsker exit-time convergence, and uniform clock estimate. Independent scientific audit has not been performed.
