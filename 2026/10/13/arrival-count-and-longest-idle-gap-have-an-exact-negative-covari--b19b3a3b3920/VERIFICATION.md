---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The domain is a homogeneous Poisson process of rate \(\lambda>0\) observed on a fixed interval \([0,t]\), with both boundary gaps included in the maximum.

The proof depends on four exact steps:

1. Conditional on \(N(t)=n\), the \(n+1\) normalized gaps are \(\operatorname{Dirichlet}(1,\ldots,1)\).
2. The maximum coordinate of a uniform \(m\)-simplex vector has mean \(H_m/m\), obtained by integrating its inclusion-exclusion tail.
3. The exponential generating function of harmonic numbers is
   \[
   \sum_{m\ge1}H_m\frac{x^m}{m!}
   =
   e^x\operatorname{Ein}(x).
   \]
4. For \(N\sim\operatorname{Poisson}(\mu)\),
   \[
   \operatorname{Cov}(N,g(N))
   =
   \mu\frac{d}{d\mu}\mathbb E[g(N)].
   \]

`checker.py` verifies the finite binomial-harmonic identity exactly over a large dimension range and checks the harmonic exponential-generating-function coefficients and the differentiated covariance series with exact rational arithmetic.

The finite checker is supplementary. The theorem for all \(\lambda>0\) and \(t>0\) follows from the analytic argument above.

The result does not cover the longest completed interarrival interval when the terminal censored gap is omitted, nor inhomogeneous Poisson processes.
