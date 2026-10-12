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

# Reproducible finite verification

From the same directory, run `python3 verify.py` using standard Python 3. The program constructs the length-one through length-five prefix/right partitions, builds the entire length-six code as sets of integer tuples, and independently tests the defining absence of all five possible proper overlaps using global prefix/suffix sets. It checks all integers \(1\le a\le8\) for the cutoff restriction. Expected successful output:

```text
VERIFY_OK q=9 n=6 size=33872 L=(2, 12, 88, 640, 4656) R=(7, 2, 0, 0, 0) prefix_suffix_disjoint=yes restricted_max=33614 gap=258
```

The codeword list is finite and produced deterministically from the formulas in the proof. This finite verification confirms an existence proof rather than substituting finite evidence for an infinite universal statement. The impossibility of a *maximum* code meeting the cutoff uses the full algebraic enumeration of all possible cutoff representations at the fixed parameter pair. The construction does not determine the unrestricted exact maximum, and an independent audit has not been performed.
