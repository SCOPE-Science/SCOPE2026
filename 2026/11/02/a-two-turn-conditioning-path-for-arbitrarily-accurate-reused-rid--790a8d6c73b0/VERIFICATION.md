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

# Reproducibility and scientific limits

Run `python verify.py` in this directory with the dependencies listed in `requirements.txt`. The verifier uses symbolic identities in SymPy and independently constructs the actual augmented right-preconditioned matrix for NumPy singular-value calculations. The script checks that the derivative identity is exact; compares direct singular-value condition numbers with the explicit formula; tests root locations, local turn types, and embedding-distortion scaling; and prints a success message only if every assertion passes.

The script passed 154 independently constructed numeric matrix, derivative, and distortion comparisons together with the exact symbolic polynomial and determinant identities. The exact proof in `RESULT.md` establishes the universal parameter claims. Finite tests cannot establish all-positive-parameter uniqueness or the Gaussian positive-probability event, which follow instead from Descartes' rule and continuity/full support.

No independence, external validation, finite-precision stability theorem, or practical convergence speed guarantee is claimed.
