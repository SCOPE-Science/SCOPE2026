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

# Verification record

The executable `verify.py` uses only Python 3's standard library and exact integer arithmetic. It verifies recurrence normalizations, the Pell-shift identity, the telescoping identity, and direct eight-window gcds for every odd length between \(1\) and \(501\), inclusive. Run `python3 verify.py` in the package directory. Compare stdout to `verification_output.txt`.

The proof is symbolic and unrestricted; eight-window checks do not prove an infinite gcd. The core infinite-obstruction argument is given in `RESULT.md` and rests on coprime adjacent balancing numbers, a forced recurrence, and a \(7\)-adic lifting identity. No independent audit has been performed.
