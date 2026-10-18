# Product-rank distribution of idempotents in nontrivially twisted centralizer codes

## Finding
Let \(q>2\) be a prime power, let \(n\ge1\), let \(A\in M_n(\mathbb F_q)\), and let \(\lambda\in\mathbb F_q\setminus\{0,1\}\). The twisted centralizer code is
\[
\mathcal C(A,\lambda)=\{X\in M_n(\mathbb F_q):AX=\lambda XA\}.
\]
Let \(\rho\) denote ordinary matrix rank. Define the **complete trivariate product-rank polynomial** of all ordered pairs of idempotents in this code, without imposing commutativity:
\[
\mathcal F_{A,\lambda}(x,y,z)=
\sum_{\substack{X,Y\in\mathcal C(A,\lambda)\\X^2=X,\ Y^2=Y}}
x^{\rho(X)}y^{\rho(Y)}z^{\rho(XY)}.
\]
Set
\[
 s=\rho(A)-\rho(A^2)=\dim(\ker A\cap\operatorname{im}A),
 \qquad t=n-\rho(A)-s.
\]
Then \(s,t\ge0\), and the exact polynomial is
\[
\boxed{\displaystyle
\mathcal F_{A,\lambda}(x,y,z)=
\sum_{r=0}^{t}\sum_{u=0}^{t}
\sum_{v=\max(0,r+u-t)}^{\min(r,u)}
{t\brack r}_q{t-r\brack u-v}_q{r\brack v}_q
q^{r(t-r)+u(t-u)+(t-r-u+v)v+2s(r+u)}
x^ry^uz^v.}
\]
Here \({m\brack k}_q\) is the Gaussian binomial coefficient, with value zero outside \(0\le k\le m\). In particular, for any positive number of ordered pairs of fixed factor ranks \(r,u\), **every** product rank in the interval
\[
\boxed{\max(0,r+u-t)\le\rho(XY)\le\min(r,u)}
\]
occurs, with the strictly positive coefficient above. All coefficients depend only on \((t,s)\), not on \(\lambda\) or on the remaining similarity invariants of \(A\).

For example, let \(q=3\) and \(A\) be the nilpotent matrix with Jordan type \((2,1,1)\). Then \((t,s)=(2,1)\); the number of idempotents is \(190\), so there are \(36100\) ordered pairs. Among rank-one pairs, \(2916\) have zero product and \(8748\) have rank-one product. In contrast, the commuting condition studied in other enumerations is not required here.

## Assumptions and scope
Matrix multiplication \(XY\) and idempotence \(X^2=X\) are ordinary matrix operations. Although \(\mathcal C(A,\lambda)\) need not be closed under arbitrary products, its idempotent elements belong to a common two-sided annihilator algebra, so their product is well-defined as an element of that algebra. The condition \(q>2\) is necessary only to allow a nonzero nonidentity twist; characteristic two extension fields are included. Both factor ranks and product rank are ordinary \(\mathbb F_q\)-vector-space ranks, not semigroup generating ranks. No simultaneous commutativity is assumed.

## Proof
**1. Idempotent reduction and sandwich algebra.** For any \(X\in\mathcal C(A,\lambda)\) satisfying \(X^2=X\), the relation \(AX=\lambda XA\) gives
\[
AX=AX^2=\lambda XAX=\lambda^2X^2A=\lambda^2XA.
\]
Since also \(AX=\lambda XA\), and \(\lambda\ne0,1\), we obtain \(AX=XA=0\). The converse is immediate. Consequently the relevant idempotents are exactly those of the associative algebra \(\mathscr R_A=\{X:AX=XA=0\}\).

Put \(K=\ker A\), \(Q=\mathbb F_q^n/\operatorname{im}A\), and \(k=\dim K=\dim Q\). Each \(X\in\mathscr R_A\) factors uniquely as \(\mathbb F_q^n\xrightarrow{\pi}Q\xrightarrow{\widetilde X}K\xrightarrow{\iota}\mathbb F_q^n\). Under this factorization, multiplication becomes \(\widetilde X\star\widetilde Y=\widetilde X(\pi\iota)\widetilde Y\). The map \(\pi\iota:K\to Q\) has kernel \(K\cap\operatorname{im}A\) of dimension \(s\) and rank \(t=k-s\). Choosing suitable independent bases puts it in normal form \(J=\operatorname{diag}(I_t,0_s)\). Thus \(\mathscr R_A\) is a square sandwich/Munn algebra whose underlying matrices are \((t+s)\)-square. The factorization preserves ordinary matrix ranks, since \(\pi\) is surjective and \(\iota\) is injective.

**2. Idempotent normal form and independent lift multiplicities.** Write a sandwich matrix as
\[
\widetilde X=\begin{pmatrix}P&B\\C&D\end{pmatrix},
\]
where \(P\) is \(t\)-square, \(B\) is \(t\)-by-\(s\), \(C\) is \(s\)-by-\(t\), and \(D\) is \(s\)-square. The equation \(\widetilde XJ\widetilde X=\widetilde X\) is equivalent to
\[
P^2=P,\qquad PB=B,\qquad CP=C,\qquad D=CB.
\]
For a fixed rank-\(r\) projection \(P\), there are \(q^{rs}\) choices each for \(B\) and \(C\), and \(D\) is forced. The resulting \(\widetilde X\) has rank \(r\) because its image is the graph of \(C\) over \(\operatorname{im}P\). A second idempotent has the same structure with a projection \(Q\) of rank \(u\) and independently \(q^{2su}\) lift choices. Thus, for every fixed ordered pair \((P,Q)\), there are exactly \(q^{2s(r+u)}\) pairs of lifted idempotents, regardless of whether they commute.

