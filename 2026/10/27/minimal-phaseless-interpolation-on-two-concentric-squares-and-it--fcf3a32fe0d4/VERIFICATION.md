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

# Verification

Run `python3 check.py` with a Python environment containing SymPy. No datasets, network access, or additional files are required. The expected standard output is supplied as `check_output.txt`.

The program constructs the real Frobenius-orthonormal basis of \(\operatorname{Herm}_3\), evaluates the exact \(8\times9\) matrix with rows corresponding to the eight nearest nonzero Gaussian-integer positions, and verifies rank eight and the exact one-dimensional kernel \(\mathbb R\operatorname{diag}(2,-3,1)\). It compares exact algebraic Gram eigenvalues, including multiplicities, to the Fourier-block decomposition and checks direct point-evaluation intensities against lifting for 60 deterministic complex coefficient triples (480 exact point comparisons). It also checks the kernel generator's determinant and Frobenius/singular-value parameters used in the analytical rank-two stability bound.

The arbitrary-radius/orientation condition, the global eight-measurement lower bound and the uniform stability inequality are proved analytically in `RESULT.md`; the finite exact checker is corroboration, not an infinite-exhaustion argument. The factor in the stated global inequality is not claimed sharp. No independent scientific audit has been performed.
