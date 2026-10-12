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

# Verification record

The unrestricted proof is in `RESULT.md`. The auxiliary Python program `verify.py` performs exact integer dynamic programming with its representation counts capped at three; this cap is logically sufficient for testing the claimed first three-representation thresholds. `verification_output.txt` contains the recorded successful execution.

The program covers every odd first denomination from \(9\) through \(201\), confirming each proposed residue threshold and ruling out earlier numbers in the same residue, then checking an additional finite interval above the maximal threshold. The finite checks do not establish the theorem for any untested first denomination; the proof does.

The mathematical comparison distinguishes the two-representation result \(F_2\) in the 2017 Cardiff thesis from the new three-representation threshold \(F_3\). Verification does not constitute independent audit, peer review, or publication.
