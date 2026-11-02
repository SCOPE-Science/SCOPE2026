---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For one initial additive parasitoid pulse q, direct recurrence gives H3=R^3H0 exp[-a(P0+q)-W+(1-R)Y+R Y exp(Y-W)] with W=acH0 and Y=W exp[-a(P0+q)]. H1 and H2 strictly decrease with q. The logarithmic H3 derivative divided by a equals G=-1+(R-1)Y-RY(1+Y)exp(Y-W), with G double-prime=-R exp(Y-W)(4+5Y+Y^2)<0. For R>1, positive G iff W>F_R(y)=y+log(Ry(1+y)/((R-1)y-1)); F_R has a unique global minimizer from the cubic derivative, giving the exact W_c and at most two positive stationary doses. Root order and decreasing Y(q) give the three starting-exposure cases, including tangencies. R<=1 gives negative derivative. Direct symbolic differentiation independently verified the H3 formula and dose derivative; exact R=3,H0=6,P0=log3,q=log2 demonstrates third-generation reversal.

## originality

PASS

The classical model is not new and Tang–Xiao–Cheke 2008 treats augmented host-parasitoid models and periodic pest management. Inspection of its primary 17-page open-access paper shows intergenerational parasitoid survival and periodic IPM dynamics rather than the single initial pulse and complete third-generation dose phase diagram. Resultary pest release papers treat asymptotic thresholds/basins or different systems. Barclay 1982 source is plausibly relevant but full text was inaccessible after OA and authorized Oxford attempts, with risk retained.

## value

PASS

The mathematically natural earliest delayed-response horizon has a sharp parameter-uniform critical release-dose threshold, two-turning-point classification, and exact counterintuitive witness; this is more than an arbitrary short simulation. The specific unregulated model and single finite pulse limit biological scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
