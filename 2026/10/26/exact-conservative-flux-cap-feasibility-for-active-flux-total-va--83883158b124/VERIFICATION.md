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

The standalone `verify.py` was executed with rational input data and exact `fractions.Fraction` arithmetic for the ternary dynamic program, brute-force ternary optimization, and cyclic interval cap. The minimized primal total-variation penalty was independently represented as a linear program with bounded flux variables and nonnegative hinge auxiliaries, solved with SciPy HiGHS.

There were 504 deterministic test cases spanning \(n=2,\ldots,8\) in which the three-state dynamic program agreed exactly with brute-force \(3^n\) enumeration, the proper-interval cutoff agreed exactly with the brute-force ternary threshold, and the float linear-program objective agreed with the exact-rational formula within \(10^{-7}\). For six additional even cycle sizes, the sharp cap \(m/(2\lambda)\) was checked by the independent exact routine. Actual output is embedded as `verification_output.txt`.

These finite checks are not proofs for unbounded \(n\); the exact minimax, discrete coarea, cyclic cut decomposition and conservation arguments in `RESULT.md` supply the mathematical proof. The numerical LP is finite-precision and is used for corroboration, not certification. The result is scoped to abstract signed face corrections and does not enforce consistency constraints of a particular PDE flux or prove multistep stability.
