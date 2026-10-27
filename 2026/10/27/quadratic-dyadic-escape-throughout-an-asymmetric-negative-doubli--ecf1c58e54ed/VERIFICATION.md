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

# Verification of the finite-time escape law

The five source-to-destination transitions in `RESULT.md` are verified algebraically by intersecting the two affine branch images with the retained intervals. The proof derives exact cylinder measures and the all-horizon matrix row identity by induction.

The standalone stdlib verifier `verify.py` checks 15 exact-rational interior parameter pairs chosen throughout the open chamber and all integer horizons from \(0\) to \(16\), a total of 255 survivor-mass comparisons. It independently constructs exact finite-time survivor intervals via the two inverse branches, clips them to the retained set, checks each Markov image transition, and compares against both the polynomial and matrix path counts.

Recorded result: `VERIFY_OK chamber_pairs=15 horizons_per_pair=17 exact_mass_tests= 255`.

The finite horizon is a test, not a proof for all times. The infinity-time theorem is the separate analytical induction on the transition matrix, whose premises and image inequalities are detailed in `RESULT.md`. There has been no independent external validation.
