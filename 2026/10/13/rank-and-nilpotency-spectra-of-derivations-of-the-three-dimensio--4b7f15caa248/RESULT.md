# Rank and nilpotency spectra of derivations of the three-dimensional Heisenberg Lie algebra

## Finding

Let \(H_3(\mathbb F_q)\) be the three-dimensional Heisenberg Lie algebra with basis \(x,y,z\) and bracket \([x,y]=z\), over an arbitrary finite field of order \(q\). If \(R_r(q)\) denotes the number of derivations of rank \(r\), then
\[
\sum_{r=0}^3 R_r(q)s^r
=1+(q-1)(q+1)^2s+q(q-1)(2q^3+2q^2-1)s^2+q^3(q-1)(q^2-q-1)s^3.
\]
Equivalently,
\[
R_0(q)=1,
\]
\[
R_1(q)=(q-1)(q+1)^2,
\]
\[
R_2(q)=q(q-1)(2q^3+2q^2-1),
\]
and
\[
R_3(q)=q^3(q-1)(q^2-q-1).
\]
Thus the exact number of invertible derivations is \(q^3(q-1)(q^2-q-1)\).

Exactly \(q^4\) derivations are nilpotent. With the convention that the zero derivation has nilpotency index \(1\), their nilpotency-index enumerator is
\[
t+(q-1)(q+1)^2t^2+q(q-1)^2(q+1)t^3.
\]
Consequently every rank-one derivation is square-zero, and every nilpotent derivation of index three has rank two.

## Assumptions and scope

The field is an arbitrary finite field \(\mathbb F_q\); no restriction on the characteristic is imposed. The Lie algebra is the ordinary three-dimensional Heisenberg algebra
\[
H_3(\mathbb F_q)=\mathbb F_qx\oplus\mathbb F_qy\oplus\mathbb F_qz,
\qquad [x,y]=z,
\]
with all other brackets between basis vectors zero.

Rank means ordinary rank as an \(\mathbb F_q\)-linear endomorphism of the three-dimensional vector space. A nilpotency index is the least positive integer \(k\) for which \(D^k=0\); under this convention the zero map has index \(1\).

## Proof

Write
\[
D(x)=ax+by+uz,
\qquad
D(y)=cx+dy+vz.
\]
The derivation identity on \([x,y]=z\) gives
\[
D(z)=[D(x),y]+[x,D(y)]=(a+d)z.
\]
Conversely, every choice of \(a,b,c,d,u,v\in\mathbb F_q\) with this formula for \(D(z)\) satisfies the derivation identity. Therefore every derivation has, and uniquely has, the matrix
\[
D=
\begin{pmatrix}
 a&c&0\\
 b&d&0\\
 u&v&a+d
\end{pmatrix}.
\tag{1}
\]
Put
\[
A=\begin{pmatrix}a&c\\b&d\end{pmatrix},
\qquad
w=(u,v),
\qquad
\tau=\operatorname{tr}A.
\]
If \(\tau\ne0\), the last column of (1) supplies a pivot independent of the first two columns, so
\[
\operatorname{rank}D=\operatorname{rank}A+1.
\tag{2}
\]
If \(\tau=0\), the last column is zero and
\[
\operatorname{rank}D
=\operatorname{rank}\begin{pmatrix}A\\w\end{pmatrix}.
\tag{3}
\]
Thus, if \(r=\operatorname{rank}A\), equation (3) has rank \(r\) for exactly \(q^r\) choices of \(w\), namely the row space of \(A\), and rank \(r+1\) for the remaining \(q^2-q^r\) choices.

It remains to count two-by-two matrices by rank and trace. The trace-zero rank-zero count is \(1\). A rank-one matrix can be written as \(uv^{\mathsf T}\) with nonzero \(u,v\in\mathbb F_q^2\), with exactly \(q-1\) such presentations. Its trace is \(v^{\mathsf T}u\). For each nonzero \(u\), exactly \(q-1\) nonzero vectors \(v\) satisfy \(v^{\mathsf T}u=0\). Hence
\[
\#\{A:\operatorname{rank}A=1,\ \operatorname{tr}A=0\}=q^2-1,
\tag{4}
\]
while the rank-one nonzero-trace count is
\[
q(q^2-1).
\tag{5}
\]
The trace-zero subspace of \(M_2(\mathbb F_q)\) has \(q^3\) elements. Its singular elements consist of the zero matrix and the \(q^2-1\) matrices from (4), so
\[
\#\{A:\operatorname{rank}A=2,\ \operatorname{tr}A=0\}=q^2(q-1).
\tag{6}
\]
Subtracting (6) from \(|\operatorname{GL}_2(q)|=q(q-1)^2(q+1)\) gives
\[
\#\{A:\operatorname{rank}A=2,\ \operatorname{tr}A\ne0\}
=q(q-1)(q^2-q-1).
\tag{7}
\]

