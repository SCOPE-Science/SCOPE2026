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

Run `python3 artifacts/verify_modular_rook_laplacian.py` with Python 3.10 or newer; only the standard library is required. It independently constructs literal degree-minus-adjacency Laplacian columns and a row/column aggregate update, verifies their agreement on every basis state, and performs finite-field Gaussian elimination. It then checks first-four-power ranks for 147 cases across three odd primes, fixed-space dimensions of 136 independent iterates, and compares the complete eventual period and entry-depth histograms of 30,080 explicitly enumerated labelled initial configurations. The expected final line is `MODULAR_LAPLACIAN_VERIFY_OK`, and the bundled `artifacts/verification_output.txt` contains the recorded output.

The verification code checks finitely many parameter values; it is not an exhaustive check of the infinite family. The full proof for all odd primes and all dimensions is algebraic, using the displayed tensor operator identity, Jordan-block ranks, and finite-field direct-sum decomposition. A separate independent audit has not been performed.
