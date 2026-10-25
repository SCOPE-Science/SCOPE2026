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

# Reproducible finite verification

Execute `python3 verify.py` in the directory containing this file and `verify.py`. It needs Python 3 standard library only and prints `VERIFY_OK` when every check succeeds. The script computes all unordered pair sums, tests the four-case predicted longest consecutive run for both gaps in `[1,100]` and five translations, and tests origin-anchored spectra by enumerating three-element subsets of `[-15,15]`. The observed output was `VERIFY_OK 50000 translated gap triples; signed [0, 1, 2, 4] nonnegative [0, 2, 4]`. These are finite transcription and boundary checks. The universal mathematical proof uses an exact ordered gap identity and parity of the starting point of the five-element consecutive block; it is not inferred from this bounded program. No independent mathematical audit has been performed.
