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

# Reproducibility and verification

The package includes `checker.py` and its actual output `check_results.txt`. Requires Python 3 and SymPy to verify exact rational matrices. Run `python checker.py` in the directory containing these two files. The checker builds the long-run k-word covariance from literal word-overlap compatibility at every relative lag and compares exact characteristic spectra against the independent anchored-pattern theorem. Eight pairs \((q,k)\) were checked, with the expected zero eigenspace multiplicities and variance coefficients. Exhaustive independent finite-string enumeration checked the mean identity for seven small pairs and sample lengths. Its final output was `CHECKS_PASS`.

The proof's analytic anchors are the orthonormal character completeness identity, independent-coordinate product orthogonality for distinct decorated supports, the multivariate finite-dependence central limit theorem, and the connected-fourth-cumulant count. The exact variance coefficient is computed from the eigenvalues via the finite geometric sum. Neither finite computations nor program execution assert the asymptotic CLT for untested parameters. The recent primary arXiv manuscript was unavailable in full text; the literature comparison explicitly retains this uncertainty.
