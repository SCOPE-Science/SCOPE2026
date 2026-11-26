# Hilbert-factorable nonregular language Hankel operators from injective graphs

## Finding

For an injection \(f:\mathbb N_0\to\mathbb N_0\), let \(L_f=\{0^a1^{f(a)}:a\ge0\}\). The real language Hankel operator of every such binary language is noncompact and factors through a Hilbert space with product of operator norms at most \(\sqrt 2\). This includes injections with arbitrary growth, with no monotonicity or effectiveness assumption.

Consequently, this family gives explicit weakly compact examples with the same compact approximation-number tail as the non-weakly-compact order-language operator for \(L_{\le}=\{0^i1^j:0\le i\le j\}\). In both cases \(a_n(H_L)=1/2\) for \(n\ge2\) by Hristov–Ilchev–Nedelcheva–Zlatanov [1]. The order-language operator has weakly compact distance \(1/2\) by the classical half-graph argument given below; the injective-graph operators have distance zero.

## Assumptions and scope

Write \(S=\{0,1\}^*\), including the empty word, and use real scalars. A language Hankel operator is \(H_L:\ell_1(S)\to\ell_\infty(S)\) with \((H_Lx)(v)=\sum_{u\in S}x(u)\mathbf1_L(uv)\). The norm of an operator between these spaces is the supremum of its absolute matrix entries. Weak compactness means the image of the unit ball is relatively weakly compact. Approximation numbers use \(a_n(H)=\inf\{\|H-R\|:\operatorname{rank}R<n\}\). Neither optimality of the factorization bound nor a classification of general weakly compact language operators is asserted.

## Proof

Fix an injection \(f\). Write \(q_u=H_{L_f}e_u\), where \(e_u\) is the unit vector at the word \(u\). For \(u=0^a\), including \(a=0\), the support of \(q_u\) is
\[
D_a=\{0^r1^{f(a+r)}:r\ge0\}.
\]
For \(u=0^a1^b\) with \(1\le b\le f(a)\), its support is the singleton \(\{1^{f(a)-b}\}\); all other derivatives vanish, since these words are not prefixes of any word of \(L_f\). The sets \(D_a\) are nonempty and pairwise disjoint: a common word determines its number \(r\) of zeros and then gives \(f(a+r)=f(a'+r)\), forcing \(a=a'\). This also treats words that are all zeros or all ones. The singleton supports are disjoint when indexed by their distinct exponents.

Define \(U:\ell_1(S)\to\ell_2(\mathbb N_0)\oplus_2\ell_2(\mathbb N_0)\) by \(Ux=(A,B)\), where
\[
A_a=x(0^a),\qquad B_m=\sum_{\substack{a\ge0,\ 1\le b\le f(a)\\ f(a)-b=m}}x(0^a1^b).
\]
The sums converge absolutely, and each coordinate of \(x\) contributes to at most one of the coordinates of \((A,B)\). Thus \(\|Ux\|_2\le \|A\|_1+\|B\|_1\le\|x\|_1\). Define \(V\) from this Hilbert direct sum to \(\ell_\infty(S)\) by
\[
V(A,B)(v)=\sum_a A_a\mathbf1_{D_a}(v)+\sum_m B_m\mathbf1_{\{1^m\}}(v).
\]
At each \(v\) there is at most one nonzero term from each summand family, so \(\|V(A,B)\|_\infty\le \|A\|_2+\|B\|_2\le\sqrt2\|(A,B)\|_2\). The derivative formulas show \(H_{L_f}=VU\), which is weakly compact by reflexivity of the Hilbert space. Since the infinitely many nonempty \(D_a\) are disjoint, their indicators are mutually at norm distance one. This shows noncompactness and nonregularity, the latter by the characterization of regularity by finitely many distinct left derivatives.

For the comparison, \((H_{L_{\le}}e_{0^i})(1^j)=\mathbf1_{\{i\le j\}}\), the half-graph with distinct iterated limits and infinitely many distinct left derivatives. To see directly its quantitative obstruction, suppose a weakly compact \(R\) were at distance \(\delta<1/2\) from \(H_{L_{\le}}\). Then \(Re_{0^i}\) would have a weakly convergent subsequence with limit \(r\). At each fixed \(1^j\) the Boolean entries eventually vanish, so \(|r(1^j)|\le\delta\). A free-ultrafilter limit along the coordinates \(1^j\) is a bounded linear functional; it takes value at least \(1-\delta\) on each \(Re_{0^i}\), since for fixed \(i\) the entries at \(1^j\) are within \(\delta\) of one for all sufficiently large \(j\). Weak convergence forces the same lower bound at \(r\), a contradiction. The rank-one midpoint with all entries \(1/2\) gives the matching upper bound. Both languages are nonregular, so [1, Theorem 8.5] yields the stated approximation numbers.

## Verification

These are infinite-dimensional operator statements with direct analytic checks: the factorization follows from the disjoint derivative supports and norm bounds, noncompactness follows from separated columns, and the order-language comparison uses its literal half-graph. Finite matrix truncations are not used as evidence of weak compactness or its failure.

## Relationship to prior work and limitations

The distinct claim is the explicit norm-controlled Hilbert factorization for every injective-graph language and its use as an example separating the compact approximation profile from weak compactness. The approximation-number tail is already proved in [1, Section 8]. The order-language obstruction uses the classical Grothendieck double-limit phenomenon [2]. More generally the real Boolean-matrix half-gap is a consequence of standard weak-compactness calculus: an approximation within \(\delta<1/2\) can be thresholded continuously on its columns in \(C(\beta J)\), where \(J\) is the target coordinate set; continuous composition preserves relatively weakly compact column sets by Eberlein–Šmulian and dominated convergence, and the closed absolutely convex hull of those columns is weakly compact. No novelty is asserted for that general consequence. The later dated record [3] obtains weak compactness for a related diagonal family using a different factorization. Earlier equivalent examples in work on weakly almost periodic languages have not been ruled out.

## References

1. M. Hristov, A. Ilchev, D. Nedelcheva, B. Zlatanov, *Banach Spaces Generated by Finite-Valued Functions: Superreflexive Rigidity, Hankel Operators, and Universality*, [arXiv:2608.15185v1](https://arxiv.org/abs/2608.15185v1), Section 8.
2. A. Pillay, *Stability and Grothendieck*, [arXiv:1703.04761v2](https://arxiv.org/abs/1703.04761v2), p. 1, stating Grothendieck's double-limit criterion.
3. *Isometric c0 structure and strictly singular weakly compact Hankel operators*, [record 3c32a2f92305](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-isometric-c-0-structure-and-strictly-singular-weakly-compact-han--3c32a2f92305), 2026-10-25.
