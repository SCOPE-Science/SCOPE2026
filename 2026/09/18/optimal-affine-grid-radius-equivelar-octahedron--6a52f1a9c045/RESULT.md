# Optimal affine integer grid radius for Mizhaev's genus-three equivelar octahedron

## Statement

Mizhaev (2026) gives an integer-coordinate realization of an equivelar polyhedral surface of type \(\{9,3\}\) and genus \(3\), with 24 vertices, 36 edges, eight planar nonagonal faces, and geometric symmetry group \(C_4\). Its published coordinates have \(\ell_\infty\)-radius \(300\). The paper explicitly does not claim coordinate minimality.

Let \(V=\{v_1,\ldots,v_{24}\}\subset\mathbb Z^3\) be Mizhaev's published vertex set. Call
\[
F(x)=Mx+t,\qquad M\in GL_3(\mathbb R),\ t\in\mathbb R^3,
\]
an **affine integer copy** when \(F(V)\subset\mathbb Z^3\). Define its grid radius by
\[
R(F)=\max_{v\in V}\|F(v)\|_\infty.
\]
Then:

**Theorem 1 (sharp affine grid radius).**
\[
\boxed{\min_F R(F)=84.}
\]
In particular, the published radius \(300\) can be reduced to \(84\), and no invertible affine reparameterization of this particular realization can produce integer coordinates in a smaller centered cube.

The minimum is attained by
\[
\boxed{
F_{84}(x,y,z)=
\left(
\frac z3,
\frac{x}{10}-\frac y5-\frac z6+15,
\frac x5+\frac y{10}+\frac z6+15
\right).
}
\]
Its 24 integer vertices are

| no. | \((X,Y,Z)\) | no. | \((X,Y,Z)\) |
|---:|:---|---:|:---|
|1|\((6,-12,12)\)|13|\((69,9,33)\)|
|2|\((34,-28,36)\)|14|\((-6,12,36)\)|
|3|\((6,36,24)\)|15|\((-34,36,24)\)|
|4|\((34,24,28)\)|16|\((6,24,0)\)|
|5|\((78,-84,84)\)|17|\((-69,66,9)\)|
|6|\((-6,0,0)\)|18|\((48,-36,48)\)|
|7|\((69,-48,66)\)|19|\((-48,30,-36)\)|
|8|\((78,36,24)\)|20|\((-78,24,-84)\)|
|9|\((-6,36,24)\)|21|\((-6,24,-12)\)|
|10|\((-34,28,-28)\)|22|\((48,18,30)\)|
|11|\((6,0,36)\)|23|\((-48,48,18)\)|
|12|\((-69,33,-48)\)|24|\((-78,84,36)\)|

Using the same face walks as the source realization, supporting planes may be written as
\[
\begin{array}{rclcrcl}
F_1&:&-2X+Y+3Z=12,&&F_2&:&Y+3Z=108,\\
F_3&:&Y+2Z=84,&&F_4&:&-X+Y+2Z=6,\\
F_5&:&-2X-2Y+Z=24,&&F_6&:&-X-2Y+Z=-54,\\
F_7&:&3X+3Y-Z=-18,&&F_8&:&X+3Y-Z=78.
\end{array}
\]
Because \(F_{84}\) is invertible affine, it preserves planarity, simplicity of the face polygons, all incidences, and the absence of unintended intersections.

There is also a sharp symmetry-preserving version. Mizhaev's generator is
\[
T(x,y,z)=(y,-x,-z).
\]
Say an affine integer copy is **Euclidean-\(C_4\)-preserving** when \(FTF^{-1}\) is a Euclidean isometry. Then:

