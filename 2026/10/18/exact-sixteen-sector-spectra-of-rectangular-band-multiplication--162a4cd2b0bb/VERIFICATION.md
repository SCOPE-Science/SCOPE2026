---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Direct separation into first-only, second-only, and product-only edges gives three tensor operators. The first has free k and requires l to differ; the second has free j and requires i to differ; the third fixes i,l and requires both j,k to differ. Their sector eigenvalues are w(t-1), (u-1)v and (v-1)(w-1), respectively. Their sum is the stated eigenvalue; constants and sum-zero factors give the stated multiplicities even when a factor has size one. The uniform degree, two connected families of fixed-coordinate moves for a,b>=2, and the direct clique union when one factor is one establish the connectivity claims. Size and degree recover the product and sum of the factor sizes, and reversing the factor order and the two inputs gives the converse graph isomorphism. At (2,2) the five Cayley steps are the images of the coordinate steps of the five-cube modulo the antipodal vector, which gives Clebsch; the exact characteristic polynomial and common-neighbor identity agree. The matrix-tree product follows from regularity and simplicity of the degree eigenvalue for connected graphs. Independent exact characteristic polynomials from the raw adjacency rule matched for all nine pairs 1<=a,b<=3. The juxtaposition XZ and YZ in the frozen proof denotes entrywise intersection of equality indicators, not ordinary matrix multiplication; the separate-edge calculation avoids that notational ambiguity.

## originality

PASS

The exact-one graph definition and rectangular-band degree formula are prior; diagonalizing the complete-graph tensor factors is standard. Pass the explicit full spectrum and the structural conclusions specific to this graph family. The closest primary paper's similarly titled lemma gives no explicit sector spectrum, and its proposed disconnected block picture does not hold for the same adjacency.

## value

PASS

This is the full exact adjacency invariant of the natural regular rectangular-band family from the motivating paper, not an isolated computed size. It replaces degree-only information by a multiplicity formula valid for all factor sizes and clarifies the misleading disconnected-block picture. It also separates the connected and degenerate cases and puts the Clebsch instance and spanning-tree count into one family. Standard diagonalization alone does not identify the graph's sector eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
