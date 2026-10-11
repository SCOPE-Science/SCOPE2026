---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Solving the predator fixed-point equation gives \(v=q(bu+c)\) with \(q=(\alpha-d)/a\). Substitution into the prey equation independently reproduces exactly the published quadratic coefficients. Since \(C_0>0\), Vieta's formulas and the discriminant give the complete positive-root classification, including the boundary \(C_2=0\) case. Fresh symbolic expansion verifies the multiplier identity. At the rational witness \((r,K,\beta,\gamma,a,b,c,k,\alpha,d)=(1,10,1/5,1,1,1/10,5,1/100,3/2,1/2)\), the quadratic has coefficients \((5001/5000,-439/50,1/2)\), discriminant \(9386/125\), and two positive roots approximately \(0.05732\) and \(8.72092\).

## originality

PASS

The initiating paper explicitly asserts in Proposition 1(iii) that the displayed quadratic has a unique positive root whenever \(\alpha>d\). The audited theorem shows that this is false and gives the complete zero/one/two-positive-root classification for the same quadratic, plus an identity tying the constant term to the invasion multiplier. Fresh Resultary search did not locate a prior correction of this exact proposition.

## value

PASS

This directly corrects the equilibrium count underlying the source paper's subsequent local dynamics and exposes a genuine two-coexistence regime and invasion/coexistence mismatch. Correcting the global fixed-point diagram of a published ecological map is substantively useful even though the algebra is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
