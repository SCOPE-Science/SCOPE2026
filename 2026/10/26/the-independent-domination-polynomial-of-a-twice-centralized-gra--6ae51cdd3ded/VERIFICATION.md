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

# Reproduction and scope

The Python standard-library file `verify.py` constructs the ordinary central graph twice from each host graph and enumerates all maximal independent sets of the resulting graph using a clique search on its complement. Those are precisely the independent dominating sets. Its output histogram is compared at every degree to the explicit polynomial, with a separate check of the minimum-set counting classification for orders at least four.

Run `python3 verify.py` with Python 3.8 or later. Recorded result:

```
n=3 exhaustive connected labelled hosts=4
n=4 exhaustive connected labelled hosts=38
n=5 exhaustive connected labelled hosts=728
n=6 seeded connected labelled hosts=100
VERIFY_OK host_graphs=870 independent_domination_sets_checked=21149
```

The finite tests enumerate every connected labelled host on at most five vertices and 100 deterministic pseudorandom connected six-vertex hosts; they do not exhaust all graphs at six vertices or prove the general result. The mathematical proof in `RESULT.md` establishes the infinite family via an explicit bijection and a complete clique classification.
