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

For z=(w,s) in the doubled epigraph put H=s−|w|²/2. The vertical section through horizontal displacement a of the centered overlap has length 2H−|a|² for |a|<sqrt(2H). Radial integration yields precisely 2^(d/2+2)V_d H^((d+2)/2)/(d+2). Flattening the epigraph has Jacobian one and the gap at x+y is h+k+|u−v|²/2. Reintegrating the resulting horizontal kernel gives mass (d+2)/(4(h+k)). Minkowski and Young reduce the norm bound to Carleman on the positive half-line; its logarithmic Fourier multiplier pi/cosh(pi xi) has essential supremum pi and equals pi only on a null set. For sharpness, first dilate a normalized nonnegative horizontal bump at a fixed log plateau in height; its translated autocorrelations converge to one and are dominated by one, so the Rayleigh quotient tends to (d+2)/4 times the Carleman plateau quotient. Then widen the log plateau to attain the limit pi. The complex-input convolution inequality follows by domination and Tonelli, and Cauchy–Schwarz gives absolute existence of each convolution integral. Strictness for nonzero data follows from the strict Carleman norm bound. For d>=1 horizontal translations commute with the flattened operator and converge weakly to zero, so no compact subtractand reduces its norm. This independently verifies the constant, strict nonattainment, and the finite-rank obstruction.

## originality

PASS

The same convex-domain Hankel family and the classical Carleman norm are prior. The supported distinct claim is the sharp epigraph evaluation with nonattainment and essential norm, not the introduction of that Hankel family or of the half-line method. The inspected results do not imply this evaluation.

## value

PASS

The epigraph is a natural unbounded curved test domain for an existing weighted inequality. The exact all-dimensional best constant, absence of extremizers and the sharp compact-approximation obstruction answer quantitative questions that mere boundedness does not. There is a substantive reason to know the exact value and whether compact approximations can reduce the error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
