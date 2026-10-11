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

The standalone `verify.py` script uses only the Python standard library. Execute `python3 verify.py` from the directory containing this file to enumerate the full pure facet complex for each \(6\le n\le11\), calculate orientation signs for every rotation, and compare all \(51\) character values with the closed formula. Its observed output terminates with `VERIFY_OK 51 exact signed character comparisons`. The finite checks do not certify the general argument; the general proof is given in `RESULT.md`. Independent audit has not been performed.
