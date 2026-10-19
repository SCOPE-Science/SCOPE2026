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

# Verification details

The finite-state partition and all edge relations are explicitly constructed in RESULT.md using rational endpoints. Run `python3 verify_markov.py` with a standard Python 3 installation. It verifies rational interval images and the quotient adjacency matrices for integer parameters \(1\le m\le12\), exact quotient characteristic polynomials for \(1\le m\le7\), exact full transition characteristic polynomials for \(1\le m\le4\), and numerical roots for \(1\le m\le24\). The observed output was `VERIFY_OK`. This is a finite consistency test, not an independent audit or proof of the universal quantification.

The all-parameter proof uses the explicit partition relations, a nonnegative Perron eigenvector, the constant slope, and an exact root identity. No external downloads, input data, or machine-specific files are required for verification. Independent validation has not been performed.
