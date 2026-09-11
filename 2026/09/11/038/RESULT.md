# Exact Baker-Norine rank 1 of the degree-3 divisor D* on the square-backbone loop-of-loops genus-5 graph Gamma5*

## Context

Genus-5 curves with Brill-Noether number rho(5,1,3) = 5 - 2*3 = -1 are
Brill-Noether general only if they carry no g^1_3. Tropical analogues test
this boundary: a metric graph of genus 5 carrying a rank-1 degree-3 divisor
is tropically Brill-Noether special. The Baker specialization inequality
r_X <= r_Gamma lets such a divisor serve as a banked obstruction divisor for
future skeleton-specific lifting analysis. The closed square-backbone
loop-of-loops is the smallest closed (non-tree-like) loop assembly reaching
genus 5 beyond the Brill-Noether-general open chain, and its trigonality is
not decided by the 3-edge-connected trigonal-equivalence theorems.

## Definitions

Let Gamma5* be the metric graph with 8-vertex loopless combinatorial model:
vertices V = {0,...,7}; backbone square 0-1-2-3-0 (four bridges, each length
1); one attached circle of circumference 2 at each backbone vertex, modelled
as a doubled edge: (0,4),(0,4), (1,5),(1,5), (2,6),(2,6), (3,7),(3,7), each of
length 1. Edge list (12 edges, all length 1):

    (0,1),(1,2),(2,3),(3,0),
    (0,4),(0,4),(1,5),(1,5),(2,6),(2,6),(3,7),(3,7)

Degrees are [4,4,4,4,2,2,2,2]; genus g = 12 - 8 + 1 = 5. Edge-connectivity is
2 (e.g. deleting opposite backbone edges (0-1),(2-3) disconnects the graph),
so the 3-edge-connected trigonal-equivalence theorems do not apply.

Let D* = v0 + v1 + v2 (degree 3 on three consecutive backbone vertices).
Vertex Baker-Norine rank: r(D) >= 1 iff for every vertex q the class
|D - q| is nonempty, i.e. the q-reduced representative is effective;
r(D) <= 1 iff some effective degree-2 divisor E = a+b has |D - E| empty.

## Result

**Theorem.** The vertex Baker-Norine rank of D* on Gamma5* is exactly 1:
r(D*) = 1. Specialization log: rho(5,1,3) = -1, so a Brill-Noether-general
genus-5 curve has no g^1_3 while Gamma5* carries the rank-1 degree-3 divisor
D*; by r_X <= r_Gamma, D* is tropically BN-special and a banked obstruction
divisor. No lifting claim is made.

## Proof / Evidence

Exact stdlib-only certification (replay `python3 output/artifacts/verify_rank.py`;
full certificate in `output/artifacts/rank_certificate.json`):

- r(D*) >= 1: for each of the 8 vertices q, F_q = D* - q has effective
  0-reduced form (hence |F_q| nonempty), cross-checked at basepoints 0 and 1
  with archived firing scripts (D - Lf = R). E.g. q=3:
  F = [1,1,1,-1,0,0,0,0], 0-reduced [2,0,0,0,0,0,0,0].
- r(D*) <= 1: 18 vertex pairs (a,b) have |D* - a - b| empty. Worked example
  (0,4): F = D* - v0 - v4 = [0,1,1,0,-1,0,0,0]; its q-reduced form is
  non-effective (R[q] < 0) at every basepoint q = 0..7
  (e.g. q=0: [-1,0,0,1,1,0,0,0]).
- q-reduced representatives are unique; equivalence tested by exact rational
  solve of the reduced Laplacian system (gauge f[q]=0, integrality check);
  Dhar burning selects the reduced representative; emptiness cross-checked at
  two basepoints. Independent audit re-solved all certificates and
  brute-force re-enumerated all q-reduced forms (uniqueness holds) and all 18
  pair witnesses.

Note on criterion wording: the fallback criterion's r<2 parenthetical says
"degree-1 divisor E0"; taken literally (degree-1 E0 with |D*-E0| empty) that
contradicts the r>=1 half. The intended standard reading is a degree-2
witness E = a+b with |D*-E| empty, which is what is produced; the binary test
rank == 1 is met.

## Limitations

- Certified rank is vertex Baker-Norine rank on the stated loopless model;
  the metric-continuum rank-1 claim (all edge-interior points) is supported
  by a 12 edge-split sweep (all p-reduced R[p] in {1,2,3}) but not formally
  closed. The upper bound r<=1 transfers to the metric graph.
- No skeleton-specific non-liftability is proved; the bounded unmodified
  harmonic-morphism sweep (zero degree-3 morphisms to small trees at slope
  cap 2, no tropical modification) is supporting evidence only.
- Edge lengths fixed exactly as published (all 1); no family genericity claimed.

## Reproducibility

`python3 output/artifacts/verify_rank.py` (stdlib only) prints genus,
degrees, all q-reduced forms, the edge-interior sweep, and the 18 pair
witnesses (exit 0, all assertions pass).
`output/artifacts/rank_certificate.json` archives singleton firing scripts at
two basepoints, the worked (0,4) witness at all 8 basepoints, D* q-reduced
forms, and the rho value.

## References

- M. Baker, S. Norine, Riemann-Roch and Abel-Jacobi theory on a finite graph
  (2007). Rank/divisor framework.
- M. Melo, A. Zheng, Tropical trigonal curves (arXiv:2501.03903, Alg. Comb.
  2026). 3-edge-connected trigonal equivalence; Gamma5* (eta=2) outside scope.
- I. Aidun et al., Graphs of Gonality Three (arXiv:1810.08665). Combinatorial
  3-edge-connected trigonal theory; Gamma5* outside scope.
- D. Jensen, D. Ranganathan, Brill-Noether theory for curves of a fixed
  gonality (arXiv:1701.06579). Fixed-gonality demand; chain case only.
