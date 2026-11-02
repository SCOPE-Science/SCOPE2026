---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For induced matchings in rook graph K_m square K_n, each selected row-oriented edge uses 1 dedicated row and 2 dedicated columns, while each column-oriented edge uses 2 dedicated rows and 1 dedicated column. Inducedness means all row coordinates from distinct selected edges and all column coordinates from distinct selected edges are disjoint, so h+2v<=m,2h+v<=n are necessary and sufficient. Choose h rows, v columns, pair and assign remaining 2v rows to column edges and 2h columns to row edges. This bijection yields m!n!/[h!v!2^(h+v)(m-h-2v)!(n-v-2h)!]. Summing z^(h+v) gives full polynomial for every positive m,n including singleton dimensions. These inequalities imply k=h+v<=m,n,floor((m+n)/3); choose h=max(0,2k-m), v=k-h to realize k=min(m,n,floor((m+n)/3)). The equivalent object is vertex-disjoint P3 (two-edge) packing in K_{m,n}, via rook graph=L(K_{m,n}); the exact factorial profile is the count of such packings. Independent exhaustive enumeration of induced matchings on all 16 boards m,n<=4 reproduces every coefficient, not used as infinite proof.

## originality

PASS

The line graph identity R_{m,n}=L(K_{m,n}) is standard, as are general induced-matching algorithms; previously studied P3-packing k-partition parameters of K_{m,n} focus on partitioning/perfect packings, not the all-k enumerator of vertex-disjoint path selections. The new claimed contribution is the labeled two-profile factorial polynomial and the consequent all-size maximum, with the caveat that similar classical rook/P3 packing generating functions may exist under different terminology. Targeted Resultary and primary-literature searches did not identify the exact all-parameter polynomial, not proof of absolute priority.

## value

PASS

The rook graph is a canonical graph (Hamming graph H(2,m,n)), and its induced-matching polynomial counts every conflict-free edge selection by size, beyond a single optimum. The rectangular boundary and exact maximum min(m,n,floor((m+n)/3)) are complete, useful invariants that can serve as exact benchmark instances for induced-packing enumerators; a natural self-contained fact need not yield a broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
