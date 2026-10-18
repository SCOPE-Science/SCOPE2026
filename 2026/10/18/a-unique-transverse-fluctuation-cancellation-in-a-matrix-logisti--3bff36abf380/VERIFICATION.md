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

The scientific proof is contained in `RESULT.md`, and the standalone consistency program is `verify.py` (Python 3 standard library, no third-party dependencies). Run `python3 verify.py` from the directory containing the packaged files.

A successful packaged execution printed:

`PASS: 4198 exact-rational or bounded floating-point consistency assertions`

The assertions check exact rational two-by-two matrix-coordinate identities on multiple parameters, the diagonal fixed-channel identity, the two special rational cosine-bracket identities, an explicit absolute tail bound for the variance series, and the finite-iterate trigonometric telescoping formula. The latter uses a numerical tolerance because it evaluates transcendental functions in floating-point arithmetic. The program is not an exhaustive test for arbitrary parameters or time, and it is not used as proof of uniqueness of the zero variance or of the infinite-time central limit theorem; those are derived analytically in `RESULT.md`.

Scientific limitations: the theorem concerns infinitesimal complex off-diagonal deviations along stationary diagonal trajectories with arcsine-distributed scalar starting point, not arbitrary full non-diagonal initial matrices. The Gaussian law uses the standard reverse-martingale central limit theorem after a proved \(L^2\) coboundary decomposition. All normalization conventions and exceptional null sets are defined in the result.
