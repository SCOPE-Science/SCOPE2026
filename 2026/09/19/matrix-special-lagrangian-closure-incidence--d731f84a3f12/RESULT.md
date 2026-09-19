# Rank-stratified incidence of matrix special-Lagrangian cone closures

## Setting

Fix integers \(N\ge 2\) and \(d\ge 1\). Kotwal--Menon define the balanced variety
\[
\mathcal M_{\mathbf 0}
=
\left\{
(W_1,\ldots,W_N)\in M_d(\mathbb C)^N:
W_kW_k^*=W_{k+1}^*W_{k+1},\ 1\le k<N
\right\}.
\]
On its invertible locus, the unitary polar factor \(Q\in U_d\) of
\(W_N\cdots W_1\) labels an exact special Lagrangian leaf \(L_Q\). They study its
closure
\[
\mathcal C_Q=\overline{L_Q}
\]
and prove that \(\mathcal M_{\mathbf 0}=\bigcup_{Q\in U_d}\mathcal C_Q\). Their
Proposition 4.3 shows that every rank-deficient point of \(\mathcal C_Q\) lies in
at least one other closure.

The result below determines the entire incidence pattern of this cover.

## Theorem 1: exact label fiber at a rank-\(r\) point

Let \(\mathbf W=(W_1,\ldots,W_N)\in\mathcal M_{\mathbf 0}\), and set
\[
P=(W_1^*W_1)^{1/2},\qquad
E=\operatorname{im}P,\qquad
r=\operatorname{rank}P.
\]
Define the set of closure labels through \(\mathbf W\) by
\[
\Lambda(\mathbf W)=\{Q\in U_d:\mathbf W\in\mathcal C_Q\}.
\]
Choose any \(Q_0\in\Lambda(\mathbf W)\). Then
\[
\boxed{
\Lambda(\mathbf W)
=
Q_0\bigl(I_E\oplus U(E^\perp)\bigr)
\cong U(d-r).
}
\tag{1}
\]

Consequently, full-rank points lie in exactly one closure, a rank-\(r\) point
with \(r<d\) lies in a \(U(d-r)\)-family of closures, and the origin lies in all
closures.

### Proof

Kotwal--Menon's Proposition 4.1 gives, for every \(Q\in\Lambda(\mathbf W)\),
unitaries \(V_0,\ldots,V_N\), with \(V_0=I_d\) and \(V_N=Q\), such that
\[
W_k=V_kPV_{k-1}^*,\qquad 1\le k\le N.
\tag{2}
\]
Although the unitary factors are no longer unique when \(P\) is singular, the
positive factor is unique because \(W_1=V_1P\) implies
\[
P=(W_1^*W_1)^{1/2}.
\tag{3}
\]
Multiplying (2) telescopically gives
\[
W_N\cdots W_1=QP^N.
\tag{4}
\]
Hence if \(Q,Q_0\in\Lambda(\mathbf W)\),
\[
QP^N=Q_0P^N.
\]
Writing \(S=Q_0^*Q\), we have \(SP^N=P^N\). Since
\(\operatorname{im}P^N=E\) and \(P^N|_E\) is invertible, \(S\) fixes \(E\)
pointwise. Unitarity then forces
\[
S=I_E\oplus S_0,\qquad S_0\in U(E^\perp).
\]
Thus \(Q\) belongs to the right coset in (1).

Conversely, if \(S=I_E\oplus S_0\), then \(SP=P\). Replacing the terminal factor
\(V_N=Q_0\) in (2) by \(Q_0S\) leaves \(W_N\) unchanged:
\[
Q_0SPV_{N-1}^*=Q_0PV_{N-1}^*.
\]
Proposition 4.1 therefore gives
\(\mathbf W\in\mathcal C_{Q_0S}\). This proves (1). \(\square\)

## Theorem 2: pairwise and multiple intersections

For \(Q,R\in U_d\), define
\[
F(Q,R)=\ker(Q-R)
      =\operatorname{Fix}(R^*Q),
\qquad
f(Q,R)=\dim_{\mathbb C}F(Q,R).
\]
Then \(\mathcal C_Q\cap\mathcal C_R\) contains a point of common matrix rank
\(r\) if and only if
\[
\boxed{r\le f(Q,R).}
\tag{5}
\]
In particular,
\[
\boxed{
\max_{\mathbf W\in\mathcal C_Q\cap\mathcal C_R}
\operatorname{rank}W_1
=
\dim_{\mathbb C}\ker(Q-R),
}
\tag{6}
\]
and, for \(Q\ne R\),
\[
\boxed{
\mathcal C_Q\cap\mathcal C_R=\{\mathbf 0\}
\iff
1\notin\operatorname{spec}(R^*Q).
}
\tag{7}
\]
Thus an open dense set of pairs of distinct labels has closures meeting only at
the cone vertex.

