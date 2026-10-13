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

Run `python3 verify_euler.py` and `python3 verify_direct.py` from the directory containing the two scripts and `profile_census.csv`; both require only the Python 3 standard library. Both were executed from the candidate artifact directory.

`verify_euler.py` checks integer flow constraints, 226 four-vertex profiles, 45 degenerate profiles, factorial divisibility, the entire 271-row CSV, the sum of 65,536, and the unique first and second fiber sizes. `verify_direct.py` enumerates every one of the 65,536 indexed binary words independently, reconstructs all profiles without the BEST formula, and checks the same CSV and rankings; it additionally verifies the length-eight comparison. Successful terminal outputs were `EULER_OK` and `DIRECT_OK`.

The mathematical premise is finite exhaustive enumeration with a separately justified graph encoding and support partition; neither program verifies an infinite theorem. Possible prior unindexed results and independent audit remain unverified.
