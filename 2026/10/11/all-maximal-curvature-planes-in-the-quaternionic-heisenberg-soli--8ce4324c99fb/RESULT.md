# All maximal-curvature planes in the quaternionic Heisenberg soliton

## Finding

Let \(N\) be the seven-dimensional quaternionic Heisenberg group with the standard left-invariant metric for which
\[
X_1,X_2,X_3,X_4,Z_1,Z_2,Z_3
\]
is an orthonormal frame and the nonzero brackets are
\[
[X_1,X_3]=[X_2,X_4]=Z_1,
\]
\[
[X_1,X_4]=Z_2,\qquad [X_2,X_3]=-Z_2,
\]
\[
[X_1,X_2]=-Z_3,\qquad [X_3,X_4]=Z_3.
\]
This is the quaternionic Heisenberg Ricci-soliton metric studied by Tatsuno.

A two-plane \(\pi\subset T_eN\) has maximal sectional curvature
\[
K(\pi)=\frac4{11}
\]
if and only if it admits an orthonormal basis
\[
A=X+Z,\qquad B=Y+W,
\]
with horizontal components \(X,Y\in V=\operatorname{span}\{X_1,\ldots,X_4\}\) and central components \(Z,W\in\mathcal Z=\operatorname{span}\{Z_1,Z_2,Z_3\}\), such that
\[
X\perp Y,\qquad Z\perp W,
\]
\[
\boxed{
|X|=|Y|=\frac2{\sqrt{11}},
\qquad
|Z|=|W|=\sqrt{\frac7{11}},
}
\]
and, after writing
\[
x=\frac X{|X|},\qquad
y=\frac Y{|Y|},\qquad
z=\frac Z{|Z|},\qquad
w=\frac W{|W|},
\]
one has
\[
\boxed{
j(z)y=j(w)x,
\qquad
j(z)x=-j(w)y.
}
\]

Thus every maximizing plane has the same horizontal-central energy split
\[
\frac4{11}:\frac7{11},
\]
and the only remaining freedom is the compatible quaternionic alignment encoded by the two displayed \(j\)-relations.

## Assumptions and scope

The \(j\)-map is defined by
\[
\langle j(Z)X,Y\rangle
=
\langle Z,[X,Y]\rangle.
\]
For the metric above, \(N\) is of Heisenberg type:
\[
j(Z)^2=-|Z|^2\operatorname{Id}_V.
\]
In particular, if \(|z|=1\), then \(j(z)\) is an orthogonal complex structure on \(V\).

The classification is pointwise at the identity. Left translation transports it to every point of the homogeneous manifold.

The statement concerns the standard quaternionic Heisenberg Ricci-soliton metric only. It does not classify maximal-curvature planes for arbitrary left-invariant metrics on the same group.

## Proof

Take any two-plane \(\pi\). By an orthogonal change of its orthonormal basis, one may arrange
\[
A=X+Z,\qquad B=Y+W,
\]
with
\[
X\perp Y,\qquad Z\perp W.
\]
Indeed, the horizontal and central Gram matrices add to the identity, so diagonalizing one diagonalizes the other.

Set
\[
p=|X|^2,\qquad q=|Y|^2.
\]
Since \(A\) and \(B\) are unit,
\[
|Z|^2=1-p,\qquad |W|^2=1-q.
\]

For this quaternionic Heisenberg structure, if \(X\perp Y\), then
\[
|[X,Y]|^2=|X|^2|Y|^2=pq.
\]
To see this when \(X,Y\ne0\), write \(x=X/|X|\) and \(y=Y/|Y|\). The map
\[
\mathcal Z\longrightarrow x^\perp,\qquad
z\longmapsto j(z)x
\]
is an isometry between two three-dimensional spaces, hence \(y=j(\zeta)x\) for a unique unit \(\zeta\in\mathcal Z\). The defining identity of \(j\) then gives
\[
[x,y]=\zeta.
\]

Tatsuno's sectional-curvature formula for an adapted orthonormal basis gives
\[
\begin{aligned}
K(\pi)
={}&
\frac14|j(W)X|^2
+\frac14|j(Z)Y|^2
-\frac34|[X,Y]|^2\\
&+\frac12\langle j(Z)Y,j(W)X\rangle
-\langle j(Z)X,j(W)Y\rangle .
\end{aligned}
\]
The Heisenberg-type identities make the first three terms exact:
\[
|j(W)X|^2=p(1-q),
\]
\[
|j(Z)Y|^2=q(1-p),
\]
\[
|[X,Y]|^2=pq.
\]
The two mixed inner products have absolute value at most
\[
\sqrt{pq(1-p)(1-q)}.
\]
Therefore
\[
K(\pi)
\le
F(p,q),
\]
where
\[
F(p,q)
=
\frac14(p+q)-\frac54pq
+
\frac32\sqrt{pq(1-p)(1-q)}.
\]

