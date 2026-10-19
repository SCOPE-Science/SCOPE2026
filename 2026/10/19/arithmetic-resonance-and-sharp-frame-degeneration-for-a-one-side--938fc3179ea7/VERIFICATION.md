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

# Verification and scope

The analytic proof supplies the all-integer-dimension statements. In particular, the exact decimation normalization, collision equivalence, the last-row finite-difference identity, the absence of triple collisions, and the local inverse Vandermonde bound are independent of finite experimentation.

Run `python check_poisson_sampling.py` with Python 3 and NumPy. This script was executed and reported: `PASS: 197 independent finite comparisons of collision times, Vandermonde determinants, alias FFTs, and sharp asymptotic coefficients.` The test script uses finite cyclic FFTs for the alias identity and separate direct SVD comparisons for the frame constants. Its finite numerical checks do not certify any infinite quantifier, completeness of literature searches, or independent audit.

The frame is bounded below precisely off the displayed resonance times. At a resonance it is injective but not bounded below, a distinction that matters for uniqueness versus stable numerical inversion. The exact leading resonance coefficient is established only for two channels; for general channel count the proof gives two-sided quadratic comparability.
