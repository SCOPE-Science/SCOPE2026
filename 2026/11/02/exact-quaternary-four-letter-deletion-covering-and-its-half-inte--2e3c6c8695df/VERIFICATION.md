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

# Verification of the exact quaternary one-deletion cover

The exact finite theorem has three certificate components. First, the deletion-shadow dual assigns weights \(1/2,1/8,3/8,1/4\) respectively to the four equality types of received triples. Its value is \(37/2\); fifteen equality patterns exhaust all 256 four-letter words and each dual sum is at most one. Second, a fractional primal supported on the five four-letter equality types `0012`, `0100`, `0101`, `0122`, `0123` has weights \(1/6,1/3,1/3,1/12,3/16\) respectively and covers every received triple to weight exactly one. Third, the displayed nineteen-word codebook covers all 64 length-three output words.

Run `python3 artifacts/verify.py`. Its exact rational and exhaustive calculations reproduce `artifacts/check_output.txt`, with terminal line `VERIFY_OK`. The checker reads `artifacts/codebook.txt` and uses only the Python standard library. No optimization solver is required for replay.

The enumeration exhausts only the finite domain \(\Sigma^4\) and \(\Sigma^3\); it is not a theorem for other lengths or alphabets. The review is not an independent external audit.
