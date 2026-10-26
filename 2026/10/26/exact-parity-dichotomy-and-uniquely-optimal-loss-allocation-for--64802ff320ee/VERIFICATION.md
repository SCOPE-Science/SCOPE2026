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
# Reproduction and limits

Run `python checker.py` using Python 3 and NumPy. It assembles and solves the discrete matching equations independently of the closed scattering amplitudes, compares reflection and transmission at 500 pseudorandom momenta, separations and loss magnitudes, verifies the absorption formula by flux balance, probes 180 fixed budgets against sampled allocations, tests the phase effect, and verifies small- and large-budget behavior. The random seed is fixed in the code. All tests must pass with the printed PASS line.

The following exact algebra is the infinite-parameter proof and is not merely inferred from samples: the band-centre scattering denominator is \(1+b+2x(b-x)\), the reflection numerator is \(b-2(b+1)x+2x^2\), and the derivative polynomial after \(z=x/(b-x)\) has negative quartic/cubic/quadratic coefficients, a potentially signed linear coefficient, and a strictly positive constant. It therefore has exactly one positive zero, giving the global optimum. The implicit asymptotic expansion follows from the same polynomial. Independent scholarly publication and independent audit have not been performed. Numerical checks alone do not establish priority, noisy-data robustness or validity outside the stated model.