**Theorem 2 (sharp Euclidean-symmetry radius).**
\[
\boxed{\min_{F:\,FTF^{-1}\text{ Euclidean}}R(F)=90.}
\]
The minimum is attained by the linear map
\[
\boxed{
F_{90}(x,y,z)=
\left(
\frac{x+3y}{10},
\frac{y-3x}{10},
\frac z3
\right).
}
\]
It commutes with \(T\), so the original order-four orthogonal symmetry survives literally as the same map. Its coordinate ranges are \([-90,90]\), \([-90,90]\), and \([-78,78]\).

## Proof of Theorem 1

Let
\[
L=\operatorname{span}_{\mathbb Z}\{v_i-v_1:2\le i\le24\}\subset\mathbb Z^3
\]
be the difference lattice of the published realization. Exact determinant arithmetic gives
\[
[\mathbb Z^3:L]=60.
\]
Equivalently, the gcd of the full-rank \(3\times3\) minors of the 23 difference vectors is \(60\).

Consider
\[
B=
\begin{pmatrix}
-1&2&4\\
-3&-4&2\\
3&0&0
\end{pmatrix},
\qquad \det B=60,
\]
and
\[
A=B^{-1}=
\begin{pmatrix}
0&0&1/3\\
1/10&-1/5&-1/6\\
1/5&1/10&1/6
\end{pmatrix}.
\]
Direct substitution shows \(Av_i\in\mathbb Z^3\) for all 24 vertices. Hence \(L\subseteq B\mathbb Z^3\). Both lattices have index \(60\), so
\[
L=B\mathbb Z^3.
\]
Therefore every dual-lattice covector has the unique form
\[
\lambda=q^TA,
\qquad q\in\mathbb Z^3.
\]
If an affine map \(F(x)=Mx+t\) sends all vertices to integer points, each row of \(M\) belongs to \(L^*\), because it takes every vertex difference to an integer. Thus the three rows of \(M\) correspond to three linearly independent integer vectors \(q\).

Put \(p_i=Av_i\), and for \(q\in\mathbb Z^3\) define the width
\[
w(q)=\max_i q\cdot p_i-\min_i q\cdot p_i.
\]
This is exactly the coordinate width of the covector \(q^TA\) on the original vertex set.

It remains to classify the very short dual covectors. To make this finite without any heuristic search, use the three differences \(p_8-p_1,p_{20}-p_1,p_{24}-p_1\), which form the columns of
\[
D=
\begin{pmatrix}
72&-84&-84\\
48&36&96\\
12&-96&24
\end{pmatrix}.
\]
If \(y=D^Tq\), then each component of \(y\) is a difference of two values \(q\cdot p_i\), so \(|y_j|\le w(q)\). Exact inversion gives
\[
(D^T)^{-1}=
\begin{pmatrix}
1/114&0&-1/228\\
1/114&1/420&41/7980\\
-1/228&-1/105&23/3990
\end{pmatrix}.
\]
The largest absolute row sum is \(157/7980\). Consequently
\[
w(q)<168
\quad\Longrightarrow\quad
|q_i|<168\frac{157}{7980}=\frac{314}{95}<4.
\]
Thus every such \(q\) lies in the finite box \([-3,3]^3\). Exact enumeration of its 342 nonzero integer points gives
\[
\boxed{w(q)<168\iff q=\pm(1,0,0),}
\]
and in those two cases \(w(q)=156\).

The three rows of an invertible \(M\) correspond to linearly independent \(q\)'s, so they cannot all have width below \(168\). At least one output coordinate therefore has range at least \(168\). Translation does not change coordinate width, and any real interval of width \(168\) has \(\max |x|\ge84\). Hence every affine integer copy satisfies
\[
R(F)\ge84.
\]

On the other hand, \(A\) itself gives coordinate ranges
\[
[-78,78],\qquad[-99,69],\qquad[-99,69].
\]
Adding \((0,15,15)\) centers the last two ranges and produces exactly the displayed map \(F_{84}\), with radius \(84\). This proves Theorem 1.

## Proof of Theorem 2

