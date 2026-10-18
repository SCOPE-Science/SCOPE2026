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

# Reproduction and limits

Execute both scripts from the directory holding all four computational files:

```text
python3 verify.py signature_levels.json derivations.json
python3 crosscheck.py signature_levels.json
```

Expected messages include `BILATERAL_ONE_LETTER_DEPTH_COUNTS_OK 39 64 66 66` and `BILATERAL_BITMASK_CROSSCHECK_OK 39 64 66`.

The set-semantic checker reconstructs all four teams and validates the inductive interpretation of both truth signs, enumerates the propositional closures at depths \(0\), \(1\), and \(2\), checks that the third closure is stable under the modality, and replays every node of the straight-line formula certificate. The independent bit-mask checker computes the operations again by integer truth tables and reproduces the signature sets. The certificate includes all \(66\) signatures, rather than only their cardinality. Correctness for arbitrary finite formulas follows from closure and structural induction; neither checker searches formulas of arbitrary size by brute force. The checked domain is exactly the one-letter, two-valuation team universe. There is no independent audit, and older unindexed equivalent work cannot be excluded by the documented searches.
