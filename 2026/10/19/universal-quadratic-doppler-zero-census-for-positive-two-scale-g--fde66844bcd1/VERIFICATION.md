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

# Verification

The proof in `RESULT.md` supplies exact Gaussian integration, a positive-envelope factorization, uniform inner/outer wedge bounds, strict convexity of negative interference lobes, and the resulting \(O(1)\)-accurate positive-frequency root count for every fixed \(0<a<b\), \(c>0\). The analytic argument, rather than numerical sampling, is the justification for the unbounded delay regime.

## Reproducible finite checks

Run `python check.py` with the dependencies in `requirements.txt`. The script independently integrates the original defining autocorrelation integral with 55-digit arithmetic for five parameter choices and compares it to the closed formula; all scaled relative discrepancies were below \(2\cdot10^{-55}\). It also counts the candidate real zeros of the normalized cosine-envelope function in its negative lobes for five sets of parameters and three delays each. Across fifteen tests the difference between the numerical zero count and the main quadratic term had absolute value less than three. The exact log is `check_output.txt`.

The checker is a finite consistency test and not an exhaustive or independently certified proof. It assumes the large-delay lobe-convexity mechanism in its candidate enumeration; the paper proves that mechanism without numerical data. Human independent mathematical audit: not performed.
