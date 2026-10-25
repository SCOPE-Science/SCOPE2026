# Surjective evolution operators with nonunique orthonormal natural bases: complete orthogonal moduli

## Finding

Let \(\mathbb K\in\{\mathbb R,\mathbb C\}\) and let \(m\geq 2\) be an integer. On \(H=\ell^2(\mathbb N,\mathbb K)\), with canonical orthonormal basis \((e_i)_{i\geq1}\), define a commutative bilinear product, continuous in both variables, by
\[
e_i e_j=0\quad(i\ne j),\qquad
e_i^2=e_1\quad(1\leq i\leq m),\qquad
e_{m+j}^2=e_{j+1}\quad(j\geq1).
\]
Call the resulting Hilbert evolution algebra \(A_m\), and denote by \(T_m\) the bounded linear evolution operator specified by \(T_m e_i=e_i^2\). Then:

1. \(T_m\) is surjective, \(\|T_m\|=\sqrt m\), and \(\ker T_m=\{\sum_{i=1}^m a_i e_i:\sum_{i=1}^m a_i=0\}\), of dimension \(m-1\). Every canonical natural-basis square is nonzero.
2. The algebraic square \(A_m^2=\operatorname{span}\{xy:x,y\in A_m\}\) equals \(\ell^1(\mathbb N,\mathbb K)\) as a subspace of \(H\); in particular \(\overline{A_m^2}=H\) although \(A_m^2\ne H\).
3. **Complete orthonormal-natural-basis classification:** every orthonormal natural basis, up to reordering, consists of the canonical tail \((\zeta_i e_i)_{i>m}\), with \(|\zeta_i|=1\), and \(m\) vectors \(f_1,\ldots,f_m\) satisfying
   \[
   (f_1,\ldots,f_m)=(e_1,\ldots,e_m)\,R\,\operatorname{diag}(\eta_1,\ldots,\eta_m),
   \qquad R\in O(m),\quad |\eta_j|=1.
   \]
   In the real case phases mean signs. Conversely all such bases are orthonormal natural bases. Modulo permutations and unimodular rescalings, their parameter space is \(O(m)/B_m\), where \(B_m\) is the finite signed-permutation group acting on the right; hence it has real dimension \(m(m-1)/2\).
4. For **any** Hilbert evolution algebra on a separable real or complex Hilbert space with bounded evolution operator \(T\) relative to an orthonormal natural basis, injectivity of \(T\) on the coefficient subspace \(\ell^1\) implies uniqueness of orthonormal natural bases up to permutations and unimodular scalars. Thus the family \(A_m\) shows, already at the minimum possible nonzero kernel dimension \(1\) (take \(m=2\)), that surjectivity of the bounded evolution operator cannot replace injectivity in this rigidity criterion.

In particular the density-only uniqueness question for Hilbert evolution algebras has a negative answer, even under the stronger assumption that an evolution operator is onto; the entire orthonormal natural-basis moduli of these examples are determined.

## Assumptions and scope

The inner product on complex \(H\) is Hermitian, while the algebra product is **complex bilinear**, never sesquilinear. For \(x=(x_i)\), write \(x\odot y=(x_i y_i)\). The coordinatewise product belongs to \(\ell^1\subset\ell^2\) for all \(x,y\in H\). An *orthonormal natural basis* means a complete orthonormal basis whose distinct vectors multiply to zero. We do not classify nonorthonormal natural bases.

Here \(T_m\) is associated to the displayed canonical orthonormal natural basis. An arbitrary basis change may change the evolution operator; no claim of basis-independent surjectivity is made. All index ranges above and below are countably infinite unless expressly finite.

## Proof

