# A quartic criterion for maximal-surface-area parallelepipeds through prescribed ellipsoid points

## Finding

Let \(A\) be any real symmetric positive-definite \(3\times3\) matrix. Define the centered ellipsoid
\[
E_A=\{x\in\mathbb R^3:x^{\mathsf T}A^{-1}x\leq1\}.
\]
An *inscribed parallelepiped* means a full-dimensional parallelepiped all eight of whose vertices lie on \(\partial E_A\). Write \(C=A^{-1}\), let \(x_0\in\partial E_A\), and normalize its direction as \(y=A^{-1/2}x_0\in S^2\). Set
\[
s=\operatorname{tr}C,\qquad m=y^{\mathsf T}Cy,\qquad q=y^{\mathsf T}C^2y,
\]
and define the explicit quartic-on-the-sphere expression
\[
F_C(y)=9m^2+2sm-12q+2\operatorname{tr}(C^2)-s^2.
\]
**Theorem.** There exists an inscribed parallelepiped having \(x_0\) as a vertex and attaining the unrestricted maximum of Euclidean surface area among all inscribed parallelepipeds if and only if
\[
\boxed{F_C(y)=0.}
\]
The unrestricted maximum is
\[
S_{\max}(E_A)=\frac8{\sqrt3}\sqrt{\det A}\sqrt{\operatorname{tr}(A^{-1})}.
\]
The criterion is invariant under orthogonal changes of coordinates, and when it holds a maximizing parallelepiped can be reconstructed explicitly from a single angle.

**Axial specialization.** If \(C=aI+(b-a)vv^{\mathsf T}\), where \(a,b>0\), \(a\ne b\), and \(v\in S^2\), then
\[
F_C(y)=(a-b)^2\bigl((y\cdot v)^2-1\bigr)\bigl(9(y\cdot v)^2-1\bigr).
\]
Hence a nonspherical ellipsoid of revolution has maximizing parallelepipeds through precisely its two normalized axis poles and the two normalized latitude circles satisfying \(|y\cdot v|=1/3\). The circles, unlike the poles, consist of non-principal-axis points. For a Euclidean ball every boundary point is admissible.

## Assumptions and scope

All matrices and vectors in the theorem are **real**, Euclidean, and three-dimensional. The matrix \(A\) is symmetric and strictly positive definite. Surface area is the sum of Euclidean areas of the six facets, not the ellipsoid's surface area or the parallelepiped's volume. The maximum is taken over *all* full-dimensional parallelepipeds inscribed in the same ellipsoid, without a prescribed vertex; the theorem decides whether that same value is attainable after imposing the specified vertex.

It is essential that \(y\) have unit norm. This is automatic from \(x_0\in\partial E_A\), and cannot be replaced by an arbitrary unnormalized vector. All formulas are valid for eigenvalue multiplicities, including the spherical case. No nondegeneracy of the quartic zero set is assumed.

## Proof

**Step 1: Surface-area equality is a restricted constant-diagonal problem.** Let the edges of an inscribed parallelepiped be \(v_j\). Expanding the eight equal quadratic equations for its vertices shows that its center is zero and \(v_i^{\mathsf T}Cv_j=0\) for distinct indices. Thus its edge matrix admits the representation
\[
v_j=\lambda_j A^{1/2}u_j,\qquad U=[u_1\ u_2\ u_3]\in O(3),\qquad \lambda_j>0,\qquad\sum_{j=1}^3\lambda_j^2=4.
\]
The six facet areas, using the principal minors of the edge Gram matrix, sum to
\[
S=2\sqrt{\det A}\left(\prod_{j=1}^3\lambda_j\right)
\sum_{i=1}^3\frac{\sqrt{u_i^{\mathsf T}Cu_i}}{\lambda_i}.
\]
Cauchy--Schwarz and \(\sum_i u_i^{\mathsf T}Cu_i=s\) imply
\[
S\leq2\sqrt{\det A}\sqrt{s}\,
\sqrt{\lambda_1^2\lambda_2^2+\lambda_1^2\lambda_3^2+\lambda_2^2\lambda_3^2}
\leq\frac8{\sqrt3}\sqrt{\det A}\sqrt{s}.
\]
The last inequality uses \(\sum\lambda_j^2=4\), with equality only when \(\lambda_j=2/\sqrt3\) for all indices. Equality in Cauchy--Schwarz then requires, and is implied by,
\[
 u_1^{\mathsf T}Cu_1=u_2^{\mathsf T}Cu_2=u_3^{\mathsf T}Cu_3=s/3.
\]
The all-plus vertex is \(x_0\) exactly when \(y=(u_1+u_2+u_3)/\sqrt3\). Thus the required maximizing parallelepiped exists precisely when there are three orthonormal vectors \(u_j\) obeying
\[
\langle u_j,y\rangle=1/\sqrt3,\qquad u_j^{\mathsf T}Cu_j=s/3\quad(j=1,2,3).
\tag{1}
\]
This agrees with the unrestricted maximum and the prescribed-vertex reduction given in Kania's Theorem 4.2 and Proposition 5.2 [1].

