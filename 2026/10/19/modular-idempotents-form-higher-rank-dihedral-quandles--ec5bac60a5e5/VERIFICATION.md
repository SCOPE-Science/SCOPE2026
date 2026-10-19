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

The standalone `verify_modular_dihedral.py` checks the claimed formula and the underlying linear kernel directly. It uses no external scientific package.

Command: `python3 verify_modular_dihedral.py`

Actual completed tests: eleven modular-rank computations for primes 3, 5, 7, 11, 13, 17, 19, 23, 31, 41, 73; explicit truncated-exponential constructions for each of these primes; direct operation preservation for prime examples having more than one coset; exhaustive classification of all coefficients for \(\mathbb F_3[R_3]\), \(\mathbb F_5[R_5]\), and \(\mathbb F_9[R_3]\). Observed complete counts were 4, 6 and 10 respectively. The script printed `VERIFY_OK`.

These are finite checks. They neither prove the infinite family nor independently certify the theorem. The accompanying mathematical proof supplies the characteristic-free-in-\(K\) argument at fixed odd characteristic.
