---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For increments from consecutive permutation comparisons, the pair of edges around each odd vertex contributes 2 exactly when S_{2k-1}>0, so N_{2n}=2Σ1_{D_{2k-1}≤k-1}. Conditioning on the previous rank-r permutation and using Eulerian insertion yields E[π_r|des=d]=r-d and E[U_r|des=d]=(r-d)/(r+1). Only the comparison sharing U_r remains correlated with early event; the covariance becomes a positive Eulerian absolute-deviation sum with factor 2r/(r+1). For independent signs, martingale orthogonality gives ΣE|W_{2k-1}|; variance of Eulerian descents (r+1)/12, Cauchy-Schwarz and exact binomial absolute moments give strict termwise smaller C_n. One-dependent CLT plus uniform integrability yields n^{3/2} constants. Direct exhaustive independent enumeration for n=1,2,3 reproduced the exact covariances. The arcsine marginal and beta-binomial variance are correctly cited as prior results, not derived from the finite check.

## originality

PASS

Best-of-knowledge statement/implication comparisons of the precise final claim, with material primary reading and relevant Resultary searches. These premises imply equal marginal N laws, but not equal (indeed they are unequal) joint laws with S. The present Eulerian rank calculation supplies the unprovided implication. Inaccessible primary work is named as residual risk rather than declared noncovering.

## value

PASS

Shows a mathematically informative failure of a one-dimensional exact distribution to determine joint dependence: two canonical walks have the same occupation marginal but strict finite-size and asymptotic covariance gaps. Exact Eulerian formula and sign hold for all n and are useful for permutation-walk joint statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
