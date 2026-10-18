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

# Reproducibility and scope

The complete executable certificate is `verify_rank2.py` (Python 3.9+, standard library only). Run `python3 verify_rank2.py` beside this file.

The code forms eight canonical coloured equivalence-class patterns; enumerates all \(3^8-1=6560\) nonzero truncated class-multiplicity vectors; computes the set of pointed rank-one witness patterns for each; groups exactly matching rank-two theories; computes minimum representative sizes in each class; and asserts the complete histogram, 207 count and two 13-element extremal vectors. It separately computes the full recursive rank-two type for every canonical finite structure, verifying that the two partitions agree for all 6560 representatives. No randomized or floating-point operations occur.

The reduction from arbitrary nonempty finite structures to those 6560 canonical models is a mathematical argument in RESULT.md, not a software inference. The independent recursive check is a second exact implementation within the same package, not independent external validation. Publication priority remains subject to unlocated literature, and independent audit has not been performed.
