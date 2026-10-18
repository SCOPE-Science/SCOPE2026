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

# Verification summary

The exact SLEM and holding formulas follow from the analytic Fourier/symmetrization proof in `RESULT.md`. The companion `verify.py` is a stand-alone finite diagnostic requiring only the Python standard library. Run it from the extracted files with `python verify.py`.

The script was executed on the actual staged scientific code and printed `verification_pass: 2993 assertions`. It checks sixteen distinct multi-cycle families by enumerating every Fourier mode, evaluates four rational spectral boundary instances, tests the odd-factor threshold for 99 odd orders, compares many feasible direction probability choices to the claimed optimum, and checks elongated asymptotics against common-edge constraints. These finite checks do not independently prove the theorem for all dimensions or cycle sizes.

The main remaining scientific risk is an unlocated pre-existing closed-form result for non-edge-transitive Cartesian products. Only self-review has been performed; independent mathematical audit has not been performed.
