# Square-zero census in finite rectangular sandwich matrix algebras

## Finding
Let \(m,n\geq 1\) and let \(P\in M_{n\times m}(\mathbb F_q)\) have rank \(r\). Give \(M_{m\times n}(\mathbb F_q)\) the associative sandwich multiplication \(X\star Y=XPY\). The number \(Z_{m,n,r}(q)\) of elements with \(X\star X=0\) depends only on \(m,n,r,q\) and is the explicit finite sum below.

Put \(s=n-r\), \(t=m-r\). Define the number of rank-\(u\) matrices of size \(a\times b\) over \(\mathbb F_q\) by
\[
R_{a,b,u}(q)=\frac{\prod_{i=0}^{u-1}(q^a-q^i)(q^b-q^i)}{\prod_{i=0}^{u-1}(q^u-q^i)}
\]
for \(0\le u\le\min(a,b)\), with \(R_{a,b,0}(q)=1\) and empty products equal to one. Let \({a\brack b}_q\) be the Gaussian coefficient, and let \(G_j(q)=\prod_{i=0}^{j-1}(q^j-q^i)\), with \(G_0(q)=1\). Set
\[
S_{r,j}(q)={r\brack j}_q{r-j\brack j}_qG_j(q).
\]
Then the complete count is
\[
\boxed{Z_{m,n,r}(q)=q^{st}\sum_{j=0}^{\lfloor r/2\rfloor}S_{r,j}(q)q^{js}
\sum_{u=0}^{\min(s,r-2j)}R_{r-2j,s,u}(q)q^{t(r-j-u)}.}
\]
The formula includes \(r=0\), giving \(Z_{m,n,0}(q)=q^{mn}\), and full-rank square-matrix multiplication, where it reduces to the classical square-zero matrix count.

For \(r=1\) the sum simplifies to
\[
\boxed{Z_{m,n,1}(q)=q^{(m-1)(n-1)}\bigl(q^{m-1}+q^{n-1}-1\bigr).}
\]
When \(m,n\ge2\), the reduced square-zero algebraic set for rank-one \(P\), over any field, is the union of two distinct affine linear subspaces of dimensions \((m-1)n\) and \(m(n-1)\), meeting in an affine subspace of dimension \((m-1)(n-1)\). The formula above counts their rational points by inclusion-exclusion.

## Assumptions and scope
All matrices have entries in an arbitrary finite field \(\mathbb F_q\), where \(q\) is any prime power, and \(m,n\) are positive. The parameter \(r\) ranges over \(0\le r\le\min(m,n)\). No restriction on characteristic, invertibility, or rectangularity is made. The rank-one reduced-locus statement is geometric and is valid over any field; it does not assert that the unreduced equation scheme is reduced.

## Proof
**1. Rank normal form.** Independent changes of bases in the row and column spaces convert every \(n\times m\) matrix \(P\) of rank \(r\) to the block inclusion matrix \(P_0=\begin{psmallmatrix}I_r&0\\0&0\end{psmallmatrix}\). These changes induce an invertible linear change of coordinates on \(M_{m\times n}\) carrying \(XPX=0\) to \(X'P_0X'=0\). Thus only the rank \(r\) matters.

**2. Four block equations.** Relative to the decomposition \(m=r+t\), \(n=r+s\), write
\[
X=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad
A\in M_r,\ B\in M_{r\times s},\ C\in M_{t\times r},\ D\in M_{t\times s}.
\]
Direct multiplication gives
\[
XP_0X=\begin{pmatrix}A^2&AB\\CA&CB\end{pmatrix}.
\]
Therefore \(X\star X=0\) if and only if \(A^2=AB=CA=CB=0\). The \(D\)-block is unrestricted, contributing \(q^{ts}\) choices.

**3. Square-zero middle block.** If \(A^2=0\) and \(\operatorname{rank}A=j\), then \(U=\operatorname{im}A\subseteq K=\ker A\), with \(\dim U=j\) and \(\dim K=r-j\). Choose \(U\), then \(K\supseteq U\), then the induced isomorphism \(\mathbb F_q^r/K\to U\). These choices are \({r\brack j}_q\), \({r-j\brack j}_q\), and \(G_j(q)\), respectively. Hence there are exactly \(S_{r,j}(q)\) eligible \(A\)-blocks of rank \(j\), and necessarily \(0\le j\le\lfloor r/2\rfloor\).

