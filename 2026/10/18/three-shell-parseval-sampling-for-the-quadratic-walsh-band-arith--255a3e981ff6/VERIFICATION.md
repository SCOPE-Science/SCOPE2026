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

# Verification of the three-shell quadratic Walsh sampling classification

The included `verify.py` was executed with a standard Python 3 interpreter; `verify_output.txt` records the actual successful program output. The checker uses integer arithmetic and exact rational fractions exclusively, without numerical tolerances or external libraries. It implements both pairwise candidate enumeration and the independent one-node discriminant algorithm proved exhaustive in the result. Both agree for every integer dimension from 4 through 250. For all 54 produced triples it verifies both cubic symmetric equations, positivity and normalization, four exact coordinate-sum moments, and zero expected Walsh characters of degrees 1 through 4.

The separate degree-two Walsh Gram calculation checks all 740 ordered basis pairs in dimensions 5 and 6 directly from exact layer Krawtchouk sums. The complete finite arithmetic scan of dimensions 4 through 64 is the executable exhaustive certificate for the first multi-orbit dimension 65, not a numerical guess. Formula checks cover 100 endpoint parameters, 66 symmetric parameters, 33 nonpolar-family parameters and twenty exact Pell iterations. The checker prints `VERIFY_OK` on success.

Infinite-dimensional implications are established symbolically by the moment-orthogonality and interpolation proof, integer discriminant completeness, positivity as exact squared-polynomial integrals, and Pell recurrence invariance. The code does not independently certify whether an older mathematical article establishes an equivalent theorem; originality is addressed separately in the scientific review. No independent external audit has been performed.
