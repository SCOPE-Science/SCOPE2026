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

# Verification steps and scope

Run `python3 checker.py` in a working directory containing the embedded checker. It uses only the Python standard library and prints `VERIFY_OK` only if all assertions pass. It performs independent exact polynomial irreducibility tests for degrees two through fifteen and direct finite-field character evaluations for degrees two through ten.

The mathematical proof, not the finite computation, establishes the theorem for all degrees. Reconstruct the root-trace identities and the three simple Artin–Schreier poles, confirm the genus-two numerator from the first two point counts and functional equation, then replay Möbius inversion and the uniform positivity bound. Literature priority has only been examined within the enumerated sources. No independent audit or external mathematical certification is asserted.