**3. Product rank depends only on the two core projections.** For lifts
\[
\widetilde X=\begin{pmatrix}P&B\\C&CB\end{pmatrix},\qquad
\widetilde Y=\begin{pmatrix}Q&E\\F&FE\end{pmatrix},
\]
we have
\[
\widetilde XJ\widetilde Y=
\begin{pmatrix}PQ&PE\\CQ&CE\end{pmatrix}.
\]
The image of the \(t\)-by-\((t+s)\) matrix \((Q,E)\) is exactly \(\operatorname{im}Q\), since \(QE=E\). The restriction of the \((t+s)\)-by-\(t\) map \(\begin{psmallmatrix}P\\C\end{psmallmatrix}\) to \(\operatorname{im}Q\) has the same kernel as \(P|_{\operatorname{im}Q}\), because \(CP=C\). Hence
\[
\rho(XY)=\rho(\widetilde XJ\widetilde Y)=\rho(PQ).
\]
In particular, the radical lift variables never change the rank of the product.

**4. Exact Grassmann intersection count.** A rank-\(r\) projection \(P\) on a \(t\)-space is specified by its image and complementary kernel. There are
\[
{t\brack r}_q q^{r(t-r)}
\]
such projections. Fix one and put \(L=\ker P\), of dimension \(t-r\). A rank-\(u\) projection \(Q\) has image \(W\), with \(\rho(PQ)=\dim P(W)=u-\dim(W\cap L)\). Therefore \(\rho(PQ)=v\) is equivalent to \(\dim(W\cap L)=u-v\).

The number of \(u\)-dimensional subspaces \(W\) meeting the fixed \((t-r)\)-space \(L\) in dimension \(u-v\) is exactly
\[
{t-r\brack u-v}_q{r\brack v}_q
q^{(t-r-u+v)v}.
\]
To see this, first choose \(W\cap L\), then choose the projected \(v\)-space in the quotient by \(L\), then choose the graph map from that quotient subspace into \(L/(W\cap L)\). For each resulting \(W\), there are \(q^{u(t-u)}\) complementary kernels \(\ker Q\), hence the same number of rank-\(u\) projections with image \(W\). Multiplying this by the number of \(P\)'s and the independently available \(q^{2s(r+u)}\) sandwich lifts gives precisely the displayed coefficient. All choices are reversible, proving an exact bijective count and the stated support interval. This completes the proof.

## Verification
The standalone checker `verify_product_ranks.py` independently constructs finite-field matrix multiplication, tests idempotence, determines matrix ranks by elimination, and enumerates **all ordered pairs of sandwich idempotents** in small cases, checking every triple \((\rho(X),\rho(Y),\rho(XY))\). It includes \(q=3\), \((t,s)=(2,1)\), which exhausts \(3^9=19683\) candidate matrices and produces \(190\) idempotents and \(36100\) ordered pairs; the predicted rank-one pair partition is \(2916\) zero products and \(8748\) rank-one products. The infinite result rests on the proof, not the finite checks. Execute with `python3 verify_product_ranks.py`.

## Relationship to prior work
The 2016 twisted centralizer code literature already proves that products of twisted codewords have multiplicatively composed twists, and thus supplies the elementary reduction to two-sided annihilators; no originality is claimed for that reduction. Muchlis et al. (2021) determine the general code basis and dimension. Dolinka and East (2015/2018) establish the structural theory of rectangular matrix sandwich semigroups, including their regular elements, Green relations, and products of idempotents, but do not report this **full rank-weighted census of ordered idempotent pairs by their product rank**. Yu, Luo, and Li (2024) investigate idempotent generation and zero-product determination in the same Munn algebra framework. A previously studied *commuting-only* sandwich-idempotent joint-rank enumerator does not imply the present distribution for all pairs, most of which need not commute. This finding uses classical Gaussian intersection counting, and the standard full-matrix case \(s=0\) is not asserted to be separately new.

## Limitations
The formula counts rank triples, not individual product matrices' factorization multiplicities. It does not cover twist zero or one, arbitrary products of non-idempotent codewords, or higher products. The Gaussian intersection identity and Munn normalization are classical; the assessed contribution is the complete rank-refined product multiplicity across all kernel-image intersection parameters and twists. An equivalent rank-triple count may exist in older finite semigroup or matrix-factorization literature under different terminology; absence from inspected search results is not proof of global novelty. Independent mathematical audit has not been performed.

## References
- Ahmad Muchlis, Galih Pradananta, Pudji Astuti, and Djoko Suprijanto, *On bases and the dimensions of twisted centralizer codes*, arXiv:2110.01826v1 (2021-10-05), https://arxiv.org/abs/2110.01826.
- Adel Alahmadi et al., *Twisted centralizer codes*, arXiv:1608.04079v1 (2016), https://arxiv.org/abs/1608.04079.
- Igor Dolinka and James East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139 (2015), https://arxiv.org/abs/1503.03139.
- Bo Yu, Kaijia Luo, and Jiankui Li, *Zero product and zero Jordan product determined Munn algebras*, arXiv:2407.00892v1 (2024), https://arxiv.org/abs/2407.00892.
- J. A. Erdős, *On products of idempotent matrices*, Glasgow Mathematical Journal 8 (1967), 118–122 (historical factorization context only).
