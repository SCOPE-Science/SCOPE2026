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

The included sources `verify.py` and `verify.cpp` are executable using Python 3 and a C++17 compiler, respectively. Both were run against their supplied source paths, with outputs:

- `VERIFY_OK max_size=8 zero_containing=30 total=240 affine_orbits=1 no_size9`
- `VERIFY_OK zero_containing=30 max=8 all_linear=true nodes8=32897 nodes9=24790`

The first script checks the complete affine orbit, whereas the second uses pair-forbidden masks and checks an independent exhaustive search. Both derive their candidate universe from the 64 length-six bit masks. Translation-to-zero plus heredity validates the global upper bound. No result for longer blocklengths or independent outside audit is implied.
