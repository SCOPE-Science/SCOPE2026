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

The included `verify.py` uses direct linear-equation enumeration to enumerate anti-commuting involutions, independently of the signed-Jordan normal form. Eleven prime-field cases and two characteristic-three quadratic-extension cases agree coefficient by coefficient with the theorem; the program prints `ALL_EXACT_CHECKS_PASSED 13`. The finite checks do not verify every dimension or every field. The general correctness rests on the proof in `RESULT.md`, not on exhaustive claims beyond the tested cases. An independent mathematical audit has not been performed.
