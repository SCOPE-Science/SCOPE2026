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
# Verification evidence

The programs `check_types.py` and `check_types.cpp` are standalone exhaustive implementations of the rank-four extension-type recurrence in `RESULT.md`. They have been executed from the actual included sources, and their complete stdout is given in `python_output.txt` and `cpp_output.txt`. Both report fourteen root classes, with singleton classes at sizes one through thirteen and one common class at sizes fourteen through seventeen. The two separate one-point output vectors exhibit the same sets of exact rank-three one-point types for sizes fourteen and fifteen.

Each program enumerates all possible tuple entries, including equality repetitions, and represents extension choices by **sets** of child types; sorting and lossless interning eliminate probabilistic hash-collision assumptions. The mathematical induction proving this recurrence is included in `RESULT.md`. No extrapolation from sizes seventeen and above is made: the infinite tail is justified by the published first-order linear-order theorem and a quantifier-free reduct argument.

Limitations: the finite certificate does not independently establish the published linear-order theorem; it applies only to this precise strict betweenness signature. Independent external validation has not been performed.