Now put
\[
u=\sqrt{pq},
\qquad
v=\sqrt{(1-p)(1-q)}.
\]
Cauchy--Schwarz gives
\[
u+v\le1,
\]
with equality exactly when \(p=q\). Since
\[
p+q=1+u^2-v^2,
\]
we obtain
\[
4F
=
1-4u^2-v^2+6uv.
\]

For fixed \(u\), this is a concave quadratic in \(v\), whose unconstrained maximum is at \(v=3u\).

If
\[
0\le u\le\frac14,
\]
then
\[
4F
\le
1+5u^2
\le
\frac{21}{16}
<
\frac{16}{11}.
\]

If
\[
u\ge\frac14,
\]
then \(v\le1-u\le3u\), so the quadratic is increasing throughout the admissible interval and
\[
4F
\le
1-4u^2-(1-u)^2+6u(1-u)
=
8u-11u^2.
\]
The last parabola has its unique maximum at
\[
u=\frac4{11},
\]
where
\[
8u-11u^2=\frac{16}{11}.
\]
Hence
\[
K(\pi)\le F(p,q)\le\frac4{11}.
\]

Equality in the second inequality requires
\[
u=\frac4{11},
\qquad
v=1-u=\frac7{11}.
\]
Because \(u+v=1\), equality in Cauchy--Schwarz forces
\[
p=q=\frac4{11}.
\]
Thus
\[
|X|=|Y|=\frac2{\sqrt{11}},
\qquad
|Z|=|W|=\sqrt{\frac7{11}}.
\]

It remains to characterize equality in the mixed inner-product estimate. With the normalized vectors \(x,y,z,w\), the mixed contribution is
\[
\sqrt{pq(1-p)(1-q)}
\left(
\frac12\langle j(z)y,j(w)x\rangle
-
\langle j(z)x,j(w)y\rangle
\right).
\]
All four displayed vectors are unit. Its maximum \(3/2\) is attained if and only if
\[
\langle j(z)y,j(w)x\rangle=1
\]
and
\[
\langle j(z)x,j(w)y\rangle=-1.
\]
For unit vectors, these two equalities are respectively equivalent to
\[
j(z)y=j(w)x
\]
and
\[
j(z)x=-j(w)y.
\]
This proves necessity.

Conversely, any adapted orthonormal basis satisfying the stated length and \(j\)-alignment conditions has equality at every step above, and therefore
\[
K(\pi)=\frac4{11}.
\]

## Verification

The bundled checker verifies the algebraic reduction
\[
4F
=
1-4u^2-v^2+6uv,
\]
the two-branch maximization, and the unique equality point
\[
u=\frac4{11},
\qquad
v=\frac7{11}.
\]

It also reconstructs the three \(j\)-matrices from the six published Lie brackets and verifies the source's exhibited plane:
\[
\operatorname{span}
\left\{
\frac2{\sqrt{11}}X_3+\sqrt{\frac7{11}}Z_2,\,
\frac2{\sqrt{11}}X_4+\sqrt{\frac7{11}}Z_1
\right\}.
\]
For that plane,
\[
j(Z_2)X_4=j(Z_1)X_3
\]
and
\[
j(Z_2)X_3=-j(Z_1)X_4,
\]
so it satisfies the equality classification.

The proof is exact and does not infer the classification from numerical sampling.

## Relationship to prior work

Tatsuno proves that the standard quaternionic Heisenberg Ricci-soliton metric has
\[
K_{\min}=-\frac34,
\qquad
K_{\max}=\frac4{11},
\]
and hence pinching ratio
\[
-\frac{33}{16}.
\]
In Section 5.4 the paper exhibits one explicit plane with curvature \(4/11\), then proves the global upper bound using a modified curvature operator.

The inspected source does not state a classification of all planes attaining \(4/11\). The result here instead follows the equality conditions in the direct sectional-curvature formula. It shows that every maximizer has the same horizontal-central norm split and exactly the displayed quaternionic alignment.

The standard Lie algebra itself goes back to the classical geometry of two-step nilpotent groups and H-type structures. Searches using the exact value \(4/11\), quaternionic-Heisenberg aliases, maximal-sectional-curvature language, and equality-plane language did not locate an earlier classification of this maximizing locus.

## Limitations

The classification is for one canonical metric on the seven-dimensional quaternionic Heisenberg group. It does not classify equality cases for all H-type groups or for deformations of this metric.

The statement is intrinsic up to the existence of an adapted orthonormal basis; it does not reduce the maximizing locus further to an explicit quotient by the full isometry group.

Although targeted searches found no earlier equality classification, older two-step nilmanifold literature could contain an equivalent description under different notation.

## References

1. Tomoya Tatsuno, *Sectional Curvature Pinching of Two-Step Nilmanifolds*, arXiv:2609.13052v1, first submitted 11 September 2026.
2. Patrick Eberlein, *Geometry of 2-step nilpotent groups with a left invariant metric*, Annales scientifiques de l'École Normale Supérieure 27 (1994), 611--660.
3. Aroldo Kaplan, *Riemannian nilmanifolds attached to Clifford modules*, Geometriae Dedicata 11 (1981), 127--136.
