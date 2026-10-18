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

# Reproducibility of the one-deletion distribution

Run `python3 verify.py` in the directory containing this document and `verify.py`. The script uses only Python's standard library. It constructs each binary word from the cyclic gap triple, deletes every symbol at every position, canonicalizes the resulting strings by every cyclic rotation, and counts the resulting distinct output necklaces. It compares the direct count with the closed individual classification and histogram, and checks the necklace Burnside count.

An execution of this exact checker printed:

`PASS circular one-deletion three-marker profile: complete_zero_totals=0..36 necklaces=3055 random_larger_cases=450`

The total of 3,055 covers all cyclic gap triples with zero counts between zero and 36 inclusive. The additional 450 tests use a fixed pseudorandom seed and larger gap totals. Finite testing does not certify an infinite classification; the unlimited-length proof is in RESULT.md. No external review was performed.
