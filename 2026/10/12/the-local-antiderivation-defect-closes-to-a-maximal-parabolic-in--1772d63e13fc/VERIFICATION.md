---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For the four-dimensional complex Lie algebra [e4,e1]=e1, [e4,e2]=-e2, [e4,e3]=e3, solving the defining antiderivation linear equations gives an 8-dimensional space. Necessary tests on e1,e2,e3,e1+e3 constrain the local maps to the displayed ten-dimensional block-triangular space; the casewise antiderivation witnesses for x4 nonzero, x4=0 with x2 nonzero, and x4=x2=0 prove sufficiency for EVERY complex vector, not just a sampled grid. The exact triple commutators [[D0,E12],E21]=E11-E22, [[D0,E12],E23]=E13 and [[D0,E21],E32]=E31 add precisely the three missing dimensions; the resulting 13-dimensional space stabilizes U=span(e1,e2,e3), is a Lie subalgebra and hence triple-closed. Ordinary pairwise brackets generate those same directions. Independent rational symbolic linear-rank/commutator checks yield dimensions 8,10,13,13. This establishes precisely the single four-dimensional example, not a general closure theorem.

## originality

PASS

The identical 10-dimensional local antiderivation space and one escaping triple bracket are PRIOR ART in Hao–Chen; the 13-dimensional generated Lie-triple system and its identification as a maximal parabolic, including one-step generation, are not given in the inspected 10-page source. They are not direct formal consequences of the single exhibited escaping bracket; the three missing directions and upper closure must be computed. Resultary semantic search found only unrelated local structures (not a coverage certificate). Best-of-knowledge new structural completion.

## value

PASS

The initiating counterexample shows lack of triple closure but leaves the size and structure of its generated closure unknown. Identifying the exact 13-dimensional maximal parabolic and proving all new directions arise in a single triple layer measures the entire defect and supplies a concrete benchmark for local antiderivation/reflexive-hull structural questions. This is a motivated closure classification of the original example, not simply a parameter relabeling or new name for its known escaping bracket.

The dated certificate retains the supplied scientific assessment, sources and limitations.
