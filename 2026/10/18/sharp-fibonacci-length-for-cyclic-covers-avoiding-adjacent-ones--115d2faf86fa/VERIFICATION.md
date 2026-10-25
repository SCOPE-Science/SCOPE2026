---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

All n>=2 linearly admissible n-words avoiding 11 form arcs in a strongly connected directed overlap graph on admissible (n−1)-words, whose base arc count is F_(n+2). For each arc 0u0 with u avoiding 11 and containing 1, duplicate it: there are F_n−1, and a direct degree calculation gives in-degree = out-degree at each vertex; strong connectivity yields an Euler cycle whose periodic spelling is legal and covers every linear admissible window with claimed multiset. For lower bound, integer vertex potential phi = number of leading zeros before first one (or n−1 if none) obeys phi(tail)−phi(head)<=1 on every permissible arc and equals 1 on every duplicated arc. Subtracting one mandatory copy of each arc from arbitrary closed covering walk yields a nonnegative balanced corrective flow whose potential sum is F_n−1, proving at least that many extra traversals. This dual bound is unrestricted, not inferred from finite counts. Independently regenerated all allowed arcs, degree-balance and potential inequalities for n2..10; supplied check.py covers n2..17 and exhaustive shorter binary cycles n2..5.

## originality

PASS

The all-linearly-admissible constrained cyclic superstring is a directed route-inspection instance but differs in demanded arc set and objective from classical restricted de Bruijn cycles; the exact Fibonacci minimum and explicit optimal repeated arcs are best-of-knowledge new. Generic postman min-cost flow is prior; its application alone would not state the closed formula.

## value

PASS

Shortest cyclic superstrings representing every binary no-11 linear word are natural constrained universal-window objects, and the gap from impossible strict de Bruijn coverage demands an exact repeated-arc optimum. The result gives a complete all-n Fibonacci length, a concrete optimal cycle multiset, and a sharp combinatorial dual potential, useful as a benchmark for constrained sequence coverage beyond a finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
