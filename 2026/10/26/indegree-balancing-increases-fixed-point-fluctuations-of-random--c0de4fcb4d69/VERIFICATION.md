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

# Reproducible checks

Both programs rely exclusively on the Python standard library and use exact integer and rational arithmetic. Execute `python verify.py` and `python convex.py` in a directory containing the two files. `verify.py` enumerates all 4, 27, 256, 3,125, 46,656, and 823,543 self-maps on orders 2 to 7; checks the signed profile covariance identity and its first-order vanishing; and verifies conditional first two moments through n=6. It also tests every sign from r=0 to n for selected n through 100. `convex.py` enumerates all integer degree partitions on orders 2 through 10 and compares stop-loss transforms of the exact fixed-point distributions for every majorization-comparable pair.

These are finite computations. The unrestricted convex-order theorem follows from the proved exact Robin Hood transfer identity; the unrestricted covariance identity follows from conditioning on two designated fixed points and a binomial decomposition. No infinite claim relies on finite enumeration. No external independent audit has been conducted.
