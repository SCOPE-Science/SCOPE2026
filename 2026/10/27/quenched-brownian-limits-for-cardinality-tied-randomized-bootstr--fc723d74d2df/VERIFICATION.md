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

# Reproducibility and proof checks

Run `python verification.py` with a standard Python 3 installation, from the directory containing this file. `verification_output.txt` is the recorded output of that command. No external libraries, downloads, private data or other files are needed.

The script checks the parity formulation of Lucas's theorem and the formula for the number of odd binomial coefficients for all integers from zero to 512 (131,841 coefficient checks). It verifies the exact independent-Bernoulli expectation identity by enumerating environmental bits with heterogeneous rational success probabilities for 45 configurations. Finally it computes the conditional-mean squared norm using binomial probabilities and checks the analytic upper bound at five sample sizes. These calculations can catch indexing and parity errors.

The infinite quenched assertion is established analytically, not inferred from computation. The critical steps are: (i) the exact conditional-mean product; (ii) the rarity of bounded binary-popcount binomial values; (iii) the strong law for independent bounded Hilbert-valued centered random elements; and (iv) the conditional martingale functional central limit theorem. Nothing here is an independent proof audit, and no external validation was performed.
