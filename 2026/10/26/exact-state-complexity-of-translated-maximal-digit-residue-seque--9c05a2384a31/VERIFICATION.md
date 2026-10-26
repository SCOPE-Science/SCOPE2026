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

The exact proof and domain appear in `RESULT.md`. Running `python3 checker.py` from this directory produces `checker_output.txt`. The checker separately constructs reachable residual-state automata, minimizes them by iterative partition refinement, and compares with an interval digit-DP count; it also checks direct outputs and the adjacent-power identities. The saved test output reports 3,840 deterministic parameter comparisons, 300 additional random parameter comparisons, and 40,000 direct input checks, all passing. The finite tests cannot certify the theorem for all parameters. Independent scientific validation has not been performed.
