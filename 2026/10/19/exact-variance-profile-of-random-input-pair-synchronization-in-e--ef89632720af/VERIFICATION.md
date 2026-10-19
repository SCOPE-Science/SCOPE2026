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
# Reproducibility of the exact variance theorem

Run `python3 verify.py` with standard-library Python 3. The checker constructs the complete transient Markov matrix for each unordered pair and each alphabet letter, solves the mean and raw-second-moment equations using exact rational Gaussian elimination for every pair in states of size three through eight, and compares the resulting variance against the closed formula. This reconstruction does not use the formula in matrix construction.

It additionally checks the symbolic boundary-recurrence polynomial residuals on an eight-by-eight grid of integers. Since both residuals have degree no more than six in each of the two symbolic variables, the Cartesian-grid vanishing proves the polynomial identities. The mathematical proof separately explains why the boundary equations characterize all sizes and why finite moments exist.

Expected output: `VERIFY_OK polynomial_grid_8x8 exact_pair_markov_moments n=3..8 states=83`.

Limitations: neither finite matrix tests nor this code independently verifies historical priority or replaces a scientific audit. The theorem is only about the fair-letter two-state merger time, not the whole-automaton reset time.
