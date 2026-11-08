---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For Q4 the graph condition is exactly selected vertices have at least two selected neighbors, and unselected vertices at least one. All 2^16 masks were examined by source and by separate independently implemented C++ enumeration. For Q5, write D=A∪B' by Q4 layers; any D satisfies the 2-limited constraint iff P(A)∧P(B)∧R(A)⊆B∧R(B)⊆A, where P requires ≥2 within-layer selected neighbors at each selected vertex and R selects the deficits (selected with exactly two, or unselected with none). This is an exact decomposition of every 32-bit set. Both programs enumerated all 8122 possible layers and all 8122²=65,966,884 ordered pairs without early pruning; independent output exactly 16 and 1830, while Q4 gives 8 and 428. The coordinate flip/adjacent-coordinate-swap generators span the entire cube automorphism group and independent BFS agrees with all six orbit sizes and canonical reps. This is exhaustive finite proof for Q4,Q5, not an inference to larger cubes.

## originality

PASS

Tepeh 2026 arXiv:2606.22428v1 presents k-limited domination and explicitly leaves the k=2,d=4,5 hypercube Table 3 cells blank; its available k=1 cube values only give upper bounds and k=d−1 total domination has a different condition. Božović studies Sierpiński graphs. The new finite values and full minimizer orbit enumerations are not directly covered by these primary statements. Later revisions and unindexed hypercube (1,d−2)-domination tables remain a risk.

## value

PASS

Two consecutive naturally missing cells in an explicit hypercube parameter table, combined with full labeled optimum counts and group-orbit classification, are motivated exact invariants of central symmetric regular graphs. They quantify not merely cardinality but optimizer degeneracy; no arbitrary subset of examples or extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
