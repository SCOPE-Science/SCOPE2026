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

# Reproducibility and limitations

Execute `python3 verify_mellin_defect.py` from the directory containing the extracted standalone script. It checks the harmonic/logarithmic matrix-entry identity against the rank-one decomposition for positive indices through 90; positivity and quadratic bounds for the lattice-error coefficients; diagonal and triangular compressions of four sizes; and, when NumPy is installed, eigenvalue-power-sum versus singular-value comparisons at exponents both below and above the proposed threshold. The finite checks are arithmetic and numerical only.

The proof of the infinite-dimensional statement does not use the numerical experiments. Its essential independent mathematical steps are: the telescoping identity \(H_n-H_{k-1}-\log(n/k)=1/n+\sum_{\ell=k}^{n-1}(1/\ell-\log(1+1/\ell))\); the bound \(0<a_\ell\le1/(2\ell^2)\) and \(\|u_\ell\|_2\|v_\ell\|_2\le1\); the \(p\)-triangle inequality in Schatten quasi-ideals for \(0<p\le1\); and finite-dimensional eigenvalue–singular-value majorization for arbitrary \(p>0\). The determinant is justified by trace-norm convergence of compressions.

No independent scientific audit, external reproduction, or publication-priority certification has been performed.
