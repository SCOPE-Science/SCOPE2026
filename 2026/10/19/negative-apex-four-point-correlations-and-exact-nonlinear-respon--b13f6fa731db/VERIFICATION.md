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

# Verification record

The exact theorem follows by conditioning on the two independent Ising leg chains at the compensated rung coupling, deriving their ordered even-spin moments, calculating all repeated-index fourth cumulants, and taking absolutely convergent geometric series. The denominator is positive for \(0<\rho<1\); the numerator polynomial \(3+2\rho-3\rho^2\) is positive.

The self-contained `verify.py` uses Python 3, `mpmath`, and `sympy`. Executed with the delivered source code, it reported 38 passed tests: 12 comparisons of finite-periodic fourth-cumulant densities to the thermodynamic formula, 24 direct independent enumerations of distinct apex-spin connected fourth cumulants, and 2 exact symbolic geometric-series identities. The finite systems have periodic sizes 30 and 60 for the tested couplings. They do not exhaust all parameter values, nor establish the asymptotic limit without the mathematical argument.

Checks and scientific limits are restricted to this result. The self-review is passed; independent audit is not performed. No physical experiment, finite-sample statistical inference, or broader class of ladder interactions is certified.
