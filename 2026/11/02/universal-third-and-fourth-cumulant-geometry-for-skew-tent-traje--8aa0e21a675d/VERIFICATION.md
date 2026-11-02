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

Run `python verification.py` in a Python environment with the `sympy` package available. The program checks finite-horizon moment and cumulant identities using exact rational arithmetic, and verifies the analytic perturbation identities symbolically for the unrestricted real parameter. It was executed successfully as embedded.

The exact finite-horizon tests cover \(a\in\{1/4,1/2,3/4\}\) and \(N\in\{1,2,4,8,16,32,64\}\). The symbolic checks prove the displayed rational-function manipulations on \(0<a<1\) once the analytical spectral-perturbation setup is established; they are not an independent proof of the spectral gap.

An exponential spectral remainder on bounded variation for each fixed skew tent map gives \(\operatorname{cum}_r(S_N)=NK_r(a)+O_a(1)\) through order four. Finite computation is never used to infer the all-time limit. The independent-audit channel remains unperformed.
