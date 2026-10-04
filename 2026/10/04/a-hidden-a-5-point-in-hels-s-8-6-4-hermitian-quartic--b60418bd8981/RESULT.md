# A hidden \(A_5\) point in Helsø’s \((8,6,4)\) Hermitian quartic
## Finding
Let \(S\subset\mathbb P^3_{\mathbb C}\) be the quartic defined by the determinant of the Hermitian matrix
\[
M=\begin{{pmatrix}}
x_0+x_3&0&x_2&0\\
0&2x_0+x_3&i x_2&-i x_1\\
x_2&-i x_2&x_2+x_3&x_1\\
0&i x_1&x_1&x_3
\end{{pmatrix}}.
\]
This is the representation labelled \((\eta,\rho,\sigma)=(8,6,4)\) in Helsø, Section 4.9. Its singular locus consists of exactly eight rank-two points. Seven are ordinary nodes of type \(A_1\), while
\[
D=[0:1:0:0]
\]
is of type \(A_5\). Hence the singularity basket is \(A_5+7A_1\), rather than eight nodes.

Put \(t_\pm=(1\pm\sqrt{{17}})/8\). The remaining points are
\[
A=[1:0:0:0],\qquad B=[0:0:1:0],\qquad C=[3:0:2:0],
\]
and the four points on the affine chart \(x_3=1\) determined by
\[
x_2=t_\pm,\qquad x_0=-\frac{{1+t_\pm}}{{2}},\qquad x_1^2=-t_\pm.
\]
Exactly six of the eight points are real. Among those six, exactly \(A\), \(C\), and the two points over \(t_-\) are represented by semidefinite matrices, so exactly four lie on the spectrahedral boundary. Thus the stated numerical configuration \((8,6,4)\) is recovered even though one essential singularity is not a node.

There are also three explicit singular trisecant lines. The line \(V(x_1,x_3)\) contains \(A,B,C\). For either root \(t=t_\pm\) of \(4t^2-t-1=0\), the line
\[
V\bigl(x_2-tx_3,\;2x_0+(1+t)x_3\bigr)
\]
contains \(D\) and the two affine singularities over \(t\), and is contained in \(S\).

## Assumptions and scope
The ground field for the complex singularity classification is \(\mathbb C\). The real and semidefinite statements use the displayed Hermitian representation and the definite point \([0:0:0:1]\). No assertion is made about other Hermitian representations of the same quartic, about deformations of this example, or about other rows of the source's table.

The phrase “type \(A_5\)” means analytic equivalence of the completed local hypersurface germ to \(uv+w^6=0\). “Node” means type \(A_1\).

## Proof
Let \(F=\det M\). On the affine chart \(x_3=1\), a reduced Gröbner basis for the four first partial derivatives of \(F\), with lexicographic order \(x_0>x_1>x_2\), is
\[
2x_0+x_2+1,\qquad x_1^2+x_2,\qquad 4x_2^2-x_2-1.
\]
Consequently there are exactly four affine critical points, namely the four points above \(t_\pm\). On the plane \(x_3=0\), the gradient equations reduce in particular to
\[
-x_1^2(4x_0+3x_2)=0,\qquad -x_1^2(3x_0-2x_2)=0.
\]
If \(x_1\ne0\), these force \(x_0=x_2=0\), giving \(D\). If \(x_1=0\), the remaining equation is \(x_0x_2(2x_0-3x_2)=0\), giving \(A,B,C\). Euler's identity for the homogeneous quartic shows that every common zero of the gradient lies on \(S\). Direct substitution also gives rank \(2\) for \(M\) at all eight points.

For \(A,B,C\) and the four affine points, the determinant of the Hessian in a local affine chart is nonzero. Thus each is an ordinary quadratic singularity, hence type \(A_1\).

At \(D\), use the chart \(x_1=1\), and put \(p=x_0+x_3\), \(q=x_2\), \(w=x_3\). The local equation becomes exactly
\[
G=-2p^2-3pq+q^2+w\bigl(2p^2q+2p^2w-3pq^2-pqw-pw^2+q^2w\bigr).
\]
The quadratic form in \((p,q)\) is nondegenerate: its Hessian determinant is \(-17\). The analytic splitting lemma therefore reduces the germ to \(uv+h(w)\). Solving \(G_p=G_q=0\) formally gives
\[
p(w)=-\frac{{2}}{{17}}w^3+O(w^5),\qquad q(w)=-\frac{{3}}{{17}}w^3+O(w^5),
\]
and substitution yields
\[
h(w)=\frac{{1}}{{17}}w^6+O(w^8).
\]
Hence \(\operatorname{{ord}}_w h=6\), proving that \(D\) has type \(A_5\).

For the real rank-two points, the nonzero eigenvalues are read from the characteristic polynomials. At \(A\), \(B\), \(C\), and \(D\) they are encoded respectively by
\[
\lambda^2(\lambda-2)(\lambda-1),\quad
\lambda^2(\lambda-2)(\lambda+1),\quad
\lambda^2(\lambda-7)(\lambda-4),\quad
\lambda^2(\lambda^2-2).
\]
For either real affine point over \(t_-\), the remaining quadratic factor is
\[
\lambda^2-\frac{{39+\sqrt{{17}}}}{{16}}\lambda+\frac{{37+3\sqrt{{17}}}}{{32}},
\]
whose two roots are positive. Thus precisely \(A\), \(C\), and those two affine points are semidefinite; \(B\) and \(D\) are indefinite.

Finally,
\[
F\big|_{{x_1=x_3=0}}=0,
\]
while on \(x_0=-(1+t)x_3/2\), \(x_2=tx_3\), one has
\[
F=\frac{{x_3^2}}{{2}}\bigl(t x_3^2+x_1^2\bigr)(4t^2-t-1).
\]
This proves that the three stated lines lie on \(S\) and contain the indicated singular triples.

## Verification
The accompanying exact SymPy verifier reconstructs \(M\) and \(F\), recomputes the affine gradient Gröbner basis, checks the complete list of eight projective singular points and rank \(2\) at each, verifies nonzero local Hessian determinants at the seven nodes, derives the order-six split term at \(D\), checks the real characteristic polynomials, and verifies the three line restrictions. Running `python artifacts/verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Helsø introduces essential singularities as corank-at-least-two points and states that Section 4 lists definite Hermitian representations with specified configurations \((\eta,\rho,\sigma)\). The source displays the matrix above under \((8,6,4)\), but does not provide the eight coordinates or local analytic types. Earlier in the paper, Conjecture 1.3 is explicitly formulated for isolated essential nodes, and the examples in Section 4 are used as the listed known configurations for that program. The computation here shows that this particular displayed \((8,6,4)\) representation has the stated rank-two counts but contains an \(A_5\) point.

published-finding corpus searches for the exact source identifier, the \((8,6,4)\) tuple, the \(A_5+7A_1\) basket, rank-two/spectrahedral aliases, and singular trisecant formulations returned no record implying this local classification. The closest returned quartic records concern unrelated apolar or Hessian problems.

## Limitations
The calculation classifies only the displayed \((8,6,4)\) matrix. It does not show that the configuration \((8,6,4)\) cannot be realized by some other nodal Hermitian quartic, and it does not settle any missing case of the source's conjecture. The spectrahedral statement is representation-dependent; the singularity basket is intrinsic to this quartic.

## References
1. Martin Helsø, “Determinantal quartic surfaces with a definite Hermitian representation”, arXiv:2007.01121, first submitted 2 July 2020; see especially Sections 1, 3.1.1, and 4.9.
