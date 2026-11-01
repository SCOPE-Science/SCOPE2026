---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For individually named finite induced parameter poset P_{n,r} with n>=2r+1, r>=1, each lower a_i is below the r consecutive upper b_j. A nonalgebraic type of the homogeneous universal poset corresponds exactly to a compatible ideal/filter (L,U), and the two-sided pairs are bicliques. If a nonempty lower subset has a common neighbor, its unique short cyclic span of length s<r gives n singleton choices and n(1+u)^{s-1} endpoint choices, producing M=n[u((1+v)^r-1)+u^2 sum_{s=1}^{r-1}(1+u)^{s-1}((1+v)^{r-s}-1)] and M(1,1)=nr2^{r-1}. For one-sided cases, selecting the upper set makes a lower vertex forced iff one of its r upper neighbors selected; cyclic binary words weighted 2 per all-zero r-window are exactly traced by T_r. Total nonalg types t=2tr(T_r^n)+nr2^{r-1}-1; characteristic polynomial lambda^r-3lambda^(r-1)+sum_{j=0}^{r-2}lambda^j equals (lambda^(r-1)(lambda-2)^2-1)/(lambda-1), including T_1=(3). Primitive Perron–Frobenius theory and monotonicity of f_r(lambda)=lambda^(r-1)(lambda-2)^2 on lambda>2 give t~2rho_r^n (fixed r) with rho_r strictly decreasing to 2. Independently rebuilt direct bitset enumeration of lower/upper choices and transfer traces for 15 (r,n) cases r=1..5, n=2r+1..2r+3 at u=2, v=3: all agree; finite checks corroborate the unlimited parameter proof.

## originality

PASS

The 1-type ideal/filter bijection is known and a broad generalized-crown ideal recurrence may be prior. The surviving novelty is a bivariate mixed-type polynomial for all widths, integrated full named-parameter one-type count, and spectral width-growth law. An inaccessible Chebyshev/generalized crown article may cover one-sided ideals; that access limitation is explicitly not treated as a negative conclusion about its full text. Best-of-knowledge PASS.

## value

PASS

The family generalizes classical cyclic crowns and the complete weighted one-point type polynomial is natural in homogeneous-poset model theory. The exact separation of linear mixed contributions and exponential one-sided contributions, algebraic Perron bases, and monotone dependence on incidence width give nontrivial parametric structure useful beyond a single small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
