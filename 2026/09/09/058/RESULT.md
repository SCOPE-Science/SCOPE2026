# No-go for partition-pointwise series-step domination in bunkbed percolation

## Context

Kasteleyn's 1985 bunkbed conjecture was disproved in general by a large
planar counterexample (Gladkov–Pak–Zimin 2024). The active boundary program
(Denart 2025; Meunier–Pournajafi 2024; Ayyer–Linusson–Ravichandran 2025) asks
which minor-closed classes still satisfy the inequality. Known fragments:
outerplanar uniform case (Linusson 2008), cactus strong case plus listed
weak block classes and reduction to biconnected components (Denart 2025).
The next test ground is K4-minor-free (series-parallel) graphs. Every
2-connected series-parallel graph has a degree-2 vertex, so the canonical
attack conditions on such a vertex w.

## Definitions

Let G be finite simple, G^{+-} = G □ K2 its bunkbed graph with horizontal
edges in two layers and a post at each vertex. In the uniform model every
edge of G^{+-} is independently open with probability p in [0,1]. For
u,v in V(G):

D(G,u,v,p) = P_p(u_0 <-> v_0) - P_p(u_0 <-> v_1).

Fix a degree-2 vertex w not equal to u,v with N(w)={x,y}. The w-incident
edges are a_0=x_0w_0, b_0=w_0y_0, a_1=x_1w_1, b_1=w_1y_1, q=w_0w_1
(5 independent edges). Let R be the rest of the configuration and C(R) its
connectivity partition on the background terminals. Put

f(pi,p) = E_w[I(u_0<->v_0) - I(u_0<->v_1) | pi],
g(pi,p) = E_w[(1/2)(I(u_0<->v_0) - I(u_0<->v_1)
  + I(u_1<->v_1) - I(u_1<->v_0)) | pi],

degree-<=5 polynomials (expectation over the 32 w-edge states).
By joint R+w bunk-swap invariance, D = E_R[g(C(R),p)].
A partition-pointwise induction would need f(pi,p) >= 0,
resp. g(pi,p) >= 0, for every partition pi and every p in [0,1].

## Result

(a) Raw: on the 7 background nodes {u_0,v_0,v_1,x_0,y_0,x_1,y_1}
(B7 = 877 partitions), 233 partitions admit p in [0,1] with f(pi,p) < 0.
In particular pi* = {{u_0,v_1,x_0,y_0,x_1,y_1},{v_0}} gives
f(pi*,p) = -1 identically in p.

(b) Symmetrized: on the 8 nodes {u_0,u_1,v_0,v_1,x_0,y_0,x_1,y_1}
(B8 = 4140 partitions), 1107 partitions admit p with g(pi,p) < 0.
In particular pi** = {{u_0,v_1,x_0,y_0,x_1,y_1},{u_1,v_0}} gives
g(pi**,p) = -1 identically.

Counts 233/877 and 1107/4140 are grid-screening counts; the certified
exact core is the two identically-(-1) witnesses.

## Proof / evidence

Fix pi; enumerate all 32 w-edge states. Let c_k be the summed signed
indicator over states with exactly k open w-edges; then
f (resp. g) = sum_k c_k p^k (1-p)^{5-k} exactly.

Raw witness: u_0 is background-connected to v_1, v_0 background-isolated
from that block. Every u_0--v_0 path would have to use w-edges to reach
v_0, but w-edges touch only x/y-copies already inside the u_0 block and
never touch v_0, so I(u_0<->v_1)=1, I(u_0<->v_0)=0 in all 32 states.
Hence c = (-1,-5,-10,-10,-5,-1) = (-C(5,k))_k and the sum is -(p+1-p)^5
= -1. Standard-basis coefficients (-1,0,0,0,0,0).

Symmetrized witness: blocks {u_0,v_1,x,y-copies} and {u_1,v_0}. Every
w-state gives I(u_0<->v_1)=1, I(u_1<->v_0)=1, cross terms 0 (the
{u_1,v_0} block has no x/y copy, so w-edges cannot join the blocks);
symmetrized indicator (1/2)(0-1+0-1) = -1 in all 32 states. Same c, -1.

Replay: `python3 output/artifacts/verify_obstruction.py` prints both
counts and both witnesses (877/233 and 4140/1107, worst std
(-1,0,0,0,0,0)).

## Limitations

No-go lemma only: it does not decide the uniform weak inequality for
series-parallel graphs (all reported exact uniform-p small-graph data
support it; no counterexample found). Percolation-realizable boundary
mixtures may still average nonnegatively. Screening counts are
grid-detected; the fully grid-independent certified core is the two -1
witnesses. No claim about the weighted-diamond direction. The
symmetrized headline partition needs at least 5 background vertices to
be percolation-realizable (realized with one auxiliary vertex z).

## Reproducibility

Stdlib Python 3 only (`fractions`, `math`, `itertools`, `time`).
Deterministic enumeration; ~7 s. Artifact:
`output/artifacts/verify_obstruction.py`.

## References

- R. Denart, The bunkbed conjecture still holds for cactus graphs and for
  graphs with certain biconnected components, arXiv:2506.09264 (2025).
- S. Linusson, On percolation and the bunkbed conjecture,
  arXiv:0811.0949 (2008).
- G. Gladkov, I. Pak, A. Zimin, The bunkbed conjecture is false,
  arXiv:2410.02545 (2024).
- S. Meunier, M. Pournajafi, Vertex gluing preserves the bunkbed
  conjecture, arXiv:2410.08957 (2024).
- G. Hollom, The bunkbed conjecture is not robust to generalisation,
  arXiv:2406.01790 (2024).
