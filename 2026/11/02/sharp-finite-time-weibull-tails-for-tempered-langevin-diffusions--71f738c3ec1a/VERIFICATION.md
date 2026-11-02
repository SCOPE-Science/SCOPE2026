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

# Reproducibility and proof checkpoints

For an exact arithmetic cross-check, execute `python3 verification/check_radial_clock.py` from the package root. It prints `radial_clock_algebra: 603 exact rational assertions passed`; the result is recorded verbatim in `verification/check_radial_clock.out`. The script uses only the Python standard library and checks the radial-power cancellation, the drift bracket, the quadratic-variation exponent, and the sharp coefficient on a rational grid. It does not simulate the diffusion.

The nonstandard proof checkpoints are analytic, not numerical: (i) verify Itô's generator on \(\Phi(y)=\lVert y\rVert^a/(\sqrt2a)\), including the constant \(c_\pi\); (ii) verify the upper clock can be flattened on a compact region with derivative between zero and one, thereby controlling quadratic variation **globally**; (iii) verify that the Brownian lower-bound event forbids return to the compact ball and forces the clock level at the specified time without assuming independence of Brownian time change; (iv) verify the Brownian bridge lower probability has exponent \(-H^2/(2v_-s)\), using an overshoot of order \(\sqrt H\); (v) use positive compact-region reachability, then pass \(s\uparrow t\) and both variance margins to zero; (vi) apply the tail-integral identity for the exponential moment.

No classification is proved at the exact coefficient equality. No independent audit or computational certification of all possible target functions has occurred. The proof does not rely on unprovided files, archived logs, or a simulation-based extrapolation.
