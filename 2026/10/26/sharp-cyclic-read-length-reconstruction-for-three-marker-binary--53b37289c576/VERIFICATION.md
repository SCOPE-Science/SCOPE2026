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

Run `python3 verify.py` from a directory containing the provided script. The checker independently constructs all binary length-\(n\) words with exactly three ones for \(3\le n\le28\), canonicalizes by direct cyclic rotation (never reversal), computes all exact directed cyclic \(k\)-gram multisets, and finds each least singleton spectrum. It compares against the five-case gap formula, exact threshold multiplicities, and sharp maximum. The completed check produced `PASS raw_weight_three_words=23751 necklaces=1098 spectra=23841`. These finite checks do not certify the infinite theorem or historical priority. The all-length argument is in `RESULT.md`.
