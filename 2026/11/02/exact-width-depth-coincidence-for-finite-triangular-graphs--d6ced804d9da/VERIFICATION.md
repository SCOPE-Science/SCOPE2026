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

For T_n=L(K_n), n>=3, the p-pebble invariant explicitly maintains a bijection between underlying root endpoints of at most p pebbled edges. After recycling, <=2(p-1) endpoints remain and both n>=2p models have at least two fresh endpoints. This preserves graph vertex equality and adjacency at arbitrary depth. The same invariant survives a p-round ordinary Ehrenfeucht-Fraisse game. For each root cutoff 4<=s<=2p, a disjoint union of c=s-r nonempty paths with r=min(p,s-1) edges requires exactly s root vertices in every induced line-graph realization: nonconsecutive path edges are disjoint and different components share no endpoints. Existential adjacency diagrams of rank/width <=p distinguish n=s-1 from n>=s. The p=1 and n=3 boundaries are correctly separate. Independent induced-graph path forest enumeration for p=2..4 and 9 cutoffs corroborated. Thus both equivalences and least distinguishing width/rank floor(m/2)+1 are proved, not inferred from finite tests.

## originality

PASS

The sharp min(n,2p) collapse for both recycled width and rank, and all exceptional classes, is not stated in the inspected survey of logical complexity or nearby published Resultary multipartite-graph records. The endpoint-support EF technique is standard, so this is a family-specific sharp classification rather than a new general game theorem.

## value

PASS

The triangular/Johnson J(n,2) family is a central finite graph family. Equality between exact bounded-variable and bounded-rank spectra, including the sharp least-tail representative p(2p-1), gives a reusable logical-complexity benchmark beyond a routine one-off instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
