# Product-idempotence rank laws and a three-quarter limit for height-two incidence algebras

## Finding
Let \(P\) be any finite poset in which every strict interval contains only its endpoints (height at most two), and let \(A=I(P,\mathbb F_q)\), where \(q\ge2\) is a prime power. For \(E,F\in A\), write \(E^2=E\), \(F^2=F\), and require \((EF)^2=EF\). With \(u,v,w\) independent indeterminates, the complete joint rank enumerator
\[
\mathcal H_{P,q}(u,v,w)=\sum_{\substack{E^2=E,\ F^2=F\\(EF)^2=EF}}u^{\operatorname{rank}E}v^{\operatorname{rank}F}w^{\operatorname{rank}(EF)}
\]
is a four-state edge partition function. Order the states as \(00,01,10,11\) and define
\[
D=\begin{pmatrix}0&1&1&2\\1&0&2&1\\1&1&0&1\\2&1&1&0\end{pmatrix}.
\]
If \(\gamma:P\to\{00,01,10,11\}\), write \(\gamma(x)=(a_x,b_x)\). Then
\[
\boxed{\mathcal H_{P,q}(u,v,w)=\sum_{\gamma}\left(\prod_{x<y}q^{D_{\gamma(x),\gamma(y)}}\right)\prod_{x\in P}u^{a_x}v^{b_x}w^{a_xb_x}.}
\]
The edges \(x<y\) are all strict comparable pairs, which coincide with covers under the height assumption. The formula also covers isolated vertices and the empty poset.

For the height-two star \(P_m\) with one minimal element below \(m\ge1\) pairwise incomparable maximal elements, put \(N_{m,q}=\mathcal H_{P_m,q}(1,1,1)\). Then
\[
\boxed{N_{m,q}=3(1+q)^{2m}+(1+3q)^m.}
\]
Since \(A\) has exactly \(2(1+q)^m\) idempotents, two independent uniformly chosen idempotents have idempotent product with probability
\[
\boxed{\Pr((EF)^2=EF)=\frac34+\frac14\left(\frac{1+3q}{(1+q)^2}\right)^m\ \longrightarrow\ \frac34.}
\]
This nontrivial \(3/4\) limit holds for every fixed finite field, including characteristic two.

## Assumptions and scope
The poset is finite and height at most two, so there is no chain of three distinct elements. The incidence algebra uses convolution and is represented by matrices with entries at ordered comparable pairs. All ranks are ordinary matrix ranks over \(\mathbb F_q\). This is a census of *ordered* pairs of idempotents in the full incidence algebra, conditioned on their ordered product being idempotent; it does not require \(EF=FE\). No assertion is made for height-three or greater posets.

## Proof
For each vertex \(x\), idempotency forces the diagonal entries of \(E\) and \(F\) to be bits \(a_x,b_x\in\{0,1\}\). Fix these bits. For each strict comparable pair \(x<y\), write \(X=E_{xy}\), \(Y=F_{xy}\), and \(a=a_x,b=b_x,c=a_y,d=b_y\). There are no nontrivial intermediate vertices, so the two idempotence equations are
\[
(a+c-1)X=0,\qquad (b+d-1)Y=0.
\]
Consequently \(X\) is free precisely when \(a\ne c\), and \(Y\) is free precisely when \(b\ne d\). All such coordinates across distinct comparable pairs are independent.

The product has diagonal bits \(ab,cd\) and off-diagonal entry \(aY+Xd\). Its idempotency imposes no further condition if \(ab\ne cd\); if \(ab=cd\), it imposes the linear condition \(aY+dX=0\). On the initially allowed subspace, this equation has rank one exactly when \(ab=cd\) and either \(a=1,b\ne d\), or \(d=1,a\ne c\). Otherwise it has rank zero. Thus the solution-space dimension at this edge is
\[
D_{(a,b),(c,d)}=\mathbf1_{a\ne c}+\mathbf1_{b\ne d}-\mathbf1_{ab=cd}\,\mathbf1_{(a=1,\ b\ne d)\lor(d=1,\ a\ne c)}.
\]
Evaluating these sixteen finite possibilities produces exactly the displayed four-by-four matrix \(D\). Each local solution space has \(q^{D_{(a,b),(c,d)}}\) elements, regardless of the characteristic. Multiplication over edges and summation over all diagonal labels proves the claimed partition function.

An idempotent matrix is diagonalizable with eigenvalues zero and one, so its ordinary rank equals its number of diagonal ones (also in positive characteristic). Since \(EF\) is assumed idempotent, its rank equals the number of vertices where \(a_x=b_x=1\). This supplies the three monomial exponents and proves the complete joint distribution.

For a star, fix the state at its unique minimal vertex. The four row sums of \(q^D\) are \((1+q)^2,(1+q)^2,1+3q,(1+q)^2\). Distinct leaves contribute independently, giving the exact expression for \(N_{m,q}\). Separately, fixing the center diagonal bit of one idempotent leaves \(1+q\) choices at each leaf (one same-bit choice or \(q\) opposite-bit choices); either center bit is possible. Thus \(\#\{E:E^2=E\}=2(1+q)^m\). Dividing by its square yields the probability formula. Finally, \(0<(1+3q)/(1+q)^2<1\) for \(q\ge2\), proving the limit.

## Verification
The standalone file `verify.py` independently enumerates the matrices of nine small incidence algebras over \(\mathbb F_2\) or \(\mathbb F_3\), checks all idempotent pairs by direct multiplication, tests whether the product is idempotent, and compares *every coefficient* of the resulting three-rank polynomial against the graph formula. It checks, among others, the two-by-two complete bipartite poset and a disconnected poset. Every case passed. Separately, twenty polynomial evaluations of the star count for four integer field sizes and five star degrees matched the formula. The integer checks at composite field size four verify the formula as a polynomial evaluation, not an independent realization of \(\mathbb F_4\). Running `python verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Can, Casimiro and Malheiro study irreducible components of incidence-monoid idempotent varieties and show that certain **antichain submonoids** of bipartite-poset incidence monoids are orthodox. Their Theorems 1.1, 1.2 and 4.9 address those components and restricted product closures, rather than counting all ordered idempotent pairs in the **full** incidence algebra whose product is idempotent. The star limit quantifies precisely such product closure in the unrestricted setting. Gargate and Gargate study counts of single polynomial-potent elements in incidence algebras; their scalar-root coordinate method is related to fixing diagonal idempotent bits, but does not impose the mixed ordered-product equation or supply its joint-rank distribution. Kolegov investigates minimal idempotent generating sets, a different invariant.

## Limitations
The height assumption is essential for the edge independence used in the proof. The limit concerns stars with a growing number of leaves at fixed field size and does not assert a universal limit for arbitrary growing posets. The counting method is elementary finite-field linear algebra. It is plausible that some product-idempotence counts are implicit in broader work on bands or orthodox semigroups; exhaustive publication priority is not established. Finite enumerations are supporting checks, not infinite-dimensional proofs.

## References
1. M. B. Can, A. Casimiro and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1, first posted 2022-08-01; especially Theorems 1.1, 1.2, 3.2 and 4.9.
2. I. Gargate and M. Gargate, *\((k+1)\)-Potent Matrices in Triangular Matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1, first posted 2020-08-30.
3. N. A. Kolegov, *Idempotent Generators of Incidence Algebras*, Bulletin of the Australian Mathematical Society, published online 2024-03-05, DOI:10.1017/S0004972724000078.
