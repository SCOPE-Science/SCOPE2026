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
# Reproducibility

Run `python check.py` from the package directory with SymPy and SciPy installed. The printed count is 96 comparisons. The exact polynomial tests cover \(1\le k\le5\) and integer \(0\le\beta\le3\), while the numerical quadrature covers \(\beta\in\{0.2,0.5,1.3,2.7\}\), \(k\in\{1,3\}\), and two values of the squared radius. `check_output.txt` is the actual output from a package-path execution.

The proof in RESULT.md uses classical Jacobi orthogonality and integration by parts, so symbolic and numerical tests do not substitute for any infinite-parameter statement. The zero count uses the classical interior simple-root theorem for Jacobi parameters greater than \(-1\). No independent scientific audit has been performed.
