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

The analytic proof in `RESULT.md` establishes the universal statement. The standalone checker `verify.py` is supplementary and does not certify an infinite inequality by enumeration.

## Executed checks

`python verify.py` was executed with `mpmath` at 55 decimal digits. The output reported `VERIFY_OK`, 144 dimension/sample cases, and maximum absolute discrepancy \(4.1761949\cdot10^{-53}\) between independently integrated original and beta-expectation expressions. All tested normalized deficits were strictly increasing, started at the exact simplex value, and lay below the predicted limiting constant. Pointwise convexity diagnostics at 99 interior arguments passed.

## Proof-critical identities

The published facet integral is transformed by the beta identity \(\binom nd B(d,n-d+1)=1/d\). The exact second beta moment produces the scaling \((n+1)(n+2)/(d(d+1))\). Strict kernel decrease is established analytically by convexity and secant slopes. The beta-tilted distributions strictly decrease in stochastic order with increasing sample size. No extrapolation from finite computations is used to establish these facts.

## Limits

The package contains no independently performed audit. Numerical quadrature and finite samples are diagnostic only. No assertion is made for alternate distributions or regimes in which dimension and sample size diverge jointly.
