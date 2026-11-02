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

# Reproduction notes

Run `python3 verification/check_firefly.py` from the extracted standalone package directory. The script uses only the Python standard library and does not fetch external data. It reconstructs the finite two-clock transition map as well as a separate full-agent parallel majority test. Checks made during preparation: 81,330 agent-level equivalence instances and all 6,779,342 phase states over 2,553 integer parameter pairs \(4\le C\le72\), \(1\le w<C\), with all exact cycles, basin counts, and explicit nontrivial wave coordinates verified.

The analytic proof in `RESULT.md` (steps 1–5) establishes the result for all integer parameters. Replaying the finite program is not a proof of infinite-parameter exhaustiveness and does not validate changes to the update order, flash-onset timing, graph topology or group-size assumptions. There is no independent external validation.
