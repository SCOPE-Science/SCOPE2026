# Affine-integer grid radius 84 for Mizhaev's genus-3 equivelar octahedron

## Result

Let \(V=\{v_1,\ldots,v_{24}\}\subset\mathbb Z^3\) be the 24-vertex coordinate realization in Ruslan Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3* (arXiv:2609.17700). Define its **affine-integer cube radius**
\[
R_{\rm aff}(V)=
\min\left\{
\max_{i,k} |(Av_i+b)_k|:
A\in GL_3(\mathbb R),\ b\in\mathbb R^3,\ AV+b\subset\mathbb Z^3
\right\}.
\]

Then
\[
\boxed{R_{\rm aff}(V)=84}.
\]

Equivalently, among all invertible affine images of this particular realization whose vertices are integral, the smallest possible axis-aligned integer cube span is exactly \(168\).

An optimal affine map is
\[
\Phi(x,y,z)=
\left(
\frac z3,\;
\frac{x}{10}-\frac y5-\frac z6+15,\;
\frac x5+\frac y{10}-\frac z6-15
\right),
\qquad
\det D\Phi=\frac1{60}.
\]
It sends Mizhaev's vertices, in the numbering of his Table 1, to

| \(i\) | \(\Phi(v_i)\) | \(i\) | \(\Phi(v_i)\) |
|---:|:---|---:|:---|
|1|(6,-12,-24)|13|(69,9,-66)|
|2|(34,-28,-28)|14|(-6,12,12)|
|3|(6,36,-12)|15|(-34,36,28)|
|4|(34,24,-36)|16|(6,24,-36)|
|5|(78,-84,-24)|17|(-69,66,48)|
|6|(-6,0,-24)|18|(48,-36,-30)|
|7|(69,-48,-33)|19|(-48,30,-18)|
|8|(78,36,-84)|20|(-78,24,-36)|
|9|(-6,36,0)|21|(-6,24,-36)|
|10|(-34,28,-24)|22|(48,18,-48)|
|11|(6,0,0)|23|(-48,48,36)|
|12|(-69,33,-9)|24|(-78,84,84)|

The coordinate ranges are
\[
[-78,78],\qquad[-84,84],\qquad[-84,84],
\]
so the cube radius is \(84\). Since \(\Phi\) is invertible, applying it to every face preserves planarity, simplicity, incidences, orientability, and the absence of unintended intersections. Thus these points, with Mizhaev's unchanged face walks, give an affine-equivalent integer realization of the same genus-3 \(\{9,3\}\) polyhedral surface. The original Euclidean \(C_4\) isometry need not remain an isometry after this non-similarity; it is conjugated to an affine order-four symmetry.

## Optimality inside the affine orbit

Put \(P=\Phi(V)\). Exact Smith/Hermite-lattice computation, equivalently the gcd of all full-rank \(3\times3\) minors of the difference matrix \(P-P_1\), gives
\[
[\mathbb Z^3:\langle P-P\rangle_{\mathbb Z}]=1.
\]
Hence the vertex differences generate the full lattice \(\mathbb Z^3\).

Suppose an invertible affine map
\[
\Psi(u)=Bu+c
\]
sends \(P\) to integer points. Because \(P-P\) generates \(\mathbb Z^3\), every row of \(B\) takes integer values on \(\mathbb Z^3\), so
\[
B\in M_3(\mathbb Z).
\]
Since \(\Psi\) is invertible, its three row covectors are linearly independent nonzero integer vectors.

For an integer covector \(a\in\mathbb Z^3\), write
\[
w(a)=\max_{p\in P}a\cdot p-\min_{p\in P}a\cdot p.
\]
If an affine-integer image fit inside a cube of span at most \(167\), each row \(a\) of \(B\) would satisfy \(w(a)\le167\).

Three differences of vertices of \(P\) are
\[
d_1=P_7-P_8=(-9,-84,51),\qquad
d_2=P_{16}-P_{20}=(84,0,0),
\]
\[
d_3=P_{12}-P_{24}=(9,-51,-93).
\]
Let \(D\) be the matrix with these rows. If \(w(a)\le167\), then
\[
\|Da\|_\infty\le167.
\]
The exact inverse is
\[
D^{-1}=
\begin{pmatrix}
0&1/84&0\\
-31/3471&-1/2314&-17/3471\\
17/3471&45/32396&-28/3471
\end{pmatrix}.
\]
Its row \(\ell^1\)-norms are
\[
\frac1{84},\qquad\frac{33}{2314},\qquad\frac{465}{32396}.
\]
Therefore
\[
|a_1|<2,\qquad |a_2|<3,\qquad |a_3|<3.
\]
There are only \(3\cdot5\cdot5-1=74\) nonzero integer vectors in this box. Exact evaluation of their widths shows
\[
w(a)\le167
\quad\Longleftrightarrow\quad
a=\pm(1,0,0),
\]
and those two covectors have width \(156\).

Thus no three linearly independent integer covectors can all have width at most \(167\). No invertible affine integral image of \(V\) can fit in an axis-aligned cube of span \(167\). The displayed \(\Phi(V)\) fits in span \(168\), proving the claimed optimum.

## Context and significance

Mizhaev's 2026 preprint supplies a self-contained integer certificate for this 24-vertex, eight-nonagon genus-3 surface, and explicitly states that its certificate does **not** establish coordinate minimality. The theorem above gives a sharp coordinate statement for the entire affine orbit of that concrete realization: the coordinates can be compressed substantially, and \(168\) is the exact best cube span obtainable by any invertible affine transformation that keeps all 24 vertices integral.

This is deliberately narrower than global coordinate minimality for the combinatorial type. A different, non-affinely-equivalent realization could conceivably fit into a smaller grid.

## Verification

`artifacts/verify_affine_grid.py` uses exact rational/integer arithmetic to:
1. apply \(\Phi\) to all 24 source vertices;
2. verify \(\det D\Phi=1/60\);
3. compute the transformed coordinate ranges;
4. certify that the transformed difference lattice has index \(1\);
5. verify the finite lattice-width certificate proving the lower bound.

The recorded output is in `artifacts/VERIFICATION.txt`.

## Limitations

- The optimality statement is for the affine orbit of Mizhaev's specific coordinate realization, not for all geometric realizations of the same \(\{9,3\}\) map.
- The affine compression does not preserve the original Euclidean metric symmetry; it preserves only the conjugate affine symmetry.
- The geometric validity of the source surface is taken from Mizhaev's exact realization theorem. The new verification independently checks the affine and lattice claims, not a second full face-intersection enumeration.
- The motivating preprint is very recent, so unindexed parallel observations remain a residual originality risk.

## References

1. Ruslan Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, arXiv:2609.17700 (submitted 15 September 2026). https://arxiv.org/abs/2609.17700
2. Stefan Hougardy, Frank H. Lutz, and Mariano Zelke, *Polyhedra of Genus 3 with 10 Vertices and Minimal Coordinates*, Electronic Geometry Models, 2006. https://www.eg-models.de/models/Surfaces/Polyhedral_Surfaces/2006.02.001/
