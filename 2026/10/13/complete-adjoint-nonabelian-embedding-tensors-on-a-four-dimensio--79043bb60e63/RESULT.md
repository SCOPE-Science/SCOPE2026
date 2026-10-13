# Complete adjoint nonabelian embedding tensors on a four-dimensional central \(3\)-Lie algebra

## Finding

Let \(K\) be a field and let \(H_K\) be the four-dimensional \(3\)-Lie algebra with basis
\[
\{e_1,e_2,e_3,e_4\}
\]
and alternating bracket determined by
\[
[e_1,e_2,e_3]=e_4.
\]
The adjoint action is coherent because every inner bracket lands in the central line \(Ke_4\).

For the coherent adjoint action, a nonabelian embedding tensor is a linear map \(T:H_K\to H_K\) satisfying
\[
[T(x),T(y),T(z)]
=
T\!\left([T(x),T(y),z]+[x,y,z]\right)
\]
for all \(x,y,z\in H_K\).

Put
\[
U=\langle e_1,e_2,e_3\rangle,
\qquad
H_K=U\oplus Ke_4,
\]
and write
\[
T=
\begin{pmatrix}
A&u\\
v&t
\end{pmatrix},
\]
where \(A\in M_3(K)\), \(u\in U\), \(v\in U^\ast\), and \(t\in K\).

Then \(T\) is a nonabelian embedding tensor if and only if
\[
\boxed{u=0}
\]
and exactly one of the following two alternatives holds.

First,
\[
\boxed{t=0,\qquad \det A=0,}
\]
with \(v\) arbitrary.

Second, there is a scalar
\[
\lambda\in K^\times,
\qquad
\lambda^2+1\ne0,
\]
such that
\[
\boxed{
A=\lambda I_3,
\qquad
t=\frac{\lambda^3}{\lambda^2+1},
}
\]
again with \(v\) arbitrary.

Thus the complete moduli consists of a large singular-matrix branch and a one-parameter invertible branch, each thickened by the free three-dimensional covector \(v\).

The arXiv-v1 version of Teng--Dai Example 2.8 prints the family
\[
T_k=\operatorname{diag}(1,1,2k,k)
\]
for arbitrary \(k\). Direct substitution gives the defect
\[
k(1-2k)e_4
\]
on the ordered triple \((e_2,e_3,e_1)\). Hence, in characteristic zero,
\[
\boxed{T_k\text{ is a nonabelian embedding tensor exactly for }k=0\text{ or }k=\tfrac12.}
\]
The later published version no longer prints the arbitrary-\(k\) family and retains only
\[
\operatorname{diag}(1,1,0,0),
\]
which is the \(k=0\) case.

For a finite field \(\mathbf F_q\), define
\[
r_q=\#\{\lambda\in\mathbf F_q^\times:\lambda^2=-1\},
\qquad
m_q=q-1-r_q.
\]
Explicitly,
\[
r_q=
\begin{cases}
1,&q\text{ even},\\
2,&q\equiv1\pmod4,\\
0,&q\equiv3\pmod4.
\end{cases}
\]
Then
\[
\boxed{
|\operatorname{NET}_{\mathrm{ad}}(H_{\mathbf F_q})|
=
q^3\!\left(
q^9-(q^3-1)(q^3-q)(q^3-q^2)+m_q
\right).
}
\]

Let
\[
N_1=(q-1)(q^2+q+1)^2
\]
be the number of rank-one \(3\times3\) matrices and
\[
N_2=q(q+1)(q^3-1)^2
\]
the number of rank-two \(3\times3\) matrices. The exact rank distribution of embedding tensors, in ranks \(0,1,2,3,4\), is
\[
\boxed{
\left(
1,
q^3-1+qN_1,
(q^3-q)N_1+q^2N_2,
(q^3-q^2)N_2,
q^3m_q
\right).
}
\]

For example, over \(\mathbf F_2\) the total is
\[
2752
\]
with rank profile
\[
(1,105,1470,1176,0),
\]
while over \(\mathbf F_3\) the total is
\[
228231
\]
with rank profile
\[
(1,1040,81120,146016,54).
\]

