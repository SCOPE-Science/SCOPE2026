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

# Reproducibility

Run `python verify.py` with standard Python 3; it uses only the standard library. It independently checks (a) the finite sixteen-state continuation and correct boundary gluing for \(2\le n\le100\) (open) and \(3\le n\le100\) (closed), and (b) the direct graph-neighbor best responses for every binary action vector through eight rungs. The script produces its expected counts and terminates without assertion failures.

The infinite-family proof uses the exact \(\mathbb F_2\) recurrence and four-periodicity; checking through one hundred rungs alone would not establish infinite validity. No random sampling, floating-point numerical claim, or external dependencies are required. There is no independent external audit or validation.
