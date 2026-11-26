---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The finite checker `check.py` uses exact integer cyclotomic polynomial coefficients. Its recorded range is all fourth rows for primes 5, 7 and 11, and odd and central fourth rows for prime 13.

The corrected `verify_expansions.py` uses exact rational algebra to expand the determinant for the formal nodes \(\epsilon_j\exp(a_j\tau)\). To reproduce the symbolic check run `python3 verify_expansions.py` with SymPy installed. The substitution \(\tau=\log(1+u)\) transfers the cubic coefficient and, on the equal-sum locus, the quartic coefficient to the cyclotomic parameter used in the proof. The quartic expression has factor \(d-1\), not \(d-4\): replacing the formal nodes by \(\epsilon_j(1+a_j u)\) changes this coefficient and does not compute the expansion at \(\epsilon_j(1+u)^{a_j}\).

The finite tests and symbolic calculations check only the stated ranges and identities. The general classification additionally uses the cyclotomic valuation argument and the exact parity-pure and central calculations in `RESULT.md`.
