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

# Reproducible algebraic checks

Run `python3 CHECK.py` with Python 3 and no third-party dependencies. Actual execution reproduced:

`VERIFY_OK moduli=29 weighted_endpoints=PASS CRT_multiplicities=PASS direct_Gram_Fourier=PASS flat_optimum=PASS`

The code exhaustively enumerates projective direction classes on each grid with sizes from 2 to 30, computes weighted Fourier incidences and reduction fibers, compares the explicit normal spectrum with independent Fourier-block products, and checks the small-grid direct Gram action. These finite computations cannot certify the infinite family, which is proved using Fourier orthogonality and the Chinese remainder theorem in `RESULT.md`. The checks do not independently establish historical priority or compare inaccessible primary full texts. Independent validation has not been performed.
