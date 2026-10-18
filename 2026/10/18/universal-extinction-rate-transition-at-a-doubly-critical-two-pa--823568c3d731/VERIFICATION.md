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

# Verification notes

The standalone `verify.py` checks six symbolic identities, exact parameter specializations on both sides of the equality threshold, and two direct numerical integrations; 38 assertions passed. Dependencies: Python, SymPy and SciPy. Run `python verify.py` in the same folder as this document.

The exact original ODE is algebraically rewritten using \(B=s\delta/(s+\delta)\), \(H=h+B\), \(v_0=s/(s+\delta)\), \(a=\delta/(s+\delta)\), and \(w=v-v_0-au\). The symbolic verifier establishes \(\dot u=u[u/(m+u)-Hu+\delta w]\) and \(\dot w=-(s+\delta)vw-a\dot u\), plus the critical identity \(u/(1/H+u)-Hu=-H^2u^2/(1+Hu)\).

For \(s=1,\ \delta=1/2,\ e=1/3,\ h=1/6\) the critical value is \(m=2\). At time \(10^5\), numerical integration from \(u(0)=0.8,v(0)=0.3\) gave \(tu^2\approx2.01172826\) (exact limit \(2\)); for \(m=3\) it gave \(tu\approx5.99777124\) (exact limit \(6\)). Tracking ratios were approximately \(0.08290023\) and \(0.05555665\), respectively, versus exact limits \(1/12\) and \(1/18\). These finite numerical values are not proof of the asymptotic statements.

All infinite-time conclusions depend on the explicit analytic comparison, fluctuation, and stable-filter arguments in RESULT.md. They have not been independently audited.
