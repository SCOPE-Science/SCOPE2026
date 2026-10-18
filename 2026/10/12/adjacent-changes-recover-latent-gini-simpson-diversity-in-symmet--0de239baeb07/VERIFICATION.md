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

For a de Finetti mixture with P~Dirichlet(alpha,...,alpha), alpha>0, m>=2, n>=2, conditional iid categorical observations yield E[1_{Xi!=Xi+1}|P]=1-sum_j P_j^2=D. Hence A_n=T_n/(n-1) is conditionally unbiased for latent D and Cov(A_n,D)=Var(D). Dirichlet rising-factorial moments for exponents (2),(4),(2,2),(3) give Var(D)=2alpha(alpha+1)(m-1)/((m alpha+1)^2(m alpha+2)(m alpha+3)). Pair-covariance splits overlapping adjacent edges (1-2S2+S3 conditional) and disjoint edges (conditional independence, unconditional Var(D)), leading to exact Var(T_n) and Corr(A_n,D)=sqrt(2)(n-1)/sqrt(c^2(n-1)+c(7n-9)+2n^2+2n-6), c=m alpha. Algebraic expansion gives Corr=1-(c+1)(c+6)/(4n)+O(n^-2). Independently enumerated exactly 45 cases (m 2,3,4; alpha 1/2,1,3/2; n=2..6) and 20007 sequence states with exact rational posterior moments, confirming formulas. The universal conditional unbiasedness holds for any random finite directing distribution, while closed expressions require symmetric Dirichlet. Decoded public RESULT.md and VERIFICATION.md contain literal ASCII BEL before 'lpha' where '\alpha' should appear, a real source-rendering corruption; no fabricated correction or publication is supplied.

## originality

PASS

Earlier Eryilmaz 2008 multicolor Polya and exchangeable multistate run theorems give marginal/joint distributions of observable run statistics, so the full marginal Var(T_n) is in principle derivable from their stronger marginal laws and is not claimed as priority. Their accessible statements concern observed run counts, not mixed covariance with latent directing vector diversity D. The identity E[A|P]=D follows a basic conditional expectation calculation, but the exact positive finite-sample latent covariance, correlation and 1/n calibration are separately motivated and not identified as explicit earlier formulas. Full 2008 articles were not materially read; overlap is a genuine high-priority residual risk, and generic probabilistic identities alone are not a literature negative proof.

## value

PASS

Gini-Simpson diversity is a canonical latent measure and adjacent-change frequency is a natural sparse local statistic of an exchangeable color sequence. Exact finite-n correlation and limiting error quantify how a statistic computable without seeing the directing proportions tracks latent diversity despite reinforced dependence. Existing observable-run marginal distributions do not determine joint dependence with unobserved D by themselves. The exact covariance is elementary from the tower property; the full explicit calibrated correlation is the substantive narrow natural fact, not a sweeping inference or optimal-estimation claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
