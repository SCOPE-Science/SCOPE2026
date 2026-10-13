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

# Verification instructions

Run `python verify.py` using Python 3.10+ and no external packages. The verifier checks 7,650 exactly weighted finite sampling paths over 15 rational parameter combinations; it reconstructs actual orthogonal projections rather than invoking the claimed recurrence as input. It also tests the spectral gap and the algebraic squared-difference identity on 19,900 grid points. A further long-product comparison tests the Perron limit in one nontrivial configuration. The expected marker is `VERIFY_OK exact_enumerated_paths=7650 spectral_grid=19900 sharp_supremum=1/8`.

These are finite reproducibility checks. The infinite-horizon limiting statement, the signs for all admissible parameters and the unattained supremum are justified by the proof in `RESULT.md`, not by empirical enumeration. The comparison with earlier literature is a self-review, not independent auditing or a claim of exhaustive bibliographic uniqueness.
