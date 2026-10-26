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

# Verification

Run `python3 verify_prime_exponent.py` in a directory containing that standalone script (Python standard library only). `verify_output.txt` records the run. The program checks all 9 equality atoms and 27 relational multiplication atoms involving the named identity and two chosen elements, over every ordered pair. It compares complete sets of pointed extension types. The tested groups include two nonabelian finite Heisenberg groups to check that commutativity is not silently assumed. It tests cyclic exponents \(2,3,5,7,11\) and selected products, but does **not** enumerate all finite groups or prove the infinite theorem.

The general proof is the atomic reduction and the exceptional-second-choice lemma in RESULT.md. The sharp nine-element bound follows from elementary order divisibility plus the six-class separation; the six-class theorem has not been independently audited.
