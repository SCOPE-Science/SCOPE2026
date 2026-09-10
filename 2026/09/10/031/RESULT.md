# Certified fibre-symmetric balanced signing of the Coxeter double cover with rho in [2.6104, 2.6105), refuting the universal 2*sqrt(2)+0.15 exclusion

## Context

The Bilu–Linial 2-lift programme asks for signings of a d-regular base graph
whose signed spectral radius is small (Ramanujan or weakly Ramanujan).
The admitted target was a universal lower-bound obstruction: every
fibre-symmetric globally edge-balanced signing of B, the 56-vertex bipartite
double cover of the 28-vertex Coxeter graph, has rho > 2*sqrt(2)+0.15 (~2.978).
This record decides that question negatively with an explicit certified witness
and explains why the admitted Tr4/Tr6-excess route was structurally void.

## Definitions

- G: 28-vertex cubic Coxeter graph (vertices 0..27), via the logged 42-edge list:
  [(0,22),(0,23),(0,27),(1,21),(1,23),(1,26),(2,20),(2,22),(2,25),(3,20),(3,21),
  (3,24),(4,18),(4,19),(4,27),(5,17),(5,19),(5,26),(6,16),(6,17),(6,25),(7,16),
  (7,18),(7,24),(8,13),(8,15),(8,22),(9,13),(9,14),(9,18),(10,12),(10,15),
  (10,17),(11,12),(11,14),(11,21),(12,27),(13,26),(14,25),(15,24),(16,23),(19,20)].
- B: bipartite double cover of G on vertices 0..55; each base edge (u,v) gives
  fibre edges (u,v+28) and (u+28,v). B has 56 vertices, 84 edges, is cubic,
  bipartite, connected, of girth 8.
- Fibre-symmetric signing: same sign on both fibre edges of each base pair,
  equivalently a base signing t on the 42 base edges with
  A_s = [[0,A_t],[A_t,0]]. Globally edge-balanced: 21 of 42 base signs +1
  (hence 42 of 84 fibre signs +1).
- rho(A): spectral radius (max absolute eigenvalue) of symmetric matrix A.

## Result

**Theorem (counterexample; two-sided enclosure).** For the base signing
t = [-1,-1,-1,-1,+1,-1,-1,-1,+1,+1,-1,+1,-1,+1,-1,+1,-1,+1,+1,+1,-1,-1,+1,+1,
+1,-1,+1,+1,-1,-1,-1,-1,+1,-1,+1,+1,+1,+1,-1,-1,+1,+1] (21 plus / 21 minus)
on the above edge order and its fibre-symmetric lift s (42 plus / 42 minus),
rho(A_s) = rho(A_t) lies in [2.6104, 2.6105). In particular
rho(A_s) < 2.978 < 2*sqrt(2)+0.15, so the universal fibre-symmetric exclusion
at slack 0.15 is FALSE. As a corollary rho(A_s) >= 2.6104 > 2.60, certifying
the preset orbit floor on this witness's orbit.

**Lemma (girth-forced trace rigidity).** On the girth-7 Coxeter base, every
signing has Tr(A^4) = 420 and Tr(A^6) = 2436 (unsigned values; cubic
Kesten–McKay tree moments 15, 87 per vertex). Hence the Tr4/Tr6-excess route
can only ever yield (15)^{1/4} ~ 1.97 or (87)^{1/6} ~ 2.11 and is structurally
incapable of reaching 2.978. First signing signal appears at Tr7 (+336
unsigned vs -168 witness) and Tr8 (15540 vs 14964).

## Proof / evidence

- Base identity: BFS gives cubic, girth 7, distance distribution
  (1,3,6,12,6) from every vertex and intersection array {3,2,2,1;1,1,1,2} at
  every vertex; exact Frame/LeVerrier characteristic polynomial equals
  (x-3)(x-2)^8(x+1)^7(x^2+2x-1)^6 coefficient-for-coefficient (Newton identities
  k=1..8 exact-0). Cover invariants: BFS + 2-colouring give B cubic,
  connected, bipartite, girth 8.
