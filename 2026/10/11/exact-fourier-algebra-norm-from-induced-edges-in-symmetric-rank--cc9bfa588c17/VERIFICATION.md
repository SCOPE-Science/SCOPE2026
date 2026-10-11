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
The proof was checked from the normalized convolution definition through the finite-group Fourier block decomposition. The critical points are: the rank-three permutation representation is multiplicity-free with exactly two nontrivial irreducible constituents; each has a one-dimensional point-stabilizer fixed space; the relevant Fourier block is therefore rank one; and the squared norm of its spherical-vector sum is the corresponding strongly regular spectral-projector quadratic form.

The included `verify.py` independently constructs the actual convolution matrix for the rank-three action of \(S_4\) on the six two-element subsets. It exhausts all \(64\) subsets \(J\), verifies the complete nonzero spectrum of the convolution Gram matrix using exact rational Gaussian elimination, and checks the resulting nuclear norm against the theorem. Expected replay output:

`VERIFY_OK exact_convolution_cases=64 max_numeric_error=2.220e-16`

The numerical comparison appears only after the exact eigenspace-multiplicity checks. The finite replay is corroborative and is not used to infer the universal theorem. No claim is made for nonsymmetric rank-three actions or for higher-rank permutation actions.
