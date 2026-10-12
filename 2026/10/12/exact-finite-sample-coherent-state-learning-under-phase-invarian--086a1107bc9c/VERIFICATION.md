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

# Verification notes

The proof reconstructs the two state averages from their coherent-state Fock expansions, uses uniform-phase orthogonality and a binomial normalization, and computes the exact two-nonzero-eigenvalue trace norm in each fixed-total-number sector. The countable direct sum is trace class because both Poisson-mixture weights sum to one. The Gaussian specialization follows by direct exponential integration; the tail is bounded by a sum of two geometric tails. The local-energy asymptotic uses an explicitly summable geometric majorant and dominated convergence.

`verify.py` is a Python-standard-library-only independent block-matrix check. It constructs \(27\) matrices directly from photon-number amplitudes (three rational parameter choices, nine photon sectors each), checks rank-two trace invariants against exact rational values, tests two convergent Gaussian series and their certified tails, and performs one finite-\(n\) asymptotic corroboration. Its successful run is recorded only after executing the actual embedded file. The numerical checks do not prove the all-prior statement; the analytical proof does.

Limitations: the model assumes a common uniformly randomized optical phase, lossless collective access to the training and signal modes, and equal prior probabilities. No independent scientific audit or hardware realization of the sectorwise projectors is claimed.
