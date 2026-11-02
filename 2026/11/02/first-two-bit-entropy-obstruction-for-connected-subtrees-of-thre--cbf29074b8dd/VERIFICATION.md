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

# Reproducible verification

Python 3.10 or later, standard library only:

```sh
python3 spider_connected_verify.py
python3 spider_root_profile.py
```

`spider_connected_verify.py` directly enumerates all allowed connected vertex sets by disjoint combinatorial forms; a second enumerator grows each set from singletons through graph adjacencies and must produce the identical list. Integer-bitset and frozenset implementations independently evaluate the complete adaptive shattering recurrence for arm lengths one through twelve. The program checks the exact concept-count formula, all twelve online dimensions, the explicit product-threshold lower bound, and that the first deficit of at least two bits occurs at arm length twelve. Its final line must read `SPIDER_CONNECTED_SUBTREES_ALL_CHECKS_PASS`.

`spider_root_profile.py` computes the complete list of possible first-query positions up to arm symmetry and both conditioned online dimensions for twelve-edge arms. Compare its output with `spider_root_profile.csv`.

Scientific limits: only the twelve computed finite online dimensions have exhaustive upper certificates; the all-arm VC equality and adaptive lower bound have separate structural proofs. These are self-contained finite checks, not independent external certification. Historical-priority uncertainty remains.
