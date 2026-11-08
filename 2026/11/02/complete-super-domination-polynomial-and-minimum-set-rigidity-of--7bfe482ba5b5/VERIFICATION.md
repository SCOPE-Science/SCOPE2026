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

For U complement of super dominating set D in K_m square K_n, a selected cell privately witnesses omitted (i,j) exactly when the omitted row/column endpoint has degree1 and opposite bipartite part has an isolate. Therefore the incidence graph B(U) is (i) a star forest with isolated row and column, or (ii)/(iii) a nonsurjective row->column or column->row function. Exponential labeled-star specification counts (i) with disjoint center convention; two Stirling corrections count (ii)/(iii). For m,n>=5 edge max m+n-4 forces exactly one long row-star and one long column-star, with m(m-1)n(n-1) ordered labels. Independent direct bitmask enumeration matched the polynomial for 3x3 {0:1,1:9,2:36,3:42} and 4x4 {0:1,1:16,2:120,3:416,4:608}; original checker inspected for 5x5 optimum enumeration. Infinite m,n statement follows combinatorially, not from finite board checks.

## originality

PASS

The scalar minimum gamma_sp=mn-m-n+4 for m,n>=4 is completely prior (Klein–Rodríguez-Velázquez–Yi Theorem 30); only full all-cardinality enumerator and rigidity/count of every minimum are assessed original. Ghanbari et al count minima of other families; Mertens ordinary domination polynomial is not super domination. Kaidash 2024 is highly relevant polynomial general study, but full chapter inaccessible after preprint/OA checks and authorized institutional access vpn_disconnected; this is explicit priority risk, not automatic scientific failure.

## value

PASS

A complete two-parameter enumeration and classification for Cartesian products of complete graphs refines a known scalar optimization by giving every feasible cardinality and all optimal configurations. This is a natural graph polynomial and extremal geometry, not restating the known minimum number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
