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

# Reproducible checks and limits

With Python and the dependencies from `requirements.txt`, run `python verify_weighted_star_maximal.py` from the directory containing this file. The checker reconstructs the centered star ball averages and the weighted Hilbert form, rather than loading a previous calculation.

It performs exact rational tests at hub masses \(1/10\), \(1\), and \(100\): for every competing radius word on the three-vertex path, Sylvester's criterion verifies strict positive definiteness of \(LW-A^{\mathsf T}WA\) with the rational thresholds specified in `RESULT.md`. Each claimed winner has a rational input vector whose exact Rayleigh quotient exceeds the corresponding threshold, and the winner's characteristic polynomial is checked symbolically. A repeated radius word induced by swapping the two leaves is treated as the same mathematical selector type.

The script also compares the compressed spectral formula against the complete raw-selector enumeration on 25 combinations of leaf count and hub mass, checks 2520 random nonnegative inputs, and tests numerical convergence in the small-hub and large-hub regimes. These finite tests corroborate but do not prove the general exact spectral formula or the asymptotic assertions; those depend on the group-symmetry and perturbation arguments written in `RESULT.md`.

All results are self-reviewed; no independent mathematical audit has been performed. The record does not certify uniqueness relative to unpublished or inaccessible literature.
