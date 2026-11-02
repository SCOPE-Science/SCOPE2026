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

# Verification and reproducibility

To run the checks from the extracted directory, execute `python3 verification/verify_aitken.py`. The script uses Python's standard library and a fixed random seed. Its 32,008 assertions include thousands of exact rational evaluations of the original two noisy Picard steps, their Aitken denominator and numerator, and the parameterized tail constants. Additional independent quadrature tests reconstruct a supercritical tail by integrating conditional uniform intervals, test the critical corner tail from its exact triangle integral, and test the approaching logarithmic mean-square slope.

For \(\rho=1/2\), \(s=1\), the exact critical cutoff is \(\eta_c=1/10\), the critical tail coefficient is \(16/75\), and the precritical squared-risk logarithm coefficient is \(32/75\). For \(\eta=1/5\), the exact supercritical coefficient is \(403/1296\).

Only the analysis in `RESULT.md` proves the infinite tail limits, exact moment spectra and asymptotic rates. The verification script supplies finite reproducibility checks and does not provide independent review or a formal proof certificate. No claims are made for correlated errors, other error distributions, later repeated iterations or floating-point safeguarding.
