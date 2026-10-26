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

# Verification of the inversion-limit theorem

The executable `checker.py` constructs every ordered binary-tree automorphism permutation at depths \(n=1,2,3,4\) directly from the wreath recursion and counts inversion pairs without using the claimed weighted-Bernoulli decomposition. It independently constructs the predicted generating polynomial, compares histograms exactly, checks the finite symmetry, mean, and variance, then validates the algebraic finite truncation identities for \(1\le n\le80\) in rational arithmetic. The program also checks representative instances of the Fourier-level inequalities numerically. The recorded exact outcomes are in `checker_output.txt`.

The observed successful execution reported **359 assertions**, including complete enumeration of \(32,768\) permutations on \(16\) leaves at depth four. To reproduce, run `python3 checker.py` using Python 3 standard-library modules only. A mismatch raises `AssertionError` and exits nonzero.

The checks do **not** establish the all-depth lowest-common-ancestor identity, interval support or differentiability on their own. Those conclusions follow from the separate combinatorial partition, deterministic tail, subsum lemma and characteristic-function Fourier argument in `RESULT.md`. No independently performed audit or human validation is asserted.
