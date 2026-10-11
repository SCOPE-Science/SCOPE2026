# Uniform chain interpolants have an exact Euclidean inradius profile
## Finding
Let
\[
m\ge2,
\]
and consider the marked chain
\[
p_0\prec p_1\prec\cdots\prec p_m\prec p_{m+1},
\tag{1}
\]
with endpoint marking
\[
\lambda(p_0)=0,
\qquad
\lambda(p_{m+1})=1.
\tag{2}
\]
For
\[
t\in[0,1],
\]
let
\[
Q_m(t)
=
\mathcal O_{(t,\ldots,t)}(P,\lambda)
\subset\mathbb R^m
\tag{3}
\]
be the Fang--Fourier--Litza--Pegel marked poset polytope, projected to the unmarked coordinates.

Define
\[
N_0(t)=1,
\tag{4}
\]
\[
N_j(t)
=
\sqrt{
1+(1-t)^2\sum_{\ell=0}^{j-1}t^{2\ell}
}
\qquad
(1\le j\le m-1),
\tag{5}
\]
and
\[
N_m(t)
=
\sqrt{
\sum_{\ell=0}^{m-1}t^{2\ell}
}.
\tag{6}
\]
Then
\[
\boxed{
r_{\mathrm{in}}\bigl(Q_m(t)\bigr)
=
r_m(t)
=
\frac1{\sum_{j=0}^mN_j(t)}.
}
\tag{7}
\]

Writing
\[
X_i^*(t)
=
r_m(t)\sum_{j=0}^{i-1}N_j(t),
\qquad
X_0^*(t)=0,
\tag{8}
\]
the unique incenter in the actual projected marked-poset coordinates is
\[
\boxed{
y_i^*(t)
=
X_i^*(t)-tX_{i-1}^*(t)
\qquad
(1\le i\le m).
}
\tag{9}
\]
All \(m+1\) facets are tangent to the inball.

At the two classical endpoints,
\[
\boxed{
r_m(0)
=
\frac1{2+(m-1)\sqrt2},
}
\tag{10}
\]
and
\[
\boxed{
r_m(1)
=
\frac1{m+\sqrt m}.
}
\tag{11}
\]

The continuous interpolation has a genuinely new metric effect. If
\[
D_m(t)=\frac1{r_m(t)},
\tag{12}
\]
then
\[
D_m'(0)
=
-\frac{m-1}{\sqrt2}<0,
\tag{13}
\]
while
\[
D_m'(1)
=
\frac{(m-1)\sqrt m}{2}>0.
\tag{14}
\]
Therefore neither the order endpoint nor the chain endpoint maximizes the Euclidean inradius. For every
\[
m\ge2
\]
there is at least one
\[
t_*\in(0,1)
\]
such that
\[
r_m(t_*)>
\max\{r_m(0),r_m(1)\}.
\tag{15}
\]

In dimension two the optimum is completely explicit:
\[
\boxed{
t_*=\frac12,
\qquad
r_2(t_*)
=
\frac1{1+\sqrt5}.
}
\tag{16}
\]

Thus the canonical uniform path through the source's parameter hypercube bulges outward in the Euclidean inradius sense: an intermediate marked poset simplex contains a larger inscribed Euclidean ball than either the order or chain endpoint.

## Assumptions and scope
The parameter vector in (3) is the diagonal vector
\[
(t,\ldots,t)
\]
in the source's hypercube
\[
[0,1]^m.
\]
This is the canonical simultaneous interpolation in which every unmarked element is moved from order behavior to chain behavior at the same rate.

The source uses
\[
t=\mathbf0
\]
for the marked order polytope and
\[
t=\mathbf1
\]
for the marked chain polytope. The theorem concerns the entire diagonal segment between those endpoints.

The Euclidean metric is the standard metric in the projected unmarked-coordinate space used by the source.

No uniqueness claim is made for the maximizing parameter when
\[
m\ge3.
\]
The unique object claimed in every dimension is the incenter of each fixed simplex
\[
Q_m(t).
\]

## Proof
The projected marked order polytope of the chain (1) is
\[
0\le x_1\le x_2\le\cdots\le x_m\le1.
\tag{17}
\]
The source's transfer map is
\[
y_p=x_p-t_p\max_{q\prec p}x_q.
\tag{18}
\]
Every unmarked element of a chain has a unique predecessor. With the uniform parameter,
\[
y_1=x_1,
\qquad
y_i=x_i-tx_{i-1}
\quad(2\le i\le m).
\tag{19}
\]
Thus the transfer map is globally linear on this chain.

Its inverse is
\[
x_j
=
\sum_{i=1}^j t^{j-i}y_i.
\tag{20}
\]

Introduce the order-simplex facet slacks
\[
s_0=x_1,
\tag{21}
\]
\[
s_j=x_{j+1}-x_j
\qquad(1\le j\le m-1),
\tag{22}
\]
and
\[
s_m=1-x_m.
\tag{23}
\]
They satisfy
\[
s_j\ge0
\]
and telescope to
\[
\sum_{j=0}^m s_j=1.
\tag{24}
\]

We now compute their Euclidean gradients in the \(y\)-coordinates.

For the first facet,
\[
\nabla_y s_0=e_1,
\]
so
\[
\|\nabla_y s_0\|=N_0(t)=1.
\tag{25}
\]

Using
\[
x_{j+1}=y_{j+1}+tx_j,
\]
we have
\[
s_j
=
y_{j+1}-(1-t)x_j
=
y_{j+1}
-
(1-t)
\sum_{i=1}^j t^{j-i}y_i.
\tag{26}
\]
Hence
\[
\|\nabla_y s_j\|^2
=
1+
(1-t)^2
\sum_{\ell=0}^{j-1}t^{2\ell}
=
N_j(t)^2.
\tag{27}
\]

