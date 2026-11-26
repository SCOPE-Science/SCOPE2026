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

At depth at most one, modal arguments are propositional and their truth sets run over every subset of the m=2^k valuations. The overlap case gives the zero test vector; with disjoint nonempty supports the inclusion-minimal positive tests are exactly the supports, so their unordered pair is recovered. The root minterm supplies the extra valuation coordinate, independently, and conjoining all signed tests and that minterm isolates each type, making all unions definable. Inclusion-exclusion on the three-way assignment of each valuation gives 3^m−2·2^m+1 nonempty ordered disjoint pairs, and swapping acts freely; add the zero type, multiply by m, and take the powerset to obtain the two counts. Representatives require one distinct world per valuation in S∪T plus a root only when its valuation is missing. For existence, reserve exactly those worlds and give each agent a constant successor row consisting of its prescribed support-world block; whenever x sees y their rows agree, ensuring seriality, transitivity and Euclideanity. The null case is realized by a singleton. Partitioning all m valuations into nonempty supports gives the sharp lower bound m. In the displayed two-world frames with p true at a only, the agent-1 row at b changes from {b} to {a}, the root rows stay {a},{b}, and Dp changes from (true,false) to (true,true), so D(Dp) is true at the first root and false at the second. All rows satisfy the KD45 condition, and on a singleton all D-subformulas are false by seriality. No finiteness assumption on input models was used, only a finite alphabet; the frozen checker was inspected, not executed.

## originality

PASS

Credit both the older modality/framework and exact extensional support-signature coverage in the indexed observability result. The distinct supported result is the finite-vocabulary depth-one semantic/type algebra together with sharp representative-world minima and the minimal two-world nesting separation, not the set-pair count in isolation. Chen–Pan and Fan remain named access risks; no claim of exhaustive priority is made.

## value

PASS

This is a complete small-model classification for a standard bundled modality, with an exact world cost for each definable type rather than just realizability, a sharp alphabet-sized satisfiability bound, and a smallest-frame obstruction to reducing iterated disagreement to the unnested fragment. Together these give concrete expressivity and model-size benchmarks. The straightforward Boolean powerset count alone would not carry the value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
