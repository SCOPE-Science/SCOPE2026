---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For each n>=5 checked the exact b-action simultaneously on sources 0 and 2. Oriented descending gap recurrence excludes b(0),b(2) simultaneous no-gap moves, with admissible contraction sites L={0,2} except d=2 and n-2. Explicit u_d,v_d satisfy the recurrence; monotonicity and Bellman potential G(pair)<=1+G(a pair),1+G(b pair) rule out gap-increasing shortcuts, and the four critical starting phases yield sharp parity diameter. Independently constructed reverse pair graph and BFS checked ALL unordered pair distances for n=5..60 against the closed formula, not merely source verifier logs. All-n proof depends on closed symbolic parity/four-phase reduction.

## originality

PASS

The exact pointwise pair-distance and worst-pair diameter belong to a rank n-2 common two-merge letter, not the one-point contraction automata or the different two-merge automata of earlier reset-length analyses. Best-of-knowledge novel labeled pair metric.

## value

PASS

An explicit individual pair shortest-merger distance and sharp diameter are natural synchronizing automata invariants, clarifying pair compression separately from full reset length. The family has real two-merger interactions and parity boundary, not a routine generic corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
