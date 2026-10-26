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

# Mathematical verification

The reduced-Hessian formula was independently recomputed using \(x=(A+kI)^{-1}(v+f)\) and \(u=v-kx\), so its linear-in-\(v\) control map is \(A(A+kI)^{-1}\). The spectral eigenvalue formula follows by orthogonal diagonalization. Differentiate the positive square root of each eigenvalue: its sign is that of \(\alpha kt-1\). The strict decrease/increase of the two endpoint ratios proves uniqueness of the global optimum. A trigonometric reparameterization establishes the sharp continuous-spectrum envelope, and the diagonal matrix with three stated eigenvalues attains it exactly; the two-eigenvalue matrix attains condition one.

Execute `python3 verify_feedback_shift.py` in the same directory as this document. The included `verification_output.txt` records seven analytical-formula comparisons, including the singular case, and 500 deterministic finite-spectrum tests with random seeds fixed in the script. All reported finite checks passed. They cannot independently certify universal correctness or originality and are not used as substitutes for the displayed analytic proof. Independent audit has not been performed.
