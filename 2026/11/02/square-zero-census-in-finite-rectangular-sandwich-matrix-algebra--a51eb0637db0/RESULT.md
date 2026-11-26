# Square-zero census in finite rectangular sandwich matrix algebras

## Finding

Let \(m,n\geq1\), and let \(P\in M_{n\times m}(\mathbb F_q)\) have rank \(r\). Give \(M_{m\times n}(\mathbb F_q)\) the associative sandwich product \(X\star Y=XPY\). The number \(Z_{m,n,r}(q)\) of elements with \(X\star X=0\) depends only on \(m,n,r,q\).

Put \(s=n-r\), \(t=m-r\), write \({a\brack b}_q\) for a Gaussian coefficient and \(G_j(q)=|\mathrm{GL}_j(\mathbb F_q)|\), with \(G_0(q)=1\). For \(0\le u\le\min(a,b)\) put
\[
 R_{a,b,u}(q)=\frac{\prod_{i=0}^{u-1}(q^a-q^i)(q^b-q^i)}{\prod_{i=0}^{u-1}(q^u-q^i)},\qquad
 S_{r,j}(q)={r\brack j}_q{r-j\brack j}_q G_j(q).
\]
Empty products are one. The all-rank count is
\[
 \boxed{Z_{m,n,r}(q)=q^{st}\sum_{j=0}^{\lfloor r/2\rfloor} S_{r,j}(q)q^{js}
 \sum_{u=0}^{\min(s,r-2j)} R_{r-2j,s,u}(q) q^{t(r-j-u)}.}
\]
The cases \(r=0\) and \(m=n=r\) give the entire matrix space and the classical full-matrix square-zero count, respectively. The substantive comparison concerns the arbitrary-rank sandwich census beyond these cases and the already covered rank-one specialization described below.

## Assumptions and scope

The count is over any finite field \(\mathbb F_q\), with \(0\le r\le\min(m,n)\), and is a count of individual matrices for fixed \(P\). The rank-one geometric observation concerns the reduced locus over any field; it does not assert that the equation scheme is reduced.

## Proof

**Rank normal form.** View \(P:k^m\to k^n\) and \(X:k^n\to k^m\), with \(k=\mathbb F_q\). If \(P_0=UPV^{-1}\) for invertible \(U,V\) and \(X'=VXU^{-1}\), then \(X'P_0X'=VXPXU^{-1}\). Thus take \(P_0=\begin{psmallmatrix}I_r&0\\0&0\end{psmallmatrix}\). In the blocks of \(X'=\begin{psmallmatrix}A&B\\C&D\end{psmallmatrix}\) of sizes \(r\times r,r\times s,t\times r,t\times s\), respectively, the equations are precisely \(A^2=AB=CA=CB=0\). The \(D\) block contributes \(q^{ts}\).

**Middle block and projection.** If \(A^2=0\) and \(\operatorname{rank}A=j\), choose \(U_A=\operatorname{im}A\) inside \(K=\ker A\), then the isomorphism \(k^r/K\to U_A\). First choosing \(U_A\) and then \(K/U_A\) gives \({r\brack j}_q{r-j\brack r-2j}_q={r\brack j}_q{r-j\brack j}_q\) flags, and the isomorphisms contribute \(G_j(q)\). From \(AB=0\), \(B\) maps into \(K\). Its projection to \(K/U_A\) has some rank \(u\), with \(R_{r-2j,s,u}(q)\) choices by factoring a rank-\(u\) map through a labeled \(u\)-space and dividing by its change of basis group. Each projected map has \(q^{js}\) lifts. In every lift \(\dim(U_A+\operatorname{im} B)=j+u\).

**Final block.** The two remaining equations for \(C\) say that \(C\) vanishes on \(U_A+\operatorname{im} B\). There are \(q^{t(r-j-u)}\) such maps. The factors and strata give the formula, including when some blocks have dimension zero.

## Rank-one specialization (covered antecedent)

If \(r=1\), the scalar block \(A\) vanishes on the reduced locus. The remaining equation is the outer-product equation \(CB=0\), with \(D\) free. This is exactly the three-block parabolic square-zero equation with block sizes \((m-1,1,n-1)\): the two short blocks are \(C,B\) and the long block is \(D\) [2]. Its locus is the union \(B=0\) or \(C=0\) over any field. For \(m,n\ge2\) these have dimensions \((m-1)n\) and \(m(n-1)\), and intersection dimension \((m-1)(n-1)\). Inclusion–exclusion gives
\[
Z_{m,n,1}(q)=q^{(m-1)(n-1)}(q^{m-1}+q^{n-1}-1).
\]
If \(m=1\) or \(n=1\), one component is contained in the other and the same formula still holds. This rank-one count and reduced-locus description are consequences of the known three-block zero-product setup, not separate originality claims.

## Verification and limitations

The supplied `verify.py` directly evaluates \(XPX\) in 19 exhaustive small-matrix cases (16 in normal form and three noncanonical rank-one sandwiches) and checks four rank-one component counts. It uses the polynomial relation \(\alpha^2+\alpha+1=0\) over \(\mathbb F_4\). Reproduction: run `python3 verify.py` in its directory; the expected marker is `SANDWICH_SQUARE_ZERO_OK 19 exhaustive matrix cases; 4 component counts`. Examples are \(Z_{3,3,2}(2)=44\), \(Z_{3,3,3}(2)=22\), and \(Z_{2,2,1}(4)=28\). The general count follows from the proof, not these tests. There is no claim about higher nilpotency indices, orbit counts, or nonreduced scheme structure.

## Relationship to prior work

Dolinka–East [1] study the same rectangular sandwich product and count idempotents in Proposition 7.2. The idempotent equation \(XPX=X\) does not give the square-zero census. The full-rank ordinary matrix boundary is classical, and the rank-one reduced-locus result follows from [2]. In higher sandwich ranks, the simultaneous middle-block square-zero constraint and projected off-diagonal rank control the count. This comparison does not establish exhaustive historical priority.

## References

1. I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139, §7, Proposition 7.2. https://arxiv.org/abs/1503.03139
2. *Rank spectra of square-zero elements in three-block parabolic radicals*, Resultary `d1f94ed041a2`, Finding and three-block zero-product proof. https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-rank-spectra-of-square-zero-elements-in-three-block-parabolic-ra--d1f94ed041a2
