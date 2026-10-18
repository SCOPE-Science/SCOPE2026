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

# Reproducible checks and boundaries

Run `python3 VERIFY.py` from the extracted directory. Its polynomial arithmetic and irreducible enumeration use only the Python standard library. In the executed tests, all 100 exact residue-class comparisons for characteristic two passed. Additional finite-degree averages use direct polynomial divisibility and square-divisibility, not an asymptotic fit.

The proof beyond these tests uses exact CRT probabilities modulo finite products of prime squares, a uniform tail bound for large square divisors, and an independent deduction of polynomial Mertens from the prime-counting identity. Finite checks are not independent validation of the infinite theorem. The field is \(\mathbb F_2\), the shift is nonzero, and the degree limit precedes the cutoff limit.
