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

The theorem is an analytic statement for every fixed real \(\kappa>5\) and is established by the prime-power Taylor expansion, comparison against every competing exponent, and a mean-value theorem for two intersecting singleton windows. It does not depend on a finite computer census.

Run `python verify_singleton_windows.py` with a standard Python interpreter. The script evaluates prime-power factors as exact rational numbers before converting to 85-digit decimal logarithms. It checks that the half-open singleton window is nonempty for several \(\kappa\) and \(p\), compares exponent one with exponents zero through thirteen at the midpoint, and verifies that the strict local upper bound excludes all later exponents. It also tests the negative singleton-width comparison for lower integer parameters at all primes below 2000.

Observed trials: 15 positive-window cases for \(\kappa\in\{6,10,16,20,100\}\) and \(p\in\{101,1009,10007\}\); finite lower-parameter checks at 303 primes below 2000 for each \(\kappa\in\{2,3,4,5\}\). The rescaled width approaches \((\kappa-5)/12\) in the positive cases. These are approximate checks of finitely many numerical cases; they do not constitute an infinite proof, an error-certified interval computation, or independent mathematical validation.

Main proof limits: no uniformity for growing \(\kappa\), no explicit bound for exceptional small primes, and no exclusion of previously unknown literature coverage.
