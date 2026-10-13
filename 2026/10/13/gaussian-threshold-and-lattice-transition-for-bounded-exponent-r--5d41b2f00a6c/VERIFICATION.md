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

# Verification

Execute `python3 verify.py` with a standard Python 3 interpreter. Recorded output is in `verify_output.txt`.

The script checks six inverse-zeta normal quantiles and the sign change at allowed prime exponent five, computes 18 exact finite Euler products over first primes, evaluates 18 Poisson cumulative probabilities directly from their point masses and compares them to the displayed first-order lattice expansion, and checks a small-mesh property of the logarithmic prime-power primorial sequence. All tests pass in the supplied replay.

The integer-prime support is finite and supplies numerical corroboration only. No amount of finite calculation proves Mertens' theorem, the prime number theorem, the central/local Poisson limit theorem, or the infinite sign assertions; the analytic proof in `RESULT.md` supplies these links. The estimates at the critical window use the classical effective Mertens estimate and first-order Stirling/Euler–Maclaurin analysis. No independent audit has been performed.
