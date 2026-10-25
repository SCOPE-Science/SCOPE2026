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

# Verification of the stated theorem

Run `python hk_contact_monotonicity_verifier.py` using only the Python standard library. The checker uses exact rational arithmetic for all first-update and random-sequence contact comparisons, then tests the harmonic cycle energy expression numerically. Its output from the provided file is:

```
PASS
Exhaustive exact first-update cases: 163105
Exact high-degree witness graphs: 23
Exact randomized path/cycle updates: 84000
First-mode spectral tests, cycle lengths: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
```

The exhaustive domain is **all labeled simple graphs with at most four vertices**, with each vertex's scalar initial opinion in \(\{-2,-1,0,1,2\}\), confidence radius \(1\), and every possible first activated vertex. The finite random-path/cycle cross-check covers more update sequences, but does not exhaust them or the continuum of initial opinions. The cycle spectral cross-check uses floating-point arithmetic with tolerance \(10^{-11}\). The published proof, not the tests, establishes the theorem for arbitrarily large finite networks, arbitrary initial real vectors, and every activation sequence. No independent audit has taken place.
