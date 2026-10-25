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

# Arithmetic verification and limits

Execute `python3 verify.py` with a Python 3 interpreter; no third-party modules are required. The exact-integer independent congruence method verifies the semigroup membership tests, together with the claimed gap, genus, and Frobenius consequences for all coprime pairs \(2\le a\le90\), \(1\le k\le50\). A separate exhaustive decomposition check compares predicted and observed minimal generators for the odd parameters at \(k=2\). The observed successful output was:

`VERIFY_OK parameter_pairs=2721 checked_memberships=267879 maximal_embedding_examples=44 integer_exact=PASS finite_only=YES`

These are finite regression checks. The unrestricted theorem is justified by the constructive argument in `RESULT.md`. No external or independent mathematical audit has been performed, and the checks do not certify publication priority.
