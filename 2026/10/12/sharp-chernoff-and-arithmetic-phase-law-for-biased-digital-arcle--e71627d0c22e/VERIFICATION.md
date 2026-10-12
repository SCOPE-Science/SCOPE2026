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

# Verification record

Run `python3 verify.py` in the directory containing this file and `verify.py`. No third-party Python packages are required. The verifier compares the polygonal graph lengths computed by explicit words and by binomial grouping for four positive binary laws and ten mesh depths each; tests the two-sided overlap envelope for three nonbinary laws and five depths each; and evaluates tilted binomial sums at seven sample sizes, with a stable evaluation of the kernel. It additionally samples the predicted periodic coefficient and calculates a nonzero first Fourier harmonic numerically.

Representative binary-bias values are \(\alpha\approx0.732486760359\), \(t\approx0.458431157846\), \(Z\approx0.893706867433\) for \(p=9/10\). At sample size \(n=2000\), the leading phase approximation has relative discrepancy approximately \(-0.00257\). The finite checks do not prove the general identities, the strict nonvanishing of beta coefficients, or any infinite asymptotic statement. Those assertions are established by exact analytic calculations in RESULT.md; the numerical values are reproducibility diagnostics, not certificates of priority or independent audit.
