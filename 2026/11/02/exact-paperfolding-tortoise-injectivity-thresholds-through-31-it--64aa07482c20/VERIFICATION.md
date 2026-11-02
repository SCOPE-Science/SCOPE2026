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

The paperfolding factors are complete for each tested length by the explicit residue-class and single-exception argument in RESULT.md; this is a finite certificate for a mathematically infinite factor set, not empirical prefix sampling. At each listed threshold the first checker verifies injectivity and an exact minimum one-count; at the predecessor it exhibits two unequal words with the same iterated tortoise image. The inheritance lemma establishes all greater lengths, while a predecessor collision establishes sharpness.

Execute `python3 verify_skeleton.py` and `python3 verify_prefix.py` with the CSV in the same working directory. Recorded output is in `skeleton_output.txt` and `prefix_output.txt`. Scripts require only Python 3 standard-library modules. They were executed with the included files and returned successful verification for all 62 finite cases. The second method uses a paperfolding recurrence and repeated one-step tortoise, not the first method's skeleton generator or deletion implementation.

Limits: depth \(k\) is restricted to 1--31. The calculations do not establish a formula for unrestricted depths. An independent audit has not been performed.
