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

# Exact reproducibility checks

Run `python verify.py` using Python 3 with no additional dependencies. The checker uses integer tuples, set comprehension, and exact integer coefficients throughout. It builds every strong-chain relation from bounded column heights for all sizes from one through seven, then evaluates the necessity operator on *all* upward-closed subsets without using the theorem's prefix-maximum formula. It separately checks the record/profile equivalence, Catalan numbers, singleton counts, entire fiber sets, cardinalities and edge-number polynomials. For the first four sizes, every ordered pair of relations is composed by enumerating intermediate worlds and checked against the calculated composition of profiles. It also detects that the source semigroup's left identity is generally not a right identity.

Output from the replay:

```
n= 1 frames= 2 modalities= 2 singleton_fibers= 2 checks= 29
n= 2 frames= 6 modalities= 5 singleton_fibers= 4 checks= 152
n= 3 frames= 24 modalities= 14 singleton_fibers= 8 checks= 1463
n= 4 frames= 120 modalities= 42 singleton_fibers= 16 checks= 30918
n= 5 frames= 720 modalities= 132 singleton_fibers= 32 checks= 33611
n= 6 frames= 5040 modalities= 429 singleton_fibers= 64 checks= 50452
n= 7 frames= 40320 modalities= 1430 singleton_fibers= 128 checks= 177137
VERIFY_OK 177137 exact assertions; 46232 accessibility matrices screened; all operators evaluated on every upset through n= 7
```

This verifies finite instances only, not every natural number. The general theorem rests on the explicit proof in RESULT.md. Independent audit has not yet been performed.
