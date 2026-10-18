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

The published CDF is F(x)=log(1+g)e^{beta(g-1)}/log2 with g=e^{-(alpha/x)^theta}. Its printed Eq(13) surrogate chooses z_q=W_0(beta q e^beta log2)/beta (equivalently unique z in (0,1) with z e^{beta(z-1)}=q log2), hence F(Qtilde(q))=q log(1+z_q)/z_q<q. As q approaches 1, z_q approaches z_beta<1 satisfying z_beta e^{beta(z_beta-1)}=log2; thus Qtilde is bounded while exact quantile diverges. Because z_beta is in (log2,1), limiting achieved coverage c_beta=log(1+z_beta)/z_beta belongs to (log2, log(1+log2)/log2). Expanding exact CDF at g=1 gives 1-F(x)~(beta+1/(2log2))(alpha/x)^theta; hence Q_exact(q)~alpha[(beta+1/(2log2))/(1-q)]^{1/theta}. Independent monotone bisection for alpha=theta=beta=1, q=.99 gave surrogate 5.0654970551, exact 171.0287464965 and coverage .7227998524. This is source equation evaluation, not claim about unknown software or empirical VaR figures.

## originality

PASS

The exact source declares Lambert-W Eq(13) an approximation yet claims it is useful at high q>=.90. The submission proves a universal strict undercoverage and limiting coverage interval, plus corrected infinite high-confidence quantile asymptotic; these full results were not in the inspected primary source or matched by relevant Resultary searches. Prior use of Lambert-W inversion and textbook log(1+z)<z is credited; the source-specific quantified tail-risk defect is the contribution.

## value

PASS

Quantifying true-versus-nominal coverage of a risk threshold is substantively motivated. Demonstrating that a proposed high-confidence VaR cutoff remains bounded while the correct quantile diverges, with exact coverage ceiling and asymptotic correction, has direct implications for tail-risk calibration; more than a cheap algebraic typo check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
