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
The finite proof was replayed from the bundled files. `verify.py` directly constructs every one-deletion up-to-one-substitution error ball, builds the compatibility graphs, excludes a four-code at length seven, enumerates exactly 12 five-codes at length eight, proves that none extends to six, and verifies the four reversal/complement symmetry classes. It prints `VERIFY_OK`.

`independent_check.py` independently represents balls as Python string sets and uses a separate recursive clique enumerator. It reproduces the length-seven upper bound, the count of 12 optimal length-eight codes, and the nonextendability needed for the length-eight upper bound, and prints `INDEPENDENT_OK 3 5 12`.

The computation is exhaustive over all binary words at the stated lengths. No inference from finite experiments to larger lengths is made.
