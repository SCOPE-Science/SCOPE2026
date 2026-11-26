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

With time scaled by R/v, the bulk reversal and wall release rates are a/2 and (a+g)/2, not a and a+g. A uniformly positive probability of no bulk flip and release within one unit if needed gives absorption within five units and a geometric tail bound. The first two backward moment equations therefore apply, with outgoing absorption at the right endpoint and the independent exponential waiting-time identity at the left. In the coordinate y=x+1, with h=a+g, the difference of first moments is -2/h-2y and the sum is S-2ay/h-ay^2, S=4+4a+(2+4a)/h. Integrating the second difference with left value -2(S+2/h)/h and then the second sum from the right gives, after subtracting the squared mean, V=5a^2/2+16a/3+1+((14/3)a^2+8a+2)/h+3(a+1)^2/h^2, equivalent to the stated polynomial fraction. Independently, expanding the specialized prior boundary Laplace transform at zero gave the same two moments. Differentiation gives the stated quartic and its constant term 2[(2g+1)^3-10]. Below the zero of that constant the descending coefficient list has exactly one sign change, so there is one simple positive root and the variance decreases then increases. At or above the threshold all coefficients are nonnegative (the a coefficient is already positive at g=1/2 and increases), yielding strict increase for a>0 and the unique minimum at zero. The g=0 case uses a>0 only. The mean derivative gives the lower threshold. At the positive mean minimizer set t=a+g=sqrt(2(1-g)/3)>1/2; the variance derivative is -3t^2-(17/2)t-2+4/(3t^2), strictly negative since the equivalent numerator 18t^4+51t^3+12t^2-8 is increasing and positive at 1/2. Thus the variance root is to its right; above the mean threshold but below the variance threshold it remains positive while the mean optimizer is zero. At the variance threshold the a derivative of the quartic is positive and the g derivative of the constant is 12 times 10^(2/3), confirming the implicit-function coefficient and its sign. The frozen symbolic and sampled checker was read but not executed; those samples cannot prove global uniqueness.

## originality

PASS

The distinct result is the all-enhancements global variance optimization and its comparison with the mean, including the higher threshold and the continuous linear collapse of the interior optimizer. The model, law, mean threshold, and moments obtainable by differentiating the law are not credited as new. The strongest indexed overlap gives exactly the zero-enhancement slice but not the transition as enhancement varies.

## value

PASS

The models' mean and variance embody different practical objectives: optimizing average escape can prescribe zero bulk tumbling even though strictly positive tumbling gives a smaller variance. The exact nonempty enhancement interval, uniqueness of both choices, and persistence of their ordering resolve that distinction globally, rather than at chosen samples. This does not claim an improvement of all quantiles or a new first-passage law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
