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

The analytic verification uses the derivative of the root-product formula, the discrete Fourier Parseval identity, rotational orthogonality of intermediate degrees, the gamma recurrence for circle means of \(1+z^n\), and holomorphic continuation in the exponent after moving the boundary-zero coordinates. The step at exponents \(0<r\le1\) is not obtained by integrating a formally divergent \(|1+z^n|^{r-2}\) weight.

For reproducibility, execute `python3 artifacts/check_hessian.py` from the directory containing this document. The program integrates the original moving-zero product in the actual circle variable and compares finite-angle ratios to the quadratic prediction. It checks several degrees and positive exponents including those below one. All observed ratios approach one, as required by the theorem. Quadrature is a diagnostic, not a proof of the all-degree or all-exponent statements.

Independent audit: not performed. No uniform quantitative neighborhood and no supremum-exponent formula are claimed.
