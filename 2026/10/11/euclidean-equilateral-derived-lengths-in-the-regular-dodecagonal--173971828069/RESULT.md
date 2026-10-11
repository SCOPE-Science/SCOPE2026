# Euclidean equilateral derived lengths in the regular dodecagonal plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\), where
\[
N_{12}(s,t)=
\max\left\{
|s|,\ |t|,\
\left|\frac{\sqrt3s+t}{2}\right|,\
\left|\frac{s+\sqrt3t}{2}\right|,\
\left|\frac{-s+\sqrt3t}{2}\right|,\
\left|\frac{-\sqrt3s+t}{2}\right|
\right\}.
\]
The six unoriented supporting functionals have Euclidean normal directions spaced by \(30^\circ\), so the unit ball is a Euclidean regular dodecagon.

For every \(x,y\in\mathbb R^2\) with
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1,
\]
the two derived equilateral-triangle lengths are rigid:
\[
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3.
\]
Therefore the Chen–Liu–Li constant
\[
G_L(X)=
\sup\left\{
\|x+y\|^2+\|2x-y\|^2:
\|x\|=\|y\|=\|x-y\|=1
\right\}
\]
has the exact value
\[
G_L(X_{12})=6.
\]

## Assumptions and scope
All scalars are real. The normalization above describes a regular dodecagon circumscribed about the Euclidean unit circle; replacing it by any linearly isometric regular-dodecagonal presentation does not change the claimed Banach-space invariant.

The statement is pointwise, not merely extremal: every admissible unit equilateral pair has both displayed derived lengths equal to \(\sqrt3\).

## Proof
Let \(E\) be the set of the twelve signed facet functionals of \(N_{12}\). Thus
\[
N_{12}(z)=\max_{f\in E}f(z).
\]
In \(\mathbb R^4\), define the compact polytope
\[
P=
\left\{
(x,y):
f(x)\le1,\ f(y)\le1,\ f(x-y)\le1
\text{ for every }f\in E
\right\}.
\]
An admissible pair with
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1
\]
has at least one tight signed facet in each of the three blocks. Hence every admissible pair belongs to a face
\[
F_{f,g,h}=
\left\{
(x,y)\in P:
f(x)=g(y)=h(x-y)=1
\right\}
\]
for some \(f,g,h\in E\).

The finite facet calculation is exact over \(\mathbb Q(\sqrt3)\). Among the \(12^3=1728\) signed-facet triples, the consistency and inequality test leaves \(168\) nonempty face presentations. Of these, \(144\) are single points and \(24\) are line segments; their endpoints comprise \(24\) distinct admissible vertices.

At every endpoint \(v=(x,y)\), exact evaluation of all twelve signed output facets gives
\[
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3.
\]
For each of the \(24\) nondegenerate segment presentations, there is a signed facet \(a\in E\) and a signed facet \(b\in E\) such that at both segment endpoints
\[
a(x+y)=\sqrt3,
\qquad
b(2x-y)=\sqrt3.
\]
Because these evaluations are affine, the same two equalities hold at every point of that segment, giving the lower bounds
\[
N_{12}(x+y)\ge\sqrt3,
\qquad
N_{12}(2x-y)\ge\sqrt3.
\]
On the other hand, each norm is convex and equals \(\sqrt3\) at both endpoints, so along the segment
\[
N_{12}(x+y)\le\sqrt3,
\qquad
N_{12}(2x-y)\le\sqrt3.
\]
Thus equality holds throughout every face and therefore for every admissible pair.

For a concrete admissible pair, take
\[
x=(\sqrt3-1,\sqrt3-1),
\qquad
y=(1,\sqrt3-2).
\]
Direct substitution gives
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1
\]
and
\[
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3.
\]
The pointwise identity immediately yields \(G_L(X_{12})=6\).

## Verification
The bundled `verify.py` is a standalone exact-arithmetic certificate. It implements \(\mathbb Q(\sqrt3)\) using rational pairs, checks all \(1728\) signed-facet triples, solves each consistent rank-three affine system, intersects its line with all \(36\) defining inequalities of \(P\), and verifies the counts and endpoint identities stated in the proof.

For every nondegenerate face it also finds common signed output facets attaining \(\sqrt3\) at both endpoints. This is the finite certificate needed by the affine-plus-convexity argument; no floating-point sampling is used to prove the continuum statement.

## Relationship to prior work
Chen, Liu and Li introduced \(G_L\) for unit equilateral pairs and proved the universal bounds
\[
\frac92\le G_L(X)\le8.
\]
They also proved that an inner-product space has \(G_L(X)=6\), with both derived lengths equal to \(\sqrt3\). Their full text computes \(\ell_\infty\) and gives estimates for \(\ell_p\), but it does not compute the regular dodecagonal plane.

The present result shows that the same pointwise Euclidean derived-length identities occur in a non-Hilbert polyhedral plane: \(X_{12}\) has flat sides, yet every admissible unit equilateral pair has the two Euclidean values \(\sqrt3\). Thus the implication “inner product \(\Rightarrow G_L=6\)” from the defining paper has no converse even in dimension two, and the failure is stronger than equality of the supremum.

A public exact computation of the same invariant for the regular octagonal plane gives a different value and concerns a different unit ball. Recent work on equilateral-triangle perimeters in regular polygonal norms studies side perimeters of triangles whose vertices lie on the unit sphere; that objective does not determine the two derived lengths in the definition of \(G_L\).

## Limitations
The argument is specific to the regular dodecagonal plane and does not classify all regular \(2n\)-gonal norms with \(G_L=6\). It also does not characterize all non-Hilbert planes whose admissible unit equilateral pairs have Euclidean derived lengths.

The originality search cannot prove absolute uniqueness. The strongest residual risk is an equivalent computation under different notation for the same regular dodecagonal norm; no such statement was found in the inspected defining paper, the same-invariant searches, the regular-polygon equilateral literature, or the checked public research records.

## References
1. B. Chen, Q. Liu and Y. Li, “Inscribed triangles in the unit sphere and a new class of geometric constants,” arXiv:2112.05922v1, first public version 11 December 2021; Mathematics Subject Classification 46B20, 46C15.
2. B. Chen, Q. Liu and Y. Li, “Inscribed Triangles in the Unit Sphere and a New Class of Geometric Constants,” Symmetry 14 (2022), 72, doi:10.3390/sym14010072.
3. J. Alonso, P. Martín and P. L. Papini, “Perimeter of Triangles Inscribed in the Unit Ball of Normed Planes,” Mediterranean Journal of Mathematics 22 (2025), article 46.
