# Joint rank–nilpotency-index fibers in an almost-regular Jordan centralizer

## Finding

Let \(m\ge 2\), let \(q\) be any prime power, and fix \(B=J_m(0)\oplus J_1(0)\) in \(M_{m+1}(\mathbb F_q)\). Let \(\mathcal N_{m,q}=\{X:XB=BX,\ X\text{ nilpotent}\}\). For \(X\in\mathcal N_{m,q}\), write \(r(X)=\operatorname{rank}X\) and \(\nu(X)=\min\{j\ge1:X^j=0\}\), so that \(\nu(0)=1\). Define the joint enumerator

\[
\mathcal P_{m,q}(U,T)=\sum_{X\in\mathcal N_{m,q}}U^{r(X)}T^{\nu(X)}.
\]

For \(1\le v\le m-2\), put \(L_v=(q-1)q^{m-v-1}\), \(h_v=\lceil m/v\rceil\), and \(\delta_v=1\) if \(2v=m-1\), otherwise \(\delta_v=0\). Define

\[
Q_v(T)=\begin{cases}
q^2T^{h_v},&h_v\ge4,\\
\delta_v(q-1)T^2+[q^2-\delta_v(q-1)]T^3,&h_v=3,\\
(2q-1)T^2+(q-1)^2T^3,&h_v=2.
\end{cases}
\]

**The complete joint-rank/index census is**

\[
\boxed{\mathcal P_{m,q}(U,T)=T+(q-1)(2q+1)UT^2+q(q-1)^2U^2T^3+\sum_{v=1}^{m-2}L_vU^{m-v}Q_v(T).}
\]

The empty sum convention applies for \(m=2\). Every coefficient counts individual matrices, not similarity orbits. In particular, \(|\mathcal N_{m,q}|=q^{m+1}\). For every \(m\ge3\), exactly \((q-1)q^m\) of these matrices have nilpotency index \(m\): the proportion is exactly \(1-q^{-1}\), for every field characteristic.

For example, when \(m=5\) and \(q=2\),

\[
\mathcal P_{5,2}(U,T)=T+5UT^2+6U^2T^2+4U^2T^3+4U^3T^2+12U^3T^3+32U^4T^5.
\]

There are therefore 64 nilpotent centralizing matrices in this example, with nilpotency-index counts 1, 15, 16, 0, 32 at indices 1 through 5. In particular, index 4 is absent, despite the existence of indices 3 and 5.

The marginal nilpotency-index coefficients \(N_j=[T^j]\mathcal P_{m,q}(1,T)\) have the further closed forms, where \(k=\lfloor m/2\rfloor\):

\[
N_1=1,\qquad N_2=\begin{cases}(2q-1)q^k-1,&m\text{ even},\\q^{k+2}-1,&m\text{ odd},\end{cases}
\]
\[
N_3=q^2\big(q^{m-\lceil m/3\rceil}-q^k\big)+\mathbf1_{\{m\text{ even}\}}(q-1)^2q^k,
\]
\[
N_j=q^2\left(q^{m-\lceil m/j\rceil}-q^{m-\lceil m/(j-1)\rceil}\right),\qquad4\le j\le m.
\]

For \(m\ge4\), the indices \(j\ge4\) occur precisely when an integer \(v\) satisfies \(\lceil m/v\rceil=j\). In particular, the number of *distinct* possible nilpotency indices grows at most on the order of \(\sqrt m\), even though the ambient matrix dimension is \(m+1\).

## Assumptions and scope

The theorem applies to every integer \(m\ge2\) and every finite field \(\mathbb F_q\), including fields of characteristic two. The large Jordan block has size \(m\), and the second block has size one. There are no constraints on the characteristic relative to \(m\). All powers are ordinary associative matrix powers; \(r\) is the ordinary matrix rank. No assertion is made for a different fixed Jordan partition or for conjugacy-orbit multiplicities.

## Proof

Identify the underlying \(\mathbb F_q[t]\)-module with \(R\oplus\mathbb F_q\), where \(R=\mathbb F_q[t]/(t^m)\) and multiplication by \(t\) represents \(B\). Put \(e=t^{m-1}\in R\) and \(\epsilon(u)=u(0)\). Every endomorphism commuting with \(B\) is uniquely of the form

\[
X(u,z)=\big(f(t)u+bze,\ c\epsilon(u)+dz\big),
\]

where \(f\in R\) and \(b,c,d\in\mathbb F_q\). The characteristic polynomial is \((\lambda-f(0))^m(\lambda-d)\). For instance, the Schur complement correction vanishes because \(\epsilon((\lambda-f(t))^{-1}e)=0\). Therefore \(X\) is nilpotent exactly when \(f(0)=d=0\). Write \(F=f\in tR\). This gives precisely \(q^{m-1}q^2=q^{m+1}\) nilpotent matrices.

Since \(Fe=0\), \(\epsilon(Fu)=0\), and \(\epsilon(e)=0\), the powers satisfy

\[
X^2(u,z)=\big((F^2+bc\,t^{m-1})u,0\big),\qquad
X^j(u,z)=\big(F^ju,0\big)\quad(j\ge3).
\]

First suppose \(F=0\). The images of \((u,0)\) and \((0,z)\) lie in independent central lines. If both \(b,c\) vanish, rank zero and index one occur once. If precisely one is nonzero, rank one and index two occur in \(2(q-1)\) cases. If both are nonzero, rank two and index three occur in \((q-1)^2\) cases.

