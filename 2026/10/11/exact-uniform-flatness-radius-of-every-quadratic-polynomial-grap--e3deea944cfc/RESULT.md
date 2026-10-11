# Exact uniform-flatness radius of every quadratic polynomial graph

## Finding

Let
\[
p(z)=az^2+bz+c,
\qquad
a,b,c\in\mathbb C,
\]
and let
\[
\Gamma_p
=
\{(z,p(z)):z\in\mathbb C\}
\subset\mathbb C^2
\]
with the standard Euclidean metric.

Its reach is exactly
\[
\operatorname{reach}(\Gamma_p)
=
\begin{cases}
\infty,&a=0,\\[0.4ex]
\dfrac1{2|a|},&a\ne0.
\end{cases}
\]

Here the reach is the supremum of the radii for which every point in the corresponding open Euclidean neighborhood has a unique nearest point on the graph. Therefore, for a genuinely quadratic graph, the exact supremal tubular thickness underlying uniform flatness is
\[
\frac1{2|a|}.
\]

In particular, the linear and constant coefficients do not affect this metric invariant. The quadratic coefficient alone determines the sharp tube scale.

## Assumptions and scope

The ambient metric is the standard Euclidean metric on
\[
\mathbb C^2\simeq\mathbb R^4.
\]

The notion of uniform flatness is the tubular-neighborhood notion used in Bargmann--Fock interpolation theory: a smooth hypersurface is uniformly flat when some fixed Euclidean neighborhood admits unique nearest-point projection to the hypersurface.

The recent polynomial-graph theorem proves existence of such a radius for every polynomial. The present statement determines the exact supremal radius for all polynomials of degree at most two.

The result is metric. It does not compute interpolation norms or claim an exact extension constant for the associated Bargmann--Fock interpolation operator.

## Proof

If
\[
a=0,
\]
then
\[
\Gamma_p
\]
is an affine complex line in
\[
\mathbb C^2.
\]
Orthogonal projection onto an affine subspace is globally unique, so its reach is infinite.

Assume now that
\[
a\ne0.
\]
Completing the square gives
\[
p(z)
=
a
\left(
z+\frac{b}{2a}
\right)^2
+
c-\frac{b^2}{4a}.
\]
An ambient translation therefore sends
\[
\Gamma_p
\]
isometrically to the graph
\[
\{(z,az^2):z\in\mathbb C\}.
\]
A unitary rotation of the second complex coordinate replaces
\[
a
\]
by
\[
A=|a|>0.
\]
It is enough to study
\[
F(z)=(z,Az^2).
\]

Fix distinct
\[
z,w\in\mathbb C.
\]
Set
\[
d=w-z
\]
and
\[
\Delta
=
F(w)-F(z)
=
d
\left(
1,A(w+z)
\right).
\]
A vector spanning the complex normal line at
\[
F(z)
\]
is
\[
n_z=(-2A\bar z,1).
\]
Indeed it is Hermitian-orthogonal to the tangent vector
\[
(1,2Az).
\]

Consequently,
\[
\left|
P_{N_z}\Delta
\right|
=
\frac{
A|w-z|^2
}{
\sqrt{1+4A^2|z|^2}
},
\]
while
\[
\|\Delta\|^2
=
|w-z|^2
\left(
1+A^2|w+z|^2
\right).
\]

Suppose that a point
\[
y\in\mathbb C^2
\]
has two distinct nearest points
\[
F(z)
\quad\text{and}\quad
F(w)
\]
at common distance
\[
r.
\]
A nearest-point displacement is orthogonal to the tangent space, so
\[
y-F(z)\in N_z.
\]
Equality of the two squared distances gives
\[
\begin{aligned}
0
&=
\|y-F(w)\|^2-\|y-F(z)\|^2\\
&=
\|\Delta\|^2
-
2\operatorname{Re}
\langle y-F(z),\Delta\rangle.
\end{aligned}
\]
Thus
\[
\|\Delta\|^2
\le
2r
\left|
P_{N_z}\Delta
\right|.
\]
Substitution yields
\[
r
\ge
\frac{
\sqrt{1+4A^2|z|^2}
\left(
1+A^2|w+z|^2
\right)
}{
2A
}
\ge
\frac1{2A}.
\]

The graph is closed and proper, so every ambient point has at least one nearest graph point. The preceding inequality therefore shows that every point at distance strictly less than
\[
1/(2A)
\]
has exactly one nearest graph point. Hence
\[
\operatorname{reach}(\Gamma_p)
\ge
\frac1{2A}.
\]

