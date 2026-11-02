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

The packaged `verify.py` uses only Python's standard library and calculates each Hasse--Witt entry by exact multinomial sums reduced modulo the relevant prime. It checks characteristic-31 diagonal entries, polynomial factorization and gcd identities, squarefreeness, boundary exclusion, and the common Hasse--Witt gcds in each smaller prime characteristic from five through twenty-nine.

Command: `python3 verify.py`. Required last line: `VERIFY_OK`. Verification of finite identities is not an independent mathematical audit. The geometric deduction uses the standard theorem connecting the Hasse--Witt/Cartier matrix and the \(p\)-rank and \(a\)-number of a smooth genus-three curve. The tables are over algebraic closures: individual quadratic factors need not split over the prime field. No assertion is made about complete Newton polygons or isomorphism-class counts.
