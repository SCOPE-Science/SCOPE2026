# Exact t-fine decomposition multiplicities for two-by-two finite-field matrices

## Finding
Let \(q\) be a prime power and let \(0\ne A\in M_2(\mathbb F_q)\). Define \(d_q(A)\) to be the number of ordered decompositions
\[
A=T+N
\]
with \(T\in\operatorname{GL}_2(\mathbb F_q)\) a torsion unit and \(N\) nilpotent. Let \(e(A)\) denote the number of eigenlines of \(A\) in \(\mathbb P^1(\mathbb F_q)\). Then
\[
d_q(A)=
\begin{cases}
q^2-q-1+e(A),&\det A\ne0,\\
q^2-1-(q-1)e(A),&\det A=0.
\end{cases}
\]
Consequently every nonzero matrix has at least \((q-1)^2\) such decompositions. If \(q>2\), equality occurs exactly for singular matrices of nonzero trace. If \(q=2\), equality also occurs for invertible matrices with no eigenline over \(\mathbb F_2\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\), including characteristic \(2\). A torsion unit means an invertible matrix of finite multiplicative order. Every element of \(\operatorname{GL}_2(\mathbb F_q)\) is automatically torsion because this group is finite. Every nilpotent \(2\times2\) matrix satisfies \(N^2=0\). The zero matrix is excluded because a sum of an invertible matrix and a nilpotent matrix cannot be zero.

The recent generalized t-fine literature studies existence of decompositions by torsion units and nilpotents. The present result instead determines the complete representation multiplicity for every nonzero element of \(M_2(\mathbb F_q)\).

## Proof
Write
\[
A=\begin{pmatrix}\alpha&\beta\\ \gamma&\delta\end{pmatrix}.
\]
Every nilpotent matrix has a unique form
\[
N(a,b,c)=\begin{pmatrix}a&b\\ c&-a\end{pmatrix},
\qquad a^2+bc=0.
\]
Conversely, this condition gives trace and determinant zero, hence nilpotence. The affine cone
\[
\mathcal N=\{(a,b,c)\in\mathbb F_q^3:a^2+bc=0\}
\]
has \(q^2\) points: its nonzero points split into \(q+1\) projective rays, each containing \(q-1\) nonzero vectors, together with the origin.

For such \(N\), direct expansion gives
\[
\det(A-N)=\det A+L_A(a,b,c),
\]
where
\[
L_A(a,b,c)=(\alpha-\delta)a+\gamma b+\beta c.
\]
The projective conic \(a^2+bc=0\) is parametrized by
\[
[u:v]\longmapsto[-uv:u^2:-v^2].
\]
On this parametrization,
\[
L_A(-uv,u^2,-v^2)
=\gamma u^2+(\delta-\alpha)uv-\beta v^2
=\det\!\begin{pmatrix}u&\alpha u+\beta v\\ v&\gamma u+\delta v\end{pmatrix}.
\]
Thus a projective nilpotent ray is annihilated by \(L_A\) exactly when the corresponding line \([u:v]\) is an eigenline of \(A\). Hence precisely \(e(A)\) of the \(q+1\) nilpotent rays have \(L_A=0\).

If \(\det A\ne0\), a nilpotent \(N\) is bad precisely when \(L_A(N)=-\det A\ne0\). On each projective ray with nonzero \(L_A\), exactly one nonzero scalar multiple has that prescribed value, while a ray with \(L_A=0\) contributes none. Therefore the number of bad nilpotents is \(q+1-e(A)\), and
\[
d_q(A)=q^2-(q+1-e(A))=q^2-q-1+e(A).
\]

If \(\det A=0\) and \(A\ne0\), bad nilpotents are exactly the points with \(L_A(N)=0\). They consist of the origin together with all \(q-1\) nonzero points on each of the \(e(A)\) annihilated projective rays. Hence there are \(1+(q-1)e(A)\) bad nilpotents, giving
\[
d_q(A)=q^2-1-(q-1)e(A).
\]

For nonzero singular \(A\), one has \(e(A)=1\) when \(A\) is nilpotent and \(e(A)=2\) when \(\operatorname{tr}A\ne0\). Thus the singular values of \(d_q(A)\) are respectively \(q(q-1)\) and \((q-1)^2\). For invertible non-scalar \(A\), one has \(e(A)\in\{0,1,2\}\), while a nonzero scalar matrix has \(e(A)=q+1\). Comparing the resulting values proves the sharp minimum statement.

## Verification
The included `verify.py` exhaustively checks every nonzero matrix for \(q=2,3,5,7\). For each field it enumerates all nilpotent matrices, counts directly those \(N\) for which \(A-N\) is invertible, independently counts projective eigenlines, and compares the direct count with the formula above. It also checks that there are exactly \(q^2\) nilpotent matrices, that the minimum is \((q-1)^2\), and that the total number of decompositions is
\[
|\operatorname{GL}_2(\mathbb F_q)|q^2,
\]
as required by counting ordered pairs \((T,N)\). The captured output ends with `CHECK_OK`.

## Relationship to prior work
Bien, Danchev, and Ramezan-Nassab introduced generalized t-fine rings and explicitly focus on decompositions by torsion units and nilpotents; their matrix-ring section studies inheritance of the existence property. Their Definition 2.1 identifies the relevant decomposition framework and their matrix-ring discussion invokes the known fact that t-fineness passes to full matrix rings.

Danchev, García, and Gómez Lozano previously proved an existence theorem for decomposing matrices as an invertible matrix plus a square-zero matrix, and in positive characteristic obtained torsion first summands under the relevant algebraicity hypotheses. For \(2\times2\) matrices over finite fields this yields existence for every nonzero matrix. The inspected paper proves existence and structural criteria but does not enumerate the number of decompositions. The formula above refines existence to a complete conjugacy-invariant multiplicity, controlled by the number of rational eigenlines.

## Limitations
The theorem is specific to \(2\times2\) matrices. In higher dimension, nilpotent matrices no longer form a projective conic and need not be square-zero, so the same ray count does not directly extend. The literature search found no equivalent multiplicity theorem, but older finite-field enumeration literature could encode the same convolution count in different language. The result does not address uniqueness of any distinguished decomposition or decompositions over infinite fields.

## References
1. M. H. Bien, P. V. Danchev, M. Ramezan-Nassab, *Generalized t-Fine and Quasi t-Fine Rings*, arXiv:2609.19882v1, first submitted 17 September 2026.
2. P. Danchev, E. García, M. Gómez Lozano, *Decompositions of Matrices into Invertible and Square-Zero Matrices*, arXiv:2301.06106v1, first submitted 15 January 2023.
3. MSC2020, classification 15B33, matrices over special rings including finite fields.
