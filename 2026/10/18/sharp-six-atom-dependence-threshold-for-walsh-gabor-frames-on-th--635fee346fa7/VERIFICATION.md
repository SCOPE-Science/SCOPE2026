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

The package contains two independent exact checking mechanisms for the universal dependence: `verify_upper.py` evaluates all eighteen sparse-matrix skew-symmetry identities and checks the annihilator determinant, and it separately expands each of 28 six-by-six minors as a polynomial with integer coefficients. Both tests passed.

The lower-bound checker `verify_lower.cpp` was compiled with a standard C++17 compiler at optimization level O3. It exhaustively examined all 595665 five-column sets containing the zero phase-space label for the integer window `(31,47,61,73,89,107,127,149)`, modulo the prime 1000003. Every matrix had rank five, and the program returned no failures. Translating phase-space labels preserves dependence up to nonzero scalar multipliers, so the enumeration covers all five-column subsets.

The universal upper proof requires polynomial density only after the three fixed annihilators have been algebraically verified. The finite lower calculation is sufficient for complex nonvanishing because a nonzero minor modulo the prime lifts to a nonzero integer minor. Genericity follows from finitely many nonzero determinant polynomials. No numerical tolerance, random test sample, or unverified infinite extrapolation is used.

Limits: no independently performed mathematical audit; no result for larger elementary abelian groups or arbitrary finite abelian groups; no quantitative conditioning bound.
