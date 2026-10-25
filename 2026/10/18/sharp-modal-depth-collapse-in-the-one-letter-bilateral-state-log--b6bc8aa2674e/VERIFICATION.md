---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

All formulas over one Boolean propositional variable are faithfully encoded as pairs of support/antisupport masks on the four teams empty, {v0}, {v1}, {v0,v1}; operations follow literal BSL clauses: ¬ swaps pairs, ∧ intersects support and takes union-convolution of antisupport, split ∨ convolves support and intersects antisupport, and ◇ applies upward nonempty-subteam reachability to support without changing antisupport. From primitives (1,15),(14,1),(5,3), independently recomputed least full propositional closure L0 of 39 masks; adding one modal level yields L1=64, L2=66, and L2 is closed under all operations including ◇. Structural induction gives universal depth<=2 collapse; the two masks L2\L1 are exactly (10,12),(12,10), witnessed by ◇¬◇p and ◇¬◇¬p. A genuinely independent eight-bit implementation recovered 39,64,66,66 and closure, confirming finite exhaustive rather than bounded syntax search.

## originality

PASS

Complete paired support/antisupport depth grading of one-letter BSL with exact 66-element algebra; prior expressivity theorems do not quantify these finite-depth minimal ranks.

## value

PASS

The finite one-generator bilateral algebra is a natural and canonical invariant of the exact semantics. Sharp modal-depth collapse, two explicit minimal-depth witnesses and exhaustive constructive coverage of 66 meanings refine expressivity in a way general completeness does not; finite does not make it arbitrary or valueless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