**4. Stratify the \(B\)-block.** The equation \(AB=0\) means that \(B:\mathbb F_q^s\to K\). Project to \(K/U\), whose dimension is \(r-2j\), and let the projection have rank \(u\). There are exactly \(R_{r-2j,s,u}(q)\) projected maps of rank \(u\). Each admits \(q^{js}\) lifts \(B\), because the kernel of \(K\to K/U\) is \(U\). For every such lift, \(\dim(U+\operatorname{im}B)=j+u\).

**5. Count \(C\).** The equations \(CA=CB=0\) say precisely that \(C:\mathbb F_q^r\to\mathbb F_q^t\) vanishes on \(U+\operatorname{im}B\). Since the quotient has dimension \(r-j-u\), there are exactly \(q^{t(r-j-u)}\) such \(C\)-blocks. Multiplying the independent factors and summing the disjoint \((j,u)\)-strata yields the stated formula. No division by the field characteristic or limiting argument occurs.

**6. Rank-one geometry.** If \(r=1\), the equation \(A^2=0\) forces the single entry of \(A\) to be zero at every point over any field. The remaining conditions are \(CB=0\), where \(C\) is a column and \(B\) is a row. Over a field, this outer product vanishes if and only if \(C=0\) or \(B=0\). The variable \(D\) is free. Taking the reduced loci gives the two claimed affine linear subspaces and their intersection. Their dimensions and inclusion-exclusion count follow directly; for \(m=1\) or \(n=1\), one of the two sets is contained in the other.

## Verification
The companion `verify.py` directly evaluates every entry of \(XPX\) for all \(X\) in sixteen canonical finite-field instances and three noncanonical rank-one sandwich matrices. It evaluates \(\mathbb F_4\) through the explicit polynomial relation \(\alpha^2+\alpha+1=0\), not arithmetic modulo four. Every independently enumerated count equals the formula. Four further identities check the rank-one two-component point count. Run `python3 verify.py`; the expected terminal marker is `SANDWICH_SQUARE_ZERO_OK 19 exhaustive matrix cases; 4 component counts`. These finite checks corroborate, but do not establish, the theorem over arbitrary dimensions and fields; the proof above provides that justification.

Examples include \(Z_{3,3,2}(2)=44\), \(Z_{3,3,3}(2)=22\), and \(Z_{2,2,1}(4)=28\).

## Relationship to prior work
Dolinka and East study the exact same rectangular matrix sandwich multiplication and, in Proposition 7.2 of their 2015-origin preprint, enumerate **idempotents**, namely solutions of \(XPX=X\). Their article gives structural and generation results but does not state the present enumeration of solutions of \(XPX=0\). The full-rank square-matrix specialization is the classical square-zero matrix census; it is included as a boundary check and is not asserted to be new. The work here concerns all intermediate sandwich ranks, the simultaneous \(A,B,C\) constraints, and the rank-one reduced-locus decomposition. Related published investigations of nilpotent matrices, matrix factorizations and matrix-rank strata do not, from the inspected material, establish an equivalent all-rank rectangular sandwich formula. Absence from searched sources is not an exhaustive priority certificate.

## Limitations
The count concerns square-zero elements in the sandwich product, not arbitrary nilpotency indices, ordinary matrix square-zero elements for nonidentity \(P\), or conjugacy/orbit classes. The rank-one geometric statement concerns reduced point loci, not possible nilpotent scheme structure in their defining equations. Overlap analysis covers the accessible materials listed below and does not certify global publication priority. Independent mathematical review has not been conducted.

## References
1. Igor Dolinka and James East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139 (first publicly submitted 2015-03-11; version 2, 2016-08-15), especially introduction and Proposition 7.2. https://arxiv.org/abs/1503.03139.
2. J. V. Brawley, *Counting matrices by Drazin index*, SIAM Journal on Algebraic and Discrete Methods 3 (1982), on classical finite-field matrix nilpotence and its full-matrix specialization.
