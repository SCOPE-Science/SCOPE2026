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

# Verification scope
The Python 3 program `verify.py` independently evaluates representation counts and semigroup reachability for all integers from zero through the proved upper bound in each of 27 cases, starting indices 4 through 30. It checks 2,622,124 integer states. Run with `python verify.py`. The file `verification_log.txt` records the actual output.

It also checks every Betti-translate membership against the property of having at least two factorizations, the congruence-class dichotomy, both exact first generalized invariants on positive residues, and the strict Frobenius inequality elsewhere. It does not test the unbounded theorem for all starting indices; the proof depends on universal polynomial identities and the published general freeness/Betti/Frobenius statements.

No independent audit has been performed.