Equations (2)--(7), together with the \(q^2\) choices of \(w\), now give the four rank strata. Rank zero has only the zero derivation. Rank one receives \(q^2-1\) choices from \(A=0\), \(w\ne0\), and \(q(q^2-1)\) choices from trace-zero rank-one \(A\) with \(w\) in its row space, giving
\[
R_1(q)=(q^2-1)(q+1)=(q-1)(q+1)^2.
\]
Rank three occurs only in (7), with arbitrary \(w\), giving
\[
R_3(q)=q^2\,q(q-1)(q^2-q-1)
=q^3(q-1)(q^2-q-1).
\]
The rank-two terms are
\[
(q^2-1)(q^2-q)+q^4(q-1)+q^3(q^2-1),
\]
which simplify to
\[
R_2(q)=q(q-1)(2q^3+2q^2-1).
\]
The four counts sum to \(q^6\), the size of the six-dimensional derivation space.

For nilpotency, the characteristic polynomial of (1) factors as
\[
\chi_D(T)=\chi_A(T)(T-\tau).
\]
Hence \(D\) is nilpotent exactly when \(A\) is nilpotent. A two-by-two matrix is nilpotent exactly when its trace and determinant vanish; there are \(q^2\) such matrices: the zero matrix and the \(q^2-1\) nonzero rank-one matrices in (4). Since \(w\) is arbitrary, the nilpotent derivation count is \(q^4\).

For nilpotent \(A\), one has \(A^2=0\) and
\[
D^2=
\begin{pmatrix}
0&0\\
wA&0
\end{pmatrix},
\qquad
D^3=0,
\]
where the displayed block form uses the decomposition \(\mathbb F_q^2\oplus\mathbb F_qz\). If \(A=0\), the nonzero choices of \(w\) give \(q^2-1\) index-two derivations. If \(A\ne0\), then \(A\) has rank one, so its left kernel has size \(q\); exactly those \(q\) choices of \(w\) satisfy \(wA=0\). Thus the nonzero index-two count is
\[
(q^2-1)+q(q^2-1)=(q-1)(q+1)^2.
\]
The remaining nilpotent derivations have index three, in number
\[
q^4-1-(q-1)(q+1)^2=q(q-1)^2(q+1).
\]
This proves the stated nilpotency-index enumerator. The rank-one count equals the nonzero index-two count, and the rank analysis above shows these are the same derivations, giving the final structural statements.

## Verification

The standalone verifier `verify.py` directly enumerates the six parameters in (1) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), computes matrix ranks and nilpotency indices, and checks the formulas coefficient by coefficient. It also enumerates every one of the \(q^9\) linear maps on \(H_3(\mathbb F_q)\) for \(q=2,3\), tests the derivation identity on basis pairs, and verifies that exactly \(q^6\) maps survive with the predicted rank histogram.

To test a non-prime field, the verifier implements \(\mathbb F_4\) as \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) and exhaustively checks all \(4^6\) derivations. The resulting rank histogram is
\[
(1,75,1908,2112),
\]
and the nilpotency-index histogram is
\[
(1,75,180),
\]
matching the formulas exactly. These finite computations corroborate the field-uniform proof; they are not used to replace it.

## Relationship to prior work

Yang and Hu determine the color derivation algebra of finite-dimensional Heisenberg Lie color algebras; their publisher metadata lists the Lie-algebra structure and derivation classifications beginning with MSC 17B05 and records online publication on 21 June 2011. This supplies an archive-era structural predecessor for Heisenberg derivation algebras, but the accessible publisher material does not give a finite-field rank or nilpotency census.

A later full-text paper of Alemi and Saeedi gives, over an arbitrary field, the ordinary three-dimensional Heisenberg derivation matrix used in (1) as an explicit example and records \(\dim\operatorname{Der}(H_3)=6\). That structural statement is compatible with the present proof but does not enumerate ranks, invertible derivations, or nilpotency indices over finite fields.

Calderón, Draper, Martín, and Sánchez study gradings and symmetries of Heisenberg-type algebras, providing a further same-object structural comparison. The searched finite-Heisenberg and derivation literature located structural, automorphism, grading, local-derivation, and commutativity results, but no statement implying the two enumerators above.

## Limitations

The theorem is only for the three-dimensional Heisenberg Lie algebra. Higher Heisenberg ranks replace the unrestricted two-by-two block by a conformal-symplectic condition, so the present counting argument does not directly yield a higher-rank rank distribution.

The full text of the 2011 Yang--Hu archive source was not accessible from the publisher in the inspected material; its abstract, classifications, date, and derivation-algebra scope were available. This is retained as a residual originality risk. The later arbitrary-field paper giving the exact ordinary \(H_3\) derivation matrix was available in full text and was inspected as the strongest direct structural comparison.

## References

H. Yang and N. Hu, “Heisenberg Lie Color Algebras,” *Communications in Algebra* 39 (2011), 1782–1795. DOI: 10.1080/00927872.2010.480950. Published online 21 June 2011.

M. R. Alemi and F. Saeedi, “Derivation algebra of direct sum of lie algebras,” *Cogent Mathematics & Statistics* 6 (2019), 1624244. DOI: 10.1080/25742558.2019.1624244.

A. Calderón, C. Draper, C. Martín, and J. M. Sánchez, “Gradings and symmetries on Heisenberg type algebras,” *Linear Algebra and its Applications* 458 (2014), 463–502. arXiv:1405.4093; DOI: 10.1016/j.laa.2014.06.024.
