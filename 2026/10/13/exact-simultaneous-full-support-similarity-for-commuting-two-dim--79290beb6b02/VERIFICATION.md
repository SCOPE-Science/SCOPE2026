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
# Reproducibility and verification

Run `python3 verify.py` from the directory containing this file and `verify.py`. The script uses only Python 3 standard-library functions. It constructs small prime fields and extension fields, independently enumerates matrices by their four entries, compares predicted and actual full-support counts for every trace/determinant pair, constructs nonscalar similarity classes by conjugating companion matrices with every invertible matrix in fields of size at most five, and counts simultaneously admissible conjugates for all scalar-shift pairs in those fields. It also enumerates all shift triples when the field has size at most four and checks the explicit \(\mathbb F_5\) pair and \(\mathbb F_8\) triple obstructions. The run reports `VERIFY_OK` only if all assertions pass.

The script was executed successfully before this package was created. These finite computations do not prove the general statement. The unrestricted proof uses cyclic similarity classes, one quadratic determinant equation, and the exact forbidden-diagonal sets; its boundary argument uses translation pairs in fields of characteristic two.

No independent audit or external validation is represented by this verification document.
