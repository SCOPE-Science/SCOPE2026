# Sharp convexity threshold for the cubic constant-width support family \(h_{\alpha,\beta}(u)=\alpha+\beta u_1u_2u_3\)

## Finding

For \(\alpha>0\) and \(\beta\in\mathbb R\), define
\[
h_{\alpha,\beta}(u)=\alpha+\beta u_1u_2u_3,\qquad u\in S^2.
\]
Then \(h_{\alpha,\beta}\) is a support function if and only if
\[
\alpha\ge \frac{4\sqrt{6}}{9}|\beta|.
\]
Since the cubic term is odd, every resulting body has constant width \(2\alpha\). In the normalization \(\alpha=1\), the exact admissible interval is
\[
|\varepsilon|\le \frac{3\sqrt{6}}{8}
\]
for \(h_\varepsilon(u)=1+\varepsilon u_1u_2u_3\).

If the inequality is strict, the curvature-radius operator is positive definite at every normal, so the body is smooth and strictly convex with positive principal radii. At equality, one radius vanishes at exactly 12 normals: their squared coordinates are a permutation of \((2/3,1/6,1/6)\), and the sign of \(u_1u_2u_3\) agrees with the sign of \(\beta\).

## Assumptions and scope

The statement is three-dimensional and concerns the explicit cubic family on \(S^2\). It does not claim an optimal threshold for other odd spherical harmonics or for higher-dimensional analogues.

The support-function criterion used below is the standard one: for a continuously differentiable constant-width function on the sphere, the homogeneous extension is a support function when
\[
\nabla^2_{S^2}h+hI
\]
is positive semidefinite on every tangent plane. For smooth \(h\), positive definiteness gives positive principal radii.

## Proof

Set
\[
f(u)=u_1u_2u_3,\qquad
A(u)=\nabla^2_{S^2}f(u)+f(u)I.
\]
For the homogeneous cubic \(F(x,y,z)=xyz\), the spherical Hessian identity on \(u^\perp\) is
\[
\nabla^2_{S^2}f=(D^2F)|_{u^\perp}-3fI.
\]
Therefore
\[
A(u)=(D^2F)|_{u^\perp}-2f(u)I,
\]
where
\[
D^2F=
\begin{pmatrix}
0&z&y\\
z&0&x\\
y&x&0
\end{pmatrix}
\]
at \(u=(x,y,z)\in S^2\).

Write
\[
s=xyz,\qquad q=x^2y^2+y^2z^2+z^2x^2.
\]
The trace and determinant of \(A(u)\) on the two-dimensional tangent plane are
\[
\operatorname{tr}A=-10s,\qquad
\det A=16s^2+4q-1.
\]
Hence the two eigenvalues are
\[
\lambda_\pm(u)=-5s\pm\sqrt{1-4q+9s^2}.
\]
The expression under the radical is nonnegative because it is one quarter of the squared eigenvalue gap of the real symmetric tangent operator.

Put
\[
X=x^2,\quad Y=y^2,\quad Z=z^2,\qquad X+Y+Z=1.
\]
The spectral radius is
\[
\rho(X,Y,Z)
=5\sqrt{XYZ}
+\sqrt{1-4(XY+YZ+ZX)+9XYZ}.
\]
On the boundary \(XYZ=0\), direct substitution gives \(\rho\le 1\). If the radical vanishes, then
\[
\rho=5\sqrt{XYZ}\le \frac{5}{3\sqrt{3}}
<\frac{4\sqrt{6}}{9}.
\]
At any remaining interior critical point, subtracting the Lagrange equations for two coordinates shows that at least two of \(X,Y,Z\) are equal. Thus it suffices to set
\[
Y=Z=t,\qquad X=1-2t,\qquad 0\le t\le \frac12.
\]
Then
\[
XYZ=t^2(1-2t)
\]
and
\[
1-4(XY+YZ+ZX)+9XYZ=(1-3t)^2(1-2t).
\]
Consequently
\[
\rho(t)=
\begin{cases}
(1+2t)\sqrt{1-2t},&0\le t\le 1/3,\\
(8t-1)\sqrt{1-2t},&1/3\le t\le 1/2.
\end{cases}
\]
The first branch has its unique maximum at \(t=1/6\), with value
\[
\frac{4\sqrt{6}}{9},
\]
while the second branch has maximum \(1\), attained at \(t=3/8\). Therefore
\[
\sup_{u\in S^2}\|A(u)\|_{\mathrm{op}}
=\frac{4\sqrt{6}}{9}.
\]

