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

# Verification

`verify.py` is self-contained and uses only the Python standard library. Run `python3 verify.py` in the directory holding the included artifacts. The program directly tests candidate scattered-subsequence absence and minimality by deleting each position, compares with the proof's local criterion, and verifies all length counts for the first eight parameter values. It then uses a separately coded transfer enumeration to check each binomial length distribution through parameter 50.

Observed result: `PASS: 349504 distinct words checked by direct subsequence membership; 347 minimal absences counted; 50 transfer-distribution checks`. See `verify_output.txt` for the individual histograms and complete recorded output.

The full proof for unbounded parameters is in `RESULT.md`; finite verification does not certify its infinitely many cases. The 2023 prior-art source cited in `RESULT.md` could not be read in full, and no independent mathematical or publication-priority audit has been performed.
