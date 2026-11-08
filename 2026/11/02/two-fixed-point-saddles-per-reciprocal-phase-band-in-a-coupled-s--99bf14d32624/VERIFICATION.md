---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every fixed a,b>0 the second fixed-point equation G(x,y)=y-sin^2(b*pi*y+a*x)=0 has G_y(0,0)=1, yielding a unique small analytic graph Y(x)=a^2*x^2+2*a^3*b*pi*x^3+O(x^4). The phase theta=a*pi/x+b*Y(x) has theta'=-a*pi/x^2+O(x) strictly below -alpha' for alpha=arcsin(sqrt(x)); the two equations theta=n*pi+/-alpha each cross once in every sufficiently high band. Taylor substitution proves x_{n,+/-}=a/n -(+/-)a^(3/2)/(pi*n^(5/2))+O(n^-7/2), y=a^4/n^2+O(n^-3), and N(epsilon)=2a/epsilon+O(1). Direct Jacobian trace/eigenvalue scale gives lambda_unstable=-sigma*2*pi*n^(3/2)/sqrt(a)+O(n^1/2), lambda_stable=2*a^2*b*pi/n+O(n^-2), opposite determinant signs. Independent scipy root searches with a=b=1 at n=30,80,150 for each sign confirmed positions, both residuals and real saddle signs. Finite tests corroborate; analytic monotonicity supplies the all-n conclusion.

## originality

PASS

Best-of-knowledge originality of the precise final mathematical addition, not its known source definition; checked actual primary statements/implications and Resultary semantic neighbors; residual access and priority risks remain explicit. The claimed formulas require IFT, strict phase monotonicity and Jacobian asymptotics absent from the inspected source material; prior model publication is credited.

## value

PASS

A local fixed-point census and sharp two-branch asymptotic/saddle spectrum for a natural singular planar sine-square map reveal bifurcation geometry invisible to numerical chaos indicators. Phase-dependent orientation and the n^(3/2) versus n^-1 multipliers are motivated dynamical invariants, not just restatements of the formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
