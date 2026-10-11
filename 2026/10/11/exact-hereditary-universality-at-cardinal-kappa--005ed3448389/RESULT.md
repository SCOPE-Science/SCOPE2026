# Exact hereditary universality at cardinal \(\kappa\)
## Finding
Let \(\kappa\) be an infinite cardinal satisfying
\[
2^{\lambda}\le \kappa\qquad\text{for every cardinal }\lambda<\kappa.
\]
There is a hereditary family \(\mathcal U\subset[\kappa]^{<\omega}\) covering \(\kappa\) such that every hereditary covering family \(\mathcal G\subset[\kappa]^{<\omega}\) occurs as an exact coordinate restriction: there is an injection \(\phi_{\mathcal G}:\kappa\to\kappa\) with
\[
A\in\mathcal G\iff \phi_{\mathcal G}[A]\in\mathcal U
\]
for every finite \(A\subset\kappa\). Hence the coordinate map \(e_{\alpha}\mapsto e_{\phi_{\mathcal G}(\alpha)}\) identifies \(X_{\mathcal G}\) isometrically with a \(1\)-complemented coordinate subspace of \(X_{\mathcal U}\).

Combining this with the contractive projection constructed in Theorem 7.1 of arXiv:2610.01919v1 gives a quantitative universal-space consequence: every real Banach space with a monotone unconditional basis of cardinality \(\kappa\) is a \(1\)-complemented isometric subspace of the single combinatorial space \(X_{\mathcal U}\).

## Assumptions and scope
A hereditary covering family on a set \(I\) means a family \(\mathcal G\subset[I]^{<\omega}\) that is closed under taking subsets and contains every singleton. For such \(\mathcal G\),
\[
\|x\|_{\mathcal G}=\sup_{G\in\mathcal G}\sum_{\alpha\in G}|x(\alpha)|
\]
defines the combinatorial norm on \(c_{00}(I)\), and \(X_{\mathcal G}\) is its completion.

The cardinal hypothesis is exactly the hypothesis used in Proposition 7.5 of arXiv:2610.01919v1 to keep the set of finite initial types at cardinality \(\kappa\). No assertion is made here that this hypothesis is necessary. The final Banach-space statement is for real spaces with a monotone unconditional basis; arbitrary unconditional bases still receive the isomorphic complemented conclusion from the source's Theorem 7.2 once an exact universal hereditary family is available.

## Proof
For each ordinal \(\alpha<\kappa\), let \(\mathrm{HC}(\alpha+1)\) denote the set of hereditary covering families on \(\alpha+1\), and put
\[
S=\{(\alpha,\mathcal A):\alpha<\kappa,\ \mathcal A\in\mathrm{HC}(\alpha+1)\}.
\]
For infinite \(\alpha\), the set \([\alpha+1]^{<\omega}\) has cardinality \(|\alpha|\), so
\[
|\mathrm{HC}(\alpha+1)|\le 2^{|\alpha|}\le\kappa.
\]
The finite stages are finite, and there are \(\kappa\) stages. Thus \(|S|\le\kappa\); since every stage has at least one hereditary cover, \(|S|=\kappa\).

Define a strict relation on \(S\) by
\[
(\alpha,\mathcal A)\prec(\beta,\mathcal B)
\]
when \(\alpha<\beta\) and \(\mathcal B\) restricted to \(\alpha+1\) is exactly \(\mathcal A\). Define \(\mathcal U\subset[S]^{<\omega}\) by putting \(\emptyset\in\mathcal U\), and for a nonempty finite set \(E\) declare \(E\in\mathcal U\) precisely when its elements form a \(\prec\)-chain
\[
(\alpha_1,\mathcal A_1)\prec\cdots\prec(\alpha_m,\mathcal A_m)
\]
and
\[
\{\alpha_1,\ldots,\alpha_m\}\in\mathcal A_m.
\]

This \(\mathcal U\) is hereditary. Indeed, a subset of a \(\prec\)-chain is still a \(\prec\)-chain. If its largest vertex is \((\alpha_j,\mathcal A_j)\), then chain coherence gives
\[
\mathcal A_j=\mathcal A_m\upharpoonright(\alpha_j+1).
\]
The new first-coordinate set is a subset of \(\{\alpha_1,\ldots,\alpha_m\}\), hence belongs to \(\mathcal A_m\) by heredity, and because all its coordinates are at most \(\alpha_j\), it belongs to \(\mathcal A_j\). Every singleton \(\{(\alpha,\mathcal A)\}\) belongs to \(\mathcal U\), since \(\mathcal A\) covers \(\alpha+1\). Thus \(\mathcal U\) is a hereditary cover of \(S\).

