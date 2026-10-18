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

The coefficient extraction and semilinear Cartier formulas, the differential-equation proof, and the parameter-root argument are given in `RESULT.md`. The pure-Python script `verify.py` independently implements coefficient extraction by binomial sums and polynomial arithmetic modulo each tested prime. Running `python verify.py` checks \(p=5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71\), with assertions for the two coefficient factorizations, the nonzero smooth-boundary values, exact degree, and squarefreeness. These finite checks are corroborating reproducibility tests, not a substitute for the general proof.

The external full-text novelty comparison is necessarily bounded by indexing and access; no claim of exhaustive unpublished-work access or independent certification is made. The result classifies the geometric \(p\)-rank and \(a\)-number of smooth members only.
