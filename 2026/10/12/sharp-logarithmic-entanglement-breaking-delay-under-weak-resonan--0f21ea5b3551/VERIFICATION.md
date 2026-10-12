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

# Verification and limits

The analytic derivation obtains the explicit Bloch matrix, its stationary vector and stationary determinant, and the near-zero-drive projectors of the two-dimensional Bloch block. For fixed \(s\), the reconstructed Choi partial transpose has Schur-complement limit \(\frac12\operatorname{diag}(1-e^{-s},1+e^{-s})\) after division by \(\Omega^4\). The strictly positive complementary block and the eigenvalue Schur equation give the same limit for the two small eigenvalues. The Peres–Horodecki qubit PPT criterion and semigroup composition then yield the entanglement-breaking threshold.

Run `python verify.py` in a directory containing the adjacent `requirements.txt` dependencies. The script uses independent matrix-unit superoperator exponentiation, directly assembles the normalized Choi matrix, computes reference-system partial transpose, compares six scaled eigenvalues to their analytic limits, numerically locates three finite-drive transition times, and checks the zero-drive negativity at four finite times. The reproduced output is:

```
VERIFY_OK weak_drive_scaled_PPT=6 first_EB_times=3 zero_drive=4
```

These finite checks corroborate the analytic computation and do not certify an asymptotic limit, publication priority, numerical tolerances outside the tested samples, or any independent review. The statement does not cover detuning, extra channels, or non-Markovian dynamics.
