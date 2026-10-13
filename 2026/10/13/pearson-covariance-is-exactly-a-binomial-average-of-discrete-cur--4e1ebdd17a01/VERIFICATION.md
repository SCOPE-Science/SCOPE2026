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

The exact domain is an equiprobable multinomial sample with \(m,n\ge2\). The cell score \(h\) is arbitrary on the finite set \(\{0,\ldots,n\}\), so the main identity has no regularity assumption.

The critical proof steps are:

1. Pearson's statistic is exactly affine in the pair-collision count:
   \[
   X^2=m-n+\frac{2m}{n}C.
   \]
2. Exchangeability reduces \(\operatorname{Cov}(C,T_h)\) to one distinguished-pair covariance.
3. Conditioning that pair to be equal or unequal changes \(\mathbb E T_h\) by exactly \(\mathbb E\Delta^2h(Y)\), with \(Y\sim\operatorname{Binomial}(n-2,1/m)\).
4. The probability of pair equality is \(1/m\), yielding the displayed coefficient.
5. For Cressie--Read statistics, the cell score is a positive or negative multiple of \(k^{\lambda+1}\); its curvature sign matches the normalization so that covariance is strictly positive for every \(\lambda>-1\). The continuous \(\lambda=0\) limit uses \(k\log k\).

`checker.py` enumerates multinomial count vectors, weights them by multinomial multiplicity, and independently recomputes the relevant covariances. It checks the likelihood-ratio specialization on a finite grid, representative negative and positive power-divergence parameters, and the quadratic consistency specialization. A large finite calculation checks the stated fixed-cell asymptotic numerically.

Finite computations are supplementary. The all-\(m,n\) identity and sign theorem follow from the symbolic argument above, not from enumeration.

No claim is made for \(\lambda=-1\), where empty cells can make the modified likelihood statistic divergent, or for nonuniform cell probabilities.
