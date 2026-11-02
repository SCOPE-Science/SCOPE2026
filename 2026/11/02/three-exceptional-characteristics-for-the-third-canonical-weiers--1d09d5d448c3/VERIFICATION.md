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

# Reproducible exact checks

Place the four accompanying Python scripts together in one directory and install Python 3 with SymPy. Run:

```
python klein_invariants_verify.py
python klein_leading_coefficient.py
python klein_modular_certificate.py
```

The first computes the degree-six, degree-fourteen and degree-twenty-one invariant polynomials and checks exactly, with integer coefficients, the remainder of \(B^2-A^3+1728U^7\) modulo the Klein equation. The second computes the leading determinant in the formal parameter \(t=y\), the Wronskian scaling constant \(27524002083766272000000\) and its prime support; it also factors \(21962\) and \(27146\). The third imports `klein_jet_check.py` and uses truncated finite-field power series and exact modular determinants at five points in each of the three exceptional characteristics \(79,139,277\), verifying the expected scalar reduction and nondegeneracy of both invariant terms.

Each script exits nonzero on an assertion failure. These are independently reproducible algebraic and finite-field checks. They do not by themselves establish the characteristic-uniform quotient statement or the global divisor formula; the proof in RESULT.md gives those mathematical arguments. The historical claim remains subject to independent bibliographic review, and no independent mathematical audit has been performed.