**(1) Bounded product, surjectivity and kernel.** Define
\[
T_m x=\Big(\sum_{i=1}^m x_i\Big)e_1+\sum_{j\geq1}x_{m+j}e_{j+1},\qquad xy=T_m(x\odot y).
\]
The first summand and the tail have orthogonal ranges. Cauchy--Schwarz shows \(\|T_m\|\leq\sqrt m\), and equality holds on the unit vector with first \(m\) coordinates \(1/\sqrt m\) and all others zero. Also \(\|x\odot y\|_2\leq\|x\|_2\|y\|_2\), so the bilinear product is bounded by \(\sqrt m\|x\|_2\|y\|_2\); all left multiplications are continuous. The bounded isometric right inverse
\[
R_m y=y_1e_1+\sum_{j\geq1}y_{j+1}e_{m+j}
\]
satisfies \(T_mR_m=I_H\). Vanishing of all output coordinates forces the tail of \(x\) to vanish and the sum of its first \(m\) coordinates to vanish, giving the asserted kernel.

**(2) The exact algebraic square.** Since \(x\odot y\in\ell^1\) by Cauchy--Schwarz and \(T_m(\ell^1)\subseteq\ell^1\), every product lies in \(\ell^1\). Conversely, given \(z\in\ell^1\), put \(c=R_m z\in\ell^1\). Factor \(c_i=a_i b_i\) with \(|a_i|=|b_i|=\sqrt{|c_i|}\) (for \(c_i\ne0\), take \(a_i=\sqrt{|c_i|}\), \(b_i=c_i/\sqrt{|c_i|}\); use zeros otherwise). Then \(a,b\in\ell^2\) and \(ab=T_m(c)=z\). Thus every element of \(\ell^1\) is itself one product, and \(A_m^2=\ell^1\). This is a proper dense subspace of \(\ell^2\).

**(3) Necessity of the basis normal form.** Let \((f_j)\) be an arbitrary orthonormal natural basis and write \(f_j=\sum_{i\geq1}u_{ij}e_i\). The matrix \(U=(u_{ij})\) is unitary (orthogonal when \(\mathbb K=\mathbb R\)). For distinct \(j,k\), the vector \(c^{jk}=(u_{ij}u_{ik})_i\) lies in \(\ell^1\), and the natural-basis equation gives
\[
0=f_jf_k=T_m(c^{jk}).
\]
The explicit kernel of \(T_m\) yields \(u_{ij}u_{ik}=0\) for every \(i>m\) and distinct \(j,k\), and \(\sum_{i=1}^m u_{ij}u_{ik}=0\). Each tail **row** \(i>m\) of \(U\) therefore has at most one nonzero entry. A row of a unitary has norm one, so that one entry has modulus one. Different such rows occupy distinct columns, by orthogonality of rows. Those columns are exactly unimodular canonical vectors; deleting them leaves precisely \(m\) columns forming an orthonormal basis of \(\operatorname{span}\{e_1,\ldots,e_m\}\). Let \(Q\in U(m)\) be their coefficient matrix. The remaining product equations say that \(Q^tQ\) is diagonal (transpose, not conjugate transpose). Since \(Q\) is unitary, \(Q^tQ\) is also unitary, so its diagonal entries have modulus one. Choose a diagonal unitary \(D\) with \(D^2=Q^tQ\). Then \(R=QD^{-1}\) is unitary and satisfies \(R^tR=I\). Hence \(R^t=R^*\), which forces \(R\) to have real entries; consequently \(R\in O(m)\). Thus \(Q=RD\). Over \(\mathbb R\) the same result is immediate with \(Q\in O(m)\). This proves necessity.

**(4) Sufficiency and moduli.** Each tail vector \(\zeta_i e_i\) is disjointly supported from the other tails and the head block. If \(f_j=\eta_j\sum_{i=1}^mR_{ij}e_i\) for \(R\in O(m)\), then for \(j\ne k\)
\[
f_jf_k=\eta_j\eta_k\Big(\sum_{i=1}^mR_{ij}R_{ik}\Big)e_1=0.
\]
The basis is orthonormal and complete. Two real orthogonal head frames yield the same *unordered, phase-ignored* vectors precisely when their matrices differ by a signed column permutation; thus the moduli quotient is \(O(m)/B_m\). The finite group \(B_m\) does not change its dimension. For \(m=2\), any angle strictly between \(0\) and \(\pi/2\) yields two head vectors each supported on both canonical head coordinates; no permutation and phase rescaling of the canonical basis can produce them.

