# A finite linear solve for the central point of a constant-width polygon
## Finding
Let \(P\) be an arbitrary convex planar polygon. Use the paired-direction rewriting of Craizer--Martini so that its vertex list is \(P_1,\ldots,P_{2n}\), allowing a repeated vertex when one member of an opposite edge-direction pair is degenerate. Fix the normalization
\[
U_i=\frac{P_i-P_{i+n}}2,\qquad
M_i=\frac{P_i+P_{i+n}}2 .
\]
Then \(U_{i+n}=-U_i\), \(M_{i+n}=M_i\), and there are unique edge coefficients \(r_i\) such that
\[
M_{i+1}-M_i=r_i(U_{i+1}-U_i),\qquad
r_{i+n}=-r_i .
\]
For the first half of the coefficients put
\[
E_U=\left\{x\in\mathbb R^n:
\sum_{i=1}^n x_i(U_{i+1}-U_i)=0\right\}.
\]
This space has dimension \(n-2\).

Define \(F_U\) to be one full double-involute step of the central equidistant, with the second involute relabeled back to the original \(U\)-indexing. Let \(R_Ux\) be the unique double \(U\)-polygon with first vertex \(0\) and edge coefficients \(x\). Because \(F_U\) is linear and translation-equivariant, there are unique linear maps
\[
A_U:E_U\longrightarrow E_U,\qquad
B_U:E_U\longrightarrow\mathbb R^2
\]
such that
\[
F_U(R_Ux)=\mathbf 1\,B_Ux+R_U(A_Ux).
\]
Then \(I-A_U\) is invertible and the central point defined by iterated involutes is exactly
\[
O(P)=M_1+B_U(I-A_U)^{-1}r.
\]

Thus the central point can be obtained by a finite, non-iterative procedure. Choose any basis of \(E_U\), build the matrices of \(A_U\) and \(B_U\) by applying the explicit one-step formulas to the basis vectors, solve one \((n-2)\)-dimensional linear system, and substitute in the displayed formula.

## Assumptions and scope
Indices are cyclic modulo \(2n\). The determinant of two planar vectors is denoted by \([\,\cdot,\cdot\,]\). The paired-direction rewriting is exactly the device used in the source to cover arbitrary convex polygons, including polygons that do not initially have parallel opposite sides.

The normalization of \(U\) fixes the otherwise irrelevant homothety in the source construction. The case \(n=2\) has \(E_U=\{0\}\), so the central equidistant is already a point and the formula reads \(O(P)=M_1\).

For completeness, the one-step map \(F_U\) can be constructed using only finite sums. If
\[
X_{i+1}-X_i=x_i(U_{i+1}-U_i)
\]
is a double \(U\)-polygon, set
\[
a_i=[U_i,U_{i+1}],\qquad
V_i=\frac{U_{i+1}-U_i}{a_i},
\]
and
\[
b_i=\frac12\sum_{j=i}^{i+n-1}x_j a_j,\qquad
Y_i=X_i+b_iV_i.
\]
Then
\[
Y_{i+1}-Y_i=b_{i+1}(V_{i+1}-V_i).
\]
Put
\[
c_i=[V_i,V_{i+1}],\qquad
g_i=\frac12\sum_{j=i}^{i+n-1}b_{j+1}c_j,
\]
and
\[
W_i=\frac{V_{i+1}-V_i}{c_i}=-U_{i+1},\qquad
Z_i=Y_i+g_iW_i.
\]
The relabeled double involute is
\[
F_U(X)_{i+1}=Z_i.
\]
These are the source involute formulas applied twice; no limiting operation occurs in the construction of \(A_U\) or \(B_U\).

## Proof
The source formulas for the central equidistant and its edge coefficients give \(M_{i+n}=M_i\) and
\[
M_{i+1}-M_i=r_i(U_{i+1}-U_i).
\]
Closing the first half of \(M\) gives exactly the two scalar conditions defining \(E_U\). Since the edge directions of a nondegenerate convex \(U\) span the plane, \(\dim E_U=n-2\).

The source defines the dual vertices by
\[
V_i=\frac{U_{i+1}-U_i}{[U_i,U_{i+1}]}
\]
and the involute by the half-sums \(b_i\) and \(Y_i=X_i+b_iV_i\). Its difference identity gives
\[
Y_{i+1}-Y_i=b_{i+1}(V_{i+1}-V_i).
\]
Applying the same formula with \(V\) in place of \(U\) yields \(Z_i\). The duality identity in the source gives
\[
\frac{V_{i+1}-V_i}{[V_i,V_{i+1}]}=-U_{i+1},
\]
so the relabeling \(F_U(X)_{i+1}=Z_i\) is again a double \(U\)-polygon. Every displayed operation is linear in the vertices of \(X\), and translations pass unchanged through both involutes. Hence \(F_U\) is linear and translation-equivariant on the affine space of double \(U\)-polygons. This proves the existence and uniqueness of \(A_U\) and \(B_U\).

