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

# Verification and limits

The source `verify.py` runs without third-party dependencies using Python standard-library exact rational fractions. Execute from the directory containing the embedded files with `python verify.py`. The execution observed during this review returned:

`VERIFY_OK finite_functionals=242 exact_face_distances=14772 sharp_ratio_witnesses=230 infinite_case_requires_proof=True`

In each tested finite atomic model, the enumerated unit masses and nonnegative face masses have denominator four. Direct minimization over the face grid equals the analytic face-distance formula. The derived upper bound is checked for every enumerated vector, and a maximal complementary coordinate achieves the predicted sharp ratio. The tests also cover signs, zero values, and multiple maximizing atoms.

The general theorem for arbitrary probability spaces is analytic: see RESULT.md, Proof steps 1–4. Finite enumeration does not establish the claims for infinitely many atoms, nonatomic measures or essential suprema that are not maxima. A norm-attaining functional without an essential gap has an explicit strong-orthogonality obstruction; this requires the full measure-theoretic proof and is not a statement of numerical infeasibility.