- Dictionary: A_s = [[0,A_t],[A_t,0]] verified entry-by-entry over integers;
  spec(A_s) = {+/- lambda : lambda in spec(A_t)} is elementary linear algebra,
  so rho(A_s) = rho(A_t).
- Trace rigidity: Tr(A^k) sums signed closed k-walks; for k <= 6 < girth every
  closed walk traverses each edge evenly (else deleting backtracks leaves a
  cycle of length <= k), so all sign products are +1. Instantiated exactly over
  integers for unsigned and witness matrices.
- Upper bound rho < 2.6105 (and direct rho < 2.978): A_s symmetric, so
  rho < R iff R^2 I - A_s^2 is positive definite. For R = 26105/10000 (and
  R = 2.978, 2.62, 2.98) the integer matrix R^2 I - A_s^2 is positive definite
  by exact rational LDL (all 56 pivots > 0, Fractions only).
- Lower bound rho >= 2.6104: for the logged integer vector w (length 56),
  w^T A_s w = 2610502980388, w^T w = 1000001200328 (exact integers) and
  10000*num - 26104*den = 998470517888 > 0, so the Rayleigh quotient is
  >= 2.6104; for symmetric A_s, rho >= lambda_max >= quotient.
- Threshold: 14142^2 = 199996164 < 2*10^8 gives sqrt(2) > 1.4142, and
  2*14142+1500 = 29784 > 29780 gives 2*sqrt(2)+0.15 > 2.9784 > 2.978.
  Margin: 2.978 - 2.6105 ~ 0.37. No floating point enters any certificate.

## Limitations

- True signing optimum of B is pinned only from below (2.6104); greedy search
  suggests ~2.6105 is near-minimal but optimality is NOT claimed (class range
  about [2.6105, 3.0] is conjectural).
- Trace-rigidity lemma covers Tr4/Tr6 only; Tr8+ carries signing signal
  (14964 vs 15540) and could support a weaker obstruction, not pursued.
- Base identity as the Coxeter graph rests on spectrum + intersection array +
  girth invariants (van Dam–Haemers determined-by-spectrum), not a nauty
  certificate in-container.

## Reproducibility

From the workspace root (stdlib only, seconds):
  python3 output/artifacts/audit_emergent_stdlib.py   # prints AUDIT_OK
  python3 output/artifacts/stdlib_reverify.py          # prints STDLIB_VERIFY_OK
Inputs: output/artifacts/coxeter_base.json (42 edges),
output/artifacts/counterexample_sign_vector.json (42 base signs + 84-entry
fibre vector), output/artifacts/rayleigh_lower_26104.json (w, num, den);
saved LDL pivots, charpolys, and graph6 strings are archived alongside.

## References

- Y. Bilu, N. Linial, Lifts, discrepancy and nearly optimal spectral gap,
  Combinatorica 26 (2006). doi:10.1007/s00493-006-0029-7
- Y. Bilu, N. Linial, Constructing expander graphs by 2-lifts (FOCS 2004);
  Ramanujan signing of regular graphs, CPC 2004. doi:10.1017/s0963548304006509
- A. Marcus, D. Spielman, N. Srivastava, Interlacing families I: bipartite
  Ramanujan graphs of all degrees, Ann. Math. 2015.
  https://annals.math.princeton.edu/2015/182-1/p07
- C. Hall, D. Puder, W. Sawin, Ramanujan coverings of graphs,
  Adv. Math. 2017. doi:10.1016/j.aim.2017.10.042
- E. R. van Dam, W. H. Haemers, Spectral characterizations of some
  distance-regular graphs, J. Algebraic Combin. 15 (2003).
- DistanceRegular.org: Coxeter graph (28v, intersection array, spectrum).
  https://www.math.mun.ca/distanceregular/graphs/coxeter.html
- Wolfram MathWorld: Coxeter Graph (F028A; bipartite double F056C).
  https://mathworld.wolfram.com/CoxeterGraph.html
- M. Conder, P. Potocnik, Foster census of cubic edge-transitive graphs.
  https://fostercensus.graphsym.net/
- House of Graphs: Graph 981 (Coxeter). https://houseofgraphs.org/graphs/981
