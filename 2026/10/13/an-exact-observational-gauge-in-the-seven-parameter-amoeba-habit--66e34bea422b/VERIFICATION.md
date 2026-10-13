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
# Reproducibility
Run `python verification/verify.py` from the extracted package root. The script requires SymPy, NumPy, and SciPy.

The checker verifies exact symbolic identities for (i) both pressure ODEs under the affine state and generation-rate transformation, (ii) the pointwise pressure-gradient output and the six-combination observable normal form, (iii) the original and transformed stimulated/unstimulated equilibrium relations, (iv) the parameter-curve null tangent, and (v) a rational alternative to the authors' seed-308 parameter set, within Table S3 calibration bounds.

The code also integrates a representative nine-day piecewise-constant stimulus through exact constant-segment matrix exponentials as an implementation sanity test, with its output trajectories agreeing at reported floating-point tolerance. This finite check is not used to infer the all-input theorem. The general equivalence follows from the explicitly shown algebraic conjugacy.

The unobserved pressures themselves change; this is not an indistinguishability theorem for joint pressure and motion measurements. The six-combination representation gives an upper bound on separately identifiable combinations and is not a proof that all six combinations are identifiable.
