# The \(p=\infty\) endpoint and simultaneous-exponent reduced algebras of weak semilattices
## Finding
Let \(S\) be an inverse semigroup without zero whose universal groupoid \(G(S)\) is Hausdorff. Equivalently, \(S\) is a weak semilattice. For each \(p\in[1,\infty]\), write \(\lambda^{S,p}\) for the usual left regular representation of \(S\) on \(\ell^p(S)\). For a nonempty set \(P\subseteq[1,\infty]\), define
\[
\|\xi\|_{P,S}=\sup_{p\in P}\|\lambda^{S,p}(\xi)\|,\qquad \xi\in\mathbb C S,
\]
and let \(F^P_{\mathrm{red}}(S)\) be the completion of \(\mathbb C S\) in this norm.

If \(\pi:\mathbb C S\to A_{\mathbb C}(G(S))\) is the canonical Steinberg-algebra isomorphism, then for every nonempty \(P\subseteq[1,\infty]\),
\[
\|\pi(\xi)\|_{P,\mathrm{red}}=\|\xi\|_{P,S}\qquad(\xi\in\mathbb C S),
\]
so \(\pi\) extends to an isometric isomorphism
\[
F^P_{\mathrm{red}}(S)\cong F^P_{\mathrm{red}}(G(S)).
\]
In particular, this supplies the endpoint \(p=\infty\) omitted from the finite-exponent inverse-semigroup comparison in the source paper.

As a consequence, if \(S\) and \(T\) are countable, strongly Morita equivalent weak semilattices without zero, then their simultaneous-exponent reduced algebras are Morita equivalent for every nonempty \(P\subseteq[1,\infty]\). The induced \(K\)-theory isomorphisms are compatible with the canonical maps arising from inclusions of exponent sets.

## Assumptions and scope
The semigroup has no zero, matching the algebraic model used in the source comparison. Hausdorffness of the universal groupoid is essential here because it is the hypothesis under which the Steinberg algebra is dense in the relevant groupoid completions and is equivalent to the weak-semilattice condition used by the source.

The definition of \(F^P_{\mathrm{red}}(S)\) above is a simultaneous-exponent completion of the same algebraic left regular representation used for the individual reduced algebras. No assertion is made for non-Hausdorff universal groupoids or for inverse semigroups with zero without first choosing the appropriate contracted model.

## Proof
For every finite \(p\), the source proves
\[
\|\pi(\xi)\|_{p,\mathrm{red}}=\|\lambda^{S,p}(\xi)\|,
\qquad \xi\in\mathbb C S.
\]
It remains to prove the endpoint \(p=\infty\).

Fix \(\xi=\sum_{s\in F}a_s s\in\mathbb C S\), where \(F\) is finite. Relative to the coordinate vectors of \(S\), each \(\lambda^{S,p}(s)\) is the same partial-permutation matrix, independent of \(p\). If \(M_\xi\) denotes the finite-row matrix of \(\lambda^{S,p}(\xi)\), inversion in the inverse semigroup reverses the partial bijection, so
\[
M_{\xi^*}=\overline{M_\xi}^{\,T}.
\]
Every row and column contains only finitely many nonzero entries because \(F\) is finite. Therefore the standard matrix formulas for the operator norms on \(\ell^\infty\) and \(\ell^1\) give
\[
\|\lambda^{S,\infty}(\xi)\|
=\sup_u\sum_t |(M_\xi)_{u,t}|
=\sup_t\sum_u |(M_{\xi^*})_{u,t}|
=\|\lambda^{S,1}(\xi^*)\|.
\]