The same finite certificate classifies every covector relevant below. If \(w(q)<180\), then
\[
|q_i|<180\frac{157}{7980}=\frac{471}{133}<4,
\]
so again \(q\in[-3,3]^3\). Exact enumeration now gives only the ten signed vectors whose five projective directions are
\[
\boxed{
(1,0,0),\ (0,1,0),\ (0,0,1),\ (1,0,-1),\ (1,1,0),
}
\]
with widths \(156,168,168,168,168\), respectively.

Suppose an affine integer copy had \(R(F)<90\). Each of the three row covectors of its linear part would then have width less than \(180\), so, up to sign, its row directions would have to come from the five vectors above. There are exactly eight linearly independent unordered triples among them. For each triple, form the corresponding row matrix \(M\) and the conjugate
\[
O=MTM^{-1}.
\]
Exact rational arithmetic gives \(O^TO\ne I\) in all eight cases. Row signs and row permutations only conjugate \(O\) by a signed permutation matrix, so they cannot change orthogonality. Hence no affine integer copy of radius below \(90\) can make \(FTF^{-1}\) a Euclidean isometry.

Finally,
\[
C=
\begin{pmatrix}
1/10&3/10&0\\
-3/10&1/10&0\\
0&0&1/3
\end{pmatrix}
\]
sends all 24 vertices to integer points with radius \(90\), and \(CT=TC\). Thus \(CTC^{-1}=T\) is orthogonal, proving Theorem 2.

## Verification

`artifacts/verify.py` uses only exact integer and rational arithmetic from the Python standard library. It verifies the source vertex-face incidences, the difference-lattice index, both affine maps, the transformed planes, the complete short-covector certificate, and all eight low-radius symmetry cases. No floating-point comparison is used.

## Relation to prior work

Mizhaev's September 2026 paper supplies the exact 24-vertex certificate, the face walks, eight plane equations, and the order-four symmetry. It explicitly states that the certificate does not establish coordinate minimality, optimal aspect ratios, or historical priority. The present result does not claim global coordinate minimality among all realizations of the same combinatorial surface. Instead, it determines exactly the best possible integer coordinate radius inside the full affine-equivalence class of the newly published realization, and separately inside the subclass retaining the published \(C_4\) action as a Euclidean symmetry.

The 2026 paper identifies its realization with variant V2 from Mizhaev's 2020 preprint *Equivelar octahedron of genus 3 in 3-space*. Accessible metadata for that older preprint describes the same eight-face genus-three combinatorial object, but its full text was not available from the sources inspected. It therefore remains a specific originality risk for historical coordinate choices, although no accessible statement located there gives the affine-lattice optimality results above.

To the best of our knowledge, searches by the recent arXiv identifier, exact title, author, coordinate values, affine/lattice terminology, coordinate-minimality terminology, and synonymous formulations did not locate a prior computation of the difference-lattice dual widths or the sharp radii \(84\) and \(90\). Searches of the current SCOPE archive by the object and claim family found no overlap.

## Limitations

The number \(84\) is optimal only among integer realizations **affinely equivalent to Mizhaev's published coordinate realization**. A non-affinely-equivalent realization of the same abstract \(\{9,3\}\) surface may have smaller coordinates. Likewise, the radius \(90\) is optimal only among affine integer copies of this realization for which the conjugated published \(C_4\) generator is a Euclidean isometry. Neither theorem claims optimal Euclidean shape, edge lengths, aspect ratio, or global minimality over the full realization space.

The 2020 precursor was not inspected in full, so it leaves residual uncertainty about historical coordinate normalizations. The motivating integer certificate is also extremely recent, leaving the usual possibility of unindexed parallel work.

## References

1. R. Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, arXiv:2609.17700 (2026), https://arxiv.org/abs/2609.17700.
2. R. Mizhaev, *Equivelar octahedron of genus 3 in 3-space*, preprint (2020), DOI: 10.31219/osf.io/hvtey.
