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

# Actual verification

The file `verify.py` independently factors the relevant positive integers and enumerates unordered square-pair representations using integer square roots. Executing `python3 verify.py` passed 7,140 pairs with \(1\le u<v\le120\) for both deletion allocations, plus explicit numerical and CRT checks. It printed `CERTIFICATE_OK`. No floating point computations are involved. The all-integer finite census is not an infinite proof; the theorem follows from the finite-obstruction reduction and Jacobi's exact two-square count in `RESULT.md`.

Independent audit: not performed.
