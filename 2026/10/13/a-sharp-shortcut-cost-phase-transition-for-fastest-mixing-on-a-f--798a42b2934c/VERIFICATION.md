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
# Verification scope

The complete universal proof is in `RESULT.md`. Its decisive checks are two budget-exact Rayleigh certificates, the eigenvector identities at the proposed optima, and complete equality-case analyses. The finite verification program is a reproducibility cross-check rather than an independent certification of the theorem for all real parameters.

Run with Python 3 from this directory:

```sh
python3 proof_check.py
```

Expected stdout:

```text
VERIFY_OK: 12 interior/endpoint parameter certificates, 41 transition points, 5 exterior budgets
```

The checker uses the Python standard library only (`fractions`, `itertools`). It reconstructs the weighted Laplacian from all four candidate rates and checks budget feasibility, eigenvectors, dual Rayleigh coefficients, and spectral separation at twelve rational values of \(h=\sqrt t\) in the range \(0<h\le3\). At the critical cost it checks forty-one rational points on the claimed optimal line segment. For five exterior rational costs it checks the optimal spanning-path weights. For every constructed matrix, it computes \(\det(zI-L)\) at five distinct rational values of \(z\), matching the predicted monic degree-four characteristic polynomial identically **for that constructed matrix**.

The program does not enumerate every feasible real rate allocation, certify external publication priority, or perform an independent audit. The global bounds and the complete uniqueness/nonuniqueness classification are mathematical consequences of the exact variational proof, not of the numerical test set. No stochastic Monte Carlo measurements or floating-point eigenvalues are required.
