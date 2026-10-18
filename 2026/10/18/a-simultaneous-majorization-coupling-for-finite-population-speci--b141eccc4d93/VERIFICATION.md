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

# Reproducible checks

Run `python verify_rarefaction.py` using Python 3 (standard library only) in the directory containing this file and the script. The program has no network or external dependencies.

The executed program checked all 506 nondecreasing positive integer partitions of total size at most 14; all 1,846 directed unit abundance-balancing transfers; 24,966 transfer/sample-size combinations; 150,643 exact integer upper-tail identities and inequalities; and 280 direct enumerations of binary pair-discovery times. All checks passed. It also verifies the stated example and exact expected gain strictness range. Every comparison is an exact integer equality or inequality, not floating-point sampling.

The general claim rests on the analytic coupling, counting, and majorization proofs in `RESULT.md`. Finite enumeration does not certify an infinite theorem, nor does it establish originality. The origin of the first public motivating source and the literature comparisons are documented in the references; independent audit remains unperformed.
