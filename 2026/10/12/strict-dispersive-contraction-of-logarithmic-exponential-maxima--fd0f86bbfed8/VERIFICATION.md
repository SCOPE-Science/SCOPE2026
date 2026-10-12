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
The exact differentiable quantile \(Q_a(u)\) is reconstructed from the continuous CDF and verified by direct differentiation. The logarithmic derivative of \(\Phi(t)\) is negative for every \(0<t<1\), since both fractions in the expression for \(t(1-t)\Phi'(t)/\Phi(t)\) individually exceed \(t\) and \(1-t\). This establishes strict quantile contraction for all quantile levels and all real parameters \(b>a>0\).

Finite second moments follow from the explicit exponential and double-exponential tails. The identity \(2\operatorname{Var}(Z)=\mathbb E(Z-Z')^2\) for independent copies transports strict pointwise contraction to variance. Doumas (arXiv:2603.11129v1, Eq. 15) provides the algebraic identification of the alternating-sum coefficient with that variance.

The packaged `CHECK.py` uses only standard Python. It tests the differentiable inequality on an interior grid and checks strict derivative ordering for several real parameters. These are sanity checks only, not a proof by numerical sampling. Neither a quantitative variance-decay rate nor general parent-distribution analog is verified. Independent audit has not been performed.
