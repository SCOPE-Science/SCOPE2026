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
# Verification of the mathematical claim

The independent-audit channel is not performed. Reproduction is provided by `verify_jacobi.py` (Python with SymPy, NumPy and SciPy). The script symbolically checks the reproduced quadratic kernel, the critical-point factorization, and the exact radicals for uniform measure. It numerically cross-checks the closed formula against direct quadrature of the kernel and sampled step/evaluation parameters over several admissible weight choices. It was executed successfully in the submitted package.

The general theorem and global extrema for all real \(q>1\) are established analytically in RESULT.md, not inferred from a finite parameter grid. The source comparisons involve full-text reading of the Kaber article and the accessible arXiv texts, plus abstracts for papers not inspected in full. The global uniqueness of the branch crossing, nonsymmetric weights, and degrees greater than two remain unproved and unclaimed.
