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

Partial fractions give the difference of signed exponential Fourier transforms divided by b²−a². Poisson summation with the same positive Zak phase gives the common phase exp(i theta xi) and the difference of the two stated hyperbolic kernels. Taking the divided difference as b→a gives the stated i pi²/a prefactor times the lambda derivative. Away from sin(theta)=0 and xi=1/2, a zero requires simultaneous cancellation of both real coefficients. Their ratio has nonvanishing derivative of sign 1−2xi, excluding both equality at distinct poles and simultaneous derivative cancellation at a repeated pole. At xi=1/2 the common coefficient cosh(lambda/2)/(cosh(lambda)−cos(theta)) decreases with strictly negative derivative. On theta=0 and pi the respective sinh and cosh ratios have strictly signed lambda derivatives except at the stated interior zero, by strict increase of s coth(lambda s) and s tanh(lambda s). At xi=0 the kernel is 1+i sin(theta)/(cosh(lambda)−cos(theta)); cancellation leaves zeros exactly at theta=0 and pi. The defining series is C¹ in both variables by summable bounds on g', k g and g, so boundary derivatives can be taken from the interior. At (theta,xi)=(0,0),(pi,0),(0,1/2) respectively, the theta derivatives of the kernel are i/(cosh(lambda)−1), −i/(cosh(lambda)+1), and i cosh(lambda/2)/(cosh(lambda)−1); the xi derivatives are −lambda coth(lambda/2), −lambda tanh(lambda/2), and −lambda/sinh(lambda/2). Every displayed scalar factor has strictly signed derivative: for the last factors this follows from sinh x cosh x>x, positivity of tanh x+x sech² x, and x cosh x>sinh x, respectively. Taking differences or lambda derivatives therefore leaves two nonzero perpendicular derivatives at every zero. The nonzero common complex prefactor and theta=2 pi t preserve nonsingularity. The proof covers all positive parameters; the reported grid and numerical Jacobian checks are only corroborative and the frozen script was not executed.

## originality

PASS

Parity-forced locations, the two-fiber reduction for the fixed pair (1,2), and existing Zak formula and frame methods must be credited. The demonstrated distinct content is the complete classification with nonsingular real Jacobians for independent positive poles, including coincident poles. The closest inspected primary text and catalog entries do not imply that result in that parameter domain.

## value

PASS

For odd windows symmetry alone leaves open both extra zeros and tangential zeros. Resolving both questions for a natural two-pole family, including the repeated-pole degeneration, gives a useful exact invariant for analyses involving Zak zeros and local stability. Its relevance does not depend on claiming a complete Gabor frame-set theorem, which the result does not give.

The dated certificate retains the supplied scientific assessment, sources and limitations.
