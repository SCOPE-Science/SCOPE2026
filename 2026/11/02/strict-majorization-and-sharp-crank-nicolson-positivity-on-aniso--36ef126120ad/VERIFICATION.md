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

The exact theorem and proof, including all hypotheses and parameter boundaries, are in `RESULT.md`. The reproducible standalone `verify.py` uses Python 3 standard-library rational arithmetic and numerical bisection; its execution reported **3,474 supplementary checks passed**.

The checker constructs the full \(2^d\)-state weighted-cube matrix for \(d=2,3,4\), inverts \(I+sL\) by exact rational elimination, verifies Walsh-return entries and Markov row sums, and checks every off-diagonal end-step entry is strictly positive for the sampled positive rates and steps. It additionally checks strict pairwise averaging for rational rates, the exact two-dimensional cubic, the balanced-dimension ordering through \(d=128\), and selected dimension and anisotropy asymptotic examples.

No finite computation is claimed to prove the uniform all-dimension strict majorization or error terms. The proof supplies the positive-definite Bernoulli Hessian, leave-one-out conditional Jensen, centered-binomial moment bounds, and singular root sandwich. At a rate floor equal to \(S/d\) there is only the balanced feasible vector; the singular formula applies only for \(\varepsilon>0\) before taking the limit. No independent validation has been performed.
