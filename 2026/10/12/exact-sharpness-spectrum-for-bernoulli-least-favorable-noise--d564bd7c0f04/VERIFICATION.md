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

The analytic proof has four critical checks.

1. For \(S=X+Y\), independence gives \(\operatorname{Cov}(X,S)=\sigma^2\), and conditioning preserves this covariance: \(\operatorname{Cov}(\mathbb E[X\mid S],S)=\sigma^2\). Cauchy--Schwarz therefore gives the universal lower bound.
2. Equality forces \(\mathbb E[\widetilde X\mid T]=aT\) with \(a=\sigma^2/(\sigma^2+v)\). Since \(\widetilde X\) is bounded, this makes \(T\) and the centered noise bounded, so both characteristic functions are entire.
3. Differentiating the characteristic-function identity gives \((1-a)\phi_X'\phi_Y=a\phi_X\phi_Y'\). A simple zero of the Bernoulli characteristic function then forces \((1-a)/a\) to be an integer zero multiplicity and identifies \(\phi_Y\) as the corresponding power of \(\phi_X\).
4. At integer ratio \(m\), the sum of \(m\) independent matching Bernoulli noises attains the lower bound by exchangeability. Existence of a least-favorable noise rules out equality of the infimum at every noninteger ratio.

The accompanying `verify.py` checks the integer construction for several rational \(p\) and \(m\) values using exact fractions. It does not attempt to certify the analytic continuation or the infinite quantifiers computationally.
