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

# Verification of the seven-symbol classification

Run the bundled standalone `verify.py` using Python 3 and its standard library:

```sh
python3 verify.py
```

Expected output (observed on the packaged source):

```
VERIFY_OK: 210 profiles, 30 labeled Fano planes, 30 optimal code constructions, unique orbit, 168 stabilizer
```

The checker enumerates all exact partitions of the \(21\) unordered pairs of a seven-set into seven triples, obtains \(30\) labeled Steiner triple systems, checks that their \(30\) associated \(35\)-word profile codes have pairwise \(\ell_1\) distance at least \(4\), and confirms that the complete \(7!\) permutation orbit comprises the same \(30\) codes. It separately computes ordered-arc contributions of all \(210\) weight-four profiles and confirms the five case counts used in the upper bound.

These finite computations corroborate the classification and prevent indexing mistakes. The independent proof that all maximum codes arise from the displayed pattern is in `RESULT.md`; enumerating the \(30\) constructions alone would not exclude a different optimal pattern. No claim about larger alphabets, other deletion counts or ordered-sequence codes is being checked.