Now suppose \(F\ne0\), with \(t\)-adic valuation \(v\). Write \(F=t^v a(t)\) with \(a(0)\ne0\). There are exactly \(L_v=(q-1)q^{m-v-1}\) such polynomials. If \(v\le m-2\), then \(\epsilon(\ker F)=0\) and \(e\in F(\ker\epsilon)\). Consequently the \(b\)-column contributes no additional image dimension, and \(r(X)=m-v\) for all choices of \(b,c\). If \(v=m-1\), then \(F\) has rank one, and the extra \(b\)-column adds a dimension exactly when \(bc\ne0\). Hence this last valuation contributes \((q-1)(2q-1)\) elements of rank one and index two and \((q-1)^3\) elements of rank two and index three. Together with \(F=0\), these are the two nonconstant terms preceding the sum in the boxed formula.

For \(1\le v\le m-2\), put \(h=\lceil m/v\rceil\). If \(h\ge4\), then \(X^{h-1}\ne0\) and \(X^h=0\) by the power formulas; every choice of \(b,c\) gives index \(h\). If \(h=2\), then \(F^2=0\) and the index is two precisely when \(bc=0\). The two counts are \(2q-1\) and \((q-1)^2\). If \(h=3\), then \(F^2\ne0\), but \(F^3=0\). The equation \(X^2=0\) can hold only when \(F^2\) is a scalar multiple of \(t^{m-1}\), which is equivalent to \(2v=m-1\). In that case \(F^2=a(0)^2t^{m-1}\), and the cancellation equation \(bc=-a(0)^2\) has exactly \(q-1\) solutions, independently of characteristic. All other \(b,c\) give index three. These three cases give \(Q_v(T)\), proving the joint formula.

Summing its coefficients over all ranks gives the stated marginal formulas: the valuation ranges with index \(j\ge4\) run from \(\lceil m/j\rceil\) through \(\lceil m/(j-1)\rceil-1\), and their counts telescope. The index-two and index-three formulas incorporate the unique middle-valuation cancellation when \(m\) is odd. For \(m\ge4\), the index-\(m\) elements have exactly \(v=1\), giving \((q-1)q^{m-2}q^2=(q-1)q^m\). For \(m=3\), the displayed \(N_3\) formula gives the same answer. Finally, the distinct ceiling quotients \(\lceil m/v\rceil\) number \(O(\sqrt m)\): split \(v\) at \(\lfloor\sqrt m\rfloor\), so there are at most \(\lfloor\sqrt m\rfloor\) small values of \(v\) and at most \(\lceil\sqrt m\rceil+1\) distinct quotient values for larger \(v\). This proves the sparse-index assertion.

## Verification

The standalone file `verify_almost_regular_nilpotency.py` reconstructs the centralizing matrices from their matrix entries, independently computes ordinary ranks by finite-field elimination and nilpotency indices by repeated matrix multiplication, and compares every two-variable coefficient to the formula. It exhaustively checks 20 parameter cases: \(q=2\) with \(2\le m\le9\), \(q=3\) with \(2\le m\le6\), \(q=4\) with \(2\le m\le5\), and \(q=5\) with \(2\le m\le4\). The \(q=4\) implementation uses \(\mathbb F_2[u]/(u^2+u+1)\) rather than reducing arithmetic modulo four. The verifier also tests 594 exact integer identities across \(q\in\{2,3,4,5,7,9\}\) and \(2\le m\le100\). It prints `VERIFY_OK_ALMOST_REGULAR_NILPOTENCY 20` on success. Computation is corroboration; the proof above establishes all dimensions and finite fields.

## Relationship to prior work

Oblak determines the possible maximal nilpotency index for matrices commuting with a fixed nilpotent matrix, rather than the finite-field multiplicities of all joint rank/index fibers. Britnell and Wildon, especially Proposition 4.4, give the exact possible Jordan partition types for the almost-regular block partition and write the same centralizer in coordinates; their classification of *which partitions can occur* is not claimed as new here. Their argument does not enumerate how many individual matrices occupy each joint fiber. Sharma counts simultaneous-similarity branches in small dimensions, a distinct orbit-counting problem. Iarrobino, Khatami, Van Steirteghem and Zhao study generic commuting nilpotent Jordan types and partition fibers, not these finite-field point counts. The square-zero sublocus (index at most two) alone does not determine the indices above two or their joint ranks. The contribution claimed here is specifically the complete two-variable cardinality formula and its exact uniform maximal-index density.

## Limitations

The closed form concerns only centralizers of \(J_m(0)\oplus J_1(0)\). It neither classifies all simultaneous conjugacy orbits nor counts general commuting nilpotent pairs with both matrices varying. The support of allowable Jordan partitions and maximal nilpotency-index bounds are established in earlier literature and are not claimed as novel. Prior results provide much of the coordinate framework, so the primary novelty is the arithmetic refinement; unlocated older enumerations under different notation remain possible. No independent mathematical validation is claimed.

## References

1. P. Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, arXiv:math/0701561 (first posted 2007-01-19), especially Section 5, Theorem 16. https://arxiv.org/abs/math/0701561
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 2010-01-06), especially Section 4, Proposition 4.4. https://arxiv.org/abs/1001.0811
3. U. B. Sharma, *Simultaneous Similarity Classes of Commuting matrices over a finite field*, arXiv:1409.2698 (first posted 2014-09-07), especially Sections 4–5. https://arxiv.org/abs/1409.2698
4. A. Iarrobino, L. Khatami, B. Van Steirteghem and R. Zhao, *Nilpotent matrices having a given Jordan type as maximum commuting nilpotent orbit*, arXiv:1409.2192 (first posted 2014-09-08), especially Sections 1–2. https://arxiv.org/abs/1409.2192
