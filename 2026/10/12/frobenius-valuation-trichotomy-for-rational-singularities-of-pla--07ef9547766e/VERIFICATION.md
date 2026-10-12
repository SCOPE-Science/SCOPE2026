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

# Verification

Run `python verify.py` with a standard Python interpreter. Its implementation expands the defining plane-curve polynomial in shifted local coordinates modulo primes, truncates at the claimed first nonzero degree, and checks the complete coefficient dictionaries against the derived initial forms. It also tests the critical repeated-root multiplicities by exact binomial translation. The output is:

`VERIFY_OK: exact truncated local coefficient identities and critical multiplicities in 14 cases`

The tests cover examples with \(s<q\), \(s=q\), \(s>q\), including characteristic \(2\), examples with one repeated and one simple tangent, and examples with one tangent of multiplicity \(q+1\). All coefficients are integers reduced exactly modulo \(p\); no floating-point arithmetic or search heuristics are used. The proof in `RESULT.md` derives the formulas for every prime power \(q\), not just the tested examples.

The tangent-collision equality is tested directly against the factorization of the translated slope polynomial. Critical-point multiplicities are conclusions about tangent cones, not claims about the number of analytic branches at nonordinary points. The mathematical statement has been reviewed using the displayed local formulas and the full originating source; no independent mathematical audit was performed.
