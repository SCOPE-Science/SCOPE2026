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

The proof in `RESULT.md` uses Bolotin--Zaporozhets's established independent-copy identity together with the standard Gaussian absolute determinant formula and analytic singularity transfer. The two correction formulas can be reconstructed from the expansion of \(\operatorname{Li}_{1/2}(z)\) and the digamma integral estimate. The proof of the asymptotic for every fixed \(p,q\) does not depend on computation.

Run the bundled pure-Python program from the package directory as `python3 verify_budget.py`. Its completed run printed `VERIFICATION_OK`. Direct enumeration independently cross-checked 34 small composition sums against the convolution recurrence; 24 maximizations compared the exact finite-sum objective with the two-term prediction; and four comparisons checked the first asymptotic correction in the generating-series coefficients. These are numerical calculations using floating-point arithmetic. They are neither an exhaustive test of the infinite theorem nor an independent audit. Their finite maximum numerical discrepancies are governed by the stated tolerance assertions in the source code.

All numerical examples use the standard Gaussian normalization; \(\zeta(1/2)\) is supplied numerically only inside the verifier. The publication-priority comparison rests on the inspected source articles and searchable mathematical records, not on an external independence certificate. The first public source date is the arXiv initial submission date, October 7, 2026; later revisions do not determine the scope date.
