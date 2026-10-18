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

# Computational verification

The standalone `verify_odd_sine_25.py` requires no nonstandard dependencies. It evaluates the odd-compressed Fourier matrix using primitive order-25 roots modulo 101 and 151, then exhaustively enumerates all relevant support pairs and performs exact modular Gaussian elimination. A full-rank specialized minor is a certificate of complex nonvanishing; explicit cyclic order-five sine waves certify the two remaining complex singularities.

For each finite field, the checked support-size pairs, test counts, and deficient pairs are respectively: (2,4): 32,670/0; (3,3): 48,400/0; (3,4): 108,900/0; (2,5): 52,272/2. Both characteristics give the same exceptional supports. The output file `verify_odd_sine_25_output.json` is the direct stdout of a successful run. The single-sign-pair case and Fourier inversion are proved separately in `RESULT.md`.

This is a finite exact proof at one group order, not an independent audit, an experimental assertion for other orders, or a general nonvanishing result for all sine minors.
