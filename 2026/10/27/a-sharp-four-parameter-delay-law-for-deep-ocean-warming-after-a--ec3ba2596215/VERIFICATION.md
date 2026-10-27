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

The full proof requires only differentiating the two-box impulse response and applying symmetric generalized-eigenvalue perturbation. It covers all strictly positive \(C_s,C_d,\lambda,\gamma,F_0,\tau\).

The attached `check_two_box.py` is a standalone Python 3 verification aid with no third-party packages. Execute `python3 check_two_box.py`. The actual test returned `CHECK_OK representative_peak=22.2543875592 delay=12.2543875592`. It includes exact rational polynomial checks and representative numerical peak, derivative and monotonicity tests. Only the written proof establishes global uniqueness or inequalities.

Independent audit and independent validation have not been performed. A source-comparison limitation is that the primary 2013 paper's appendix formulas were not fully accessible; the article's model and scenario descriptions, an author-hosted earlier climate paper, and a full later model-analysis article were materially inspected.
