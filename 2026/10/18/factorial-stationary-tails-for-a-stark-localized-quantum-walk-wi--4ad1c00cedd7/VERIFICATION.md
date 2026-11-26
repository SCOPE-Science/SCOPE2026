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

Conditioning on the last reset gives the stationary exponential-age mixture; the initial-state term decays exactly as e^(−rt) in trace norm on equal-trace differences. This proves existence and uniqueness among normal states and hence the unique limiting position law. In Fourier coordinates the time-integrated hopping phase along k−F(t−s) is (4h/F) sin(Ft/2) cos(k−Ft/2); its Bessel Fourier coefficients give the exact diagonal and evenness, for either sign of h or F. The Bessel remainder relative to the leading monomial is bounded uniformly on the fixed argument range by exp(A²/[4(n+1)])−1, with zeros handled by factoring out the monomial. Independently of the frozen product proof, letting a=r/|F|, the remaining age moment is 2a/(1−e^(−2πa)) times the integral of e^(−2au)sin^(2n)(u) on [0,π]. Laplace scaling u=π/2+v/√n gives e^(−πa)√(π/n), yielding exactly a√π/sinh(πa). The stated finite product also follows from the integration-by-parts ratio K_n/K_(n−1)=n(2n−1)/(2(n²+a²)). The parameter limit is at fixed h,F,r. The supplied code was inspected, not run: its finite Hamiltonians and pointwise quadratures would corroborate only their stated test cases.

## originality

PASS

The renewal principle and the unreset propagator are prior inputs. The exact position integral is also already implicit in the zero-frequency specialization of Dattagupta–Das–Gupta, as made explicit below; the frozen record does not claim the renewal integral as new. The distinct supported claim is the sharp fixed-field factorial tail with its rate-dependent prefactor.

## value

PASS

A qualitative localization bound, the exact renewal integral, or a logarithmic factorial estimate leaves the leading stationary mass undetermined. The result isolates a factorial rather than exponential profile, the n^(-1/2) integration factor, and the explicit dependence on reset rate through the weights of recurrent excursion maxima. It gives a useful benchmark for distinguishing static-field coherent transport with resets from field-free or driven reset laws without extrapolating to singular parameter limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
