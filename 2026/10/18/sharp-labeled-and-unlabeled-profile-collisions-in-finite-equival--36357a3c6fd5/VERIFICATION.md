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

# Verification and reproducibility

Execute `python3 verify.py` with a Python 3 interpreter. The program has no third-party dependencies. It computes direct quantifier-free atomic signatures separately from the integer-partition/factorial/Stirling model and tests the exact first-collision classification.

Observed execution result:

`VERIFY_OK partitions_tested=44 injective_profile_checks=240 direct_tuple_assignments=626590 first_nondegenerate_labeled_collision=n5 first_nondegenerate_unlabeled_collision=n4 n5_injective_profile=(1, 2, 4, 7, 10)`

The program enumerates equivalence-class-size partitions on one to seven elements, checks each possible injected labeled relation by direct enumeration, compares type counts obtained from direct tuple assignments against the stated formulas through arity five, and tests the special five-element pair through arity seven. The full infinite-arity equality of profiles and all-cardinality counting formula require the mathematical proof in `RESULT.md`; finite enumeration alone does not establish them. This is a local computational check and not an independent scientific audit.
