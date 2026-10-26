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

# Mathematical verification

The standalone file `check.py` was executed in the delivered package directory with Python 3, SymPy, and SciPy. It reported successful third-order symbolic Taylor coefficient identities for the normalized cavity map, matching the exact quadratic and cubic coefficients used by the proof. It tested the root count and fixed-point slope predictions over nine active-period parameters and seven connectivity ratios, solved the positive-fold tangency equations at mean active period \(\tau=2\), and compared computed positive roots near the continuous and tricritical thresholds with their asymptotic amplitudes.

The numerical fold at \(\tau=2\) is \((z_{\mathrm s},q_{\mathrm s})\approx(1.9414370917955184,0.36615089428352876)\). The unique critical period and connectivity are \(\tau_{\mathrm c}\approx1.420049608669704\), \(z_{\mathrm c}\approx1.4701592197462061\). The tricritical plant-fraction amplitude is \(1.0573452291260566\).

The universal fixed-point count is established analytically from the strict monotonicity of the logarithmic-slope derivative, not from grid coverage; the script's finite grid merely stress-tests potential algebraic and branch-selection mistakes. Independent audit has not been performed. The result applies only to the specified mean-field cavity system and does not certify finite random graphs or ecological trajectories.
