# Affine-lattice box optimality of an integer equivelar octahedron of genus 3

## Result

Mizhaev's integer realization of the equivelar octahedron of genus 3 (arXiv:2609.17700v1) has all 72 listed coordinate entries divisible by 3. Dividing every vertex by 3 therefore gives another integer-coordinate realization of exactly the same embedded polyhedral surface, with the same face incidence, genus, and geometric symmetry. Write its vertex set as \(V\subset\mathbb Z^3\).

The normalized coordinates are

\[
\begin{array}{c|rrr@{\qquad}c|rrr}
1&-24&28&6&13&-3&-49&69\\
2&-12&37&34&14&28&24&-6\\
3&24&-28&6&15&37&12&-34\\
4&12&-38&34&16&-16&-28&6\\
5&0&100&78&17&49&-3&-69\\
6&-28&16&-6&18&-6&42&48\\
7&3&49&69&19&-42&-6&-48\\
8&0&-100&78&20&-100&0&-78\\
9&28&-16&-6&21&-28&-24&-6\\
10&-38&-12&-34&22&6&-42&48\\
11&16&28&6&23&42&6&-48\\
12&-49&3&-69&24&100&0&-78
\end{array}
\]

For a finite set \(X\subset\mathbb R^3\) and \(u\in\mathbb R^3\), define its directional width by
\[
w_X(u)=\max_{x\in X}\langle u,x\rangle-\min_{x\in X}\langle u,x\rangle.
\]
Then the normalized configuration has the following sharp integral-affine property.

**Theorem.** Let \(F(x)=Ax+b\) be any invertible affine map of \(\mathbb R^3\) such that \(F(V)\subset\mathbb Z^3\). If \(s_1\le s_2\le s_3\) are the three side lengths of the axis-aligned bounding box of \(F(V)\), sorted increasingly, then
\[
\boxed{(s_1,s_2,s_3)\ge (156,200,200)}
\]
coordinatewise. The normalized coordinates above attain equality. Consequently, among all integral affine images of this realization,
\[
\boxed{\min s_1s_2s_3=6{,}240{,}000}
\]
and the smallest possible longest coordinate span is exactly \(200\).

Equivalently, the normalized realization has lattice width
\[
\boxed{\operatorname{lw}(V)=156,}
\]
and the only primitive lattice directions attaining width \(156\) are \(\pm e_3\); every other primitive lattice direction has width at least \(200\).

This is an affine-orbit optimality statement. It does **not** assert global coordinate minimality among all geometric realizations of the same combinatorial surface.

## Proof

### 1. The factor-three normalization is integral and geometrically valid

Every coordinate in Mizhaev's Table 1 is a multiple of \(3\). Homothety by \(1/3\) is an invertible affine map, so it preserves planarity of faces, the face-intersection pattern, embeddedness, orientability, genus, and the \(C_4\) symmetry. Thus the table above is an integer realization of the same polyhedral surface. Its coordinate ranges are
\[
x,y\in[-100,100],\qquad z\in[-78,78],
\]
so the attained coordinate-span profile is \((156,200,200)\) after sorting.

### 2. The normalized vertex-difference lattice is all of \(\mathbb Z^3\)

Let \(v_i\) denote the normalized vertices and let
\[
L=\operatorname{span}_{\mathbb Z}\{v_i-v_1:1\le i\le24\}\subseteq\mathbb Z^3.
\]
Two explicit maximal minors of the difference matrix are
\[
\det[v_{15}-v_1,\ v_{17}-v_1,\ v_{23}-v_1]=-8
\]
and
\[
\det[v_2-v_1,\ v_{12}-v_1,\ v_{15}-v_1]=1325.
\]
Since \(\gcd(8,1325)=1\), the index of \(L\) in \(\mathbb Z^3\), which divides every maximal minor, is \(1\). Hence
\[
\boxed{L=\mathbb Z^3.}
\]
In particular, the factor-three rescaling is a primitive integral normalization: no further nontrivial uniform contraction, even combined with a translation, can keep all vertices integral.

