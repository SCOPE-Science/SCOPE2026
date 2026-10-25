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

## Verification performed

The proof is analytic: Brownian first-passage Laplace transform, renewal decomposition, strict exponential convexity, one-dimensional strict convexity for the mean, and strict concavity for discounted success. These arguments cover all Borel relocation laws, all \(p\in[0,1]\), all \(s>0\), and all \(0<a<L\), \(D,r>0\).

`verify.py` was executed with NumPy/SciPy. It passed 160 randomly selected parameter test instances, independent scalar minimizations/maximizations, strict interior-law replacement checks, the two exact prior thresholds, universal symmetric optimality for seven discounts, and a 40,000-path exact first-passage-reset Monte Carlo comparison. Example results were sample mean 12.036206 versus analytic 12.016518 and sample discounted transform 0.505020 versus analytic 0.505490. The computations do not certify infinitely many parameters or a prior-literature originality claim.

## Scope of unperformed checks

No independent scientific audit or external reproducibility assessment has been performed. No ordinary stochastic dominance is claimed; the rigorously established comparison concerns Laplace transforms for every positive discount. More general renewal clocks, relocation costs, and resetting-rate optimization remain outside the theorem.
