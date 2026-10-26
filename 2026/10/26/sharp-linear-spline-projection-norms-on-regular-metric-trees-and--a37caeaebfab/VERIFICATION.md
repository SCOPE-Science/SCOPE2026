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

The included `verify.py` runs with Python 3 and the standard library only. Execute `python3 verify.py` in the extracted package. Its rational verifier constructs finite graph mass matrices from edge incidence, inverts each exactly, checks matrix products, integrates the absolute affine kernel exactly, and independently compares high-girth truncated rows with the line. Its 70-digit arithmetic tests the analytic tree recurrence, geometric shell sums, degree monotonicity, and selected large-degree asymptotics. A replay produced `PASS 1648 exact arithmetic/independent shell checks`.

The checker is a finite consistency certificate, not a proof that arbitrary finite graphs or all infinite trees have been enumerated. For general degrees and graph orders the proof rests on the recurrence and Neumann norm inequalities in `RESULT.md`. Independent mathematical or bibliographic auditing has not been conducted.
