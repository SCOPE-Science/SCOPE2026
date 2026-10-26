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

The included `verify.py` needs Python 3 with only standard-library dependencies. Run `python3 verify.py` from its directory. Its exact checks reconstruct the combinatorial transfer states, evaluate each state walk through size 122, and verify the degree-bounded polynomial identity required for the infinite generating function. It separately counts occurrences from all 128 codewords at size 9 and from all ordinary permutations through size 7, retaining only inversion trees. The complete proof of the finite-to-infinite step is in RESULT.md; a finite sample alone would not be a proof. No independent audit has occurred.
