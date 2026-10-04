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
The primary source equations were inspected directly in the open-access PDF, including the model equation and the predator-free equilibrium section.

Analytic checks:
- At \(z=0\) and \(y>0\), the infected-prey balance gives \(x=\nu(\alpha+y)/\beta\).
- Substitution yields the quadratic \(F(y)=r(\alpha+y)[\beta K-\alpha\nu-(\beta+\nu)y]-\beta^2Ky\).
- If \(\beta K\le\alpha\nu\), then \(F(y)<0\) for every \(y>0\).
- If \(\beta K>\alpha\nu\), the quadratic has exactly one positive root because its leading and constant coefficients have opposite signs after multiplying by \(-1\).
- The same threshold is the sign change of the infected-prey linear growth rate at \((K,0,0)\).

Reproducibility checks:
- `verify.py` symbolically reconstructs the eliminated polynomial from the printed equations.
- It verifies the exact counterexample \(r=\alpha=\nu=1\), \(\beta=2\), \(K=2/5\), for which the source's condition holds but no positive predator-free endemic root exists.
- It verifies the exact feasible case \(r=\alpha=\nu=1\), \(\beta=2\), \(K=1\) and substitutes the closed-form root into both prey equilibrium equations.

Limits:
- The result concerns only predator-free endemic equilibria.
- Numerical or symbolic examples illustrate the theorem but are not used to infer the general zero-versus-one classification.
- No independent audit has been performed.
