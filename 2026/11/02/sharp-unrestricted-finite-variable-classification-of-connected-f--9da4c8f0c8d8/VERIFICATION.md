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

The stated unrestricted-depth theorem is proved mathematically in `RESULT.md`. The following standalone runnable standard-library Python sources provide finite corroboration:

`python3 verify_structure.py` regenerates the structural enumeration and prints the exact reference output in `structure_output.txt`. It covers all 819 labelled positive-block parameter choices with one to three levels and block sizes in \(\{1,2,3\}\), and verifies the rank/twin schema and Burnside counts for three cutoff values.

`python3 verify_logic.py` computes no-counting \(k\)-variable replacement refinement to stabilization over 524 canonical parameter choices (and targeted sharpness pairs), comparing stable diagonal types against clipped staircase parameters. Its exact output is in `logic_output.txt`.

Both scripts were run successfully against their embedded-output counterparts. They do not constitute an exhaustive test over unbounded parameters or independent proof certification. Independent audit is not yet performed.
