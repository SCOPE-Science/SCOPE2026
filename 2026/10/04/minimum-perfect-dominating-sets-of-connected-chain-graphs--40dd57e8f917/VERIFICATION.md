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

For an unselected vertex in \(A_i\), the number of selected neighbours is exactly the selected prefix count \(Y_i\); for an unselected vertex in \(B_j\), it is exactly the selected suffix count \(X_j\). This proves the full profile criterion directly. A singleton can dominate perfectly only when its own bipartition side has one vertex. With both sides of size at least two, every extreme pair \(A_p\times B_1\) works. If a selected B-vertex lies above \(B_1\), all lower A-blocks not adjacent to it must fit into the single selected A-vertex; dually for a nonextreme A-vertex. Combining the two constraints yields only the stated \(p=2\), \(\alpha_1=\beta_2=1\) exceptional nonedge. The exhaustive checker through order ten is corroborative.

## originality

PASS

Targeted chain/Ferrers searches and Resultary found no prior theorem with the prefix/suffix profile criterion or the exceptional nonedge minimum pair. The inspected 2021 paper overlaps only the one-block complete-bipartite boundary, while other primary literature treats grids or circular-arc algorithms. The audited theorem therefore survives best-of-knowledge originality, with a residual indexing risk typical for older chain-graph literature.

## value

PASS

Chain graphs are a canonical nested-neighborhood class, and the theorem gives the entire minimum perfect-domination geometry and exact count rather than only the parameter value. The exceptional nonedge boundary is a genuine structural feature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
