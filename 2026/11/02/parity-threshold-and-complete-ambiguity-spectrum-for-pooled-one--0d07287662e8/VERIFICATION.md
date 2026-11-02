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

Run `python3 verify.py` with Python 3. The script uses only the standard library, constructs each weight-one strand as a literal binary word, and pools the actual prefix and suffix of length one less than the word. It groups source multisets by the exact sorted multiset of read strings and verifies the full predicted fiber histogram and maximum fiber size.

Executed result:

```
VERIFY_OK parameter_pairs=63 source_multisets=19440 distinct_profiles_accumulated=19209 method=literal_nminus1_factor_multisets
```

The exhaustive finite ranges are \(2\le n\le10\) and \(0\le k\le6\), covering 63 choices of parameters. They cannot establish infinite validity. The proof in `RESULT.md` supplies the all-parameter argument through exact read counts, integer-kernel classification, canonical representatives and binomial counting. No independent scientific audit has been performed.
