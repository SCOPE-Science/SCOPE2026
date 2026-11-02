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

# Reproducibility and limits

`verify.py` is a standalone Python 3 program using NumPy and SciPy. Run `python verify.py` in the same directory. The actual output is embedded in `verification_output.txt`. In the completed check, 454 finite assertions passed. These include 400 exact-rational polynomial identities for neighboring Gamma survival polynomials and 54 numerical checks for six finite sample configurations.

The exact finite last-completer integral uses the density of the higher-quota group maximum times the lower-quota group CDF. The numerical checks compare it with the predicted asymptotic intensity split and compare exact Poissonized completion CDFs with the Gumbel CDF. They are evidence against simple sign, factor, or centering mistakes; they do not establish the infinite-sequence theorem. That theorem depends on the explicit analytic density-to-tail estimate, the Gamma CLT centering separation, uniform exponential local tails, the Poisson maximal inequality, and the rate-function scaling analysis presented in `RESULT.md`.

The code is not an exhaustive verification of all multiplicities or all asymptotic sequences. Independent mathematical audit has not been performed.
