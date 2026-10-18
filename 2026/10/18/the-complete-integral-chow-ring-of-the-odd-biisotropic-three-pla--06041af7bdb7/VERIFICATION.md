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

# Reproducible checks and boundaries

The standalone `verify.py` is written in standard-library Python 3. Running `python verify.py` computes all four exact Schubert pairing matrices both by coefficient extraction and by an independently coded 35-fixed-point rational localization sum. It asserts equality of each entry, degree 61, a unit low/high pairing, a determinant \(-1\) in codimensions two/four, and a determinant \(1\) in the middle. The executable produces a `VERIFY_OK` line only if every assertion succeeds.

The correctness proof relies additionally on the geometric input that the zero locus is smooth of dimension six and has an affine paving with ranks \((1,1,2,2,2,1,1)\), as established in the cited literature, and on unimodular integral Poincaré duality. Numerical checks cannot alone prove that algebraic Chow restriction is surjective or that no earlier stronger theorem was published. The argument in RESULT.md supplies these logical bridges; historical priority remains subject to independent review.
