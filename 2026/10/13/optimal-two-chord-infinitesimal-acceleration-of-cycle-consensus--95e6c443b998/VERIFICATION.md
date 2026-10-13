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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and NumPy. The script enumerates all 707,078 unordered chord pairs over network sizes 4 through 32. It performs the exact continuous split optimization analytically for each fixed pair, checks all three parity classes, and independently recomputes the projected Fourier matrix's smallest eigenvalue with a matrix eigensolver. Selected cycles are verified using 54 full-Laplacian eigenvalue computations, including direct small-budget comparisons and single-chord no-improvement checks. Small floating-point tolerances are specified in the code.

Observed output from the actual packaged checker:

`VERIFY_OK: exhaustive_pairs=707078 chord_edges=4930 full_laplacian_spectra=54 n=4..32 all_three_residue_cases`

The finite checks exercise the derived formulas, not an infinite proof. All-size validity and the asserted uniqueness of optimal length and weight patterns follow from the written analytical inequalities and equality cases. The small-budget estimate is asserted for fixed \(n\), with an \(n\)-dependent constant; no uniform-in-\(n\) finite-budget bound is claimed. Independent mathematical audit has not been performed.
