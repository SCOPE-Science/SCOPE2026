# Commutator-rank census of finite rectangular-band semigroup algebras

## Finding
Let \(m,n\ge1\) be integers, let \(q\) be any prime power, and put \(A=\mathbb F_q[S_{m,n}]\), where \(S_{m,n}=[m]\times[n]\) has multiplication \((i,j)(k,l)=(i,l)\). Identify \(A\) as a vector space with \(M_{m\times n}(\mathbb F_q)\); matrix rank here means the ordinary rank of that array, not the rank of a left-regular representation. For independently chosen \(X,Y\in A\), let \(N_j\) be the number of ordered pairs for which the coefficient matrix of their algebra commutator \([X,Y]=X\star Y-Y\star X\) has rank \(j\).

Set \(h=(m-1)(n-1)\), \(T=q^{m+n-1}\), and
\[
K=T+(q^{n-1}-1)q^{n-1}+(q^{m-1}-1)q^{m-1}
+(T-q^{n-1}-q^{m-1}+1)q.
\]
For every integer \(d\ge1\) define
\[
F_d^{(0)}=(q^{d-1}-1)(q^{d-1}-q),\qquad
F_d^{(*)}=q^{d-1}(q^{d-1}-1),
\]
where both expressions are zero at \(d=1\). Let \(B=F_m^{(0)}F_n^{(0)}+(q^2-1)F_m^{(*)}F_n^{(*)}\). Then the **complete exact distribution** is
\[
\boxed{N_0=q^{2h}K,\qquad N_2=q^{2h}B,\qquad
N_1=q^{2mn}-N_0-N_2.}
\]
No ranks beyond two occur. In particular the element commuting probability is \(N_0/q^{2mn}\). For \(m,n\ge2\), the rank-two commutator locus is a nonempty Zariski-open dense subset of \(A^2\) after scalar extension to an algebraic closure; for \(\min(m,n)=1\), rank two never occurs.

The formula also provides the full centralizer-size distribution. Write \(r(X)\) for the vector of row sums and \(c(X)\) for the vector of column sums. For each \(X\) the number of commuting \(Y\) is
\[
\begin{cases}
q^{h+m+n-1},&r(X)=0,\ c(X)=0;\\
q^{h+n-1},&r(X)=0,\ c(X)\ne0;\\
q^{h+m-1},&r(X)\ne0,\ c(X)=0;\\
q^{h+1},&r(X)\ne0,\ c(X)\ne0.
\end{cases}
\]
The respective numbers of \(X\) in these four classes are \(q^h\), \(q^h(q^{n-1}-1)\), \(q^h(q^{m-1}-1)\), and \(q^h(T-q^{n-1}-q^{m-1}+1)\).

## Assumptions and scope
The field has exactly \(q\) elements; no restriction on characteristic is made. All counts concern **labelled elements of the semigroup algebra**, not just the basis semigroup and not simultaneous-conjugacy classes. The algebra is allowed to be nonunital and is equipped with the multiplication induced by the rectangular band. The convention \(m,n\ge1\) includes its one-row and one-column degenerate cases.

## Proof
Write \(X=(x_{ij})\), \(Y=(y_{ij})\). Directly expanding the rectangular-band multiplication gives
\[
(X\star Y)_{i l}=\sum_{j=1}^{n}\sum_{k=1}^{m}x_{ij}y_{kl}
=r_i(X)c_l(Y).
\]
Consequently
\[
[X,Y]=r(X)c(Y)^t-r(Y)c(X)^t.
\]
Let \(u\in\mathbb F_q^m\), \(v\in\mathbb F_q^n\) denote possible row- and column-sum vectors of the same element. Necessarily \(\boldsymbol1^t u=\boldsymbol1^t v\); conversely every such pair arises, by filling the first row and column and adjusting the upper-left entry. Thus the sum map onto
\[
W=\{(u,v):\boldsymbol1^tu=\boldsymbol1^tv\}
\]
is surjective with dimension \(m+n-1\) and kernel dimension \(h\). Every ordered pair of sum data has precisely \(q^{2h}\) lifts to an ordered pair of algebra elements.

Fix \((r,c)\in W\) and solve \(r d^t-s c^t=0\) for \((s,d)\in W\). If \(r=c=0\), all \(T\) choices work. If \(r=0,c\ne0\), then \(s=0\) and \(d\) may be any sum-zero vector: exactly \(q^{n-1}\) choices. If \(r\ne0,c=0\), there are \(q^{m-1}\) choices. If both are nonzero, equality of the two rank-one matrices forces \(s=\lambda r\) and \(d=\lambda c\) for the same unique \(\lambda\in\mathbb F_q\); all \(q\) choices satisfy the common-total condition. The numbers of \((r,c)\) in the four cases are, respectively,
\[
1,\qquad q^{n-1}-1,\qquad q^{m-1}-1,\qquad
T-q^{n-1}-q^{m-1}+1.
\]
Adding the commuting fibers proves \(K\), the centralizer formulas, and \(N_0\).

