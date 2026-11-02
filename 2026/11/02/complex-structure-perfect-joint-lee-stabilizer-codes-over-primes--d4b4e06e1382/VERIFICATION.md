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

The modular-arithmetic verifier `verify.py` is standalone and requires Python 3 only. Execute `python3 verify.py` and compare stdout with `verify_output.txt`. The verified parameter pairs are (3,2), (3,4), (3,6), (7,2), (11,2), and (19,2). For each pair it constructs distinct four-element orbits, checks all commuting stabilizer generators, confirms row rank, enumerates all single-shift syndromes, produces a zero-syndrome witness of joint-Lee weight three, and enumerates the physical weights of all nonidentity stabilizers. In the (3,2) corner it checks algebraic properties but does not assert a logical code distance since there are zero logical qudits.

The theorem for all allowable primes and even ranks follows from the orbit partition, finite-field second-moment identity, and stabilizer-support bound proved in `RESULT.md`; testing finitely many instances alone is not a proof. No independent audit has yet been performed.
