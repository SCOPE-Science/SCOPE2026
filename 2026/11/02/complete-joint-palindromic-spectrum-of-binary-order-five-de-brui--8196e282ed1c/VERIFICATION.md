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

# Reproducibility and limits

Execute `python checker.py` from the directory containing `checker.py`, `joint_spectrum.tsv`, `lengthwise_profiles.tsv`, and `full_census.tsv`. The checker reports exactly 2048 canonical binary order-five de Bruijn cycles; verifies that Euler-edge DFS and all 65536 local outgoing-edge orderings give the same set; checks all 1024 possible window lengths and starts per cycle against a second odd/even palindrome-center method; confirms all three full reference tables byte-for-byte and verifies the displayed distributions.

For independent table regeneration, run `python generate_tables.py` in the same directory. Both commands depend only on Python's standard library. The complete finite enumeration is exhaustive by the Euler-tour representation and the unique all-zero window convention; it does not assert a theorem for higher de Bruijn orders.

Actual result: `PASS: 2048 primitive de Bruijn cycles; 2 generators agree; 2 palindrome tests agree; 23 joint classes; 51 lengthwise profiles`.

External independent mathematical audit has not been performed. Historical-priority verification is incomplete: a relevant 2014 circular-palindrome article was not available in full. The scientific claim is conditional on the precise definitions of distinct literal palindromic strings, rotation classes, and circular factors of length no more than 32.
