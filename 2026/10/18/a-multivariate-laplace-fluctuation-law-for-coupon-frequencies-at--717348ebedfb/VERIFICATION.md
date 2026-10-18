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

# Reproducibility and proof checks

Running `python3 verify_coupon.py` requires Python 3 standard library only. The program independently checks \(\mathbb E K_{n,1}=H_n\) for \(2\le n\le15\) using exact fractions, the finite \(n=3\) all-singleton probability \(2/9\), an independent direct-sampling experiment for \(n=12\), and conditional multinomial simulation for \(n=350\). These finite checks are deliberately not described as certification of all \(n\).

Analytic critical steps: the last first-arrival index produces exactly one compulsory singleton; other count classes form a multinomial sample with probabilities \(q_r(t)=e^{-t}t^r/[r!(1-e^{-t})]\). The first arrival maximum gives \(n e^{-\tau_n}\Rightarrow\operatorname{Exp}(1)\). The conditional multinomial Lindeberg condition is satisfied at the logarithmic frequency scales for every fixed finite dimension. The independent clock comparison has exact mean-square error \(H_n/n\) and is negligible under the random centering.

No infinite-dimensional or growing-\(R\) limit is asserted. The normal-mixture/characteristic-function statement has not undergone an independent audit.
