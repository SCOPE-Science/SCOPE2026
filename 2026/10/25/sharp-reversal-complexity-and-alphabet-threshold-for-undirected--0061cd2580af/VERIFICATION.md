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

# Verification record

To reproduce the finite checks, run `python verify.py` with Python 3.9 or later and no third-party packages. The program builds each specified involutive transition, enumerates reachable subset states, minimizes the reverse automata by partition refinement, and directly tests word reversal. It also enumerates all transitive pairs of involutions for state sizes two through five and checks the binary threshold in the exceptional cases.

Observed output:
```
VERIFY_OK parameters 36 word_membership_checks 118080 exhaustive_transitive_two_letter_pairs 159 largest_witness_reverse 126
```

The complete proof and quantifiers are in `RESULT.md`. Computation is exhaustive only over the explicitly specified finite ranges, and the checks do not establish or certify the infinite theorems. No external or independent mathematical validation has been performed.
