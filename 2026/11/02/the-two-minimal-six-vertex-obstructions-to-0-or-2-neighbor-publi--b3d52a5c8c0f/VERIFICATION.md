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
# Verification and limitations

Run `python3 verify.py` in Python 3.8 or later. The standard-library script asserts all six connected-graph counts, zero no-equilibrium cases at orders one through five, exactly 300 at order six, two canonical graph classes with multiplicities 180 and 120, and the nonexistence of equilibrium for each displayed representative. The program is self-contained and deterministically traverses all edge masks, all binary actions, and all six-vertex vertex permutations for each exceptional graph. The general low-degree existence lemma and individual nonexistence proofs are mathematical arguments independent of this finite enumerator. No independent audit has been performed. Uniqueness of discovery or publication priority is not certified by finite enumeration or bibliographic searches.
