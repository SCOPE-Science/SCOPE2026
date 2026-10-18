---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For independent nonnegative integer variables, R=P(Y<X)=sum_{x>=0} p_X(x) F_Y(x-1). For every omitted x>=K+1 monotonicity of the CDF gives F_Y(K)<=F_Y(x-1)<=1; multiply by p_X(x)>=0 and sum to obtain the exact two-sided certificate F_Y(K)Pr(X>K)<=R-R_K<=Pr(X>K). The original DAPW PMF is S(x)-S(x+1) with S(k)=alpha/(alpha-1)*(1-alpha^{-theta^{k^beta}}) (continuous alpha=1 limit theta^{k^beta}). Checked the 2026 PDF (Sec 2 Eq 1–5, p4 line stating stopping condition |R_K-R_{K-1}|<10^-6, and Scenario 4 p14). At alpha=.3, theta1=.4, beta1=.2, theta2=.4, beta2=2, K=4041: independent stable expm1 arithmetic gives last term 9.99890871231611e-7, S_X(4042)=0.0041684145856391575, F_Y(1)=0.9865850241462029, and certified lower remainder 0.0041124954046241925. The finite high-cutoff checker is diagnostic, not the source of the theorem.

## originality

PASS

The 2022 DAPW paper gives the survival formula and an infinite stress–strength series but no printed truncation remainder bracket. The actual 2026 Elkalzah source prints a last-increment threshold below 10^-6 but no global error certificate. The distribution-free probability bound is elementary and not claimed as broadly new numerical analysis; the applied exact DAPW stopping-rule counterexample and certified closed-form replacement are not implied by either source’s stated result. Resultary and web comparison found no matching DAPW-specific explicit >0.0041 residual example; a general textbook tail inequality may predate all papers.

## value

PASS

This is an actionable precision failure in a published, repeated reliability-series computation: one term below 10^-6 coexists with a rigorously omitted positive probability >0.004112, over 4,100 times that term. Because the model’s survival is explicit, the replacement tolerance criterion can be implemented without a large extra sum. The material numerical gap supplies the specific motivation beyond an otherwise routine monotone-CDF inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
