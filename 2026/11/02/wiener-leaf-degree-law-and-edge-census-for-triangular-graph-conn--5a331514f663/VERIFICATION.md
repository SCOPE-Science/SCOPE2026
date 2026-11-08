---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Minimum connected dominating sets of T_n=L(K_n) correspond exactly to spanning trees on n-1 of n ground vertices: selected edges must meet every edge and be connected, hence at most one omitted ground vertex and at least n-2 edges. For a tree F on m=n-1 vertices, fixed omitted-vertex jumps insert a non-tree edge and delete one of d_F(u,v) edges along its unique cycle, contributing W(F)-(m-1). Support-changing jumps remove precisely a leaf edge and attach the formerly omitted vertex to one of m-1 survivors, contributing (m-1)ell(F). Their sum is W(F)+(m-1)(ell(F)-1). The connectivity argument via fundamental-cycle tree exchanges and changing omitted vertex using common-center stars works even for m=2. Prüfer leaf enumeration and weighted edge-cut enumeration of tree Wiener indices yield the closed global edge sum. Star/path degrees differ by -(m-8)(m-3)(m-1)/6; a double broom settles the m=8 coincidence with a universal +4 degree gap. Independently enumerated all labeled trees via Prüfer strings for m=2..6, calculated actual W and leaf counts, and matched the edge totals 3,36,540,9420,187845. The all-n theorem rests on bijections, not on tested m.

## originality

PASS

The minimum size/count and standard tree exchanges are known. The assessed result is the full token-jump solution-graph degree formula, all-order edge census, connectedness across changing supports and regularity/witness. A specialized tree-base-exchange graph result might cover it under alternate terminology.

## value

PASS

The exact edge count and local degree of the natural optimal-solution reconfiguration graph are mathematically meaningful and needed to analyze connectivity, random moves and regularity. The formula shows an interplay of two independently natural tree statistics, Wiener index and leaves, and the double-broom demonstrates that neither alone controls exchange degree. This is an all-parameter classification, not an arbitrary finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
