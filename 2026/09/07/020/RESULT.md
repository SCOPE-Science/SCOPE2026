# Certified maximum sizes and complete-size spectra of caps in AG(3,3) and PG(3,3)

## Context

Small-order caps govern ovoids, MDS/near-MDS codes and blocking phenomena, yet explicit replayable certificates for the maximal strata of the two smallest 3-dimensional geometries over F3 are scattered across existence/spectrum papers without closed verification. This record closes the maximal end at q=3 by exhaustive search with independent replay.

## Definitions

- AG(3,3) = GF(3)^3, 27 points labelled `xyz` with x,y,z in {0,1,2} in lexicographic order (index 0 = 000). Lines (117): triples {a, a+d, a+2d} with d != 0. Each line has 3 points; 13 lines through each point; each point-pair lies on exactly one line.
- PG(3,3): 40 projective points = nonzero vectors in GF(3)^4 modulo scalars, canonical representative with first nonzero coordinate 1, labelled `wxyz` in lexicographic order (index 0 = 0001). Lines (130): 4-point spans of point-pairs. 13 lines through each point; each pair lies on exactly one line.
- A cap is a set with no 3 collinear points. A cap is complete if no outside point can be added without creating a collinear triple (maximal by inclusion). For 3-point AG lines and 4-point PG lines, an outside point p is blocked iff some line through p contains >=2 points of the cap.

## Result

**Theorem 1 (maxima).** The largest cap in AG(3,3) has 9 points; the largest cap in PG(3,3) has 10 points.

**Theorem 2 (complete-size spectra).** Every complete cap of AG(3,3) has size 8 or 9; every complete cap of PG(3,3) has size 8 or 10. In particular PG(3,3) has no complete 9-cap. Exact counts of complete caps containing the point 0 (index 0): AG: 13806 = 13104 (size 8) + 702 (size 9); PG: 115830 = 113724 (size 8) + 2106 (size 10).

**Witnesses.**
- AG 9-cap (indices [0,1,3,4,9,10,14,17,23]): 000, 001, 010, 011, 100, 101, 112, 122, 212.
- PG 10-cap (indices [0,1,4,8,13,17,24,28,36,38]): 0001, 0010, 0100, 0111, 1000, 1011, 1102, 1120, 1212, 1221.
- Both are caps and complete. The full per-outside-point witness table (outside point -> blocking pair in the cap, collinear on a geometry line) is in `artifacts/enumerator_output.json` (`AG_max_failed_additions` covering all 18 outside points, `PG_max_failed_additions` covering all 30 outside points) and is machine-checked.

By point-transitivity (AG translations; PGL(4,3) basis extension) these point-0-containing statements lift to global statements, and total numbers follow as total_k = count0_k * n/k.

## Proof / Evidence

Machine-verified exhaustive enumeration (stdlib only, seconds):

1. Geometry built from scratch and checked: 27/117 and 40/130 incidences, 13 lines per point, unique line per pair. Artifact line lists verified exactly as sets by independent construction (affine triples; projective 2D spans mod scalars).
2. Lex-ordered DFS over subsets visits every subset once; blocking test above is exact for 3-point and 4-point lines. Independent audit reimplementation uses precomputed blocking pairs (13 per AG point, 39 per PG point).
3. Optimality: branch-and-bound DFS fixing point 0 proves no 10-cap (AG) resp. 11-cap (PG) containing 0 (artifact nodes 16293/169494; independent replay UNSAT with 74298/874591 nodes under different bounding, <3 s). Transitivity lifts to global maxima 9 and 10; witnesses show tightness.
4. Census: exhaustive DFS with no bound pruning collects all inclusion-maximal caps containing 0: 13806 (AG) and 115830 (PG) with the distributions above (artifact nodes 175865/1359619; independent replay 383083/3541933 nodes, ~0.3 s + ~6.4 s, exact count match including zero PG 9-caps). Every collected cap re-tested for cap property and completeness.
5. Distinguishes computational exhaustive proof (closed search + replay) from analytic proof; no heuristic or sampling is used for the theorems.

## Limitations (explicit non-claims)

- Full PGL(4,3)/AGL(3,3) orbit classification (number of orbits, one representative per orbit, stabilizer orders) is NOT established; counts above are for the point-0-containing family, which meets every orbit by transitivity but is finer than orbits.
- No claim about caps in any other ambient space or order q != 3.
- Minimality below completeness is covered only by the spectra (no complete caps below size 8 in either space).

## Reproducibility

Stdlib-only Python, seconds on a laptop. Artifact `artifacts/enumerator_output.json` archives geometry (point labels, full line lists), maxima with examples and timings, complete-census distributions, per-outside-point failed-addition tables, and log. Independent verification rebuilds points/lines by a different code path, rechecks cap/completeness/witness collinearity, and re-runs both optimality searches and full censuses to exact count match.

## References

- D. Bartoli et al., Tables, bounds and graphics of the smallest known sizes of complete caps in PG(3,q) and PG(4,q), arXiv:1610.09656 (2016). https://arxiv.org/abs/1610.09656 — smallest/minimum-size heuristics for large q, not maximal strata at q=3.
- A. Cossidente et al., Small complete caps in PG(4n+1,q), arXiv:2105.14939 (2021). https://arxiv.org/abs/2105.14939 — Veronese infinite family for general q, not fixed-order census.
- R. Hill et al., On complete caps in the projective geometries over F_3, J. Geom. 67, 127-144 (2000). https://link.springer.com/article/10.1007/BF01220305 — PG(5,3) 48-caps and 56-cap bounds, not AG(3,3)/PG(3,3) spectra.
- G. Faina, F. Pambianco, On the spectrum of the values k for which a complete k-cap in PG(n,q) exists, J. Geom. 62, 84-98 (1998). https://link.springer.com/article/10.1007/BF01237602 — general spectrum survey.
- K. Abdukhalikov et al., Ovoids in the cyclic presentation of PG(3,q), arXiv:2410.04126 (2024). https://arxiv.org/abs/2410.04126 — (q^2+1)-ovoid existence, not maximality/spectra/counts.
