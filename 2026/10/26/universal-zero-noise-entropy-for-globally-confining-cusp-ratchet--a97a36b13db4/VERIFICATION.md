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
# Verification scope

The proof relies on a strict inward-drift Lyapunov estimate, a tight rescaled stationary-law argument, and an exact entropy--moment identity. All of these are stated and derived in `RESULT.md`; finite-volume computations are supplementary checks, not proofs of the small-noise limit.

The standalone `VERIFY.py` requires Python 3 with NumPy, SciPy and SymPy. Run `python VERIFY.py` from the directory containing that file. It verifies symbolic normalization/mean and entropy simplification, and tests finite-volume stationary solutions at decreasing diffusivities for a straight and a non-straight two-cusp potential. Numerical convergence alone does not certify the infinite statement. No formal third-party or independent audit was performed.
