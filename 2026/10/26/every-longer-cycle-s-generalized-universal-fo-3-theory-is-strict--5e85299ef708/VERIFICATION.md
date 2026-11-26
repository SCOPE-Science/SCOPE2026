---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The fragment is the three-variable universal closure under conjunction and disjunction of literals, with equality. Negation pushed through the formula yields the dual existential fragment with the same variables. For an assignment from C4 paired with one from C_n, require all three pairwise distances (0, 1 or 2) to agree. After rebinding one variable, the two retained square positions are equal, adjacent or opposite. If equal, a position at any requested distance 0, 1 or 2 exists in C_n. If adjacent, either copy one endpoint or use the off-edge neighbor of the appropriate endpoint; for n≥5 it is exactly distance two from the other endpoint. If opposite, their images are distance two apart, so copy an endpoint or choose the common neighbor on a length-two path. This suffices for either of the square's common neighbors because the moved variable's old value is not retained. The strategy preserves all literals, so structural induction gives E3 truth transfer from square to longer cycle at all depths. Starting from constant assignments and dualizing gives U3 transfer from longer cycle to square. The separator η expresses that every third distinct vertex meets an edge at one of its ends; this holds in the square and fails at (0,1,3) for every n≥5, including n=5. The independently written finite replay checked all 9,960 distinct canonical extension signatures over 5≤n≤1000 and the strictness witness; it is not the proof for unbounded n or formula depth.

## originality

PASS

The pentagon-to-square inclusion and the general assignment-extension proof template are credited to Andréka–van Benthem–Németi. The supported distinct contribution is the uniform inclusion for C_n with n>5, and the explicit separator witnessing the strict family relation. The original pentagon invariant is not sufficient uniformly; the added distance-two constraint is substantive. The inspected full-FO equivalence classification has a different conclusion and offers no such one-sided relation.

## value

PASS

The cycles come from a canonical counterexample in finite-variable preservation. Determining the relation of an entire natural family to the square resolves a genuine one-sided theory question, not just a finite formula test. The short distance invariant works uniformly at arbitrary formula depth and the explicit separator makes the inclusion sharp. This is a useful structural family lemma, not a new general preservation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
