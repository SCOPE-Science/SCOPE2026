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

# Reproduction

Both programs use Python 3 with the standard library only. From an extracted artifact directory run:

```sh
python3 verification/coordinates.py
python3 verification/singer.py
```

The coordinate program checks the 13 point and 13 line representatives, closure and orbit disjointness of all 38,730 ideal states, seven cycle-length classes, the collineation generators' closure of size 5616, and all 22 projective orbit classes. The Singer program works with translated four-point lines modulo 13 and derives rowmotion from minimal elements of the ideal complement directly; it reconstructs 38,730 states, verifies a bijection, and checks the identical cycle census and permutation order 6930.

Neither implementation proves a result for arbitrary projective-plane order. The finite computations and complete state spaces are the evidence here; no outside independent scholarly audit has been performed.
