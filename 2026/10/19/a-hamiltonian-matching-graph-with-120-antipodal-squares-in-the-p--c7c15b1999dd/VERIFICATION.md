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

Run `python check.py` with Python 3 and SciPy installed from this directory. This enumerates all seven-edge matchings of the Petersen line graph by two independent finite procedures, cross-checks reconfiguration edges by two definitions, compares all-pairs distances by graph traversal and SciPy, verifies the 120-distance-nine-C4 structure and six natural symmetry orbits, then validates the 480-index Hamilton cycle certificate stored in `hamcycle.txt` including wraparound. Its exact stdout is recorded in `check_output.txt`; the first line is `VERIFY_OK`. All computations concern the finite graph explicitly defined in the checker. The cycle is a reproducible witness, not a general algorithm for arbitrary graphs. No independent external audit has been performed.
