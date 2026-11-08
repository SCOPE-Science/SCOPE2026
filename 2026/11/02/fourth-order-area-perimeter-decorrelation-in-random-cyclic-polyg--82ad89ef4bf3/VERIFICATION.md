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

Ordered uniform circle gaps have Dirichlet(1,...,1) law and exact moments E P_r=nr!/(n)^overline r, E(P_rP_s)=n[(r+s)!+(n−1)r!s!]/(n)^overline(r+s). Exponential representation and delta method for (E,E³,E⁵) give centered P3/P5 joint Gaussian at n^(5/2), n^(9/2), with κ33=360, κ35=28800, κ55=3254400. Taylor expansion of sin with L² P7=O(n^-6) yields centered S=−(π³/6)P3~+(π⁵/120)P5~, A=−4(π³/6)P3~+16(π⁵/120)P5~. Exact least squares projection gives β_n=4−48π²n^-2+o(n^-2), projected n^(9/2) residual=(π⁵/10)(P5~−80n^-2 P3~)+o_L², covariance constant [3254400−160·28800+6400·360]/100=9504 times π^10. Since Var(A)~160π^6n^-5, regression identity gives 1−ρ~(297π⁴/10)n^-4; fixed slope4 variance 32544π^10, relative 33/113. Independently recalculated every κ and these constants exactly.

## originality

PASS

Qualified PASS for exact n-dependent optimal linear regression slope, fourth-order deficit and orthogonalized Gaussian residual. Earlier Wang–Xu–Liu 2021 established fixed-slope Gaussian extrapolation, not the checked least-squares residual distribution. Xu–Meng–Li 2019 also concerns extrapolation means; Koroleva–Nikitin subsets use a different sampling statistic. A full older Bélisle 2011 paper remained inaccessible and might have an implicit joint-covariance result; original limit theorems do not automatically state the exact projected coefficients but could imply them by moment expansions.

## value

PASS

The sharp correlation deficit and optimal prediction variance are natural quantitative joint statistics of full-sample random cyclic polygons. The optimally adapted correction reduces residual variance to 33/113 of a conventional fixed-slope estimator, identifying a meaningful fourth-order effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