## Assumptions and scope

The source definition is Teng--Dai Definition 2.6 specialized to the coherent adjoint action of their Example 2.8.

The source assumes characteristic zero. The classification above is proved from the alternating bracket and the polynomial embedding-tensor identity and is valid over an arbitrary field. In characteristic two, alternating means the bracket is defined by the alternating trilinear extension of \([e_1,e_2,e_3]=e_4\).

The theorem concerns this fixed four-dimensional \(3\)-Lie algebra and the coherent adjoint action. It does not classify nonabelian embedding tensors for arbitrary coherent actions.

The publication-stage change to Example 2.8 is treated as prior correction of the specific generic arXiv-v1 family; originality is claimed only for the complete classification and finite-field census.

## Proof

Let \(\omega:U^3\to K\) be the alternating volume form with
\[
\omega(e_1,e_2,e_3)=1.
\]
Then
\[
[x,y,z]=\omega(\pi x,\pi y,\pi z)e_4,
\]
where \(\pi:H_K\to U\) is projection.

Write an element of \(H_K\) as \((x,s)\) with \(x\in U\) and \(s\in K\). Then
\[
T(x,s)=(Ax+su,\ v(x)+ts).
\]
The \(U\)-component of the nonabelian embedding-tensor identity is
\[
\left(
\omega(Ax+su,Ay+ru,z)+\omega(x,y,z)
\right)u=0
\]
for all \(x,y,z\in U\) and \(r,s\in K\).

Suppose \(u\ne0\). Varying \(s\) shows
\[
\omega(u,Ay,z)=0
\]
for every \(y,z\), so \(Ay\in Ku\) for every \(y\). Thus \(\operatorname{im}A\subseteq Ku\), and therefore
\[
\omega(Ax,Ay,z)=0
\]
for every \(x,y,z\). Setting \(r=s=0\) in the same \(U\)-component would then force
\[
\omega(x,y,z)=0
\]
for all triples, a contradiction. Hence
\[
u=0.
\]

With \(u=0\), the free covector \(v\) disappears from the bracket equations. The identity becomes
\[
\det(A)\,\omega(x,y,z)
=
t\left(\omega(Ax,Ay,z)+\omega(x,y,z)\right).
\]
The standard adjugate identity gives
\[
\omega(Ax,Ay,z)=\omega(x,y,\operatorname{adj}(A)z),
\]
so nondegeneracy of \(\omega\) yields the matrix equation
\[
\boxed{
t\left(\operatorname{adj}(A)+I_3\right)=\det(A)I_3.
}
\]

If \(t=0\), this is equivalent to
\[
\det A=0.
\]

Now suppose \(t\ne0\). Then
\[
\operatorname{adj}(A)=cI_3,
\qquad
c=\frac{\det A-t}{t}.
\]
The scalar \(c\) cannot be zero: if \(\operatorname{adj}(A)=0\), then \(\operatorname{rank}A\le1\), hence \(\det A=0\), while the displayed formula gives \(c=-1\). Thus \(\operatorname{adj}(A)\) is invertible, so \(A\) is invertible. Since
\[
\operatorname{adj}(A)=\det(A)A^{-1}
\]
is scalar, \(A\) itself is scalar:
\[
A=\lambda I_3
\]
with \(\lambda\ne0\). Substitution gives
\[
t(\lambda^2+1)=\lambda^3.
\]
Therefore \(\lambda^2+1\ne0\) and
\[
t=\frac{\lambda^3}{\lambda^2+1}.
\]
Conversely, both branches satisfy the matrix equation, proving the classification.

For the arXiv-v1 family
\[
A=\operatorname{diag}(1,1,2k),
\qquad t=k,
\]
the ordered triple \((e_2,e_3,e_1)\) gives the defect
\[
2k-k(2k+1)=k(1-2k),
\]
which proves the stated characteristic-zero restriction.

