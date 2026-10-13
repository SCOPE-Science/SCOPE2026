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
# Verification

Run `python3 verify.py` beside `census.cpp` and `certificate.json`.

A published structural theorem for binary complete reachability guarantees a full-cycle letter. The C++ census fixes it as \(b(q)=q+1\pmod n\) and enumerates every map \(a:Q\to Q\) for \(2\le n\le8\). For each automaton it performs exact breadth-first search from the full state set in the power automaton, so every recorded reaching threshold is a shortest-path distance. Complete reachability is equivalent to reaching all \(2^n-1\) nonempty subsets.

The checker verifies the complete-reachability counts, absence of Don violations through \(n=7\), the \(544\) normalized violations at \(n=8\), the fact that every such violation is a unique six-state target of distance \(17\), and the \(68\) cyclic-relabeling orbits.

A separate Python implementation then reconstructs the displayed representative, independently reaches all \(255\) nonempty subsets, confirms the target distance \(17\), replays `abbbbbbabbbbbabbb`, and verifies that this target is the representative's unique Don violation.

Independent audit has not been performed.
