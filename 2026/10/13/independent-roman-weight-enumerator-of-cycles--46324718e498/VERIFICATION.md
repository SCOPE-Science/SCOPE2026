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

The proof is symbolic for every \(n\ge5\). The accompanying `verify.py` is an independent finite stress test of definitions and boundary cases, not an infinite certificate.

For each \(5\le n\le12\), the program enumerates all \(3^n\) labelings of \(C_n\). It checks: (1) the independent Roman neighborhood definition; (2) equivalence with the three allowed cyclic gap patterns; (3) equality of the brute-force weight counts with the closed formula; and (4) the minimum weight and the exact number of minimum-weight functions.

Replay result:

`VERIFY_OK n_range=5..12 labelings=797040 irdf_functions=294 criterion_checks=797040 coefficient_checks=144 minimum_checks=8 max_order=12`

The finite range does not prove the arbitrary-order theorem; the gap argument in `RESULT.md` does.
