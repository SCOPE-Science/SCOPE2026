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

Run `python3 check.py` from the directory containing the embedded checker. The script independently implements (a) the direct definition using every length-three position choice and a subsequence test and (b) dynamic programming for the longest common subsequence. It prints the complete ten-word target-membership comparison, checks all shorter layers for the five equivalent words, and checks all binary candidate sources through length ten. Its recorded output is in `check_output.txt`.

The computational domain is explicitly finite; the unrestricted-length assertion is justified in `RESULT.md` by admissible and excluded symbol-count witnesses. No external independent mathematical audit or formal certification has been performed.
