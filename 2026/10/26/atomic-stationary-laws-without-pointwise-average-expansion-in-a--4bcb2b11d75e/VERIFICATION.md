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
# Reproducibility and analytical scope

`CHECK.py` enumerates exactly the 16 possible four-bit prefixes at both endpoint probabilities and computes every certificate inequality in rational arithmetic. Its minimum strict slacks are respectively `3409/170000000` and `268567/10200000000` when the target contraction factor is `3999/4000`. It also cross-checks the binary rewriting and denominator-depth changes against exact rational evaluations of both circle maps for 504 finite states with depths 4 through 9. `CHECK_OUTPUT.txt` is a record of actual execution from this standalone source.

The proof of the all-depth drift is analytic: the first three bits and the depth change of each output depend only on the first four input bits for every state of depth at least four. The probability dependence is affine. Tightness, stationary existence, exponential moment, and uniqueness are deduced from a proper drift function and accessibility, not from the finite state enumeration. The result makes no statement concerning arbitrary non-dyadic initial states.
