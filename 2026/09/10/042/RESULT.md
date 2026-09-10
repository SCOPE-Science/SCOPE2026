# Vanishing loose-triangle 6-set density over linear 3-uniform hypergraphs: T* = 0

## Context

The admitted target asked for a two-sided interval 1/30 <= T* <= 1/8 for the
asymptotic loose-triangle density T* over linear Fano-free 3-uniform
hypergraphs, via a <=7-vertex rational flag certificate plus an infinite
tightness construction. The submitted result completely resolves the target by
disproof with a stronger uniform bound, proved by exact integer combinatorics
with no SDP, SAT, or floating-point trust.

## Definitions

- H is linear 3-uniform: every edge has 3 vertices; distinct edges share at
  most one vertex.
- C3 (loose triangle): edges 123, 345, 561 on six vertices; pairwise
  intersections are three distinct singletons. Distinct from the Pasch
  configuration (6 vertices, 4 edges).
- t(H) = (number of 6-sets S with H[S] containing a loose triangle) / C(n,6).
  A spanning loose triangle uses all 6 vertices since |123 union 345 union 561| = 6.
- T* = limsup_{n -> infinity} max{t(H)} over linear Fano-free H on n vertices.
- U'(n) = 120(n-1)/((n-2)(n-3)(n-4)(n-5)).

## Result

For every linear 3-uniform H on n >= 6 vertices (Fano-free or not),

  t(H) <= U'(n) -> 0,

hence T* = 0 exactly. In particular the target interval 1/30 <= T* <= 1/8 is
FALSE: U'(n) < 1/30 for all n >= 20 and U'(n) < 1/8 for all n >= 15.

## Proof / evidence

Fix linear H on n >= 6 vertices. Let h = number of hit 6-sets and
T = number of unordered loose-triangle edge triples.

1. h <= T: each hit 6-set contains a spanning loose triangle (union is 6
   vertices); each triangle spans exactly one 6-set. So T = sum_S m_S >= h
   with m_S >= 1.
2. 3T <= 4 * sum_v C(d(v),2): each triangle has exactly 3 corner vertices.
   For fixed center v with a = {v,x1,x2}, b = {v,y1,y2} disjoint off v by
   linearity, a completing edge c must meet each of a, b in one vertex
   different from v, giving 2 x 2 = 4 pairs (x,y), each in at most one edge
   by linearity. An edge through v cannot complete the triangle.
3. Linearity gives 2*d(v) <= n-1, so d(v) <= (n-1)/2 and
   sum_v C(d(v),2) <= n(n-1)^2/8. Hence h <= T <= n(n-1)^2/6.
4. Dividing by C(n,6) gives t(H) <= U'(n). Exact ratio
   U'(n+1)/U'(n) = n(n-5)/(n-1)^2 < 1 iff -3n < 1, so U' decreases to 0.
   Base U'(20) = 19/612 witnessed by 68400 < 18*17*16*15 = 73440; induction
   step holds since (n-1)/(n-5) >= n/(n-1) iff 3n+1 >= 0. Same induction from
   U'(15) = 14/143 gives the 1/8 leg.
5. Per-n maxima M(n) = max t(H) exist (finite nonempty family) and satisfy
   0 <= M(n) <= U'(n) -> 0, so T* = limsup M(n) = 0.

Machine replay `output/artifacts/verify_disproof.py` (stdlib, exact
integers/Fractions) prints ALL CHECKS PASSED: STS(7) T=28, h=7; STS(9) T=72,
h=72/84; greedy linear graphs n=8,10,12 satisfy 3T <= 4*sum C(d,2), h <= T,
t <= U'(n); exact threshold table and monotonicity/induction checks on
[6,2000)/[20,2000); tails closed by the proved lemmas.

## Limitations

- Refutes rather than proves the target interval; the upper leg T* <= 1/8
  holds only as a corollary of the stronger vanishing bound.
- Asserts no absolute edge-density cap below 1; near-Steiner Fano-free linear
  families are untouched.
- Small-n densities can be large (t=1 at n=7, 6/7 at n=9); the claim is
  asymptotic (T*=0) with explicit finite-n bound U'(n).
- The preset fallback <=6-vertex ledger-identity was not pursued; it is moot
  given the stronger vanishing theorem.

## Reproducibility

Run `python3 output/artifacts/verify_disproof.py` (stdlib only). Re-derives
STS(7)/STS(9) counts, greedy-graph inequalities, and exact rational threshold
table. The general bound is closed-form mathematics, not sampling.

## References

- L. Bellmann, C. Reiher, Turan's Theorem for the Fano plane,
  arXiv:1804.07673 (general Fano edge-extremal; disjoint functional/host).
- J. Nie, S. Spiro, J. Verstraete, Triangle-free Subgraphs of Hypergraphs,
  arXiv:2004.10992v2 (loose-triangle definition, retention/container bounds;
  no 6-set triangle-density limit).
- Ruzsa-Szemeredi / Erdos-Frankl-Rodl linear triangle-free edge theory as
  cited therein (edge counts under triangle-freeness, not triangle density).
