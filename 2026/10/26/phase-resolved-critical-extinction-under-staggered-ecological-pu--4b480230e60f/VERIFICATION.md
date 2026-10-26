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

# Reproduction and proof checks

Run `python verify_pulse_critical.py` with Python 3.9 or newer; it requires only the standard library. The program returns four PASS lines and reports analytic and numerical critical amplitudes for coincident and staggered pulses. The program was run successfully using its packaged code.

The proof's checkable analytical dependency chain is: the periodic multiplier \(\Phi\) is normalized by the exact per-period critical relation; the ratio \(R=x/y^q\) divided by \(\Phi\) has no pulse jumps and has reciprocal derivative \(\kappa\Phi y^q\); boundedness and resident viability force the reciprocal integral to diverge; scalar comparison makes \(y\) converge to the unique positive pulsed resident cycle; the periodic Cesàro average yields the exact inverse-time coefficient.

The verification code independently computes the resident fixed point through reciprocal logistic dynamics, checks the integral identity along numerical solutions, and checks the predicted phase effect with fixed-step Runge–Kutta integration over 3,000 periods. Numerical tolerances are finite and do not certify a universal asymptotic statement; the latter is justified by the written proof. No independent external audit has been performed.
