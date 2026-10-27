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

# Verification

The graph cycle space is identified with path-constant coefficients satisfying one terminal conservation equation. Averaging coordinate-isometric projections reduces the global edge-ℓ1 norm minimization to an exact one-variable comparison of two column sums. Outside the interval \([0,1]\) the norm is no better; inside that interval the crossing or the endpoint yields the two exact branches. The canonical orthogonal projection is independently reconstructed as \(Z(Z^TZ)^{-1}Z^T\) using the explicit cycle basis. Its norm is evaluated from the full column sums.

Run `python projection_bundle_checker.py` using a Python standard-library installation to replay the 28 exact-rational checks: projected-column conservation, idempotence, exact predicted norms, basis-Gram reconstruction and finite competitor tests. This finite checker does not establish the infinite parameter theorem; see RESULT.md for the analytic proof.

The prior literature comparison is limited by unavailable full papers on generic hyperplane projection constants. The result has not received an independent mathematical audit.
