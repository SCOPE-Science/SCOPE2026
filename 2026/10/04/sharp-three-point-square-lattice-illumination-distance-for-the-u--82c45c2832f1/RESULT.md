# Sharp three-point square-lattice illumination distance for the unit disk
## Finding
Let \(B=\{x\in\mathbb R^2:\|x\|\le 1\}\). For a three-point set \(S\subset\mathbb Z^2\) and a translate \(B+c\), write
\[
d(S,B+c)=\max\{\|p-y\|:p\in S,\ y\in B+c\}.
\]
Among all pairs \((S,c)\) for which \(S\) illuminates \(B+c\),
\[
\inf d(S,B+c)=1+\sqrt 5,
\]
and the infimum is not attained. Indeed every feasible pair satisfies \(d(S,B+c)>1+\sqrt5\).

The constant is sharp. With
\[
S_0=\{(-2,0),(2,0),(0,3)\},\qquad c_\delta=(0,1+\delta),
\]
for every
\[
0<\delta<\frac{4-\sqrt{13}}2,
\]
the disk \(B+c_\delta\) lies strictly inside \(\operatorname{conv}S_0\), hence is illuminated by \(S_0\), and
\[
d(S_0,B+c_\delta)=1+\sqrt{4+(1+\delta)^2}\longrightarrow 1+\sqrt5.
\]

## Assumptions and scope
Illumination is by exterior points in the usual Euclidean sense: a boundary point is illuminated when the ray from the illuminating point through that boundary point enters the interior immediately after crossing the boundary. Only the Euclidean unit disk, the square lattice \(\mathbb Z^2\), and exactly three lattice illuminators are considered. Translation of the disk is allowed. No claim is made for other lattices, other convex bodies, or larger illuminating sets.

## Proof
For a boundary point \(c+u\), where \(\|u\|=1\), a point \(p\) illuminates \(c+u\) exactly when
\[
\langle p-c,u\rangle>1.
\]
Hence three points \(S\) illuminate \(B+c\) exactly when \(B+c\) is strictly contained in the triangle \(T=\operatorname{conv}S\). Moreover
\[
d(S,B+c)=1+M,\qquad M=\max_{p\in S}\|p-c\|.
\]

Assume for contradiction that a feasible pair has \(M\le\sqrt5\). Let \(A\) and \(P\) be the area and perimeter of \(T\). Since the distance from \(c\) to every side line is strictly larger than \(1\), decomposition into the three triangles with apex \(c\) gives \(A>P/2\). The sharp triangle isoperimetric inequality
\[
P^2\ge 12\sqrt3\,A
\]
therefore implies \(A>3\sqrt3\). A lattice triangle has half-integral area, so \(A\ge 11/2\).

All three vertices lie in the closed disk of radius \(\sqrt5\) centered at \(c\). The maximal area of a triangle inscribed in a disk of radius \(R\) is \(3\sqrt3 R^2/4\); thus
\[
A\le\frac{15\sqrt3}{4}<\frac{13}{2}.
\]
Half-integrality leaves only \(A\in\{11/2,6\}\).

If \(q_1,q_2,q_3\) are the squared side lengths of \(T\), each is a positive sum of two integer squares and each is at most \(20\). Consequently
\[
q_i\in Q=\{1,2,4,5,8,9,10,13,16,17,18,20\}.
\]
Heron's identity in squared-length form is
\[
16A^2=2(q_1q_2+q_2q_3+q_3q_1)-(q_1^2+q_2^2+q_3^2).
\]
Exhausting the unordered triples from \(Q\) at \(A=11/2\) and \(A=6\) gives exactly
\[
(10,13,17),\ (8,20,20),\ (9,17,20),\ (10,16,18),\ (13,13,16).
\]
Thus every remaining lattice triangle has a side of length at least \(4\). If that side has endpoints \(p,q\), length \(L\ge4\), and the distance from \(c\) to its line is \(h>1\), orthogonal projection onto the side line gives
\[
\max\{\|p-c\|^2,\|q-c\|^2\}\ge \frac{L^2}{4}+h^2>5,
\]
contradicting \(M\le\sqrt5\). Therefore every feasible pair satisfies \(M>\sqrt5\), so \(d>1+\sqrt5\).

For sharpness, the triangle with vertices \((-2,0),(2,0),(0,3)\) has base-line distance \(1+\delta>1\) from \(c_\delta\). Its other two side-line distances equal
\[
\frac{4-2\delta}{\sqrt{13}}>1
\]
precisely on the displayed range of \(\delta\). Hence the translated unit disk is strictly contained in the triangle. The farthest vertices are \((-2,0)\) and \((2,0)\), giving the stated distance and limit. Since the lower bound is strict for every feasible pair, the infimum is not attained.

## Verification
The standalone checker `artifacts/verify.py` reproduces the complete finite Heron enumeration from the analytically forced set \(Q\), verifies that every surviving squared-side triple has a member at least \(16\), and checks the elementary rational inequalities used for the explicit sharpness family. The infinite statement does not rest on finite experimentation: the finite enumeration occurs only after the proof has forced \(A\in\{11/2,6\}\) and \(q_i\in Q\).

## Relationship to prior work
Fukshansky's *On lattice illumination of smooth convex bodies* (arXiv:2501.10570) introduces the lattice illumination distance used here and proves general effective lattice upper bounds for smooth convex bodies, including a real-space ball estimate. Its statements do not give the exact three-point square-lattice value for a translated planar unit disk. Targeted searches for equivalent formulations in terms of circumscribed lattice triangles, lattice inradius, and exact three-point illumination did not locate a result implying the strict constant \(1+\sqrt5\) or its nonattainment.

## Limitations
The result is specific to exactly three points of \(\mathbb Z^2\). It does not determine the unrestricted lattice illumination distance if more lattice points are allowed, nor does it classify all asymptotically extremizing lattice triangles. The originality comparison cannot exclude an older result stated under substantially different terminology for circumscribed lattice triangles, although targeted equivalence searches found no such coverage.

## References
1. L. Fukshansky, *On lattice illumination of smooth convex bodies*, arXiv:2501.10570, first submitted 2025-01-17.
2. Heron's formula and the sharp maximal-area theorem for a triangle in a fixed circumdisk, used in their classical forms.
