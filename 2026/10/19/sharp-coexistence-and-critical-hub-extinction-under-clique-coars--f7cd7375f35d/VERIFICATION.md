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

# Mathematical verification
The paper's proof uses an exact clique-sum differential inequality, a within-clique logarithmic-ratio identity, the symmetric quadratic Lyapunov function, a block Schur-complement calculation, and a stable-leaf perturbation argument to compute the center-direction coefficient at threshold. The identities are independently reproducible by `python verify.py` with dependencies in `requirements.txt`. The script checks exact polynomial roots for sample partitions, equilibrium equations, critical eigenvector and network spectral positivity below threshold. Numerical integrations support but do not establish the asymptotic statements. The general limit statements require the analytic proof in `RESULT.md`; no exhaustive finite experiment or formal external certification is claimed. The critical statement excludes zero hub initial conditions, as required by strict positivity.
