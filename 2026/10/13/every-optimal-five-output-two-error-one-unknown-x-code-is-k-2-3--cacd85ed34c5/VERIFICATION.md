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
# Verification

The package proves a finite statement and performs no probabilistic or floating-point computation. Run `python3 artifacts/verify.py` from the package root.

The replay exhausts all \(736281\) six-subsets and all \(2629575\) seven-subsets of the \(31\) nonzero vectors in \(\mathbb F_2^5\). On every candidate it compares a direct OR/XOR X-code predicate with an independently coded support-set predicate. It also performs a separate include/exclude search, compares the resulting ten maxima with `artifacts/census.json`, and enumerates all \(120\) coordinate permutations.

Expected terminal line:

```text
VERIFY_OK M(5,2,1)=6 labeled_maxima=10 all_K23=true S5_orbits=1 orbit_size=10 stabilizer=12
```

Scientific limits: the computation establishes only the stated finite binary parameter and its equality layer. It does not extrapolate to larger \(m\) or other \((d,x)\). The absence of size seven is exhaustive rather than a timeout or failed search.

Artifact hashes used in this review:
- `artifacts/verify.py`: `d0425ee1a147635addd8d095cb2233b1e7cc0ee7eabe1d9b3ad63acf64ffff0c`
- `artifacts/census.json`: `eaff0c285f1905b3b48cbf90b010827af3d8633cd6ea5285b22e6c0639f5e6b6`
- `artifacts/verification_output.txt`: `ae2e234bb963007abd77448db16fa4e02ea2c50b33ffde1dc67f2c5dfa9bbf42`
