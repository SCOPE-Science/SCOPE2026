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
# Numerical and analytic verification notes

The scientific statement is established in `RESULT.md` using the nonnegative renewal identity and the solved, finite-dimensional moment equations. The standalone `verify.py` performs 312 check groups using Python's standard library, including 100 independent direct Runge–Kutta moment computations (three moment comparisons for each), ten scaling checks, a direct 80,000-tree Monte Carlo sanity check, and rate-optimality checks. Execute with `python verify.py` from the package directory. The exact constants, rate, threshold and numerical checks are printed by the script.

The independent differential-equation computation verifies the explicit closed forms for \(\mathbb E[H_f(t)^2]\) and \(\mathbb E[H_{f'}(t)^2]\) on times strictly below the critical threshold. The direct weighted-tree samples are checked only where the variance is finite. The proof of divergence, uniqueness and the optimal horizon is analytic; no finite computation is treated as a certificate of an infinite statement. An external independent audit has not been carried out.