The commutator has rank two exactly when \(r,s\in\mathbb F_q^m\) are linearly independent **and** \(c,d\in\mathbb F_q^n\) are linearly independent, since it factors as a product of an \(m\)-by-two full-column-rank matrix, an invertible two-by-two alternating matrix, and a two-by-\(n\) full-row-rank matrix. The factorization is valid also in characteristic two.

For a fixed two-vector of coordinate totals \(t\in\mathbb F_q^2\), count ordered independent \((r,s)\) having those totals. If \(t=0\), both vectors lie in the \((m-1)\)-dimensional sum-zero hyperplane, giving \(F_m^{(0)}\). If \(t\ne0\), choose an invertible two-by-two change of ordered vectors so that the prescribed totals become \((1,0)\); the first vector has \(q^{m-1}\) possibilities and the second has \(q^{m-1}-1\) choices avoiding its span, giving \(F_m^{(*)}\). The independent column-vector pairs are counted similarly. Compatibility of the totals on the row and column sides imposes the same \(t\), so summing one zero and \(q^2-1\) nonzero total vectors yields \(B\). Multiplying by \(q^{2h}\) yields \(N_2\); subtraction from the total \(q^{2mn}\) gives \(N_1\).

When \(m,n\ge2\), taking first and second coordinate vectors on both sides, with matching totals, witnesses rank two. Independence is an open condition on \(A^2\); since \(A^2\) is affine space and thus irreducible, this nonempty open set is dense over the algebraic closure. If \(\min(m,n)=1\), one factor has dimension one and rank two is impossible. This concludes the proof.

## Verification
The standalone script `verify_rectband.py` independently constructs the product by four nested sums of semigroup basis products, computes ranks by finite-field Gaussian elimination, and compares the complete \(0,1,2\) histogram against the formulas. It checks eight exhaustive cases at \(q=2\) or \(q=4\), including \((m,n)=(3,3)\) at \(q=2\), and prints `RECTANGULAR_BAND_COMMUTATOR_OK 8 complete enumerations`. For example \((m,n,q)=(2,2,2)\) yields \((N_0,N_1,N_2)=(88,120,48)\). These finite tests corroborate the general argument but do not establish it alone.

## Relationship to prior work
Livshits, MacDonald, Mathes, and Radjavi, *On band algebras* (2001), Section 4, give structural statements about commutators of members of an operator band, including cube-zero commutators for such idempotent **basis elements**. The present census instead concerns arbitrary linear combinations in a finite semigroup algebra and counts their coefficient-matrix ranks in every field. Choi, Gourdeau, and White, *Simplicial cohomology of band semigroup algebras* (arXiv:1004.2301, 2010), Sections 2--3 and their principal results, treat rectangular-band structure and cyclic/simplicial cohomology, not finite-field commutator-rank frequencies. Livshits and collaborators, *Matrix semigroups with commutable rank* (2003), study equality of \(\operatorname{rank}(AB)\) and \(\operatorname{rank}(BA)\), which does not imply an enumeration of \(\operatorname{rank}(AB-BA)\). More recent work on commuting graphs of Rees matrix **semigroups** also has a different underlying object and does not count pairs in the associated algebra. No comprehensive global priority claim is made.

## Limitations
No commutator fibers at a prescribed nonzero target matrix, automorphism orbits, or analogous formula for general non-rectangular bands is derived. Ordinary matrix rank depends on the chosen natural rectangular-band coefficient array. The analysis concerns rational points over finite fields and the stated reduced rank strata, not scheme structures of commutator fibers. Possible implicit derivations in historical semigroup-ring literature remain a priority risk; independent validation has not been performed.

## References
1. L. Livshits, G. MacDonald, B. Mathes, H. Radjavi, *On band algebras*, Journal of Operator Theory 46 (2001), 545--560, https://jot.theta.ro/jot/archive/2001-046-003/2001-046-003-005.pdf.
2. Y. Choi, F. Gourdeau, M. C. White, *Simplicial cohomology of band semigroup algebras*, arXiv:1004.2301 (first posted 2010-04-14), https://arxiv.org/abs/1004.2301.
3. L. Livshits, G. MacDonald, B. Mathes, J. Okniński, H. Radjavi, *Matrix semigroups with commutable rank*, Semigroup Forum 67 (2003), 288--316, doi:10.1007/s00233-002-0013-5 (published 2003-05-09).
4. *Commuting graphs of Rees matrix semigroups*, Semigroup Forum (2025), doi:10.1007/s00233-025-10597-0 (theorem 3.14 concerns the basis semigroup).
