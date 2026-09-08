# Complete cospectral census of connected cubic bipartite graphs on 18 vertices with exact polynomials and certified minimal pair

## Context
Cubic spectra sit between textbook interlacing bounds and deeper Ramanujan / Haemers-conjecture questions, but order-stratified cospectral catalogs for the bipartite cubic subfamily are gap-ridden. This record closes the n=18 connected cubic bipartite (bicubic) stratum with exact polynomials, a certified cospectral pair, and a per-class diameter table, for use as a graph-isomorphism benchmark and spectral-uniqueness reference. The isomorphism-type count 149 is external (OEIS A006823; Brinkmann-McKay-Faradzev enumeration), verified live; the new closure is the spectral partition and diameter annotation, not the count.

## Definitions
- Stratum: graphs on vertices 0..17 that are 3-regular (cubic), connected, bipartite. Connected cubic bipartite on 18 vertices forces bipartition sizes 9+9 and |E|=27.
- Spectrum means adjacency spectrum. Characteristic polynomial p_G(x)=det(xI-A), monic degree 18 over ZZ; for bipartite graphs only even powers appear.
- Cospectral means sharing p_G (equivalently the same 18-eigenvalue multiset). A type is DS-in-stratum iff its cospectral class has size 1.
- Catalog ids 0..148 are discovery-order labels (seed 38) with no mathematical meaning; graphs are identified by edge lists.

## Result (conditional completeness stated)
(a) 149 pairwise non-isomorphic connected cubic bipartite graphs on 18 vertices are catalogued (edge lists in `artifacts/catalog_edges.csv`), each cubic, connected, bipartite 9+9.
(b) Their exact integer characteristic polynomials (`artifacts/polys.csv`, 19 coefficients x^18..x^0) take exactly 131 distinct values: 114 occur once, 16 occur twice, 1 occurs three times. Hence within the catalog there are 17 non-singleton cospectral classes comprising 19 unordered cospectral non-isomorphic pairs.
(c) An independent float spectrum (numpy eigvalsh, sorted, `artifacts/spectra_float.csv`) induces exactly the same partition at tolerance 1e-6 (19 pairs both ways, zero mismatch; max within-class eigenvalue difference <5e-15).
(d) Graphs id 3 and id 24 form an explicit cospectral non-isomorphic pair with shared polynomial and dual spectra, certified non-isomorphic by exhaustive search.
(e) Diameters over the 149 types are {5:98, 6:25, 4:23, 7:3}; girth {4:146, 6:3}. Diameter is not a spectral invariant in this stratum (triple class {55,103,128} diams 5,5,4; pair {22,67} diams 6 vs 5). The three girth-6 types (ids 138,143,147, diam 4) are all singletons (DS-in-stratum).
(f) Completeness: assuming published enumeration OEIS A006823 a(9)=149, (a)-(e) cover every isomorphism type, i.e. the complete cospectral census with diameter table. Unconditionally, (a)-(e) are a certified 149-type spectral catalog; the only gap is reproduction of the external count.

Minimal-pair certificate. Shared polynomial (x^18 first):
`1 0 -27 0 293 0 -1675 0 5507 0 -10585 0 11463 0 -6273 0 1296 0 0`,
i.e. x^18-27x^16+293x^14-1675x^12+5507x^10-10585x^8+11463x^6-6273x^4+1296x^2 (even-only, zero constant term).
Graph A (id 3): 0-12; 0-13; 0-16; 1-12; 1-14; 1-16; 2-11; 2-15; 2-16; 3-9; 3-12; 3-15; 4-9; 4-11; 4-13; 5-11; 5-14; 5-17; 6-10; 6-13; 6-14; 7-9; 7-10; 7-17; 8-10; 8-15; 8-17.
Graph B (id 24): 0-9; 0-15; 0-16; 1-10; 1-12; 1-14; 2-9; 2-10; 2-17; 3-11; 3-14; 3-17; 4-11; 4-13; 4-16; 5-13; 5-14; 5-15; 6-11; 6-12; 6-16; 7-10; 7-15; 7-17; 8-9; 8-12; 8-13.
Sorted float spectra (both, max pairwise diff 2.7e-15): +/-3.0, +/-2.278413609496, +/-1.891219848710, +/-1.732050807569 (x2), +/-1.317430607981, +/-1.0, +/-0.704624368767, 0 (x2). Both have diameter 5, girth 4, 2 four-cycles. "Minimal" means smallest catalog indices in discovery order; all 19 pairs are equivalent witnesses.

## Proof / Evidence (computed, independently re-verified)
- Universe: fixed sides L=0..8,R=9..17; labelled graphs sampled as union of 3 uniform perms (seed 38), reject multi-edge/disconnected; dedup by invariant bucket plus exhaustive bipartition-restricted backtracking. Audit re-ran the full 11026-pair check: 0 isomorphic pairs.
- Spectra A (exact): SymPy charpoly (Berkowitz over ZZ) per type; audit spot-recomputed ids 3,24 exactly. Spectra A2 (independent): Bareiss fraction-free determinants of tI-A at t=0..18 plus exact Vandermonde solve; matches all 149/149 (verify.py ~10 s).
- Spectra B (float): numpy eigvalsh sorted; partition at 1e-6 identical to exact (19/19 pairs, 0 mismatch); audit recompute agrees to <5e-13 stored, <3e-15 within pair.
- Non-isomorphism: exhaustive search over (S9xS9)xC2 with bitmask VF2, both side-swaps, two orderings; audit added an independent backtracking implementation (pair/triple members False; self and permuted-copy True).
- Diameters via all-pairs BFS; girth via per-edge BFS; n4 via common-neighbor counts; audit recomputed 0/149 mismatches.
- `python3 artifacts/verify.py` reproduces stratum, exact-polys, partition agreement, and pair non-isomorphism: VERIFY OK.

## Limitations
- Completeness (no 150th type) is conditional on OEIS A006823 a(9)=149 (Sloane/McKay, Faradzev/Brinkmann); random-search tail (45765 negatives after last discovery) corroborates but does not prove completeness.
- Isomorphism filtering uses validated custom backtracking, not nauty certificates (unavailable); argued via 298 perm-copy positives, dual orderings, full-pair check, and independent re-implementation.
- No claims about Ramanujan status, DS-in-full, or Godsil-McKay switching explanations.

## Reproducibility
Artifacts: `catalog_edges.csv` (149 edge lists), `polys.csv` (149x19), `spectra_float.csv` (149x18), `cospectral_classes.csv` (131 classes), `diameters.csv` (149 diam/girth/n4), `minimal_pair.json` (pair 3,24), `verify.py`. Rerun: discovery (~46 s) + spectra (~2 s) + checks (~10 s); `python3 artifacts/verify.py` re-verifies stored tables in ~10 s. Seeds fixed (38). Requires stdlib+numpy+sympy only.

## References
- van Dam-Haemers, Which graphs are determined by their spectrum? Lin. Alg. Appl. 2003. (DS/NDS survey; existence background only.)
- Godsil-McKay, Constructing cospectral graphs, Combinatorica 1982. (switching; existence method, not this census.)
- Robinson-Wormald, Numbers of cubic graphs, JGT 1983; McKay nauty/geng; Meringer regular-graph tables; House of Graphs cubic lists. (Universe.)
- OEIS A006823 (connected trivalent bipartite, 2n nodes; a(9)=149); A002851 (connected cubic, 41301 at 18 vertices).
- Brinkmann-Goedgebeur-McKay, Generation of cubic graphs, DMTCS 2011. (Generation standard behind counts.)
