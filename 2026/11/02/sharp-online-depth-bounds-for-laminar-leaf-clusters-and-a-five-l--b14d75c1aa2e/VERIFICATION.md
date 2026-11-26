---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

# Verification procedure and limits

Run `python3 CHECK_LAMINAR.py` and `python3 CHECK_LABELED.py` with Python 3 and the standard library. They generate hierarchy shapes by child multisets and labeled set partitions, respectively, then check dimensions via the version-space recurrence. The recorded output in `CHECK_OUTPUT.txt` agrees on the unlabeled shape counts 1, 1, 2, 5, 12 and the rank split of nine at two and three at three on five leaves. The proof in `RESULT.md` identifies the three attaining shapes directly; it does not rely on finite extrapolation. Regular-tree evaluations in these files are background, not part of the claimed contribution.
