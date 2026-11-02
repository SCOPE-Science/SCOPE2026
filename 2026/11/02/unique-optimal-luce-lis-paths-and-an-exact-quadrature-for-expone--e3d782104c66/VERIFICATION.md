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

# Reproducibility of the mathematical checks

Running `python verify.py` with Python 3, SciPy and NumPy prints `VERIFICATION PASSED` and a table of shooting constants and LIS constants. The recorded execution passed 249 assertions. The checks verify numerical normalization \(T_\beta(C_\beta)=1\), the alternate quadrature identity, the strict monotonicity and unit terminal value of the derived path, and its performance relative to ten independently selected smooth competing curves per tested parameter. They also check the uniform-weight base case and the local first-order perturbation.

The proof of uniqueness is not inferred from the tests. It is the exact BV calibration in `RESULT.md`: \(p'=\beta pg'\), strict concavity, nonnegative singular measure, and nonpositive endpoint boundary terms. The strict existence of the scalar root and both parameter asymptotics are likewise analytical. The code reports normal floating-point quadrature tolerance; an integration warning near the singular shooting boundary is not an impossibility or a proved error bound. These checks do not establish stochastic finite-sample convergence beyond the cited existing limit theorem.

No independent audit has been performed.
