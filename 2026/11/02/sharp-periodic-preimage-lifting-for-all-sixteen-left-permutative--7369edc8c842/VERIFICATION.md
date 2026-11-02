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

# Exact verification and limits

Run `python3 verify.py` from the package directory with Python 3 (standard library only). The checker constructs each rule truth table independently from its four-bit index; it enumerates each complete finite transformation monoid, verifies all expected minimum-cycle counts, and traverses all reachable augmented word automaton states with an invariant assertion at **every** state. The maximum augmented-state count per rule is 428. These are exhaustive finite closures; they certify the exceptional-language conditions for words of all lengths, subject to correct implementation of the stated four-state inverse recurrence.

It separately enumerates all forward images of indexed binary rings of lengths one through twelve and makes 5,120 exact comparisons between direct forward-image membership and the inverse-cycle criterion, covering targets of lengths one through six with permitted repetitions. The observed terminal line was `VERIFY_OK`.

The proof in `RESULT.md` explains why the finite closures establish the infinite statement. Computational checks cannot establish unrelated properties such as independent historical priority, primitive least-period lifting, exact predecessor multiplicities or multi-step dynamics.
