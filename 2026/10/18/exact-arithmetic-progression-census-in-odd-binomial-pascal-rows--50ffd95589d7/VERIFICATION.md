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

# Verification instructions

Run `python3 CHECK.py` using Python 3.8 or newer; it requires only the standard library. The executable recomputes parity supports independently from the proposed run-product formula and enumerates actual increasing progressions for all positive row indices through 1024 and lengths 2 through 9. Separate assertions cover maximal progression counts, the no-three-term-progression criterion, and the Fibonacci census.

For clarity, the script is a **finite corroboration** rather than a certificate of the universally quantified theorem. The universal result follows from Lucas' theorem, the separated-block additive rigidity argument, and exact interval-progression enumeration presented in `RESULT.md`. The source comparisons do not establish absolute publication priority; independent validation is not reported or implied.
