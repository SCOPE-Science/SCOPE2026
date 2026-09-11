# Refutation of the [N/24, N/8] independence window for the q=4 Hermitian-unital Section-3 host

## Context

Off-diagonal Ramsey theory asks for the growth of r(4,t), the least N forcing a
K4 or an independent t-set. Mattheus and Verstraete proved
r(4,t) = Omega(t^3 / log^4 t) as t -> infinity via a Hermitian-unital
construction: secants of the Hermitian unital in PG(2,q^2) become vertices,
points of the unital index cliques of size q^2, and each clique is replaced by a
random bipartition whose complete bipartite edges are unioned (Section 3,
H_q^*). The pseudorandomness theorem is proved only for large q (q >= 2^40).
The admitted target asks for the independence profile of the smallest instance,
q = 4: with N vertices near 200, decide whether
N/24 <= alpha(H_4) <= N/8 (for N = 208, 9 <= alpha <= 26).

## Definitions

- GF(16) = GF(2)[t]/(t^4+t+1), primitive polynomial 0x13.
- PG(2,16): 273 normalized nonzero triples (first nonzero coordinate 1).
- Hermitian unital H = {<x,y,z> : x^5+y^5+z^5 = 0}, |H| = 65 = 4^3+1.
- Secants: 208 lines meeting H in 5 points; tangents: 65 lines meeting H in 1 point.
- For each p in H, the 16 secants through p form a clique C_p; distinct C_p share
  at most one vertex.
- H_4^*: fix seed 20260911; for each C_p take a uniform random bipartition
  (A_p, B_p) and union the complete bipartite graphs on (A_p, B_p) over all 65 p.
  Filed instance: N = 208, 3851 edges.
- alpha(G): independence number. Target upper bound: N/8 = 26.
- K4-free means no 4 vertices pairwise adjacent (the R(4,t) property used); the
  instance does contain triangles (4916), unlike the admission shorthand.

## Result

The target window is FALSE. The exact seeded q=4 Section-3 instance H_4^*
(seed 20260911, N = 208, verified K4-free) satisfies alpha(H_4^*) >= 35,
witnessed by the explicit pairwise-nonadjacent 35-set

  [8, 10, 13, 16, 17, 20, 27, 31, 39, 43, 45, 49, 51, 62, 63, 79, 84, 101,
   118, 124, 127, 128, 132, 133, 134, 139, 140, 151, 153, 165, 166, 170,
   175, 185, 197],

which strictly exceeds the claimed upper bound N/8 = 26 by 9 vertices
(alpha/N >= 0.168 versus the claimed <= 0.125).

## Proof / evidence

1. Geometry (exact enumeration, stdlib-only): rebuild GF(16), PG(2,16) with
   273 points, unital of 65 points, 208 secants and 65 tangents; per-point
   16-cliques pairwise sharing at most one vertex; secant and clique ledgers
   match the filed h4star.json exactly.
2. Instance consistency: adjacency equals the union of the 65 filed complete
   bipartitions on the rebuilt cliques (bitwise equality of all 208 rows).
3. K4-freeness: exhaustive edge-indexed bitset census over common-neighborhood
   pairs counts K4 = 0 (independently recounted with set code: 0).
4. Independence: all C(35,2) = 595 pairs of the witness are non-edges against
   the filed adjacency bitsets (independently recounted: 0 violations).
5. Replay: `python3 output/artifacts/construct_h4star.py` rebuilds h4star.json
   from the seed; `python3 output/artifacts/verify.py` replays geometry, clique
   ledger, bipartition consistency, K4 = 0, and the 35-set, printing VERIFY_OK.
6. Typicality (reported, not replayed): six further independent seeds yield
   greedy plus local-search independent sets of size 33-36.

## Limitations

- Certifies alpha >= 35 > 26 for the single fixed seeded Section-3 instance
  (N = 208); exact alpha of that instance is not determined.
- Does not audit other seeds or the deterministic union-of-cliques graph H_q
  (reported 13-set, inside the window): a separate object.
- Admission preflight mislabels the Section-3 host as triangle-free; the filed
  randomized instance contains 4916 triangles and is K4-free, which is the
  property the R(4,t) application and this refutation use.

## Reproducibility

- Stdlib-only Python 3 scripts: output/artifacts/construct_h4star.py,
  output/artifacts/verify.py, data output/artifacts/h4star.json
  (seed 20260911, n 208, ~25.6 KB).
- verify.py rebuilds all geometry from scratch without trusting search code.

## References

- S. Mattheus, J. Verstraete, "The asymptotics of r(4,t)", arXiv:2306.04007;
  Annals of Mathematics 2024, 199(2):8. doi:10.4007/annals.2024.199.2.8.
- S. Mattheus, "The asymptotics of r(4,t)" (blog exposition).
- VUB news report on the Hermitian-unital combination of finite geometry and
  graph theory.
