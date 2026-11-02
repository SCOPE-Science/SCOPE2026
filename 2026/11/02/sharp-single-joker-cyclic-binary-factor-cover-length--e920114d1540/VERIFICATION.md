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

# Computational checks and limits

Run `python3 one_joker_cover_verifier.py` with Python 3 using only the standard library. The program constructs the retained-edge Euler trail and checks the completed cyclic word by independently scanning all its cyclic windows and both joker substitutions. It prints:

```
k=1 length=1 distinct=2 excess=0
k=2 length=3 distinct=4 excess=1
k=3 length=6 distinct=8 excess=1
k=4 length=13 distinct=16 excess=1
k=5 length=28 distinct=32 excess=1
k=6 length=59 distinct=64 excess=1
k=7 length=122 distinct=128 excess=1
k=8 length=249 distinct=256 excess=1
k=9 length=504 distinct=512 excess=1
k=10 length=1015 distinct=1024 excess=1
k=11 length=2038 distinct=2048 excess=1
k=12 length=4085 distinct=4096 excess=1
VERIFY_OK k=1..12, checked_window_positions=8123, short_host_exhaustion=4118
```

Additional direct structural tests at orders 4–14 checked all removed edges ending in one, all append-one paths from nonexceptional vertices, and all four retained edges joining exceptional vertices. These tests corroborate the connectivity lemma. The proof in `RESULT.md` verifies the graph-theoretic construction for all orders without assuming any finite search implies an infinite theorem. The external literature comparison is not a substitute for an independent scientific audit.