Now
\[
\nabla^2_{S^2}h_{\alpha,\beta}+h_{\alpha,\beta}I
=\alpha I+\beta A(u).
\]
It is positive semidefinite for every \(u\) exactly when
\[
\alpha\ge |\beta|\sup_{u\in S^2}\|A(u)\|_{\mathrm{op}}
=\frac{4\sqrt{6}}{9}|\beta|.
\]
This is both necessary and sufficient by the support-function criterion, after rescaling the constant-width normalization if desired.

The maximizers have squared coordinates equal to a permutation of \((2/3,1/6,1/6)\). At
\[
u=\frac{1}{\sqrt{6}}(2,1,1),
\qquad
v=\frac{1}{\sqrt{2}}(0,1,-1)\in u^\perp,
\]
one has
\[
A(u)v=-\frac{4\sqrt{6}}{9}v.
\]
Thus for \(\beta>0\) the zero eigenvalue at the threshold occurs precisely at the 12 maximizers with \(u_1u_2u_3>0\); for \(\beta<0\), it occurs at the 12 maximizers with \(u_1u_2u_3<0\).

Finally,
\[
h_{\alpha,\beta}(u)+h_{\alpha,\beta}(-u)=2\alpha,
\]
so every admissible member has constant width \(2\alpha\).

## Verification

The tangent trace follows from
\[
\operatorname{tr}(D^2F-2sI)=-6s,\qquad
u^\mathsf{T}(D^2F-2sI)u=4s,
\]
hence the tangent trace is \(-10s\).

For the determinant, the determinant of the restriction to \(u^\perp\) equals
\[
u^\mathsf{T}\operatorname{adj}(D^2F-2sI)u.
\]
Using \(x^2+y^2+z^2=1\), this simplifies exactly to
\[
16s^2+4q-1.
\]
The one-variable maximization was differentiated symbolically; its two candidate maxima are \(4\sqrt{6}/9\) and \(1\), with the former larger.

No numerical experiment is used as proof.

## Relationship to prior work

Myroshnychenko, Ryabogin, and Saroglou use
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3
\]
to establish that the triangular projection-symmetry case is exceptional. Their Theorem 5.4 proves convexity only for sufficiently small \(|\varepsilon|\), by continuity of the curvature-radius operator. Their Proposition 5.1 supplies the great-circle Fourier structure that gives threefold rotational symmetry of every planar projection up to translation.

The present calculation supplies the exact missing convexity range for that canonical family and identifies the curvature-degeneracy normals at the endpoint.

Earlier expository constant-width constructions also include an \(xyz\) term in a spherical support function, but the inspected formula source only requires the constant term to be “large enough”; it does not state the sharp threshold above.

## Limitations

This is a sharp statement for one explicit cubic family in \(\mathbb R^3\), not a classification of all non-spherical bodies with threefold-symmetric planar projections. It does not determine whether endpoint bodies have additional geometric regularity beyond what follows from the semidefinite support-function criterion.

Targeted source and semantic-record searches found no prior statement of the exact constants \(4\sqrt{6}/9\) or \(3\sqrt{6}/8\) for this family, but bibliographic search cannot prove absolute novelty; an older result under different notation remains a residual risk.

## References

1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, “On convex bodies with rotationally symmetric planar projections,” arXiv:2609.27192v1, 2026.
2. R. Hynd, “On Extreme Constant Width Bodies in \(\mathbb R^3\),” Discrete & Computational Geometry, 2025, doi:10.1007/s00454-025-00779-6.
3. 3D-XplorMath Consortium, “Surfaces of Constant Width,” explicit support-function formulas, accessed 2026-10-01.