On the groupoid side, the endpoint computation in the source gives
\[
\|f\|_{\infty,\mathrm{red}}=\|f^*\|_{1,\mathrm{red}}
\]
for compactly supported convolution functions. The canonical Steinberg map respects involution because \(\mathcal O_{s^*}=\mathcal O_s^{-1}\). Hence, using the source's \(p=1\) case,
\[
\begin{aligned}
\|\pi(\xi)\|_{\infty,\mathrm{red}}
&=\|\pi(\xi)^*\|_{1,\mathrm{red}}\\
&=\|\pi(\xi^*)\|_{1,\mathrm{red}}\\
&=\|\lambda^{S,1}(\xi^*)\|\\
&=\|\lambda^{S,\infty}(\xi)\|.
\end{aligned}
\]
Thus the canonical norm identity holds for every \(p\in[1,\infty]\). Taking the supremum over \(p\in P\) proves equality of the simultaneous-exponent norms.

Finally, the Steinberg algebra \(A_{\mathbb C}(G(S))\) is dense in \(C_c(G(S))\) in the \(I\)-norm for Hausdorff ample groupoids, and every reduced \(p\)-norm, hence every \(P\)-reduced norm, is bounded by the \(I\)-norm. Therefore the isometric extension has dense and closed range and is onto. The Morita-equivalence consequence follows by transporting the source paper's \(F^P_{\mathrm{red}}\)-Morita equivalence for equivalent groupoids across these isometric identifications.

## Verification
The proof was checked at the level of matrix entries rather than by density of finitely supported vectors in \(\ell^\infty\); this is necessary because that density fails at the endpoint. For one generator \(s\), the left regular operator is a partial permutation whose transpose is the partial permutation for \(s^*\). For a finite linear combination, conjugate transpose gives the matrix of the involuted element, and the exact row-sum/column-sum formulas yield the endpoint norm identity.

The groupoid endpoint equality was independently matched to the source's explicit \(p=1\)/\(p=\infty\) reduced-norm calculation. The finite-exponent comparison, Steinberg density, weak-semilattice/Hausdorff equivalence, groupoid \(P\)-Morita equivalence, and compatibility under exponent-set inclusions were checked in the cited source sections.

## Relationship to prior work
Chung, Delfín and Wang prove the canonical reduced inverse-semigroup/groupoid isomorphism for \(1\le p<\infty\), after explicitly restricting the inverse-semigroup subsection to finite exponents. They also state that they are not aware of a reduced analogue in the literature for \(p\ne2\), while their general groupoid Morita theorem itself includes \(p=\infty\) and their simultaneous-exponent groupoid theorem allows arbitrary nonempty \(P\subseteq[1,\infty]\).

Bardadyn, Kwaśniewski and McKee prove the corresponding full inverse-semigroup/groupoid isomorphism for every \(p\in[1,\infty]\) and develop full and reduced groupoid endpoint norms. Their inverse-semigroup theorem is a full/universal completion theorem, not the canonical reduced left-regular comparison proved here.

The present observation closes precisely this endpoint mismatch and then upgrades the inverse-semigroup comparison to the simultaneous-exponent completion.

## Limitations
No claim is made that the Hausdorff/weak-semilattice hypothesis can be removed. The argument also does not address semigroups with zero without passing to a contracted algebra and the corresponding groupoid model. The simultaneous-exponent consequence depends on defining the semigroup \(P\)-norm as the supremum of the individual left-regular norms.

The literature comparison found no implication-equivalent reduced endpoint theorem, but an older formulation under a different inverse-semigroup Banach-algebra convention could still exist. The proof establishes a canonical isometric identification under the stated definitions; it does not classify all possible reduced completions used elsewhere.

## References
1. Y. C. Chung, A. Delfín and Z. Wang, *Morita equivalence for \(L^p\)-operator algebras associated with étale groupoids*, arXiv:2609.39031v1, 2026. In particular, Sections 2.1, 4 and 8.3, Proposition 8.10, Corollary 8.11, Remark 4.12 and Proposition 4.13.
2. K. Bardadyn, B. K. Kwaśniewski and A. McKee, *Banach algebras associated to twisted étale groupoids: inverse semigroup disintegration and representations on \(L^p\)-spaces*, arXiv:2303.09997v4; Journal of Functional Analysis 289 (2025), 111163. In particular, Section 6 and Corollary 6.10.
