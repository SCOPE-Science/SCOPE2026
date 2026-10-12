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

# Reproducibility and boundaries

The exact model is the \(N\)-site nearest-neighbor adjacency Hamiltonian with monitored site projectors \(P_r\) and fixed positive rates \(\gamma_r\). The proof of the full asymptotic-state identity is in `RESULT.md`; it is based on the sine spectrum, Hilbert–Schmidt dissipation, peripheral eigenoperator classification, and the absence of imaginary-axis Jordan chains. Its arithmetic Cesàro formula is evaluated by a finite Fourier sum, with no appeal to numerical extrapolation.

Install the declared Python packages from `requirements.txt`, then execute `python verify.py` in the directory containing both files. The verifier constructs the full complex Liouvillian using Kronecker products independently of the sine-based analytic formula, diagonalizes it, computes its zero-frequency projection and checks the predicted dark-mode imaginary spectrum. A successful direct replay prints:

```
VERIFY_OK monitor_sets=83 initial_sites=461 peripheral_eigenvalues=105
```

The checks cover every single monitored vertex and every pair of monitored vertices on each path of size \(2\le N\le7\), with strictly positive example rates, and every possible localized input on these paths. Numeric tolerance is \(2\times10^{-7}\), not an interval-arithmetic certificate. The finite experiments do not establish the infinite family of finite-size cases. The analytic argument does. No independent audit has been performed. The scope excludes vanishing rates and all non-path Hamiltonians.
