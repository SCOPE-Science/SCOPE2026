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

# Reproducible verification

Run `python3 verify.py` from the package directory with Python 3 and no third-party modules. The script constructs every transition of the explicitly indexed automaton and uses breadth-first subset dynamic programming with distinct-letter path counts to check the shortest length and exact number of shortest reset words across 37 parameter pairs, including all displayed range endpoints. The script separately generates *all* admissible labeled event permutations for four small parameter pairs and checks one-to-one decoding into distinct reset words. It also tests 1,008 seeded random valid event permutations at larger parameters and an excluded-parameter boundary case. The actual recorded replay appears in `verify_output.txt` and ends with `VERIFY_OK`.

These computations provide finite falsification checks only, not a proof for unbounded parameters. The universal assertion rests on the token conservation, event-bijection and independent-arrival-time integration in `RESULT.md`. Independent external mathematical auditing has not been performed. Historical data, external verification channels and publication priority were not certified by the standalone script.
