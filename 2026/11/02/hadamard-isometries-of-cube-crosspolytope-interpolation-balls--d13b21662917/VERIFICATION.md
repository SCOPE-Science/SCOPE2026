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

# Reproducibility and limits
Run `python3 check.py` from the directory containing the six documentation files and the standalone script. A successful run reports the preservation of all eight unit-ball vertices in dimension two, all 24 in dimension four, and the four-pattern multiplicities for all \(56+560+4960\) triple supports in Sylvester orders \(8,16,32\).

The script uses floating-point arithmetic only to diagnose dimension-two irrational coordinates and the normalized higher-dimensional values. The dimension-four vertex membership is exact after verifying integral images. Its tests cover Sylvester examples only; the universal proof in `RESULT.md` uses elementary exact equalities from arbitrary Hadamard column orthogonality. No exhaustive census of Hadamard equivalence classes is claimed.

The lower bound on transform norm is certified analytically by \(x=e_i+e_j+e_k\). Bibliographic comparisons to the 2022 primary source concern the distinct Schur-multiplier quantity. No independent scientific audit has been performed.
