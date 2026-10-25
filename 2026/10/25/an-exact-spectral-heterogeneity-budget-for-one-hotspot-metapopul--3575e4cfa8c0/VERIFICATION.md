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

# Verification of the spectral-risk threshold

Execute `python verify.py` with Python 3 and SymPy. The program is standalone and reconstructs every example matrix from printed rational entries.

It checks the uniform-hub two-dimensional characteristic trace, determinant and centered characteristic identity symbolically in the patch-number and model parameters. It then checks all row sums, symmetry, nonnegativity, and identical hotspot columns for two five-by-five matrices. Exact rational matrix inverses produce \(529543/11008272\) and \(245/5956\) for the heterogeneity statistic, which lie strictly above and below \(1/24\). Exact determinants of the full reproduction matrices independently have the signs predicted by the theorem. It also checks four different background travel patterns at each of two uniform-hub flux strengths against the exact reduced eigenvalue.

The proof for arbitrary finite size is the positive-definite rank-one argument, not an extrapolation from these finite checks. Spectral-energy comparison requires the symmetry, common recovery, equal populations, and one-hotspot hypotheses stated in the result. No independent audit, external certification, or human mathematical verification has been performed.
