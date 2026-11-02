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

# Verification evidence

The proof of the all-length statement appears in RESULT.md. Run `python3 verify.py` to independently reproduce bounded instances by direct enumeration of all weight-three words and cyclic orbits. It checks codeword construction, the exact formula, every ordered pair for all nonempty proper prefix/suffix lengths, and each primitive orbit.

The actual executed run printed:

```
VERIFY_OK lengths=3..26 total_weight_three_words=17550 primitive_necklaces=864 codeword_pair_tests=53940 formula_lengths=3..1000
```

This verifies \(3\le n\le26\) by exhaustive finite enumeration of 17,550 fixed-weight words, plus the closed arithmetic identity for \(3\le n\le1000\). It does not by itself verify arbitrary lengths. No independent scientific review or external proof-certificate validation has been performed.
