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
# Reproducible verification

Run `python3 verify.py` in the directory containing the standalone artifact. A successful run prints `VERIFY_OK` and exits with status zero; a failed exact equality raises an exception.

The program uses only integer arithmetic and Python's floor division. It verifies \(4r+1\) distinct shell phases, phase increments, invariance, and exact protected periods for integer shell radii through 40. It also enumerates first-return orbits for \(2\le q\le120\), confirms exact periods \(8q-2\), counts both visited shells, and compares the complete hand-scale itineraries at \(q=2\) and \(q=3\).

The program cannot prove the statements for all integers \(q\), all integer radii or arbitrary real \(\lambda\). Those claims are justified by the finite-case-free analytic argument in `RESULT.md`. No machine-generated log is used as a substitute for a proof. The independent audit status above remains not performed.
