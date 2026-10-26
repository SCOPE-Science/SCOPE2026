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
# Exact finite arithmetic verification

The standalone certificate `verify_index13.py` uses only the Python standard library. Run it from this directory with `python3 verify_index13.py`.

It computes the integer \(13\)-by-\(13\) Wendt-circulant determinant by Bareiss elimination and checks the complete prime factorization. For each of the four excluded primes, it exhaustively enumerates product-condition roots \(\zeta\in\mathbb F_p\) and all possible \(U\in\mathbb F_p\) for the first inverse-power-sum polynomial. The two possibilities for the second condition are checked at all four surviving first-equation roots, and those eight entries are independently recomputed using the generating-series coefficient identity.

A successful run prints `WENDT_OK`, four `EXCLUSION_OK` lines, `WITNESS_53_OK`, `WITNESS_27_OK`, and `CERTIFICATE_OK first_tests= 19306 second_tests= 8`. The witness checks enumerate all elements of \(\mathbb F_{53}\) and all \(27\) elements of \(\mathbb F_3[\alpha]/(\alpha^3-\alpha-1)\).

The elimination of *arbitrary* extension degrees depends on the theoretical Wendt, quotient, product and inverse-power-sum lemmas from Tang and Fan, arXiv:2610.18584v1. Finite verification alone would not prove the infinite statement. Independent validation has not been performed.
