---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read exact Kenyon--Prause Section 3.4 boundary s(R)=avg_i a_i/(R+a_i), t(R)=avg_j R/(R+c_j), a_i=alpha_i^2<c_j=beta_j^-2 (R>0). s strictly decreases from 1 to 0; t increases 0 to 1; a_i<c_j ensures t(R)<1-s(R) so the curve bounds a genuine area against s+t=1. By orientation area=1/2-int_0^1 T(s)ds=1/2-int_0^infty t(R)(-s'(R))dR. Expansion gives ordered pair integrals int_0^infty [R/(R+c_j)] [a_i/(R+a_i)^2] dR. Setting R=a_i x, q=a_i/c_j reduces to I(q)=int_0^infty qx/((1+qx)(1+x)^2) dx = q/(q-1)-q log(q)/(q-1)^2. F(q)=1/2-I(q), matching asserted formula for all m1,m2. Independently evaluated exact integral numerically for q=.01,.1,.5,.9, obtaining F approximately .4631142722,.3268413465,.11370563888,.0175535908, equal to closed form within quadrature precision; analytic separation, not quadrature, proves arbitrary periods.

## originality

PASS

Kenyon--Prause published boundary parametrization and simply-periodic predecessor are prior. The newly assessed claim is a different mathematical quantity, integrated total coexistence area, with a nontrivial all-period arithmetic averaging identity not stated in the inspected full source. The outer boundary need not collapse cellwise even though the integral does. Originality remains best-of-knowledge for unindexed notes.

## value

PASS

The coexistence region has a natural geometric size in the model's physically meaningful slope simplex. Despite nontrivial higher-period boundary dependence, its area reduces exactly to the arithmetic mean of universal one-cell contributions, giving a reusable global invariant across arbitrary periods and a precise way to compare environments without reconstructing the full phase curve. This is more than a cosmetic simplification of a previously evaluated scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
