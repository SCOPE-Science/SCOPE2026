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

# Reproducibility and limits

The standalone `verify.py` is shipped with this result and requires only Python 3 with the standard library. Run `python verify.py`. It performs 356 deterministic tests: exact one-dimensional uniform moments, direct versus localized finite-grid error identities for seven power exponents on both mesh parities, exact \(\gamma=1\) behavior, and approximate one-dimensional moment checks of the large-offset coefficients and Gaussian asymptotic constants. Its test routine finishes by printing `PASS: 356 deterministic checks` when every assertion succeeds.

The proof of the infinite series, normal limits, and threshold does **not** depend on these finite tests. Reproducibility of the analytical derivation is provided through equations (1)--(6) of RESULT.md: the exact finite-grid decompositions, uniform local Taylor remainder, local variance expansion, summability versus divergence, and bounded-summand triangular-array limit theorem. The non-Gaussian conclusion further invokes Cramér's standard normal-decomposition theorem. The proof covers only independent within-cell complementary pairs, a uniform mesh, the interior cusp at \(1/2\), and \(0<\gamma\le2\).

No machine-checked infinite proof, independent audit, or empirical validation of all possible related literature is claimed.
