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

## Executed checks
Running the standalone `check_w1.py` under Python 3 completes 4,704 finite assertions. Rational checks integrate absolute differences of piecewise-affine distribution functions and compare them to the claimed coefficients for integer parameters; noninteger checks compare independent finite differences with analytic local slopes. The same computation also checks reflection symmetry of the slope.

## Proof dependency and limits
For the continuum claim the decisive facts are the CDF derivative identity, \(C_p=\sup_x\ell_p(x)\), the endpoint blow-up for \(0<p<1\), the sign partition for \(p>1\), and the positivity of the derivative numerator for \(R_p\). All are in RESULT.md; no external computation or full-paper dependency is required. Sampling is not an infinite verification. No independent audit or external certification has been performed.
