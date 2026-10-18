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

# Verification and exact scope

The finite computations are reproducible from the two included Python scripts and their captured stdout files. They do not replace the general argument. `verify_global.py` checks all 1,596 Young shapes through 18 cells and compares global fingerprints computed with the same colour names across all shapes of each fixed size. `verify_cellwise.py` tests 1,806 further shape instances, checks binomial root-path counts and separately computes stable classes. The latter comprises 124,300 cells with a fixed PRNG seed; this is sampling, not exhaustive enumeration of large sizes.

Checks performed: both programs ran to completion, the logs were inspected for their concluding PASS markers, and the all-parameter proof was checked separately for preservation of incoming/outgoing neighbour multiplicities, the off-diagonal propagation argument, and the global histogram comparison. A stable equitable partition ensures all root-walk counts are constant within classes, providing the invariant used in the proof. No independent audit has been performed, and no assertion outside the stated Young-diagram family is verified.
