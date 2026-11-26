---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the corrected RESULT.md, multiplication of the three exact densities cancels n but leaves both parameter-dependent normalizers. At frozen old parameters, n has weights proportional to eta_0^n/(lambda_0+n theta_0 y)^(lambda_0+1), and Z conditional on n is gamma of shape lambda_0+1 and rate lambda_0+n theta_0 y; the four expectations are finite. The positive m*lambda*log(lambda) term of both literal printed variants dominates their linear shape terms, while Stirling's formula in the corrected objective leaves strictly negative linear coefficient m+B−C by nondegeneracy and log(z)<=z−1. The gamma pole gives left-end decay, and the trigamma sum exceeds the integral 1/lambda, proving strict concavity and uniqueness. The scores are direct derivatives, and the original article's Eq. (4.9) really includes the log-series derivative absent from (4.5). The frozen line 105's unqualified box-boundary claim was not correct for arbitrary boxes: with one y=exp(4) and old parameters (1,1,1/2), B<−3 and C>0, making the printed shape score log(lambda)+1+1/lambda+B−C negative throughout [1,2]. The repair proves the valid eventual-upper-bound statement for a fixed positive lower bound, and keeps the example boxes as examples. It also states the article's eta=0 limiting convention separately from the interior calculation. Fresh high-precision posterior summation and solving the shape score in the supplied example gave lambda=2.4963599403727288.

## originality

PASS

The published article already factorizes the complete likelihood correctly before dropping terms, restores the eta normalizer derivative in Eq. (4.9), and reports a corrected fixed-shape simulation. Those facts are credited, not claimed as new. The surviving diagnosis is specific to the literal LGF joint shape objective: the extra log(lambda), the omission of the gamma normalization, absence of a finite M-step, and a corrected shape objective and exact box behavior. Neither the same-model tail result nor the earlier related model's digamma score diagnoses this printed joint M-step.

## value

PASS

The issue is not only a missing term in notation: the article prints an objective that has no finite joint shape maximizer, so literal reproduction of the procedure can select an arbitrary large numerical cap instead of estimating the parameter. The corrected normalized objective has a unique finite conditional shape maximum, and the explicit small-box counterexample prevents treating any boundary result as a universal diagnostic. The distinction from a fixed-shape simulation and an observed-likelihood fit keeps the correction useful for replicating or implementing the actual joint EM algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