Now suppose \(F(x)=Ax+b\) is invertible and \(F(V)\subset\mathbb Z^3\). Then
\[
A(v_i-v_1)=F(v_i)-F(v_1)\in\mathbb Z^3
\]
for every \(i\). Because the differences generate \(\mathbb Z^3\), it follows that \(A\mathbb Z^3\subseteq\mathbb Z^3\), hence every entry of \(A\) is an integer.

### 3. Two vertex pairs force width at least 200 in every nonvertical lattice direction

The normalized table contains the exact differences
\[
v_5-v_8=(0,200,0),\qquad v_{24}-v_{20}=(200,0,0).
\]
Therefore for every integer covector \(u=(a,b,c)\),
\[
w_V(u)\ge 200|b|,\qquad w_V(u)\ge200|a|.
\]
If \((a,b)\ne(0,0)\), then
\[
\boxed{w_V(u)\ge200.}
\]
If \((a,b)=(0,0)\) and \(u\) is primitive, then \(u=\pm e_3\), and the displayed coordinate range gives
\[
w_V(\pm e_3)=78-(-78)=156.
\]
This proves the lattice-width statement and the uniqueness, up to sign, of the minimizing primitive direction.

### 4. The full bounding-box profile is sharp

Let \(r_1,r_2,r_3\in\mathbb Z^3\) be the three rows of the integral matrix \(A\). The three coordinate spans of \(F(V)\) are exactly
\[
w_V(r_1),\quad w_V(r_2),\quad w_V(r_3).
\]
Because \(A\) is invertible, its rows are linearly independent. At most one row can have first two coordinates both zero. Hence at least two rows have width at least \(200\), while every nonzero vertical integer row \((0,0,c)\) has width \(156|c|\ge156\). Thus, after sorting,
\[
(s_1,s_2,s_3)\ge(156,200,200).
\]
The identity map attains equality, proving sharpness and the box-volume product bound.

## Context and significance

Mizhaev's paper gives an exact integer certificate for a closed orientable \(\{9,3\}\) polyhedral surface of genus \(3\), with 24 vertices, 36 edges, eight nonagonal faces, and geometric symmetry \(C_4\). Its reproducibility section explicitly states that the certificate does not establish coordinate minimality or optimal aspect ratios. The present result identifies a canonical primitive rescaling and then proves a sharp coordinate-span theorem throughout the entire affine orbit subject to integrality.

The distinction from global coordinate minimality is essential. Earlier work of Hougardy, Lutz, and Zelke studied coordinate-minimal realizations of different genus-3 triangulations by enumerating integer configurations in small cubes. No analogous enumeration is performed here, and the theorem leaves open whether a genuinely different realization of Mizhaev's combinatorial surface can use smaller coordinates.

## Verification

`artifacts/verify.py` checks, using only exact integer arithmetic, the two determinant certificates, their coprimality, the forcing vertex differences, the coordinate ranges, and the attained box-volume product.

## Limitations

- Optimality is proved only within the affine class of the displayed realization under the requirement that all transformed vertices remain integral. It is not a global minimum over all realizations of the same map.
- The theorem minimizes the sorted coordinate-span profile and hence the bounding-box volume product and longest span in this affine-integral class. It does not claim an optimal Euclidean aspect ratio among arbitrary realizations.
- Mizhaev's 2020 precursor was identified and its available bibliographic/abstract material was checked, but its full text was not inspected here; a differently phrased earlier coordinate observation remains a residual historical risk.
- The 2026 integer-coordinate preprint is very recent, so a later revision may incorporate the normalization or the affine-lattice argument.

## References

1. R. Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, arXiv:2609.17700v1 (2026). https://arxiv.org/abs/2609.17700
2. R. Mizhaev, *Equivelar octahedron of genus 3 in 3-space* (2020), DOI: 10.31219/osf.io/hvtey.
3. S. Hougardy, F. H. Lutz, M. Zelke, *Polyhedra of genus 3 with 10 vertices and minimal coordinates*, arXiv:math/0604017 (2006). https://arxiv.org/abs/math/0604017
