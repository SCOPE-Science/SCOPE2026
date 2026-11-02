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

# Verification of the two-fluctuator lineshape criterion

The analytic argument and exact assumptions are in `RESULT.md`. Install Python 3 and NumPy and run `python3 check_spectrum.py` in the same directory. The checker independently constructs a four-state Markov generator for the two telegraph variables, solves its complex resolvent at 390 parameter/detuning combinations and compares against the closed formula. It additionally checks the exact polynomial derivative-factorization and samples the two- versus zero-positive-root regimes of the controlling cubic.

An executed check gave a maximum normalized formula discrepancy of approximately \(1.0620\times10^{-15}\); all assertions passed. The symbolic polynomial proof, rather than finite numerical sampling, establishes the quantifiers for every positive pair of switching rate and coupling strength. No claim is made for nonsymmetric or dependent fluctuations, non-Poisson residence times, extra linewidth, or zero switching rate. Independent audit has not been performed.
