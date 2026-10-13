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

Run `python3 verify.py` using the standard Python library. It builds explicit finite fields and all magma operation tables, then tests all promised automorphisms and translation socles through order sixteen, exhaustively verifies the full pointed-automorphism group through order nine, and reproduces the collision and interpolation sublemmas on all tested fields. The expected terminal output is `VERIFY_OK`. These are finite consistency checks; the universal proof, including the unique-small-field cases and the at-most-six-exclusions argument, is in `RESULT.md`. No independent audit has been conducted.
