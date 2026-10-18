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

# Verification and reproducibility

The included `verify.py` is self-contained and requires Python 3 with its standard library only. Run `python verify.py` from the directory containing the extracted files.

It checks all \(330\) parameter triples \(3\le d\le8\), \(1\le n\le10\), \(1\le r\le n\) using a direct enumeration of weak compositions, with rational arithmetic. Both the local covariance and aggregate covariance are reconstructed from direct event counts, independently of the analytic derivation, and compared with the formulas. Signs and exact zeros are checked separately.

The checker also uses a Pólya-draw transition recurrence to reconstruct the full count-vector distribution for \(d=3,4,5\) and \(1\le n\le6\), verifying uniformity over weak compositions in 18 additional cases. Three displayed witnesses are checked exactly. The observed output was `PASS: 330 exact covariance triples and 18 Pólya recursions`.

**Limits.** Finite checks are not a proof for arbitrarily large parameters; the proof is the uniform-composition counting and exact symbolic cancellation in `RESULT.md`. No independent audit or formal-proof certification has been performed.
