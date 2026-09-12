# Theta-type genus-2 Mumford curve over Q_2: explicit rank-two Schottky group with skeleton edge lengths 1, 3, 3

## Context
Let K = Q_2 with normalized valuation v_2(2) = 1 and |x|_2 = 2^{-v_2(x)}.
A p-adic Schottky group is a finitely generated, discrete, torsion-free subgroup
of PGL(2,K), equivalently a free group all of whose non-identity elements are
hyperbolic. By Mumford uniformization, a rank-g Schottky group Gamma gives a
smooth projective Mumford curve X = Omega_Gamma / Gamma of genus g, where
Omega_Gamma is P^1_an minus the limit set. Its minimal Berkovich skeleton is
the quotient of the convex hull of the disc boundary points by the group
pairings. In genus 2 there are two combinatorial types: theta (two vertices
joined by three edges) and dumbbell. The admitted target asked: does a
rank-two Schottky group over Q_2 with a good fundamental domain of four
pairwise disjoint closed discs exist whose genus-2 Mumford quotient has theta
type with all edge lengths computed from generator valuations, or is there a
residue-field obstruction forcing dumbbell type? Scope is all hyperbolic pairs
over Q_2; either explicit certified matrices or a proof of impossibility
resolves it.

## Definitions
Closed discs: D_1^- = B(0,1/4), D_1^+ = {|z|_2 >= 4} union {infinity},
D_2^- = B(1,1/4), D_2^+ = B(2,1/4). Generators: gamma_1(z) = z/16 with matrix
[[1,0],[0,16]]; h(z) = (2z+1)/(z+1) with matrix [[2,1],[1,1]] of determinant 1;
gamma_2 = h gamma_1 h^{-1} with matrix [[-14,30],[-15,31]]. Translation length
of a hyperbolic element is the valuation gap of its eigenvalues. The spine is
the Berkovich segment joining the two paired boundary points of gamma_1; the
branch points are where the gamma_2 disc boundaries attach.

## Result
There exists a rank-two p-adic Schottky group Gamma = <gamma_1, gamma_2> over
Q_2 with good fundamental domain F = P^1_an minus the interiors of the four
pairwise disjoint closed discs above. Gamma is free of rank 2, each generator
is hyperbolic with translation length 4, and X = Omega_Gamma / Gamma is a
smooth projective Mumford curve of genus 2 whose minimal Berkovich skeleton is
a theta graph with edge lengths 1, 3, 3, all computed from 2-adic valuations.

## Proof / evidence
Disjointness: |0-1|_2 = 1, |0-2|_2 = 1/2, |1-2|_2 = 1, each strictly greater
than 1/4, so the three affine discs are pairwise disjoint by the ultrametric
inequality; points of D_2^- have |.|_2 = 1 and of D_2^+ have |.|_2 = 1/2, both
below 4, hence disjoint from D_1^+, and D_1^- has |.|_2 <= 1/4 below both.
Hyperbolicity: gamma_1 = diag(1,16) has eigenvalues 1 and 16 with distinct
valuations, fixing 0 and infinity; gamma_2 is PGL(2,K)-conjugate with trace 17
and determinant 16, characteristic polynomial (t-1)(t-16), fixing h(0) = 1 and
h(infinity) = 2. Ping-pong: |gamma_1(z)|_2 = 16|z|_2 gives
gamma_1(P^1 \ int D_1^-) subset int D_1^+ and the inverse inclusion. The
identities h(z)-1 = z/(z+1) and h(z)-2 = -1/(z+1) give exact valuation
equalities: for |z|_2 <= 1/4, |z+1|_2 = 1 so |h(z)-1|_2 = |z|_2, i.e.
h(B(0,1/4)) = B(1,1/4) with explicit inverse z = (w-1)/(2-w); for |z|_2 >= 4,
|z+1|_2 = |z|_2 so |h(z)-2|_2 = 1/|z|_2 <= 1/4, i.e. h({|z|_2 >= 4}) = B(2,1/4).
Conjugation transfers the pairing to gamma_2. By the Gerritzen-van der Put /
Mumford Schottky criterion Gamma is free rank 2 and Schottky. Genus 2 follows
from Mumford uniformization. Skeleton: with p_1^- = zeta_{0,1/4},
p_1^+ = zeta_{0,4}, q^- = zeta_{1,1/4}, q^+ = zeta_{2,1/4}, the spine
[zeta_{0,4}, zeta_{0,1/4}] has length 4, split by y = zeta_{0,1} and
x = zeta_{0,1/2} = zeta_{2,1/2} into segments of lengths 2, 1, 1; the pendant
[y,q^-] has length 2 and [x,q^+] length 1. Quotienting p_1^- ~ p_1^+ and
q^- ~ q^+ turns the spine into a circle of length 4 split by x,y into arcs 1
and 3, and glues the pendants into a third arc of length 2+1 = 3, giving theta
edges 1, 3, 3. Axes [0,infinity] and [1,2] overlap in length 1 < min(4,4), the
standard theta criterion. All steps were rechecked with exact rational
valuation arithmetic in output/artifacts/verify_theta.py.

## Limitations
Exhibits one explicit theta example with edge triple (1,3,3); does not
classify all attainable theta triples, all Schottky bases, or minimal
obstructions. Relies on classical Mumford uniformization and the
Gerritzen-van der Put criterion rather than re-proving them.

## Reproducibility
Run `python3 output/artifacts/verify_theta.py` with exact rational arithmetic;
it checks the matrix product, trace/determinant, fixed points, disc
disjointness, h disc-image valuation identities, gamma_1 valuation shift, and
edge-length arithmetic, printing ALL CHECKS PASSED.

## References
D. Mumford, An analytic construction of degenerating curves over complete
local rings, Compositio Math. 24 (1972); L. Gerritzen and M. van der Put,
Schottky Groups and Mumford Curves, LNM 817, Springer 1980; R. Morrison and
Q. Ren, Algorithms for Mumford curves, arXiv:1309.5243; J. Poineau and
D. Turchetti, Schottky spaces and universal Mumford curves over Z,
arXiv:2107.07884; J. Teitelbaum, p-adic periods of genus two Mumford-Schottky
curves, J. reine angew. Math. 385 (1988).
