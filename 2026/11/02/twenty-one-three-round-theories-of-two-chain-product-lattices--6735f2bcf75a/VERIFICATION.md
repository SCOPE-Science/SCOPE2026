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

# Verification procedure

From a directory containing the two Python programs, run:

```sh
python3 verify_grids.py
python3 verify_game.py
```

Both are standard-library-only and deterministic. Their exact finite-set computations agree on the 21 three-round equivalence classes among the complete list of 28 normalized rectangles of side lengths at most seven. `verify_grids.out` and `verify_game.out` record the checks and complete class assignments.

The programs do not directly enumerate infinitely many rectangles. That step relies on the proof that three-round EF strategies on sufficiently long chains compose coordinatewise to produce a three-round EF strategy on the product order. The cutoff is seven per coordinate, giving the exhaustive 28-case reduction. Quantifier rank four and higher is not tested or claimed.
