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

For K_n□P_L, graph distance is |s−t|+[i≠j]. Three selected vertices in distinct columns cannot be a geodesic triple because two horizontal moves cost two versus at most one at endpoints; at least two in one column are necessary. Three in one vertical column are forbidden. With doubled heights a<b, every other selected height must be strictly interior, and at most one column can double. This proves two disjoint admissible forms and Ψ=(1+Lz)^n+n z² Σ_{h=0}^{L−2}(L−1−h)(1+hz)^(n−1). Doubled adjacent heights yield n(L−1) maximal pairs; doubled nonadjacent require all other columns filled (B_{n,L} maximal sets size n+1). First-form maximal sets have all n columns filled and are counted by complementing extendible tuples with unique minimum or maximum; inclusion–exclusion gives A_{n,L} from source. Explicit all-equal heights and end-to-end doubled columns prove three coefficients positive for n,L≥3. Independent direct graph-distance enumerations in three small parameter cases recovered maximal count triples (6,21,3),(9,34,18),(8,73,4); universal statement follows from structure, not those samples.

## originality

PASS

Qualified PASS for both complete set enumerator and inclusion-maximal cardinality polynomial for K_n□P_L. Existing work establishes general-position notions, Cartesian-product maxima and path-grid enumeration, not the full exact clique-path classification. Search cannot certify absence of differently indexed predecessors.

## value

PASS

General-position polynomials encode an established graph invariant, and inclusion-maximal configurations are distinct from maximum ones. A complete labelled two-parameter count exposes unusually large gaps in possible terminal sizes: exactly 2,n,n+1, even though all-set polynomial is dense. This is a motivated exact classification rather than a routine bound on gp(G).

The dated certificate retains the supplied scientific assessment, sources and limitations.
