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

# Finite verification and logical scope

Run `python3 verify_rotation.py` using the Python 3 standard library. This program enumerates all perfect matchings and all subfaces of their simplices for \(n=4,6,8,10\); constructs the automorphism on graph edges rather than assuming fixed-face counts; compares all invariant simplices with the exact orbit classification for both one- and two-step rotations; calculates reduced Lefschetz numbers using their signed cycle counts; and computes exact reduced binary boundary ranks for \(n=4,6,8\).

Expected completion marker:

```
VERIFY_OK 4 perfect-matching enumerations; 8 complete fixed-simplex checks; 3 exact reduced mod-2 chain computations
```

For the even parameters \(n=4,6,8\), the nonzero reduced mod-two Betti number is two in degree \(n/2-1\); all other degrees vanish. For \(n=10\), the checker verifies the matching and fixed-face classification, but intentionally does not compute homology, which would require larger matrices. The checks do not establish the infinite case or identify integral torsion independently. The infinite statement depends on the explicit orbit argument, the standard reduced Lefschetz identity, and the cited published homotopy classification of Agarwal and Basak. There is no independent audit of this result.
