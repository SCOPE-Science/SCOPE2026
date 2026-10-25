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

# Verification and reproducibility

Run `python3 check_stdlib.py` in the directory containing that file. The script uses only the Python 3 standard library; `check_output.txt` contains its actual output from a successful execution. It enumerates the fixed-particle SSEP Markov chain on four sites, evaluates one- and two-particle dual generators by uniformization, checks strict nonpositivity of finite-time conditional pair covariance, verifies the normalization of the Pareto equilibrium-age density, and evaluates the limiting covariance kernel numerically for several positive Pareto exponents and both spatial signs.

The run passed 70 deterministic assertions. At exponent \(\alpha=3/2\), the computed kernel values are \(K_{3/2}(1,2)\approx0.0182786826692\) and \(K_{3/2}(-1,2)\approx-0.0182786826692\).

The proof of the infinite-volume limit is analytical: the discrete heat equation gives the one-point limit; the two-particle generator equation and reflected gap kernel control conditional covariances uniformly; stationary renewal mixing and dominated convergence then yield the limit; strict monotonicity supplies the signs; conditional negative covariance bounds imply the macroscopic block \(L^2\) law. Finite-state numerical checks are not treated as infinite-volume proofs. The methods do not certify publication priority or substitute for independent scientific audit.
