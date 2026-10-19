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

Run `python verify.py` with Python 3 and no third-party packages. The program checks the cyclic \((7,3,1)\), \((13,4,1)\), and \((31,6,1)\) perfect difference sets, verifying every nonzero difference exactly once. It then evaluates all normalized Fourier ambiguity magnitudes for flat windows with nontrivial complex pointwise phases and compares them with the three exact spectral classes. For nonflat positive weights it checks every nonzero-shift coefficient, the variance bound and the strict conditioning loss.

For each of these three examples, it also checks the asymptotic sharpness sequence whose one distinguished probability is \(1-(k-1)\varepsilon\) and whose other probabilities are \(\varepsilon\). Finally, it constructs all \(49\) Gabor rank-one projectors in dimension \(7\), acts with the operator frame on each of the \(49\) Weyl matrices and compares all \(2401\) matrix entries to the predicted eigen-equations.

Observed output:

```
v=7 k=3 ambiguity_eigenvalues=49 difference_test=PASS variance=PASS
v=13 k=4 ambiguity_eigenvalues=169 difference_test=PASS variance=PASS
v=31 k=6 ambiguity_eigenvalues=961 difference_test=PASS variance=PASS
VERIFY_OK ambiguity_comparisons=2307 exact_difference_families=3 operator_entries=2401 eigen_equations=49
```

The checker uses floating-point complex arithmetic for root-of-unity sums, with an explicit tolerance. Its finite tests do not certify the general finite-abelian theorem. The unrestricted proof is the incidence, character-orthogonality, Hilbert--Schmidt diagonalization and probability-product argument in RESULT.md. No independent mathematical audit is asserted.
