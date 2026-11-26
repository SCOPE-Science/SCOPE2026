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

In the stated semantics all connectives preserve persistence under taking substates, including the modal clauses by their pointwise support. If every neighborhood of a contains a and {a} itself is a neighborhood, persistence gives E(theta) iff theta at a. At {a} the propositional clauses depend only on their subformulas there (implication checks also the empty state, which supports both formulas). Induction therefore gives locality at a for all atoms and all nesting depths. Both neighborhood families in the witness are upward; fixed p(a)=1 makes ?p true on {a} in both models, but {a,b} supports ?p exactly in the valuation with p(b)=1. Thus top implies ?p in the strict neighborhood sense differs while the existential fragments agree. On one world the empty neighborhood family makes the conditional vacuously true, and the only nonempty family makes it ordinary implication at the singleton. The displayed elimination formula expresses this split, is supported at the empty state as well, and can be substituted recursively. Independent semantic replay `python3 /workspace/audit_recompute.py 4` computed the closed set of 13 joint support denotations with local atomic agreement for the fixed two-world frame, checked the separating states, and checked the elimination table on both singleton frames. The structural proof covers the full language and proves minimality; the finite closure is corroboration.

## originality

PASS

The first of the published Open Problem 4.6 questions is exactly this existential-only/upward-monotone question. The distinct two-unary/convex result was compared at the level of its actual frames, not excluded by date or its headline. Its witnesses do not provide an upward-monotone separation. No inspected result supplies the same-frame two-world obstruction or one-world elimination.

## value

PASS

This resolves an explicit published expressivity question and identifies the obstruction: persistence turns existential neighborhood inspection into evaluation at the generating singleton, whereas the binary modality can test whether a larger neighborhood settles an atom. The one-world translation makes the countermodel size optimal. The separate question over convex frames with both modalities is not a contribution of this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
