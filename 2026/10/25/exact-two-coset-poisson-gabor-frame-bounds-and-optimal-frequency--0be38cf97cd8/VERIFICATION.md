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

Run `python verify.py` with Python 3 standard library; the observed completion marker is `CHECK_OK: exact Zak extremal fibers, numeric grid, direct sums, and balanced-lattice limit`. It verifies exact analytical fiber evaluations numerically, the claimed extrema on a finite mesh, separate long bilateral sums, and the balanced-lattice identity.

The proof in `RESULT.md`, not the finite sample, justifies uncountably many parameter choices, strict global extrema, and sharpness. The Fourier transform of the Poisson window, the Zak Parseval identity, positive cosine derivative, and strict frequency convexity are the decisive mathematical steps. No independent audit has been performed.
