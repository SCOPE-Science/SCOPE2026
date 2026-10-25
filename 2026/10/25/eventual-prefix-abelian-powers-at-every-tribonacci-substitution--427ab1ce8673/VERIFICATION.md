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

Run `python3 verify.py` from the extracted package. The script uses standard-library `decimal` for locating finite beta-greedy digits, checks each produced beta-polynomial identity as an exact triple in the cubic integer ring, verifies the `111`-free condition, checks substitution-length and Parikh-vector identities, and directly compares canonical prefix decomposition for ten thousand lengths and five prefix-power examples. Expected final line: `TRIB_PREFIX_ABELIAN_PASS beta_expansions=200 canonical_prefix_tests=10000 parikh_examples=5`.

The script checks sample inputs only. The all-\(k\) claim rests on the cited Frougny–Solomyak finiteness theorem, exact recurrence transfer and explicit induction; no finite experiment establishes property (F) or substitutes for an infinite proof. The published source's publisher full text was inaccessible, while its theorem statement was verified through a mathematical exposition. Independent audit has not been performed.
