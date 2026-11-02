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
# Reproducibility and verification

The self-contained source `verify.py` requires Python 3 with NumPy and SciPy. Execute `python verify.py` from the extracted package directory. It checks exact gamma constants for block widths 2, 3 and 4, evaluates the angular integral by numerical quadrature against an independently evaluated elliptic-integral expression for several spectral ratios, checks spectral homogeneity, and verifies the normalizing integral for the ordered singular values of a standard Gaussian 2-by-k matrix. A seeded 300,000-sample direct Gaussian simulation checks a finite-threshold implementation smoke test; its threshold is not used to infer the limiting exponent.

The mathematical limit, sharp constant and all-rank-two quantifiers are established by the proof in `RESULT.md`, not by numerical trials. Neither symbolic normalization nor simulation certifies against unexamined historical priority. No independent audit or validation has been performed.