It remains to show that \(I-A_U\) is invertible. Take any \(x\in E_U\), let \(X=R_Ux\), and choose
\[
q>\max_{1\le i\le n}|x_i|.
\]
The polygon with vertices \(X_i+qU_i\) on the first half and the corresponding paired vertices on the second half has positive edge coefficients \(q+x_i\) and \(q-x_i\); hence it is a convex polygon of constant \(U\)-width whose central equidistant is \(X\). Craizer--Martini's convergence theorem therefore applies to \(X\): the iterates \(F_U^k(X)\) converge to a point.

Taking edge coefficients of those iterates shows
\[
A_U^k x\longrightarrow0
\]
for every \(x\in E_U\). In finite dimension this implies that every eigenvalue of \(A_U\) has modulus strictly below \(1\). Therefore \(I-A_U\) is invertible.

Now write the original central equidistant as
\[
M=\mathbf1\,M_1+R_Ur.
\]
Translation equivariance gives
\[
F_U(M)=\mathbf1\,(M_1+B_Ur)+R_U(A_Ur).
\]
Inductively,
\[
F_U^k(M)
=
\mathbf1\left(M_1+
B_U\sum_{j=0}^{k-1}A_U^jr\right)
+
R_U(A_U^kr).
\]
The last term tends to zero. Since the spectral radius of \(A_U\) is less than \(1\),
\[
\sum_{j=0}^{\infty}A_U^j=(I-A_U)^{-1}.
\]
The source theorem says the left-hand side converges to the constant polygon at \(O(P)\). Comparing the constant term proves
\[
O(P)=M_1+B_U(I-A_U)^{-1}r.
\]
Although the proof identifies the inverse with a convergent Neumann series, the stated method computes it by one finite linear solve and never performs the involute iteration.

## Verification
A standard-library exact-arithmetic checker is supplied as `verify.py`. It implements the two source involute formulas for a rational centrally symmetric octagon, constructs the induced \(A_U\) and \(B_U\) on its two-dimensional space \(E_U\), solves the direct center equation exactly, and verifies the fixed-center identity
\[
M_1+B_U(I-A_U)^{-1}r
=
M'_1+B_U(I-A_U)^{-1}r'
\]
after one double-involute step. The checker is an independent algebraic sanity check of the indexing and signs; the proof for arbitrary polygons is the argument above and does not rely on the example.

## Relationship to prior work
Craizer and Martini define the central point as the limit of iterated involutes and prove convergence. Immediately after their convergence theorem they ask whether there is a direct method to obtain that point from the polygon. Their paper supplies all local formulas used above but does not give a finite solve for the translation component of the limiting point.

Craizer, Teixeira, and Balestro later develop a linear-algebraic theory of discrete evolutes and cycloids. Their curvature-radius representation is explicitly only up to translation, and their double-evolute and pseudo-inverse operators therefore do not determine the absolute translation that is precisely the central point here. The present formula augments the shape operator \(A_U\) by the translation cocycle \(B_U\) and sums that cocycle in closed finite-dimensional form.

Arnold, Fuchs, Izmestiev, Tabachnikov, and Tsukerman study different polygonal evolute/involute discretizations based on perpendicular or angular bisectors and introduce Steiner or pseudo-Steiner points in those theories. Those constructions do not use the Craizer--Martini Minkowski constant-width involute and do not imply the formula above.

## Limitations
The theorem depends on Craizer--Martini's convergence theorem for their specific Minkowski involute construction. It does not identify their central point with a classical affine or Steiner center, and it does not give a universal closed expression with coefficients independent of \(U\). The matrices \(A_U\) and \(B_U\) depend on the edge geometry of the associated symmetric polygon \(U\).

The originality search found no prior statement of the finite solve or translation-cocycle formula. A residual indexing risk remains for later or obscure work that may have combined the 2014 convergence theorem with subsequent operator formulations without using the same terminology.

## References
1. M. Craizer and H. Martini, *Involutes of Polygons of Constant Width in Minkowski Planes*, arXiv:1406.3205, first posted 2014-06-12; later Ars Mathematica Contemporanea 11 (2016), 107--125. Relevant items: Lemmas 2.1--2.3, equations (3.1), (3.5), (3.14), (4.1), Theorem 5.1, and the question immediately following it.
2. M. Craizer, R. Teixeira, and V. Balestro, *Discrete Cycloids from Convex Symmetric Polygons*, arXiv:1702.00522. Relevant items: curvature-radius space, double polygons, double evolute transform, and the pseudo-inverse discussion.
3. M. Arnold, D. Fuchs, I. Izmestiev, S. Tabachnikov, and E. Tsukerman, *Iterating evolutes and involutes*, arXiv:1510.07742. Relevant items: the distinct perpendicular-bisector and angular-bisector polygonal theories and their Steiner-point constructions.
