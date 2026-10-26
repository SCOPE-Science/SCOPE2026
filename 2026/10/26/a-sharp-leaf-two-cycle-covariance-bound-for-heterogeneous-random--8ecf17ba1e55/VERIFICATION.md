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

Run `python check_mapping_dependence.py` from the folder containing this file and the checker. Only Python's standard library is used.

The exact-rational run printed `PASS exact assertions: 318 positive-mass mappings enumerated: 150456 families enumerated: 26`. It independently enumerated all positive-probability mappings for selected target laws in dimensions two through six and compared direct mixed moments with the derived formulas. Separate rational checks cover dimensions seven through twenty. The cases include uniform, unequal, geometric, and partially supported probability vectors.

These checks are not an exhaustive proof over all real target vectors or unbounded dimension. For that claim, the proof in `RESULT.md` establishes the exact mixed-moment identity and applies an antitone covariance inequality; it also treats equality and degenerate support separately. No external or independent audit has taken place.