**(5) General injective-operator rigidity.** In any Hilbert evolution algebra with bounded \(T\), let \((e_i)\) be its defining orthonormal natural basis and \((f_j)\) another. As above, \(c^{jk}=(u_{ij}u_{ik})_i\in\ell^1\), and \(0=f_jf_k=T(c^{jk})\). If \(T|_{\ell^1}\) is injective, every \(c^{jk}\) vanishes, forcing each row of the unitary basis-change matrix to have only one nonzero coefficient, of modulus one. Unitarity makes distinct rows select distinct columns and makes every column selected; the change of basis is monomial. This argument requires no surjectivity or lower norm bound.

## Verification

The proof is exact and does not infer any infinite-dimensional statement from finite truncations. The standalone program `artifacts/verify.py` uses rational arithmetic to check, for \(m\in\{2,3,4,5,6\}\), the rank \(n\) and nullity \(m-1\) of an \(n\)-output coordinate window of \(T_m\) and verifies all cross-product identities for an explicit nonmonomial rational Householder orthogonal rotation on the first \(m\) coordinates. Running `python artifacts/verify.py` produces `VERIFY_OK`. The analytic steps above establish continuity, density, completeness, and the universal quantifiers; none of these follows from finite checks alone.

## Relationship to prior work

Question 46 in Kaygorodov--Martín González--Viruel (arXiv:2610.22248v1, first posted 2026-10-15) asks whether dense algebra square forces uniqueness of an orthonormal natural basis. The family above answers that subquestion negatively and proves a complete moduli formula, even when the associated linear evolution operator is onto. The classical finite-dimensional uniqueness argument for perfect evolution algebras uses independence of the natural-basis squares, corresponding here to injectivity of \(T|_{\ell^1}\), not mere density of its image.

Cadavid--Rodriguez--Vidal (arXiv:2311.08387, Section 3.2, Examples 3.6--3.7) already exhibit different natural orthonormal bases, but in Example 3.6 pairs of canonical squares coincide as \(e_{2j-1}^2=e_{2j}^2=e_{2j}+e_{2j+1}\). Their square span is contained in the proper closed subspace spanned by these pair-sums, so that example does not satisfy the dense-square hypothesis. Vidal--Cadavid--Rodriguez (arXiv:2012.05124, Section 2) establishes the Hilbert evolution-algebra definition and boundedness framework; it does not give this surjective-operator, finite-kernel orthonormal-basis classification. These are implication comparisons, not merely title comparisons.

## Limitations

The result covers a specific countable Hilbert family and the stated sufficient rigidity condition, not all Hilbert evolution algebras. The injectivity condition is not asserted necessary for uniqueness; neither the bounded automorphism group nor the derivation algebra is classified. The finite computational checks supplement but do not establish the infinite-dimensional proof. Novelty is assessed against the cited sources and bounded literature/database comparisons; unindexed or inaccessible equivalent treatments remain possible.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026-10-15), especially Question 46. https://arxiv.org/html/2610.22248v1
2. P. Cadavid, P. M. Rodriguez, S. J. Vidal, *Hilbert evolution algebras, weighted digraphs, and nilpotency*, arXiv:2311.08387v2 (2024), especially Section 3.2, Examples 3.6--3.7. https://arxiv.org/pdf/2311.08387
3. S. J. Vidal, P. Cadavid, P. M. Rodriguez, *Hilbert evolution algebras and its connection with discrete-time Markov chains*, arXiv:2012.05124v2 (2021), especially Section 2. https://arxiv.org/pdf/2012.05124
