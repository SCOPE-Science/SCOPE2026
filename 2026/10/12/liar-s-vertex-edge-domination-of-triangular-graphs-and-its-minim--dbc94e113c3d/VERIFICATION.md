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

Every edge of the triangular graph L(K_n) comes from two intersecting original edges whose union is a triple. Its closed edge-neighborhood consists of selected K_n edges meeting this triple; a triangle of three triangular-graph vertices makes the liar union condition equivalent to at least three selected original edges incident to every triple. Lower bounds by isolated vertices, K2 components and per-component size give m>=ceil(3n/4). Disjoint spanning trees on blocks of sizes 4..7 attain the bound. For n>=8 extremal total defect Σ(4e-3c)=4ceil(3n/4)-3n <=3 excludes cyclic components of order>=4 and leaves exactly the forest type, plus a single triangle only when n mod4=3. Cayley labeled-tree EGF gives the displayed census. Independently enumerated all candidate edge subsets at sizes optimum-1 and optimum for n=4..8, obtaining no smaller and counts 20,210,1773,20629,8960 respectively; infinite proof remains the component/defect argument.

## originality

PASS

Bhattacharya–Paul 2023 define liar vertex-edge domination and prove general hardness, approximation and tree algorithm results, not the exact nonchordal triangular graph family. The related k-vertex-edge domination definition specializes on L(K_n), but no inspected result computes its optimum, all extremal component types or enumeration. Resultary similar liar domination results concern ordinary vertex domination of complete multipartite graphs.

## value

PASS

Complete exact minimum and labeled extremal-set classification across the natural Johnson/triangular graph family is a substantive structural graph invariant, including a clean reduction to a 3-incident-edge covering problem and tree-defect rigidity. The count is not an arbitrary isolated value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
