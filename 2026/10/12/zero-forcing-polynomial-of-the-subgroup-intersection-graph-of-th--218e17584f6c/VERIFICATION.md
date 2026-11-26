---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The maximal subgroups are the inverse images of the p+1 lines of G/Z, and any noncentral cyclic subgroup of order p is confined to the one maximal subgroup belonging to its image. The order-p subgroups in each elementary abelian maximal subgroup other than the center are its p private leaves. Thus there is a clique of p+2 core vertices and p(p+1) leaves. Two white leaves in one block cannot be separated. With at most one white per block, blue leaves can first color every hub. If the center is white with one white leaf in every block, the center and those leaves form a fort: each hub meets it twice, all other vertices zero times. Otherwise the blue center or a fully blue leaf block permits finishing. This criterion gives u^(p²−1)(1+u)^(p+1)[(1+u)(u+p)^(p+1)−p^(p+1)]. Size p² permits no blue hubs: all blocks leave one white if the center is blue, or exactly one block leaves none if the center is white. The two counts p^(p+1) and (p+1)p^p sum as claimed, and N−p²=2p+2. Independent replay: python /workspace/audit_checks.py 1 generates subgroups by closure for p=3,5 and tests all 131072 initial sets on the actual p=3 intersection graph, matching the criterion and all coefficients, including 189 at degree 9. This corroborates rather than proves the all-prime statement.

## originality

PASS

The distinct content supported by the comparisons is the complete forcing criterion and two minimum regimes for this partially decorated core, not the subgroup-intersection construction or a generic private-module method. Exact same-family prior domination results and closely related polynomial results do not give the accepted claim. In particular the same-day clique-decoration theorem has internal clique edges necessary to its effective-root reduction; its assumptions and effective-root process do not hold for the private independent leaves and naked center in this finding. Priority is not inferred from catalogue dates.

## value

PASS

The extraspecial groups form a natural infinite nonabelian family. The undecorated center produces an exact fort obstruction and two qualitatively different optimal configurations; the full enumerator gives a test case for zero forcing on subgroup-intersection graphs, in which the incidence structure and propagation constraints can both be checked directly. No minimum-rank or larger-group extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
