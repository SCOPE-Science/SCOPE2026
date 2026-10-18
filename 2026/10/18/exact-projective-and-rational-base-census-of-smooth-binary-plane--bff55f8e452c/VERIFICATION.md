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

The reproducible mathematical claim is the full count, rational-base distribution and rational-projective orbit/stabilizer distribution of two-dimensional all-smooth subspaces of the binary ternary-quartic space.

* `pencils_main.cpp` performs degree-ten binary Macaulay-rank checks on all \(32{,}767\) forms; iterates all eligible pairs; computes the seven rational-point evaluations; generates all \(168\) projective transformations; checks representative element orders and the order-\(21\) normalizer. Execute with C++17 and compiler optimization from this directory. The output is `pencils_main.out`.
* `pencils_fourier.cpp` reads the generated `smooth_form_masks.txt` and verifies the complete rational-base distribution by exact Walsh transforms, subset incidence counts and binomial inversion. Its output is `pencils_fourier.out`; this independently checks the aggregation, not the rank-derived input list.
* `verify_groebner.py` reads the \(78\) masks in `smooth_representatives.txt` and verifies the affine Jacobian ideal is \((1)\) on three charts for each; it requires SymPy and produces `verify_groebner.out`. This checks smoothness of all positive projective orbit types, not every nonsmooth mask.

The programs were executed successfully and all printed totals agree. The mathematical proof of the Macaulay criterion, the finite-range coverage, the three-to-one pair multiplicity, the group-order weighting and the stabilizer-orbit equations are stated in `RESULT.md`. No reliance is placed on finite sampling as a proof of geometric smoothness. An external independent scientific audit has not been performed.
