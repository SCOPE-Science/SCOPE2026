---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Write the inner conjunction as B=¬□a∧¬¬a. On the two-world chain with universal R, a false at the bottom and true at the top, every box test for a sees the bottom and every order test for ¬a sees the top; therefore □a and ¬a both fail everywhere, B holds everywhere, and □B witnesses the failure of ¬□B at the root. Universal R satisfies both confluences and is reflexive and transitive; the valuation is upward closed. On a one-world IS4 frame, box is identity and intuitionistic negation is Boolean, so B is false for both valuations and F is true. On a singleton IK4 frame empty R is transitive and confluent vacuously, makes □B true independently of a, and refutes F. A refutation needs at least one world. These cases prove the exact minima under the cited semantics.

## originality

PASS

Example 2.6 already gives this formula and its IS4 nonprovability. The distinct claim is exact cardinality in both semantics, including the optimal two-world construction and exclusion of all IS4 singleton models. No checked prior statement gives that conjunction of results or implies it by the general finite model property alone.

## value

PASS

The example was independently motivated by a real looping failure mode in proof search. The exact IS4 size is a useful minimal benchmark: the loop occurs even when just two worlds suffice and a one-world closure would be invalid. The IK4 singleton provides a clean semantic control in which removing reflexivity removes even that one-world obstruction. The combination separates intrinsic countermodel size from the size behavior of the naive construction without claiming a general bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
