---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At fixed positive a,b and velocity separation V, put K=kV. The real dispersion function has one crossing outside each pole and a single minimum (a^(1/3)+b^(1/3))³/K² between them. Its quartic has just one simple root in the upper half-plane for 0<K<(a^(1/3)+b^(1/3))^(3/2), and growth vanishes at both endpoints by root continuity. Thus an interior maximum exists. Implicit differentiation at w=(z−K)/z gives z′=b/(aw³+b), so an extremum lies on the π/3 or 2π/3 ray. The first gives negative K² for all positive feasible ratios (the zero imaginary-equation denominator at r=1/2 cannot solve that equation); the second gives the claimed K and gamma. The ratio r³(r+2)/(2r+1) increases strictly from zero to infinity, so there is exactly one stationary candidate and hence precisely one peak. The sharp bound also follows independently from Re[(x+iy)^(-2)]≤1/(8y²) for y>0, with equality iff x²=3y². Equality for both streams forces x=K/2 and imaginary cancellation then forces a=b; the balanced solution attains the bound. A separate quartic optimizer spanning b/a=10^-4 to 10^4 corroborated the peak, without running the uploaded checker.

## originality

PASS

The matching forward dispersion and several special-case peaks are classical. The inspected arbitrary-density treatment uses asymptotic or numerical results in the relevant passages; it does not establish the exact all-positive-ratio optimizing wavenumber and growth or their global uniqueness. The nearby indexed three-population result does not cover this two-population optimization. Credit is for the explicit global optimization for fixed a,b and the sharp fixed-total-weight statement, not for the dispersion, instability mechanism, or familiar balanced and dilute limits.

## value

PASS

The all-ratio formula locates the one actual temporal optimum, rather than giving a cutoff, a root-finding prescription at a specified wavelength, or two asymptotic limits. A researcher can predict the peak and compare unequal weight allocations at fixed total weight without a numerical optimization. The sharp bound and its equality condition give a useful benchmark within the ideal model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