**Step 2: Parametrize every barycentric orthonormal basis.** Fix any oriented orthonormal pair \(e,f\) spanning \(y^\perp\). Every orthonormal triple satisfying the first part of (1), up to permuting its columns, has the form
\[
u_j=\frac y{\sqrt3}+\sqrt{\frac23}\,
\bigl(\cos\theta_j\,e+\sin\theta_j\,f\bigr),
\qquad \theta_j=\phi+\frac{2\pi(j-1)}3.
\tag{2}
\]
Indeed, the projected vectors have squared length \(2/3\) and pairwise inner product \(-1/3\), so they make an equilateral triangle in \(y^\perp\); conversely (2) gives an orthonormal triple with the required barycentre.

Put \(P=I-yy^{\mathsf T}\), \(b=PCy\in y^\perp\), and define the traceless self-adjoint operator on that plane
\[
D=(PCP)|_{y^\perp}-\frac{s-m}{2}I_{y^\perp}.
\]
In the frame \((e,f)\), let \(b=b_1e+b_2f\) and \(D\) have matrix
\[
\begin{pmatrix}d_1&d_2\\d_2&-d_1\end{pmatrix}.
\]
Substitution of (2) yields the *exact* diagonal residual
\[
u_j^{\mathsf T}Cu_j-\frac s3
=\frac23\left[\sqrt2(b_1\cos\theta_j+b_2\sin\theta_j)
+d_1\cos2\theta_j+d_2\sin2\theta_j\right].
\tag{3}
\]

**Step 3: The threefold resonance has a solution exactly at one norm equality.** At the three angles in (2), the identities
\[
\cos2\theta_j=\cos(3\phi-\theta_j),\qquad
\sin2\theta_j=\sin(3\phi-\theta_j)
\]
turn the bracket of (3) into \(\alpha\cos\theta_j+\beta\sin\theta_j\), where
\[
\alpha=\sqrt2 b_1+d_1\cos3\phi+d_2\sin3\phi,\qquad
\beta=\sqrt2 b_2+d_1\sin3\phi-d_2\cos3\phi.
\]
All three residuals vanish if and only if \(\alpha=\beta=0\), because a nonzero first harmonic cannot vanish at three equally spaced angles. With \(\delta=d_1+id_2\) and \(\eta=b_1+ib_2\), the two equations become
\[
e^{3i\phi}\overline\delta=-\sqrt2\,\eta.
\tag{4}
\]
For \(\delta\ne0\), a real \(\phi\) exists if and only if \(|\delta|^2=2|\eta|^2\), and (4) explicitly specifies its phase modulo \(2\pi/3\). If \(\delta=0\), equation (4) is soluble exactly when \(\eta=0\); then any \(\phi\) works. Thus the complete solvability condition is
\[
d_1^2+d_2^2=2(b_1^2+b_2^2)
\quad\Longleftrightarrow\quad
\operatorname{tr}_{y^\perp}(D^2)=4\|b\|^2.
\tag{5}
\]
This is independent of the arbitrary tangent frame \((e,f)\).

**Step 4: Reduce (5) to the invariant quartic.** Since \(m=y^{\mathsf T}Cy\) and \(q=y^{\mathsf T}C^2y\), elementary projection identities give
\[
\|b\|^2=q-m^2,\qquad
\operatorname{tr}_{y^\perp}(D^2)
=\operatorname{tr}(C^2)-2q+m^2-\frac12(s-m)^2.
\]
Consequently
\[
2\bigl(\operatorname{tr}_{y^\perp}(D^2)-4\|b\|^2\bigr)
=9m^2+2sm-12q+2\operatorname{tr}(C^2)-s^2=F_C(y).
\]
Equations (1)--(5) therefore establish both implications of the theorem for every strictly positive-definite \(C\), with no genericity exceptions.

