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

# Reproducibility

The included `verify.py` is a standalone support program requiring NumPy, SciPy, and SymPy. Execute with `python3 verify.py` from the directory containing the file. Successful execution prints a PASS summary. The actual packaged program was executed successfully prior to review, covering symbolic Feynman–Kac and moment identities, three Laplace-time renewal comparisons, finite covariance integrations, monotonicity checks, and a mobility-only Monte Carlo of the characteristic function. Its controlled comparison gave \(0.67599544\) (independent renewal quadrature) versus \(0.67686311\) (conditional Monte Carlo) for \(\alpha=1.3\), \(\Lambda=0.7\), \(t=2\), and wave-number \(0.6\). The Monte Carlo sampling is finite, approximate, and randomly seeded; it is not an analytic proof.

The mathematical claims require invariant mobility initialization, independent Brownian drivers, a common mobility across components, and a deterministic reset to mobility zero. The proof in `RESULT.md` independently establishes the stationary moments and covariance, the strict derivative sign and invertibility, the squared-increment law, the renewal-kernel Feynman–Kac representation, and the weak Gaussian limit. Previous generic non-Gaussian and partial-reset formulas are acknowledged rather than claimed as novel.

Independent audit: not performed. Publication priority beyond the inspected literature is not certified.
