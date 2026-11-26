---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A vector in a simplex factor has unique barycentric increments b_j summing to zero. Membership in t(Δ−Δ) is equivalent to Σ(b_j)_+≤t by taking the positive and negative parts and filling both with the same nonnegative mass. The overlap constraints are z_j≥max(0,b_j), Σz_j=1, hence the overlap volume fraction is (1−Σ(b_j)_+)^d (zero at tangency). The two signs of the translation give the same volume. Uniform product measure and convexity now give the directional survival product, or equivalently the minimum of independent scaled Beta(1,d_i) variables, omitting zero blocks. The difference-body gauge is the maximum factor gauge a, so after multiplying the exit time by a, at least one normalized gauge is 1. On 0<t<1 each survival factor is at least (1−t)^{d_i}; a maximal-gauge factor bounds the product above by (1−t)^δ. In each case non-equality gives strict inequality throughout that interval: the lower equality requires every normalized gauge to be 1; the upper equality requires one active factor of dimension δ. The polynomial survival on [0,1] has bounded density with no endpoint atoms, giving integrable logs and finite moments for p>−1. Strict stochastic order therefore gives strict power-mean order, including p<0 where the sign is reversed twice, and strict logarithmic-mean order at p=0. Beta integration and the derivative at zero give the stated constants. Both contact types exist for every fixed product. For the ratio, log(1+p/j)/p=∫_0^1 (j+pv)^(−1) dv, continuous at p=0 and strictly decreasing in p. At −1 the sum over j>δ telescopes to log(D/δ), and at positive infinity it tends to zero. With D=2N and δ=N the sum is a Riemann sum for (1/λ)∫_1^2 log(1+λ/t)dt if p_N/N→λ>0; the uniform expansion for p_N=o(N) and the bound (N/p_N)log(1+p_N/N) for p_N/N→∞ give the other limits, including p_N=0 or negative on the small-parameter side. This verifies the contact and limit claims with the intrinsic gauge, not Euclidean radii.

## originality

PASS

The supported distinct claim is the sharp two-sided, fixed-product comparison with all gauge contacts beyond parallelotopes and the balanced high-dimensional crossover. The general lower inclusion is covered by prior work and is not credited as new. The one-simplex computation and product factorization make the exit law a direct consequence, and the segment-product law and its envelope are covered. The checked results do not provide the mixed-dimensional sharp upper bound with the simultaneous equality classification and limiting profile. This is a best-of-knowledge assessment with unresolved older full-text access.

## value

PASS

This answers the geometric problem of how much the intrinsic radial-mean radius varies with direction for a fixed product rather than bounding it uniformly over an unrelated class. The worst and best directions behave differently: synchronization across every factor gives the inner contact, while complete concentration in a smallest-dimensional factor gives the outer contact. That sharp dichotomy and the complete crossover at p of order N show how dimension and exponent compete in anisotropy even when the shapes of the simplices vary. The value is in the joint sharp classification and asymptotic regime, not the already covered lower inclusion or factorization as a standalone formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
