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

The theorem is proved analytically in `RESULT.md`. Its crucial conditional moment follows by conditioning on the minimum and maximum and averaging independent uniform interior observations; the range has a beta law. The covariance and correlation follow from three beta moments and the elementary degenerate-pair decomposition of the Cramér–von Mises statistic.

Run `python3 verify.py` using Python 3 and its standard library. The executable computes exact Dirichlet-simplex moments, independently of the conditioning proof, to test \(\mathbb EW\), \(\operatorname{Cov}(R,W)\), and \(\operatorname{Var}(W)\), at each sample size from 2 through 7. It separately checks conditional moments at four rational endpoint pairs per size. The observed output is `PASS: 48 independent exact-rational identities`. These checks are finite, so they do not certify the all-size theorem by themselves.

Self-review status: passed. Independent audit: not performed. No external validation is claimed.
