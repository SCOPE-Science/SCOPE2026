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

Run `python VERIFY.py` with standard Python 3. The verifier constructs every word of length \(N+2\) containing exactly two ones, for each \(0\le N\le60\); directly computes the scattered \(01\) counts of the word and of its lexicographically smallest literal rotation; groups the observations; and compares all fiber-size histograms and explicit doubleton pairs with the theorem.

Observed terminal result:

```text
VERIFY_OK zero_counts=0..60 words=39711 direct_rotations=yes explicit_pairs=yes
```

It additionally checks, independently for each word, that the direct observation matches the proof's run formula. The program relies only on Python's standard library and is included in full. The all-length proof is the classification in `RESULT.md`; exhaustive checks to length \(62\) do not establish an infinite theorem. Access to the full 2021 journal article for a complete historical comparison was unavailable.
