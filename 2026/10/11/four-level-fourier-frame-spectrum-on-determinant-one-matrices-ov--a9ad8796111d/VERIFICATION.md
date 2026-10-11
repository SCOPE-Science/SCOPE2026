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

# Reproducibility and verification

The test program `check_sl2.py` uses Python 3 and NumPy; execute `python check_sl2.py` from the extracted package directory. It independently constructs \(\mathbb F_q\) using explicit irreducible-polynomial quotients for extension-field cases, enumerates all matrices of determinant one, assembles the complex Fourier Gram matrix, and compares the complete spectrum against the formulas in `RESULT.md`.

It checks the opposite-entry Kloosterman identities \(K_\epsilon K_\epsilon^*=q^2 I-(q+1)J\) for both signs, all predicted Gram entries, all constructed eigenspaces (including simple extremizers), and all eigenvalues with multiplicities. Fields tested: \(q\in\{2,3,4,5,7,8,9,11\}\). Last executed output:

`VERIFY_OK tested_fields=[2, 3, 5, 7, 11, 4, 8, 9] sampled_matrices=3090 Fourier_columns=172 all_Kloosterman_unitarity=PASS all_Gram_entries=PASS all_equality_spaces=PASS all_Gram_spectra=PASS max_error=2e-15`

The script checks finite fields only; it is **not** an exhaustive verification of the infinitely many prime powers. The written proof establishes the unbounded parameter range by additive-character orthogonality, exact block identities and elementary eigenvalue inequalities. NumPy floating-point comparisons have tolerance \(3\times10^{-10}\) for spectra and \(4\times10^{-11}\) for eigenvector residuals. This is an ordinary reproducibility check, not independent validation.
