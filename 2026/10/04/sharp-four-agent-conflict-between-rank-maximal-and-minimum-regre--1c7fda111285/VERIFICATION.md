---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Independent exhaustive reconstruction in this audit reproduced the stable-matching count histogram \(1098\) profiles with one stable matching, \(150\) with two, and \(48\) with none, and reproduced the objective relation histogram \(1176\) equal, \(48\) rank-maximal proper subset of minimum-regret, \(24\) disjoint, \(48\) unsolvable. The actual verifier independently computes stability two ways, rank-maximality both lexicographically and by a steep exact scalar score, minimum regret both directly and by threshold, and then canonically quotients all disagreements under \(S_4\). For the canonical disjoint profile, the two stable matchings have rank vectors \((1,3,2,1)\) and \((2,2,1,2)\), so one uniquely maximizes the rank profile while the other uniquely minimizes regret.

## originality

PASS

Simola--Manlove's full primary preprint defines exactly the rank-maximal and minimum-regret objectives and studies their algorithms/complexity, but it does not enumerate all four-agent profiles or identify the sharp first conflict, relation frequencies, or relabeling orbits. Targeted Resultary and web searches for the four-agent census and disjoint conflict found no prior equivalent statement.

## value

PASS

The result isolates the first possible disagreement between two standard fairness/quality objectives in Stable Roommates and gives the complete geometry of that boundary, including exact frequencies and symmetry orbits. This is a meaningful finite cutoff rather than a disconnected computational statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
