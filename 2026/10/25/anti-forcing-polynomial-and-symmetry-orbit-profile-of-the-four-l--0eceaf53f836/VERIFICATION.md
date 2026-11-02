---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The 24 vertices, 36 edges and even/odd inversion bipartition are explicit. Every matching is enumerated uniquely by branching on the least uncovered vertex, yielding 169. Alternating cycles after contracting matching edges correspond exactly to directed cycles, and deleting nonmatching edges that hit every alternating cycle equals minimum feedback arc deletion. The subset dynamic program minimizes backward arcs over every topological order, so its 4096-state answer is an exact optimum. Independent private code rebuilt all 169 matchings from scratch, recomputed the complete coefficient table, generated all 48 group maps, 17 symmetry orbits, and checked the entire orbit-size/anti-forcing/two-factor-type table term by term against the claim. The source also supplies an independent hitting-set method for 17 orbit representatives; its code was read but the latter method was not independently reimplemented this execution. Exhaustion is genuinely finite here.

## originality

PASS

The alternating-cycle anti-forcing definition and computational reduction are established; the known general (4,6)-fullerene bound already gives maximum 10. No accessed primary theorem supplies the complete 169-matchings multiplicity polynomial plus 17-class orbit/2-factor profile. The full 2017 and 2022 fullerene papers remain a material priority risk; inaccessible literature alone does not negate the otherwise best-of-knowledge positive assessment.

## value

PASS

Exact anti-forcing multiplicities and 17 symmetry classes distinguish perfect matchings of a canonical Archimedean 24-vertex graph. Demonstrating that the complementary 2-factor type does not determine anti-forcing number is a nontrivial structural observation potentially useful in anti-forcing enumeration; the result is not merely re-computing the already known maximum. The exhaustive recurrence gives an independently reproducible finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
