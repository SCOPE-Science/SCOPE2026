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

## Reproducibility

Run `python3 verify.py` (standard library only). Successful output ends with `VERIFIED`. The program exhaustively checks the \(16\) odd three-bit prefix/residue cells against all \(32\) triples of leading bits and binary-length differences. The interval overlap constraints are also checked independently as exact rational bounds. It tests small actual quotients and exact dyadic-shell counting as consistency tests.

## Mathematical evidence and scope

The infinite obstruction rests on the necessary length, modular, and interval conditions and a complete finite \(32\)-state check, with an independent direct inequality argument for each forbidden cell. The density calculation is a separate elementary shell-count identity. Finite representability tests are explicitly non-exhaustive over arbitrary palindrome lengths and are not proofs of nonrepresentability. No external audit or independent validation has been performed.
