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
# Reproducible verification

Run `python3 CHECK.py` in the directory containing the files. The checker requires only the standard Python library. Its current successful run reports exactly **35,409 finite assertions** covering the positive-contraction defect inequality, finite spectral-band estimates, square-zero numerical-radius sharpness, and near-norming diagonal examples.

The proof of the universal theorem is analytic. Critical nonfinite steps are the characterization of weak-null unit sequences by compact injective positive defects, double-tail compression formulas for the essential norm and numerical radius, and existence of a partial isometry from an infinite low spectral band to an infinite high band for noncompact injective defect. The code does not certify any of those infinite-dimensional steps.

The manuscript and checker cover positive norm-one contractions on separable infinite-dimensional complex Hilbert spaces. The title, precise ratio and the zero/half cases are consistent across files. The prior published compact-defect characterization is credited rather than claimed as original. Publication priority is assessed on available sources only. Independent audit has not been performed.
