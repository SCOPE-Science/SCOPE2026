---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The cofactor formula gives S(u)=pi sqrt(abc)/sqrt(u^T Q u), P(u)=pi sqrt(abc)sqrt(u^T Q^-1u), so Z=(u^T Q u)(u^T Q^-1u)=1+A w1w2+B w1w3+C w2w3, w_i=u_i^2. Kantorovich AM-GM gives K=(a+c)^2/(4ac), attained at exactly four directions with u2=0 and |u1|=|u3|=1/sqrt2. Local spherical coordinates have Haar density dtheta dy/(4pi), deficit B s^2+D y^2+O((|s|+|y|)^3), D=(B-A-C)/2=(b-a)(a+c)(c-b)/(2abc)>0; summing four ellipse-cap areas gives gamma=1/sqrt(BD). The endpoint k=c/a recovered from K; gamma fixes t+k/t, giving precisely t and k/t, the unavoidable polar alternatives. Independently verified all algebra by symbolic factorization and the exact gamma values at (1,2,3),(2,3,7),(1,4,25), including example K=4/3,gamma=3/2.

## originality

PASS

Classical Kantorovich gives the max K but not two-dimensional Hessian coefficient or inversion from it. Kim-Yaskin-Zvavitch examine marginal area distributions for sections or projections, not the paired same-direction quotient. Resultary inverse-square section moments determine ellipsoid axes via a different measurement, and Fish et al study parallel section functions. No read source subsumes the paired upper-tail slope and polar-ambiguous inversion. An older general product-quadratic-form density might, so best-knowledge risk remains.

## value

PASS

Two observable scalar features of the joint same-direction section/projection law recover the complete generic triaxial shape up to the unavoidable polar duality; this is an identifiability theorem with a sharp geometric obstruction, not merely evaluating the known Kantorovich maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
