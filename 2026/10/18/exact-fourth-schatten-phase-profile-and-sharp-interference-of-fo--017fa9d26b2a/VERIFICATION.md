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

Run `python CHECKER.py` with Python 3 and NumPy available. The deterministic checker constructs complex four-layer nilpotent matrices in four different block-size profiles. It checks that the exact traced fourth power matches the one-harmonic formula for each matrix at five weights and four angles; it verifies the sharp trace upper bound, explicit four-site equality at four positive weights, and angle-flatness in a cube-zero example. The checker passed `FOURTH_NILPOTENT_PHASE_PROFILE_OK 4805` in the packaged source folder. The critical analytic steps are written in `RESULT.md`, including the all-dimensional kernel-filtration proof and exact equality classification. At the endpoint weights t=0 and t=1, every eligible operator yields equality of zero oscillation and zero upper bound; the nontrivial extremizer classification holds only for 0<t<1. The 4,805 finite assertions are diagnostics, not a proof for all Hilbert spaces or parameters.

Independent mathematical audit has not been performed.
