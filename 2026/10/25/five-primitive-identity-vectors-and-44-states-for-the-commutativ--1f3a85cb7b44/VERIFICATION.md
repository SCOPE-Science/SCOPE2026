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
Run `python3 verify_s4.py` using the standard library. It constructs the 24 permutations of four symbols, computes all products represented by each of the 325 Parikh pairs with total length at most 24, checks the exact five-generator monoid equality for all those pairs, and tests five explicit identity witnesses and generator irredundancy. The algorithm then checks a separate length-100 membership profile and constructs a reachable 65-state complete DFA. Two independent finite partition procedures agree on precisely 44 right quotients, with every pair of different quotients separated by a suffix of length at most seven.

# Scientific proof limit
The finite group-state pigeonhole lemma is what extends the exhaustive length-24 computation to every word length. The length-100 tests provide independent finite corroboration only. Exact matching checks of the supplied Python code were run; no independent audit has been performed.