**Step 5: Axial specialization.** Substitute \(C=aI+(b-a)vv^{\mathsf T}\), put \(t=(y\cdot v)^2\), and use
\[
s=2a+b,\quad m=a+(b-a)t,\quad
q=a^2+(b^2-a^2)t,\quad
\operatorname{tr}(C^2)=2a^2+b^2.
\]
Direct expansion factors the criterion as \(F_C(y)=(a-b)^2(t-1)(9t-1)\), proving the pole/latitude assertion. For \(a=b\), all the terms cancel and every point qualifies. \(\square\)

## Verification

The included standalone Python script `checker.py` uses exact symbolic arithmetic to verify the invariant identity in an arbitrary symmetric matrix written in coordinates with \(y=e_3\); the axial factorization; an explicit non-axis example; and all eight ellipsoidal vertex equations and the sharp total surface area. It also tests 300 nontrivial three-harmonic reconstructions numerically, with maximum measured orthogonality error below \(6\times10^{-16}\) and maximum constant-diagonal error below \(9\times10^{-15}\). These finite tests are consistency checks, not a substitute for Steps 1--4.

An exact nonspherical example is
\[
C=\operatorname{diag}(1,1,2),\qquad
y=\left(\frac{2\sqrt2}{3},0,\frac13\right)^{\mathsf T},\qquad
U=\begin{pmatrix}
1/\sqrt6&1/\sqrt6&2/\sqrt6\\
-1/\sqrt2&1/\sqrt2&0\\
1/\sqrt3&1/\sqrt3&-1/\sqrt3
\end{pmatrix}.
\]
Then \(U^{\mathsf T}U=I\), \(U^{\mathsf T}y=(1,1,1)^{\mathsf T}/\sqrt3\), and all diagonal entries of \(U^{\mathsf T}CU\) are \(4/3\). The corresponding parallelepiped has edge vectors \((2/\sqrt3)A^{1/2}u_j\) and attains the unrestricted surface-area maximum, although \(y\) is not a principal-axis direction.

## Relationship to prior work

Kania [1] determined the unrestricted maximal facet area and its equality conditions. Proposition 5.2 reduced the prescribed-vertex problem to a barycentric constant-diagonal orthogonal basis, and Theorem 5.5 treated dimension three **only when the prescribed direction is an eigenvector**. Problem 6.1 expressly asks for the general pair classification. The theorem here supplies an exact all-direction criterion in dimension three; its axial non-polar latitude circles are not covered by the eigenvector theorem.

The general real simultaneous-hollowization theorem of Damm and Faßbender [2, Proposition 5] gives one hollow and one *almost* hollow real symmetric form after a shared orthogonal change. It does not require both forms to have zero diagonal and hence does not yield the criterion above. Nicholus [3, Theorem 5.4, Note 5.6] treats *conjugate* transformations using the orthogonal matrix in opposite orders, with the real second form again generally only almost hollow; the complete complex-unitary result does not imply simultaneous real-orthogonal diagonal equalization with a barycentric constraint. The stated result concerns the specifically linked pair \(C-sI/3\) and \(yy^{\mathsf T}-I/3\) and gives its exact real solvability condition.

## Limitations

The theorem resolves the three-dimensional case only. It neither classifies the corresponding restricted Schur--Horn problem in dimensions at least four nor maximizes surface area among only the parallelepipeds through a given point when the global maximum is unattainable. The condition is an equality, not an inequality; numerical roundoff near its zero set should not be treated as an exact existence certificate. The explicit phase construction uses a chosen tangent frame but the criterion and resulting geometry are coordinate-invariant. Published literature unindexed in the inspected sources could affect historical priority; no independent audit or third-party verification is claimed.

## References

[1] T. Kania, *Parallelepipeds of Maximal Facet Area and Total Edge Length in Ellipsoids, Through Prescribed Boundary Points*, Results in Mathematics **81**, article 186 (2026), DOI: 10.1007/s00025-026-02757-7. Earliest public preprint: arXiv:2510.16488, submitted 2025-10-18. See Theorem 4.2, Proposition 5.2, Theorem 5.5 and Problem 6.1. https://link.springer.com/article/10.1007/s00025-026-02757-7

[2] T. Damm and H. Faßbender, *Simultaneous hollowisation, joint numerical range, and stabilization by noise*, arXiv:1910.08813 (2019), especially Proposition 5 and Remark 6. https://ar5iv.labs.arxiv.org/html/1910.08813

[3] D. R. Nicholus, *Zeroing Diagonals, Conjugate Hollowization, and Characterizing Nondefinite Operators*, arXiv:2508.00096v2 (2026), Theorem 5.4 and Note 5.6. https://arxiv.org/html/2508.00096v2