For the reverse inequality, take
\[
y_v=(0,v)
\]
with
\[
v>\frac1{2A}.
\]
For
\[
z=\rho e^{i\theta},
\]
the squared distance from
\[
y_v
\]
to
\[
F(z)
\]
is
\[
\rho^2
+
\left|
A\rho^2e^{2i\theta}-v
\right|^2.
\]
For each fixed
\[
\rho,
\]
this is minimized exactly when
\[
e^{2i\theta}=1.
\]
Put
\[
u=\rho^2.
\]
The radial minimization becomes
\[
\phi_v(u)
=
u+(Au-v)^2,
\qquad
u\ge0.
\]
Its unique positive minimizer is
\[
u_v
=
\frac{2Av-1}{2A^2}.
\]
Accordingly,
\[
y_v
\]
has exactly the two symmetric nearest graph points
\[
F(\sqrt{u_v})
\quad\text{and}\quad
F(-\sqrt{u_v}).
\]

Their common distance is
\[
r_v
=
\sqrt{
\frac{4Av-1}{4A^2}
}.
\]
As
\[
v\downarrow\frac1{2A},
\]
one has
\[
r_v
\downarrow
\frac1{2A}.
\]
Therefore every radius strictly larger than
\[
1/(2A)
\]
contains points with nonunique nearest projection. This gives
\[
\operatorname{reach}(\Gamma_p)
\le
\frac1{2A}
\]
and completes the proof.

## Verification

The normal-projection identity was checked directly from the Hermitian tangent vector
\[
(1,2Az)
\]
and normal vector
\[
(-2A\bar z,1).
\]
Their inner product vanishes exactly.

The sharpness calculation is one-dimensional after the angular minimization. Differentiating
\[
u+(Au-v)^2
\]
gives the unique minimizer
\[
u_v=(2Av-1)/(2A^2),
\]
and substitution gives
\[
r_v^2
=
(4Av-1)/(4A^2).
\]

No finite sampling or numerical search is used to prove the infinite statement.

The primary polynomial-graph article was verified at its publication metadata, abstract, classification data, and accessible publisher preview. Its complete article text was not accessible in the sources available for inspection. Targeted searches under the exact title, the quadratic graph, reach, tubular radius, and the constant
\[
1/(2|a|)
\]
did not expose this exact quantitative statement. This access limitation is retained as an originality risk rather than treated as negative evidence.

## Relationship to prior work

Wang and Zhang prove that the graph of every polynomial in one complex variable is uniformly flat in
\[
\mathbb C^2,
\]
and hence, together with the Bargmann--Fock extension theory they invoke, such graphs are interpolation curves of vanishing upper density.

Earlier Bargmann--Fock work formulates uniform flatness through the existence of a fixed tubular neighborhood with unique nearest-point projection. Those results use the existence of a tube as a geometric hypothesis rather than determining the exact largest tube for the quadratic polynomial family.

General reach theory separates local focal behavior from global bottlenecks, but no implication-equivalent exact formula for these complex quadratic graphs was located in the checked literature.

The present result is the complete exact quantitative answer for the first nonlinear polynomial degree:
\[
\operatorname{reach}
=
1/(2|a|).
\]
It also shows that arbitrary lower-order coefficients are irrelevant because completing the square is an ambient translation.

## Limitations

The formula is proved only for degree at most two. For higher-degree polynomial graphs, competing local curvature and nonlocal bottleneck effects may make the exact reach substantially more complicated.

The theorem does not produce a sharp Bargmann--Fock interpolation norm. It identifies the exact geometric tube scale entering uniform-flatness formulations.

Because the complete text of the recent Wang--Zhang paper was unavailable for inspection, an unindexed internal example in that article remains a residual originality risk. The accessible abstract and preview state only the qualitative uniform-flatness theorem.

## References

1. X. Wang and L. Zhang, *On the uniform flatness of polynomial graphs*, Bulletin of the London Mathematical Society 58 (2026), e70253, DOI: 10.1112/blms.70253; first published 16 December 2025; arXiv:2609.15599v1.
2. J. Ortega-Cerdà, A. Schuster, and D. Varolin, *Interpolation and sampling hypersurfaces for the Bargmann--Fock space in higher dimensions*, Mathematische Annalen 335 (2006), 79--107, DOI: 10.1007/s00208-005-0726-3.
3. V. P. Pingali and D. Varolin, *Bargmann--Fock extension from singular hypersurfaces*, Journal für die reine und angewandte Mathematik 717 (2016), 227--249.
