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

The exact derivation in `RESULT.md` covers every integer \(m\ge3\), every real \(t>0\), and every nonnegative individual edge allocation subject to the specified budget. The low-dimensional quotient calculation can be independently verified by expanding
\[
\det(XI-L)=X(X-u)^{m-2}\bigl[X^2-(2w+mu)X+(m+1)wu\bigr].
\]
The derivative sign calculation then locates the unique symmetric optimum, and the two Rayleigh-quotient arguments establish uniqueness in the full feasible simplex, not only its symmetric slice.

To replay auxiliary exact arithmetic, run `python star_optimum_check.py` using Python and SymPy. The program uses symbolic simplification for the derivative and branch formulas, computes rational characteristic polynomials for \(3\le m\le8\), and checks positive-semidefinite conditions and strict asymmetric perturbations in 40 exact-rational cases. Its expected output is `VERIFY_OK 58 exact cases`. These finite tests are corroboration, not an exhaustive replacement for the analytic argument.

Scientific limitations: The claim excludes \(m=2\), more than one exceptional edge price, nonuniform stationary distributions, discrete-time stochastic kernels, and non-star topologies. Whether some older specialized exact spectral-design treatment is logically equivalent remains an originality risk. Independent audit: not performed.
