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

The complete proof is in `RESULT.md`. The independent Python 3 standard-library scripts here test several finite consequences, not unrestricted validity or historical priority.

Run `python3 verification/verify_fo.py` and compare stdout to `verification/fo_output.txt`. It computes stable partitions of atomic \(k\)-tuple types with coordinate-replacement successor sets, precisely the unrestricted-round \(k\)-pebble equivalence for the finite structures examined. It compares 2,415 pairs at width two, 2,415 at width three, and 105 at width four: all 4,935 match the predicted equivalence formula.

Run `python3 verification/verify_structure.py` and compare stdout to `verification/structure_output.txt`. It validates 3,203 canonical caterpillar structures, checks the local leaf-count witness construction in 45,180 configurations, and independently enumerates the reversal classes at 15 pairs of parameters.

The mathematical argument is necessary for arbitrarily large graphs, arbitrary numbers of variables and unlimited quantifier depth. The checkers do not supply independent mathematical auditing.
