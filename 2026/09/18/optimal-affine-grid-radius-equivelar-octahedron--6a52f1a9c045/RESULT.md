# Sharp Euclidean-symmetry-preserving affine grid radius for Mizhaev's genus-three equivelar octahedron

## Statement

Let \(V\subset\mathbb Z^3\) be the 24-vertex integer realization in Ruslan Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, and let
\[
T(x,y,z)=(y,-x,-z)
\]
be its published order-four Euclidean symmetry.

Consider invertible affine maps
\[
F(x)=Mx+t
\]
such that \(F(V)\subset\mathbb Z^3\) and the conjugate \(FTF^{-1}\) is a Euclidean isometry. Define
\[
R(F)=\max_{v\in V}\|F(v)\|_\infty.
\]
Then
\[
\boxed{
\min_{F:\,F(V)\subset\mathbb Z^3,\;FTF^{-1}\ {\rm Euclidean}}R(F)=90.
}
\]

The minimum is attained by
\[
F_{90}(x,y,z)
=
\left(
\frac{x+3y}{10},
\frac{y-3x}{10},
\frac z3
\right).
\]
This map sends all 24 vertices to integer points with coordinate ranges contained in
\[
[-90,90]\times[-90,90]\times[-78,78],
\]
and it commutes with \(T\), so the source symmetry remains literally the same orthogonal transformation.

An unrestricted affine-integer radius \(84\) for this same realization had already been established publicly before this result. That unrestricted optimum is prior context here, not part of the new claim. The contribution is the sharp extra coordinate cost forced by retaining the published \(C_4\) action as a Euclidean symmetry.

## Proof

Let
\[
L=\operatorname{span}_{\mathbb Z}\{v_i-v_1\}
\]
be the difference lattice of the source vertex set. Exact determinant arithmetic gives
\[
[\mathbb Z^3:L]=60.
\]
With
\[
B=
\begin{pmatrix}
-1&2&4\\
-3&-4&2\\
3&0&0
\end{pmatrix},
\qquad
A=B^{-1},
\]
direct substitution gives \(Av_i\in\mathbb Z^3\) for every source vertex and \(|\det B|=60\), so \(L=B\mathbb Z^3\). Every row covector of the linear part of an affine integer copy is therefore uniquely of the form
\[
q^TA,\qquad q\in\mathbb Z^3.
\]

Write \(p_i=Av_i\) and define
\[
w(q)=\max_i q\cdot p_i-\min_i q\cdot p_i.
\]
Using three explicit vertex differences gives an invertible integer matrix \(D\) whose inverse has maximum absolute row sum \(157/7980\). Thus
\[
w(q)<180
\quad\Longrightarrow\quad
|q_i|<4.
\]
It is therefore enough to enumerate the finite box \([-3,3]^3\).

Exact evaluation shows that the only projective directions with width below \(180\) are
\[
(1,0,0),\quad
(0,1,0),\quad
(0,0,1),\quad
(1,0,-1),\quad
(1,1,0),
\]
with widths \(156,168,168,168,168\), respectively.

If \(R(F)<90\), all three row covectors of \(M\) have width below \(180\). Up to signs and row permutations, the row directions must therefore be a linearly independent triple chosen from the five directions above. There are exactly eight such unordered triples.

For each triple, form the corresponding rational row matrix \(M\) and compute
\[
O=MTM^{-1}.
\]
Exact rational arithmetic gives
\[
O^TO\ne I
\]
for every one of the eight triples. Changing row signs or row order only conjugates \(O\) by a signed permutation matrix and cannot turn a non-orthogonal matrix into an orthogonal one. Hence no affine integer copy with radius below \(90\) can preserve the source \(C_4\) generator as a Euclidean isometry.

Finally,
\[
C=
\begin{pmatrix}
1/10&3/10&0\\
-3/10&1/10&0\\
0&0&1/3
\end{pmatrix}
\]
maps all vertices to integer points with radius \(90\) and satisfies \(CT=TC\). Therefore \(CTC^{-1}=T\) is orthogonal, proving sharpness.

## Verification

`artifacts/verify.py` uses exact integer and rational arithmetic. It verifies the source incidence data used by the coordinate calculation, the difference-lattice index, the complete short-covector classification, the eight independent low-width triples, non-orthogonality of every sub-\(90\) conjugate, and the radius-\(90\) attaining map.

## Relation to prior work

Mizhaev's primary paper gives the 24-vertex integer realization and its exact \(C_4\) symmetry but does not claim coordinate minimality. A public result dated 2026-09-17 already proved that the unrestricted affine-integer cube radius of the same realization is \(84\). The present theorem is deliberately different: it imposes the additional requirement that the distinguished source symmetry remain Euclidean after affine reparameterization and proves the sharp constrained radius \(90\).

## Limitations

The theorem concerns the affine orbit of the published realization. A non-affinely-equivalent realization of the same abstract \(\{9,3\}\) surface may have smaller coordinates. The symmetry constraint concerns the published order-four generator. No claim is made about global coordinate minimality, optimal edge lengths, or all possible symmetry actions.

## References

1. R. Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, arXiv:2609.17700.
2. R. Mizhaev, *Equivelar octahedron of genus 3 in 3-space*, DOI: 10.31219/osf.io/hvtey.
