---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible checks

Run `python3 verify.py` with a standard Python 3 interpreter. It tests all functions on the Boolean cube, counts the feasible complementary-pair decoders, and verifies that the first and second write agree on every input with current state `000` when using a common update function. It checks the corresponding count of one reachable table per decoder and distinguishes it from the sixteen possibilities when separate first- and second-write maps are permitted. Unreachable inputs are not counted.
