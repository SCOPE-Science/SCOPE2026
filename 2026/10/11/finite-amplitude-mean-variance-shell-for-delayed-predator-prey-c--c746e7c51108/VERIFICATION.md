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

The proof was reconstructed directly from the printed scaled equations. The critical checks are:

1. For a positive periodic orbit, integrating \(d(\log x)/dt=1-x-y\) over one period gives \(\bar x+\bar y=1\).
2. Periodicity gives \(\int_0^T x(t-\tau)y(t-\tau)\,dt=\int_0^T x(t)y(t)\,dt\), so the predator balance gives \(\overline{xy}=x_*\bar y\).
3. Integrating the prey equation gives \(\overline{x^2}=\bar x-\overline{xy}\), which simplifies to \(\operatorname{Var}_T(x)=(\bar x-x_*)(1-\bar x)\).
4. Substitution yields \(\operatorname{Cov}_T(x,y)=-\operatorname{Var}_T(x)\).
5. A nonconstant positive periodic orbit cannot have constant \(x\). Hence prey variance is positive, forcing \(x_*<\bar x<1\). Cauchy–Schwarz yields \(\operatorname{Var}_T(y)\ge\operatorname{Var}_T(x)\); equality would force \(x+y\equiv1\), and hence \(\dot x\equiv0\), contradicting nonconstancy.

The accompanying checker verifies the algebraic identities and the source-parameter numerical value at \(\tau=81\). It does not numerically integrate the delay equation and is not used as a substitute for the analytic proof.

Limit: no claim is made about nonperiodic invariant measures or chaotic time averages in this package.
