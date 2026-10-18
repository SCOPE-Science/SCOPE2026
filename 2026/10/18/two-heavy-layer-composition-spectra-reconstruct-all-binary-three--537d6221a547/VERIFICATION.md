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

# Verification and limitations

Run `python3 verify.py` with standard Python 3. The checker independently computes the exact weight-two and weight-three contiguous-factor composition histograms from word prefixes and from gap-extension sums, and exhaustively compares all 40,920 binary words with three ones of lengths 3 through 32. It accepts equal histograms only for equal or reversed words. The code also checks the published, nonreversal, four-one complete-spectrum ambiguity and demonstrates that the weight-three layer alone is insufficient. The executable has no network or package dependencies.

The mathematical proof in `RESULT.md` establishes the theorem at arbitrary lengths; finite verification is supporting evidence only. The sharp four-one pair is not new. All results assume exact multiplicity-preserving observations.
