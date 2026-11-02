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

The standalone checker `checker.py` requires Python 3 with SymPy, NumPy, and SciPy. Invoke `python checker.py` from the directory containing the file. On the reviewed package it reported:

`PASS: 23 independent polynomial, nullity, and propagator checks.`

Its symbolic characteristic-polynomial computations cover half-ring sizes \(m=2,3,4,5,6\); exact generalized-kernel nullities at \(\gamma=2\) cover both parities in the same range, and exact embedded-Jordan nullities cover selected positive \(\gamma\). Three numerical matrix-exponential comparisons check the predicted long-time powers. Each is a finite check only.

The complete unbounded-size proof is in `RESULT.md`, using the reflection-even/odd decomposition, exact tridiagonal determinant recurrence, simple zeros of \(U_{m-1}\), the irreducible-tridiagonal eigenspace recurrence, and a finite-dimensional Jordan exponential argument. No finite enumeration proves the infinitely many parameter values; the written proof does. The normalization of the cycle edges is explicitly fixed for \(m=2\). No independent audit, experimental validation, or claim of exhaustively novel historical priority is offered.
