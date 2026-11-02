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

The included standalone `checker.py` evaluates the four-valued truth tables and the value-indexed modalities used in the construction. Run `python3 checker.py` in the artifact directory; the deterministic expected outcome is `ALL_CHECKS_OK 1090 finite semantic checks`.

The tests reconstruct all one-letter pointed supports, verify that crisp value tests, global-existence tests, pointed-support guards, and nonclassical-value flags have their claimed outputs, and replay twelve prescribed complete term-function tables. Selected two-letter supports and the exact first two exponents are checked as further regression cases.

Finite tests are not a proof of an arbitrary-atom theorem. The proof in RESULT.md separately supplies induction on formula structure, a depth-one constructive normal form for every permitted semantic function, and the sharp-world witness. Historical priority and independent mathematical review have not been certified.