Now let \(\mathcal G\subset[\kappa]^{<\omega}\) be any hereditary cover and define
\[
\phi_{\mathcal G}(\alpha)=\bigl(\alpha,\mathcal G\upharpoonright(\alpha+1)\bigr).
\]
The map is injective, and its range is a \(\prec\)-chain. If \(A=\{\alpha_1<\cdots<\alpha_m\}\), then the largest label on \(\phi_{\mathcal G}[A]\) is \(\mathcal G\upharpoonright(\alpha_m+1)\). Therefore
\[
\phi_{\mathcal G}[A]\in\mathcal U
\iff A\in\mathcal G\upharpoonright(\alpha_m+1)
\iff A\in\mathcal G.
\]
After identifying \(S\) with \(\kappa\), this proves exact hereditary universality.

Let \(M=\phi_{\mathcal G}[\kappa]\). Since \(\mathcal U\upharpoonright M\) is exactly the transported copy of \(\mathcal G\), the coordinate map \(J:X_{\mathcal G}\to X_{\mathcal U}\) is an isometry. The coordinate projection \(Q_M\) has norm at most \(1\), because the canonical basis of every combinatorial space is \(1\)-unconditional, and its range is exactly \(J[X_{\mathcal G}]\). For a nonzero range its norm is therefore exactly \(1\). Thus \(X_{\mathcal G}\) is \(1\)-complemented isometrically.

Finally, Theorem 7.1 of arXiv:2610.01919v1 constructs, for every real Banach space with a monotone unconditional basis of size \(\kappa\), an isometric embedding into some \(X_{\mathcal G}\) together with a contractive projection onto the image. Composing that projection with the isometric coordinate embedding and \(Q_M\) gives a norm-one projection in \(X_{\mathcal U}\), proving the stated universal-space consequence.

## Verification
The proof is purely symbolic. The cardinal count was checked separately at finite and infinite stages. Heredity was checked for subsets whose maximum changes, which is the only nontrivial case. Exactness was checked in both directions directly from the top initial type. The Banach-space consequence uses only the norm definition and contractivity of coordinate projections, followed by the explicit contractive projection already proved in Theorem 7.1 of the focal source.

A stress test against the source's Proposition 7.5 explains why coherence is needed. In that proposition's explicit hypergraph, fix its canonical coding range for a family \(\mathcal G\). Given any finite set of coded vertices with first-coordinate set \(A\), choose a larger first coordinate \(\beta\) and a new vertex whose label contains \(A\cup\{\beta\}\). The enlarged finite set is a hyperedge, so the original coded finite set lies in the hereditary closure regardless of whether \(A\in\mathcal G\). Thus the hereditary closure is complete on that canonical range. The coherent-type family above prevents precisely these incompatible one-step extensions.

## Relationship to prior work
Section 7 of arXiv:2610.01919v1 seeks a nonseparable analogue of Pełczyński's complementedly universal space. Its Theorem 7.4 passes from a universal hypergraph to a hereditary closure, and Proposition 7.5 gives an explicit universal hypergraph under the same cardinal hypothesis used here. The exact-restriction check above shows that the canonical Proposition 7.5 coding is not preserved by that hereditary-closure step. The present construction works directly in the category of hereditary covers and therefore supplies an exact coordinate model under Proposition 7.5's cardinal hypothesis.

The countable predecessor arXiv:2404.01733v1, Section 4.G, constructs a universal hereditary family by a Fraïssé extension property and obtains Pełczyński's separable universal space. That result supplies the \(\kappa=\omega\) antecedent. The construction here is an explicit cardinal-\(\kappa\) initial-type analogue and yields the norm-one/isometric coordinate statement for monotone unconditional bases.

## Limitations
No necessity of the cardinal arithmetic hypothesis is claimed. The construction does not prove the full implication “existence of an arbitrary \(\kappa\)-universal hypergraph implies existence of a \(\kappa\)-Pełczyński space”; it proves the desired universal hereditary family directly under the stronger explicit cardinal hypothesis used by Proposition 7.5. General universal-structure theory may contain abstract variants of the set-system construction; the searches performed did not locate a statement that supplies this exact hereditary restriction together with the Banach-space \(1\)-complemented isometric consequence.

## References
1. P. Borodulin-Nadzieja, M. Marsy, K. Ryduchowski, *Non-separable combinatorial Banach spaces*, arXiv:2610.01919v1, especially Section 7, Theorem 7.1, Theorem 7.4, Proposition 7.5.
2. P. Borodulin-Nadzieja, B. Farkas, S. Jachimek, A. Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces*, arXiv:2404.01733v1; published in *Studia Mathematica* 282 (2025), 101–132, DOI 10.4064/sm240407-14-1, especially Section 4.G.