For finite-field counting, the first branch contains
\[
q^3S_q
\]
operators, where
\[
S_q=q^9-(q^3-1)(q^3-q)(q^3-q^2)
\]
is the number of singular \(3\times3\) matrices. The second branch contains
\[
q^3m_q
\]
operators. They are disjoint because the second branch has \(t\ne0\).

For the rank distribution in the first branch, if \(A\) has rank \(r\), the full matrix
\[
\begin{pmatrix}A&0\\v&0\end{pmatrix}
\]
has rank \(r\) exactly when \(v\) lies in the \(r\)-dimensional row space of \(A\), and otherwise has rank \(r+1\). There are \(q^r\) covectors in that row space. Combining this with the exact rank-one and rank-two \(3\times3\) matrix counts \(N_1,N_2\) gives the displayed profile. Every operator in the second branch is invertible, contributing \(q^3m_q\) to rank four.

## Verification

The included program `artifacts/verify.py` evaluates the defining ternary identity directly, without assuming the classification.

It exhaustively checks all \(2^{16}\) endomorphisms over \(\mathbf F_2\) and verifies that the direct identity agrees exactly with the two-branch criterion. It obtains
\[
2752
\]
operators with rank profile
\[
(1,105,1470,1176,0).
\]

It independently enumerates the classified \(\mathbf F_3\) locus and obtains
\[
228231
\]
operators with rank profile
\[
(1,1040,81120,146016,54).
\]

The checker also evaluates the arXiv-v1 diagonal family over \(\mathbf Q\): \(k=0\) and \(k=\tfrac12\) pass, while \(k=1\) fails on \((e_2,e_3,e_1)\).

It returns `VERIFY_OK`.

The finite enumerations are replay checks. The arbitrary-field theorem is the adjugate argument proved above.

## Relationship to prior work

Teng and Dai introduce nonabelian embedding tensors on \(3\)-Lie algebras and give this exact four-dimensional central algebra as Example 2.8. The arXiv-v1 full text states the diagonal family
\[
\operatorname{diag}(1,1,2k,k)
\]
for arbitrary \(k\). The published 2025 full text changes the displayed example to
\[
\operatorname{diag}(1,1,0,0),
\]
so the publication already removes the invalid generic parameter family.

Neither inspected version gives the complete adjoint classification. In particular, the singular-matrix branch contains every singular \(A\), with an arbitrary bottom covector, while the nonzero-\(t\) branch is a separate scalar family controlled by
\[
t(\lambda^2+1)=\lambda^3.
\]

The earlier embedding-tensor paper of Hu, Hou, Song, and Zhou studies the abelian-source embedding-tensor notion on \(3\)-Lie algebras, not the nonabelian identity containing the additional intrinsic bracket term. It therefore does not imply this classification.

Targeted semantic-database and web searches for Example 2.8, the diagonal family, adjoint nonabelian embedding tensors, four-dimensional central \(3\)-Lie algebras, and the exact finite-field formulas did not locate a complete classification.

## Limitations

The result is specific to the central four-dimensional \(3\)-Lie algebra of Teng--Dai Example 2.8 and its coherent adjoint action.

The generic error in arXiv v1 is not claimed as an uncorrected publication defect: the 2025 published version already replaces it by the valid \(k=0\) example.

No automorphism-conjugacy quotient is computed.

A specialized classification under different terminology may exist. Failed searches do not prove absolute novelty.

## References

1. W. Teng and X. Dai, “Nonabelian embedding tensors on \(3\)-Lie algebras and \(3\)-Leibniz-Lie algebras,” arXiv:2310.06990v1, first public 16 August 2023; *Electronic Research Archive* 33 (2025), 1367–1383, DOI `10.3934/era.2025063`.
2. M. Hu, S. Hou, L. Song, and Y. Zhou, “Deformations and cohomologies of embedding tensors on \(3\)-Lie algebras,” *Communications in Algebra* 51 (2023), 4622–4639, DOI `10.1080/00927872.2023.2214215`.
