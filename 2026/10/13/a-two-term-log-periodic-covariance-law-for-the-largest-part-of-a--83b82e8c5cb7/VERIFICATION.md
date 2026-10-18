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

Under uniform unrestricted compositions of N, cut bits n=N-1 are iid fair; K=1+ones and M=1+longest zero run. Bernoulli differentiation gives Cov=-1/4 sum_{r>=1} partial_p Pr_p(L_n<r)|p=1/2. The avoidance generating function is (1-(qz)^r)/(1-z+p q^r z^(r+1)). Differentiating its dominant-pole residue uniformly for log2 n±3log2 ln n, with Rouché separation on |z|=3/2, gives -n epsilon_r' exp(-n epsilon_r)+ summable o(1) errors, epsilon_r=p q^r. Short-run disjoint-block tails are superexponentially suppressed and long-run pivotality tails contribute O((ln n)^-2). Reindexing lambda_r=n 2^(-r-1) yields Cov= -1/2[(log2 n-2)P({log2 n})+Q({log2 n})]+o(1), with P and Q as absolutely convergent dyadic series. Gamma Fourier coefficients imply P nonconstant, and longest-run variance bounded above and away from zero gives Corr=-Theta((ln N)/sqrt N). Independent exact recurrences give declining absolute differences through n=4096; numerical values alone cannot establish the o(1) uniform error.

## originality

PASS

Finch directly studies the same joint statistics but proposes a different decay law; prior Resultary work proved negative regression and a weaker log-squared covariance bound, not this uniform absolute-o(1), phase-resolved two-term formula. Lou 1996 supplies exact finite distributions; its full article remains inaccessible and is a specific priority risk, not proof of novelty or an automatic O failure.

## value

PASS

The question of asymptotic dependence of composition length and maximum is explicitly posed for the same statistics. The new absolute-o(1) covariance expansion identifies the sharp log scale, the lattice-phase dependence and the correct root-N decorrelation regime, superseding a conjectured different decay order. This is a mathematically motivated sharp asymptotic result, not merely finite runs enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
