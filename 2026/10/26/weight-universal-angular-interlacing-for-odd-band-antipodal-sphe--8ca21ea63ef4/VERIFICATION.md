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

# Verification notes

Run `python check.py` in an environment with NumPy and SciPy. The included `check_output.txt` is the captured output from the standalone checker: 3726 assertions passed. The checker constructs rational polynomial moment matrices for odd dimensions \(d=3,5,7\), odd bandwidth indices \(K=0,1,2,3\), rational cutoffs \(c=1/3,1/2,2/3\), and the positive zonal densities \(h(s)=1\), \(h(s)=1+2s\), and \(h(s)=1+s^2\). Matrices are exactly assembled as rational numbers, then converted to floating point for generalized eigenvalue comparisons. The checker does not certify universal positivity by enumeration; the symbolic likelihood-ratio argument, finite-dimensional min–max reasoning, and cutoff-evaluation lemma in RESULT.md give the complete proof.

The full-source comparison is incomplete for arXiv:2103.14650. Independent verification and priority confirmation have not been performed.
