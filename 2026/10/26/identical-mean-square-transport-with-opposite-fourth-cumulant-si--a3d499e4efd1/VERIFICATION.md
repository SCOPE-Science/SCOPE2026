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

The source file `CHECK.py` is complete and standalone apart from `sympy` and `mpmath`. Invoke `python CHECK.py`. It passed **55** deterministic assertions when run from its packaged content, including the following mathematically distinct validations:

- Symbolic order-four expansion of the joint renewal equation, compared with the independently written moment formula.
- Independent high-precision numerical quadrature of the two mixed beta logarithm integrals, checked against \(\zeta(2)\) and \(\zeta(3)\) closed forms.
- Rigorous strict positivity certificate based on \(\pi>157/50\) and the first five terms of the defining \(\zeta(3)\) series.
- Root solving of the exact renewal transforms at three decreasing tilts for four mixture weights, with fourth-order coefficient extrapolation.
- An independent exact square-root exponent for the comonotone endpoint and direct checks of exponential moments.
- Direct stationary renewal calculation: two velocity observations have nonzero expected product only when they occur in the same run, giving \(v^2 e^{-|s|}/2\).

The root check is numerical and is explicitly supplementary to the proof. The large-time fourth-cumulant rate uses an analytic renewal theorem for nonarithmetic cycles with exponential moments and a simple leading singularity; its stated scope does not include arbitrary heavy-tailed intervals or finite-time signs. No independent audit or external certification has been performed.
