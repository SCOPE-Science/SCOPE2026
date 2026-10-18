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
# Computational and proof checks

The two included scripts are standalone Python standard-library programs. Execute `python brute_cycle.py` and `python gap_cycle.py` in the extracted package. Each asserts every claimed finite identity independently and prints `REPLAY_OK` only after all checks. The corresponding `.out` files record reference outputs. The brute verifier tests the graph predicate directly on every selected vertex subset, independently of gap-word generation. The gap verifier uses run-word configurations and an explicit schedule of clockwise moves, including intermediate legality. The scripts are separate implementations and have no mutual imports.

The exhaustive range is finite and supplies regression checks, not a proof for all parameters. The infinite theorem is justified by the cyclic gap classification, composition counts, movable-token connectivity construction, conserved modular sum and floor-schedule cycle construction provided in `RESULT.md`. The observation that no odd closed walk of length below \(n\) exists uses actual integer sums of \(\pm1\) and is not deduced from incomplete graph exploration.

Scientific limitations: only simple cycles and nonminimum cardinalities are claimed. External originality and correctness audits have not been performed. Literature-indexing gaps remain possible.
