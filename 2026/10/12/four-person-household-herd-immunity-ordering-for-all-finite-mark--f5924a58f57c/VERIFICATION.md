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

# Reproduction and scope

The verification materials consist of `verify_household.py`, `positivity_coefficients.tsv` and `independent_dp.py`. Run `python verify_household.py` with Python 3 and SymPy 1.14 (compatible versions may work). No network access, external proof service or downloaded article is needed for this check.

The verifier recomputes the triangular infection-size and expected-household-size recurrences, constructs the exact rational normalized threshold gap, and verifies the denominator and numerator degrees. It transforms the numerator from the power basis to the degree-13 Bernstein basis in \(\pi\), asserts all coefficient signs exactly, and independently reconstructs every power-basis coefficient from the 406 entries in the supplied TSV. The coefficients are exact rationals, not rounded numerical data. Since every nonzero Bernstein basis function is strictly positive on \(0<\pi<1\), the nonnegative row coefficients prove the parameter-wide sign in conjunction with \(\ell>0\).

The second program uses exact rational continuous-time Markov chain recursion rather than the source's triangular final-size identity. At \(\ell=1\), \(\pi=1/2\), it checks the four-state household means and the five-point final-size distribution. That cross-check is not treated as an infinite proof. The verifier reports `VERIFY_OK` only if all algebraic, certificate and CTMC checks pass.

No independent audit or third-party verification has been performed. None of these tests asserts novelty or establishes statements outside the theorem's Markovian four-person scope.
