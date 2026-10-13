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

Run `python3 verify.py` with Python 3 and no external dependencies. Observed output:

```
VERIFY_OK regular_exhaustive_cases 8 regular_colorings 15137 nonregular_colorings 6102 direct_modal_closures 330 binary_three_level 384
SHARP_DEPTH_OK levels 7
```

The verification enumerates every specified coloring of eight small level-regular hierarchies and six nonuniform hierarchies, independently compares fixed-point ordinary modal partitions to rooted-tree rigidity, and checks the regular-hierarchy counting formula. A separate direct closure routine constructs the Boolean algebra under named diamonds for 330 random colorings. It also verifies a recursively built sharp-depth family through height seven. The code and its assertions are part of the package. This is finite experimental support, not an independent mathematical audit or proof of the unrestricted statements.
