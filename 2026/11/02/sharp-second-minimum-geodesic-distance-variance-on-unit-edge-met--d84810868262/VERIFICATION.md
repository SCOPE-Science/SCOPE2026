---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For m>=3 unit edges and two independent arclength-uniform points, conditional edge-pair integration gives E D=E X+1/(3m), E D²=E X²+1/6. Writing X=1_{E != F}+Z gives the exact surplus Var(D)-Vstar=Var(Z)+4 EZ/(3m), Z>=0. Degree-sequence majorization bounds p=P(Z>0) below by 2(m-2)/m² (equality only once-subdivided (m-1)-arm star) and above by (m-1)(m-2)/m²<1-q. Conditional total-variance then yields Var Z>=p(1-p)>=q(1-q), EZ>=p>=q and sharp gap G=2(m-2)(3m²-2m+12)/(3m^4). Direct independent exhaustive Prüfer-tree checks through 7 vertices (18,244 labeled trees for sizes n=4..7) corroborate; universal proof comes from incidence/variance bounds, not enumeration. m=3 is 3-edge path as nonstar equality.

## originality

PASS

The nearest cited primary network papers optimize one-facility variance or mean pairwise distance, whereas this theorem optimizes the variance of two independent uniform-arclength points, determines the global second extremizer and exact excess identity. Stochastic first-order ordering of distances is insufficient for variance ordering. No equivalent second-minimum result identified in bounded Resultary/published and primary searches.

## value

PASS

Mean-distance tree extremizers are known, but variance is a distinct natural measure of typical pair-distance dispersion and is not monotone under stochastic dominance. The exact gap, unique second-optimal topology for every m, and positive surplus formula give a complete motivated extremal classification, useful as a sharp stability benchmark for nearly star-shaped metric trees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