Finally,
\[
s_m
=
1-\sum_{i=1}^m t^{m-i}y_i,
\]
so
\[
\|\nabla_y s_m\|^2
=
\sum_{\ell=0}^{m-1}t^{2\ell}
=
N_m(t)^2.
\tag{28}
\]

The intrinsic Euclidean distance from an interior point to facet \(j\) is therefore
\[
\frac{s_j}{N_j(t)}.
\tag{29}
\]

A nondegenerate Euclidean simplex has a unique incenter, and at that point all facet distances are equal. Write the common distance as \(r\). Then
\[
s_j=rN_j(t)
\qquad(0\le j\le m).
\tag{30}
\]
Summing (30) and using (24) gives
\[
r\sum_{j=0}^mN_j(t)=1,
\]
which proves (7).

The order coordinates at the incenter are obtained by cumulative slacks:
\[
x_i^*
=
s_0+\cdots+s_{i-1}
=
r_m(t)\sum_{j=0}^{i-1}N_j(t).
\]
Applying (19) gives (9).

At
\[
t=0,
\]
the normal lengths are
\[
N_0=N_m=1,
\qquad
N_j=\sqrt2
\quad(1\le j\le m-1),
\]
which proves (10).

At
\[
t=1,
\]
the normal lengths are
\[
N_0=N_1=\cdots=N_{m-1}=1,
\qquad
N_m=\sqrt m,
\]
which proves (11).

For the endpoint derivatives, differentiate the squared normal lengths. At
\[
t=0,
\]
each internal normal satisfies
\[
N_j'(0)=-\frac1{\sqrt2}
\qquad(1\le j\le m-1),
\]
while
\[
N_m'(0)=0.
\]
Thus (13) holds.

At
\[
t=1,
\]
every internal normal has derivative zero, while
\[
N_m(t)
=
\sqrt{1+t^2+\cdots+t^{2m-2}}
\]
gives
\[
N_m'(1)
=
\frac{m(m-1)}{2\sqrt m}
=
\frac{(m-1)\sqrt m}{2}.
\]
This proves (14).

Continuity and the two derivative signs imply that moving into the interval from either endpoint initially increases the inradius. Therefore the global maximum occurs in the interior and strictly exceeds both endpoint values, proving (15).

For
\[
m=2,
\]
the denominator becomes
\[
D_2(t)
=
1+
\sqrt{1+(1-t)^2}
+
\sqrt{1+t^2}.
\tag{31}
\]
It is symmetric under
\[
t\longmapsto1-t
\]
and strictly convex, since
\[
u\longmapsto\sqrt{1+u^2}
\]
is strictly convex. Hence its unique minimum is
\[
t=\frac12.
\]
Substitution into (31) gives
\[
D_2\!\left(\frac12\right)
=
1+\sqrt5,
\]
which proves (16).

## Verification
The arbitrary-\(m\) formula is symbolic.

The primary full text was checked at the definition of the continuous family, the statement that
\[
t=\mathbf0
\]
and
\[
t=\mathbf1
\]
recover the marked order and marked chain polytopes, and the parametrized transfer map. For a chain, the maximum over predecessors in the transfer map has only one term, so the map becomes the linear bidiagonal transformation (19).

The accompanying `verify.py` constructs the facet slacks directly in the \(y\)-coordinates for deterministic dimensions and parameter values. It independently solves the full Euclidean Chebyshev-center linear program and checks the incenter, radius, endpoint formulas, derivative signs, and the exact two-dimensional optimum. The finite replay is corroborative only.

## Relationship to prior work
Fang, Fourier, Litza, and Pegel introduce the full hypercube-parametrized family and prove piecewise-linear transfer equivalence with the marked order polytope. Their focus is Ehrhart equivalence, combinatorial degeneration, tropical subdivisions, and vertex structure. Their full text does not contain an inradius or Euclidean-radius theorem.

Fang and Fourier's earlier marked chain-order polytopes correspond to discrete zero-one choices of order and chain behavior. That work gives the combinatorial and representation-theoretic predecessor of the continuous family but does not supply the metric profile of the interior diagonal.

The two endpoint values in (10)--(11) are consistent with direct Euclidean geometry of the order simplex and chain simplex. The new content is the exact all-\(t\) profile, the explicit moving incenter, and the fact that every dimension
\[
m\ge2
\]
has a strictly better interior inradius than either classical endpoint.

Targeted searches under “continuous family of marked poset polytopes”, “marked chain-order polytope”, “order-chain interpolation”, “transfer map”, “Euclidean inradius”, and “Chebyshev center” did not locate a statement implying (7)--(16).

## Limitations
The theorem treats the uniform diagonal parameter path for a marked chain. It does not give the inradius for an arbitrary marked poset or for a general parameter vector in
\[
[0,1]^m.
\]

For
\[
m\ge3,
\]
existence of an interior maximizing parameter is proved, but no closed formula or uniqueness theorem for that maximizer is claimed.

The diagonal specialization is natural because it moves all unmarked elements at the same rate from the order endpoint to the chain endpoint, but a broader metric theorem for arbitrary transfer matrices could subsume the calculation under different terminology.

## References
1. Xin Fang, Ghislain Fourier, Jan-Philipp Litza, and Christoph Pegel, *A Continuous Family of Marked Poset Polytopes*, arXiv:1712.01037, first public version 2017-12-04; *SIAM Journal on Discrete Mathematics* 34 (2020), 611--639, DOI 10.1137/18M1228529.
2. Xin Fang and Ghislain Fourier, *Marked Chain-Order Polytopes*, arXiv:1508.02232, first public version 2015-08-10; *European Journal of Combinatorics* 58 (2016), 267--282, DOI 10.1016/j.ejc.2016.06.007.
