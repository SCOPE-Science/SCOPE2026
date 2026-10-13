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
# Finite verification and proof boundary

Run `python3 verify.py` from the directory containing this file. The program uses only the Python standard library, checks all input paths through length six for 400 state machines, constructs exact collision witnesses for thousands of larger parameter pairs, and independently counts the opacity-level spectra in small ranges. It asserts every predicted shortest path when within its search bound and the absence of shorter observed conflicts. On success it prints `VERIFY_OK` with numerical ranges.

For the unbounded assertion, consult the direct integer proof in `RESULT.md`: every conflicting prefix pair has a difference that is a positive multiple of \(m\) but not of \(b\), bounded above by \(b^L-b\); the explicit word obtained from \(m=c(b^{L-1}-1)+t\) attains the first possible length. The correctness of the infinite formula does not depend on test coverage. The relationship to the published Allouche–Yao general theorem is specified in `RESULT.md`.

The revised journal full text was not obtained and possible priority overlap is a stated limitation. No external independent audit or certification is asserted.
