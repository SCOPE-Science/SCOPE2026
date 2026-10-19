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

The standalone Python program `verify.py` reconstructs the Thue–Morse word in two independent ways and directly checks the stated radii across all gap positions at substitution depths 4 through 16. The assertions cover axis uniqueness, the four sharp off-axis centers, the absence of odd palindromes of length five, and two distinct long circular palindromes at representative even lengths. Run `python3 verify.py`; expected terminal line begins `VERIFY_OK`. All claimed infinite ranges are justified by the proof, not by finite tests. No independent scientific audit has been performed.
