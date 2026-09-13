# No single-step whole-layer advance for thick slabs in strict-majority bootstrap on high-dimensional tori

## Context

The admitted target asked for a near-one-half window law (WMAJ) for strict-majority
bootstrap percolation on the growing-dimension torus
T_n^{d(n)} = (Z/nZ)^{d(n)} with d(n) = floor((log log n)^3): percolation probability
tending to 0 below p = 1/2 - 1/sqrt(d) and to 1 above p = 1/2 + 1/sqrt(d), with a
fully infected thickness-2 slab spanning d-1 directions acting as a critical witness
that invades the remaining direction with conditional probability at least 1-n^{-2}
above the window via a first-passage (one-step whole-layer) coupling.

While pursuing that slab-invasion bound, the exact slab-boundary one-step success
probability q = P(Bin(2d-1,p) >= d) at p = 1/2 + 1/sqrt(d) was computed and found to
be bounded away from 1 (q ~ 0.998), so that whole-layer one-step advance
q^{n^{d-1}} tends to 0. Isolating the point-mass failure term and combining it with
a 3-separated independent packing turns this observation into the rigorous
impossibility theorem below. This is an emergent finding: it refutes the target's
stated one-step first-passage coupling mechanism, not the slab-invasion conclusion
itself.

## Definitions

Let T = (Z/nZ)^d with the strict-majority rule: degree 2d; a healthy vertex becomes
infected iff at least d+1 of its 2d nearest neighbours are infected; infected
vertices stay infected; the initial set outside any conditioned region is i.i.d.
Bernoulli(p).

Let S = {x : x_d in {0,1}} be a fully infected thickness-2 slab spanning d-1 torus
directions, and L = {x : x_d = 2} the adjacent layer. For v = (y,2) in L, let N(v)
denote its 2d-1 non-slab neighbours (the 2(d-1) within-layer neighbours plus
(y,3)), and let F_v be the failure event that at most d-1 of these are initially
infected.

## Result

Theorem (no-one-step-slab-advance). Condition on the fully infected thickness-2
slab S, with all other vertices i.i.d. Bernoulli(p) at p = 1/2 + 1/sqrt(d). Then
for all d >= 16 and n >= 20, with explicit c = e^{-8}/4 and
m = floor(n/4)^{d-1} >= (n/8)^{d-1}:

  P(L becomes fully infected in a single step | S infected) <= (1 - c/sqrt(d))^m
    <= exp(-c m / sqrt(d)).

In particular along d(n) = floor((log log n)^3) -> infinity this probability tends
to 0 super-exponentially fast, so it is eventually far below 1 - n^{-2}. Hence no
proof of slab invasion at p = 1/2 + 1/sqrt(d) can proceed by a one-step whole-layer
(first-passage) coupling; any valid invasion argument must use multi-round
within-layer bootstrap cleanup.

## Proof / Evidence

Each v = (y,2) in L has exactly one neighbour in S, namely (y,1) (using n >= 4 so
the three layers are distinct). To be infected in one step, v needs at least d+1
infected neighbours, hence at least d of the remaining 2d-1 others initially
infected. Thus

  P(F_v) = P(Bin(2d-1,p) <= d-1) >= P(Bin(2d-1,p) = d-1)
         = C(2d-1,d-1) p^{d-1} (1-p)^d.

Write p = (1+delta)/2 with delta = 2/sqrt(d). The central-binomial lower bound
a_d = prod_{k=1}^d (2k-1)/(2k) = C(2d,d) 4^{-d} >= 1/(2 sqrt(d)) holds by induction
(base a_1 = 1/2; step uses (2d+1)^2 >= 4d(d+1)), so
C(2d-1,d-1) = C(2d,d)/2 >= 4^d/(4 sqrt(d)). Then
p^{d-1}(1-p)^d = 2^{-(2d-1)} (1+delta)^{d-1} (1-delta)^d, and 4^d 2^{-(2d-1)} = 2,
giving point mass >= (1/(2 sqrt(d))) (1-delta^2)^{d-1} (1-delta). With
delta^2 = 4/d and ln(1-x) >= -x-x^2 for x in [0,1/2],
(d-1) ln(1-4/d) >= -(d-1)(4/d+16/d^2) >= -6 for d >= 8, so (1-4/d)^{d-1} >= e^{-6};
and 1-delta = 1-2/sqrt(d) >= 1/2 for d >= 16. Hence for d >= 16,

  P(F_v) >= e^{-6}/(4 sqrt(d)) >= e^{-8}/(4 sqrt(d)) =: c/sqrt(d).

Packing: for v = (y,2), w = (z,2) at torus distance >= 3 inside L, the sets N(v)
and N(w) are disjoint (closed radius-1 balls in L are disjoint, and the outward
vertices (y,3), (z,3) lie outside L). Take the spacing-4 grid
Y = {y : all coords in {0,4,...,4(floor(n/4)-1)}}, m = |Y| = floor(n/4)^{d-1}
points pairwise at distance >= 4 (for n >= 8). The events {F_v} over Y x {2}
depend on disjoint sets of i.i.d. variables, hence are independent, each with
probability >= c/sqrt(d). Whole-layer one-step advance implies all succeed, so
its probability is at most (1-c/sqrt(d))^m <= exp(-c m/sqrt(d)). Since
floor(n/4) >= n/8 for n >= 8, m >= (n/8)^{d-1}. Along
d(n) = floor((log log n)^3), log(c m/sqrt(d)) -> infinity. The same holds for the
other adjacent layer by symmetry.

Numerical check: exact binomial tails P(F_v) at p = 1/2+1/sqrt(d) are 0.001302
(d=16), 0.001406 (d=18), 0.001700 (d=27), 0.002061 (d=64), 0.002160 (d=100),
0.002294 (d=400), exceeding c/sqrt(d) by factors 62-547; the proved bound is
deliberately loose, favouring a short rigorous chain, and the packing exponent m
dominates regardless. Script: output/artifacts/emergent_check.py.

## Limitations

This theorem refutes only the one-step whole-layer mechanism, not the
slab-invasion conclusion itself: multi-round within-layer bootstrap cleanup over
at least 2 rounds remains a live route. It proves neither side of the full window
law WMAJ (both percolation sides and the multi-round slab bounds remain open).

## Reproducibility

Definitions, proof, and numerical table are self-contained above. The verification
script output/artifacts/emergent_check.py recomputes exact binomial tails, the
central-binomial bound, and the packing growth using only the Python standard
library (math.comb).

## References

- J. Balogh, B. Bollobas, R. Morris, Majority bootstrap percolation on the
  hypercube, arXiv:math/0702373 (2009): critical probability 1/2+o(1) for
  fast-growing dimension; window location, not one-step slab dynamics.
- M. Collares, J. Erde, A. Geisler, M. Kang, Universal behaviour of majority
  bootstrap percolation on high-dimensional geometric graphs, arXiv:2406.17486
  (2024): window location/width for geometric graphs including tori.
- H. Duminil-Copin, R. Morris, The sharp threshold for bootstrap percolation in
  all dimensions (2016): sharp r-neighbour thresholds on grids.