More generally, for \(Q_1,\ldots,Q_m\in U_d\), put
\[
F=\bigcap_{j=2}^m\ker(Q_j-Q_1),\qquad f=\dim_{\mathbb C}F.
\]
Their common intersection contains a rank-\(r\) point if and only if \(r\le f\),
and its maximum rank is \(f\).

### Proof

If \(\mathbf W\in\mathcal C_Q\cap\mathcal C_R\), equation (4) applied to both
labels yields
\[
QP^N=RP^N.
\]
Therefore
\[
\operatorname{im}P
=
\operatorname{im}P^N
\subseteq\ker(Q-R),
\]
which proves necessity in (5).

Conversely, let \(E\subseteq F(Q,R)\) have dimension \(r\), and choose a
positive-semidefinite Hermitian \(P\) of rank \(r\) with
\(\operatorname{im}P=E\). Taking
\[
V_0=\cdots=V_{N-1}=I_d
\]
produces the tuple
\[
(P,\ldots,P,QP).
\]
Because \(QP=RP\), the same tuple has terminal factor \(R\), so Proposition 4.1
places it in both closures. This proves (5)--(7). The same argument with
\(E\subseteq\bigcap_{j\ge2}\ker(Q_j-Q_1)\) proves the multiple-intersection
statement. \(\square\)

## Theorem 3: dimensions of the rank strata

Let \(Q_1,\ldots,Q_m\in U_d\), and let
\[
F=\bigcap_{j=2}^m\ker(Q_j-Q_1),\qquad f=\dim_{\mathbb C}F.
\]
For \(1\le r\le f\), the common intersection
\[
\bigcap_{j=1}^m\mathcal C_{Q_j}
\]
has a smooth rank-\(r\) stratum of real dimension
\[
\boxed{
D_{N,d,f}(r)
=
(2rf-r^2)+(N-1)(2dr-r^2)
=
2r\bigl(f+(N-1)d\bigr)-Nr^2.
}
\tag{8}
\]
For one label (\(f=d\)) this becomes
\[
\boxed{
\dim_{\mathbb R}\{\mathbf W\in\mathcal C_Q:\operatorname{rank}W_1=r\}
=
N(2dr-r^2).
}
\tag{9}
\]

### Proof

The support \(E=\operatorname{im}P\) is an \(r\)-plane inside the fixed
\(f\)-plane \(F\). Choosing \(E\) contributes
\[
\dim_{\mathbb R}\operatorname{Gr}_{\mathbb C}(r,f)=2r(f-r),
\]
and choosing a positive-definite Hermitian form \(P|_E\) contributes \(r^2\).
Thus the allowed positive factors contribute \(2rf-r^2\) dimensions.

For fixed \(P\), each intermediate unitary \(V_k\), \(1\le k<N\), is determined
only modulo right multiplication by a unitary acting trivially on \(E\).
That stabilizer is \(U(d-r)\). Hence each intermediate factor contributes
\[
d^2-(d-r)^2=2dr-r^2
\]
dimensions. The stabilizer action is free and proper on the fixed-rank
factorization data, giving the smooth quotient and (8). \(\square\)

## Checks and interpretation

For \(d=1\), the only singular rank is \(0\), and (1) says that the common
vertex belongs to every \(U(1)\)-label, recovering the scalar Harvey--Lawson
picture.

For \(N=2\), Kotwal--Menon give the explicit linear description
\[
\mathcal C_Q=\{(A,QA^*):A\in M_d(\mathbb C)\}.
\]
Then
\[
\mathcal C_Q\cap\mathcal C_R
=
\{(A,QA^*):(Q-R)A^*=0\},
\]
so the maximum rank is visibly
\(\dim_{\mathbb C}\ker(Q-R)\). Its rank-\(r\) locus has real dimension
\(2r(d+f-r)\), exactly (8) with \(N=2\).

The new description upgrades the existence statement of Proposition 4.3 to a
complete rank-stratified incidence law. The failure of the invertible
special-Lagrangian foliation to remain disjoint on the balanced variety is
controlled precisely by the nullity of the common positive factor, and
pairwise overlap is read spectrally from the multiplicity of the eigenvalue
\(1\) of the relative unitary \(R^*Q\).

## Limitations

The result is set-theoretic and differential-topological on fixed-rank strata.
It does not prove that \(\mathcal C_Q\) extends across the singular locus as a
special Lagrangian integral current, does not compute intersection
multiplicities or angles, and does not describe local analytic normal forms where several rank strata meet. The motivating preprint is very recent,
so later revisions or unindexed parallel observations remain a residual
originality risk.

## References

1. T. Kotwal and G. Menon, *Special Lagrangian Cones in Deep Learning*,
   arXiv:2609.20159v1 (2026). In particular Proposition 4.1, Lemma 4.2, and
   Proposition 4.3.
2. T. Kotwal, *Symmetries and Gradient Flows in the Deep Linear Network*,
   Ph.D. dissertation, Brown University (2026), DOI: 10.26300/bd6x-0503.
