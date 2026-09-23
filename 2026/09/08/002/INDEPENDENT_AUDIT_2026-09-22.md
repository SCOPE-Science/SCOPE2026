# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/08/002`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `b0e9805ea83549bf1381c59d0a70d4706ead6a0a`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A complete exact spectral partition and diameter/girth annotation of the 149 connected cubic bipartite graphs on 18 vertices.

## Correctness — PASSED

Fresh exact trace-moment/characteristic-polynomial checks on the stored 149 graphs reproduced 131 spectral classes: 114 singletons, 16 doubletons and one tripleton, hence 19 unordered cospectral pairs. Independent BFS reproduced the diameter distribution {4:23,5:98,6:25,7:3} and girth distribution {4:146,6:3}. The explicit minimal cospectral pair and non-isomorphism checks were also consistent. Completeness remains correctly stated as conditional on the published 149-type universe.

## Originality — PASSED

The count of 149 connected cubic bipartite graphs on 18 vertices is prior catalog data and is not claimed as new. Searches of House of Graphs/OEIS-linked universe sources and cospectral-graph literature did not locate the exact characteristic-polynomial partition of those 149 types, the 19-pair annotation, or the complete diameter/girth cross-table. That finite spectral annotation survives as the original contribution relative to checked sources.

## Scientific value — PASSED

The exact partition supplies a compact benchmark for graph isomorphism and exact spectral software, identifies all within-stratum cospectral collisions, and records a concrete failure of diameter to be spectrally determined in the stratum. Those are specific reusable outputs rather than a random sample.

## Search and independent checks

Independent checks:

- exact spectral partition recomputation on all 149 stored graphs
- independent all-pairs BFS diameter/girth recount
- independent non-isomorphism checks for cospectral witnesses

Literature/search queries:
- `149 connected cubic bipartite graphs 18 vertices cospectral`
- `cubic bipartite 18 vertices characteristic polynomial census`
- `House of Graphs cubic bipartite cospectral 18`

Sources:
- https://houseofgraphs.org/Cubic

## Final disposition

**PASSED.** The record remains accepted on all three audited axes.
