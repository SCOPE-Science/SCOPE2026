# Exact one-deletion shadow profiles of additive multiset syndrome codes

## Finding

Fix a finite abelian group \(G\) of order \(q\ge2\), written additively, and a positive integer \(n\). Let \(\mathcal X_n(G)\) consist of all multiplicity vectors \(x=(x_g)_{g\in G}\) with nonnegative integer entries and \(\sum_g x_g=n\). The additive syndrome and support number are
\[
 s(x)=\sum_{g\in G}x_g g,\qquad r(x)=|\{g:x_g>0\}|.
\]
The syndrome class \(C_a(n)=\{x\in\mathcal X_n(G):s(x)=a\}\) corrects one multiset deletion. Its **complete one-deletion shadow profile** is
\[
 W_{a,n}(u)=\sum_{x\in C_a(n)}u^{r(x)}.
\]
The coefficient of \(u^r\) is the exact number of codewords with \(r\) distinct one-deletion outputs.

**Theorem (complete character-order profile).** Let \(E\) be the exponent of \(G\), and write \(\widehat G\) for its character group. For each positive divisor \(d\) of \(E\) set
\[
 R_d(a)=\sum_{\substack{\chi\in\widehat G\\ \operatorname{ord}\chi=d}}\chi(-a).
\]
Then for every \(a\in G\) and \(n\ge1\),
\[
 \boxed{W_{a,n}(u)=\frac1q\sum_{d\mid\gcd(n,E)}R_d(a)Q_{d,q/d,n/d}(u)},
\]
where \(R_d(a)\) is an integer and the fully explicit polynomial is
\[
 Q_{d,h,k}(u)=\sum_{j=0}^{\min(h,k)}(-1)^j\binom hj\binom{h+k-j-1}{h-1}(1-u)^{dj}.
\]
If \(G\cong\prod_{i=1}^s\mathbb Z/m_i\mathbb Z\) and \(a=(a_i)\), no complex arithmetic is needed:
\[
 \boxed{R_d(a)=\sum_{e\mid d}\mu(d/e)\!\left(\prod_{i=1}^s\gcd(e,m_i)\right)\!\mathbf1_{\,\gcd(e,m_i)\mid a_i\ \forall i}.}
\]
Here \(\mu\) is the ordinary Möbius function. In particular, **the support profile is independent of the syndrome for all \(a\) if and only if \(\gcd(n,E)=1\)**.

For a prime-sized alphabet \(G=\mathbb Z/p\mathbb Z\), the preceding classification collapses to exactly one profile when \(p\nmid n\), and exactly two profiles when \(p\mid n\). More precisely, for \(1\le r\le\min(p,n)\),
\[
 \boxed{[u^r]W_{a,n}(u)=\frac{\binom pr}{p}\left(\binom{n-1}{r-1}+\mathbf1_{p\mid n}\,\varepsilon_a(-1)^{r-1}\right),}
\]
where \(\varepsilon_0=p-1\) and \(\varepsilon_a=-1\) for \(a\ne0\). This is a coefficientwise, not merely total-cardinality, balance law.

Every class has the same total shadow occupancy,
\[
 \boxed{\sum_{x\in C_a(n)}r(x)=W'_{a,n}(1)=\binom{n+q-2}{q-1}.}
\]
Further, in the graph joining two distinct size-\(n\) multisets whenever one symbol is replaced by a different one, **every pair of distinct syndrome classes has exactly** \(\binom{n+q-2}{q-1}\) **connecting edges**, and the number of neighbors in another fixed class of a vertex \(x\) is precisely \(r(x)\). Thus the polynomial simultaneously records the inter-class transfer-degree distribution.

## Assumptions and scope

All groups are finite abelian groups, not necessarily cyclic. The alphabet is the entire group \(G\), with each group element used once as a distinct symbol label. The group is written additively; the composition entries are ordinary nonnegative integers. The syndrome classes are not ordinary linear codes over a finite field, and \(r(x)\) measures deletion-shadow size, not a Hamming distance. The theorem includes \(n=1\), groups of composite order, and arbitrary syndrome labels. It does not assert analogous formulas for a nonbijective map from an alphabet into a larger syndrome group or for multiple deletions.

For every \(n\ge1\) and \(q\ge2\), the number of received multisets of size \(n-1\) is \(B=\binom{n+q-2}{q-1}\).

## Proof

**1. Deletion shadows.** Deleting one occurrence of symbol \(g\) from \(x\) gives \(x-e_g\); this operation is possible exactly when \(x_g>0\), and different occupied labels give different outputs. Thus the number of distinct deletion outputs is \(r(x)\). Given any received \(y\in\mathcal X_{n-1}(G)\) and target syndrome \(a\), there is exactly one parent in \(C_a(n)\), namely \(y+e_{a-s(y)}\), since the label set is the full group. Therefore the shadows of \(C_a(n)\) form an exact partition of \(\mathcal X_{n-1}(G)\); in particular, \(\sum_{x\in C_a(n)}r(x)=B\). This is a **one-sided deletion-shadow partition**, not a claim about metric-perfect balls in the discrete simplex.

**2. Character filter.** For \(\chi\in\widehat G\), each coordinate \(g\) contributes the formal power series
\[
 1+u\sum_{m\ge1}(\chi(g)z)^m=\frac{1-(1-u)\chi(g)z}{1-\chi(g)z}.
\]
Consequently the generating series weighted by \(\chi(s(x))\) and by the support number is
\[
 F_\chi(z,u)=\prod_{g\in G}\frac{1-(1-u)\chi(g)z}{1-\chi(g)z}.
\]
If the order of \(\chi\) is \(d\), its image consists of all \(d\)-th roots of unity, each attained by exactly \(q/d\) group elements. Multiplying the corresponding cyclotomic products gives the identity of formal power series
\[
 F_\chi(z,u)=\left(\frac{1-(1-u)^dz^d}{1-z^d}\right)^{q/d}.
\]
Character orthogonality on \(G\) yields
\[
 W_{a,n}(u)=\frac1q\sum_{\chi\in\widehat G}\chi(-a)[z^n]F_\chi(z,u).
\]
Only orders \(d\) dividing \(n\) can contribute. For \(h=q/d\) and \(k=n/d\), expand the numerator by the binomial theorem and the denominator by the negative-binomial series:
\[
 [t^k]\left(\frac{1-(1-u)^dt}{1-t}\right)^h
 =\sum_{j=0}^{\min(h,k)}(-1)^j\binom hj\binom{h+k-j-1}{h-1}(1-u)^{dj}.
\]
Collecting characters of order \(d\) proves the stated formula for \(W_{a,n}\).

**3. Integral character-order coefficients.** By Möbius inversion in the divisor lattice,
\[
 R_d(a)=\sum_{e\mid d}\mu(d/e)\sum_{\chi^e=1}\chi(-a).
\]
The characters with \(\chi^e=1\) annihilate \(eG\). Their sum at \(-a\) equals \(|G[e]|\) when \(a\in eG\), and zero otherwise, by finite-group orthogonality. For \(G\cong\prod_i\mathbb Z/m_i\mathbb Z\), one has \(|G[e]|=\prod_i\gcd(e,m_i)\), and membership in \(eG\) is equivalent to \(\gcd(e,m_i)\mid a_i\) for every \(i\). This proves the integral formula, including repeated-prime and noncyclic cases.

**4. Exact criterion for coefficientwise balance.** If \(\gcd(n,E)=1\), multiplication by \(n\) is a bijection on \(G\). Relabeling each alphabet symbol by the translate \(g\mapsto g+b\) preserves \(r(x)\) and shifts \(s(x)\) by \(nb\), so it acts transitively on all syndrome classes and preserves their complete profiles. Conversely, if \(\gcd(n,E)>1\), the homomorphism \(g\mapsto ng\) has a nontrivial kernel and proper image. Support-one vectors are exactly \(ne_g\): the coefficient of \(u\) in \(W_{a,n}\) is \(|\ker(n:G\to G)|\) when \(a\in nG\), and zero otherwise. Hence the profiles cannot all be equal. This proves the claimed if-and-only-if, not just a sufficient condition.

**5. The prime two-profile specialization.** When \(G=\mathbb Z/p\mathbb Z\), the trivial character of order one contributes the total support enumerator
\[
 \sum_{r=1}^{\min(p,n)}\binom pr\binom{n-1}{r-1}u^r.
\]
Every nontrivial character has order \(p\) and therefore contributes zero unless \(p\mid n\). If \(p\mid n\), its length-\(n\) coefficient is \(1-(1-u)^p\), with coefficient \((-1)^{r-1}\binom pr\) at positive degree \(r\). The sum over nontrivial characters is \(p-1\) at syndrome zero and \(-1\) otherwise. Division by \(p\) gives the asserted formula, with all coefficients exact integers.

**6. Transfer neighbors.** Fix distinct target syndromes \(a,b\) and set \(t=b-a\ne0\). For each occupied \(g\) of \(x\in C_a(n)\), form \(x-e_g+e_{g+t}\), which lies in \(C_b(n)\). The \(r(x)\) resulting neighbors are distinct: equality of two replacements with the same nonzero shift \(t\) would equate distinct directed unit-transfer vectors, which is impossible. Conversely, any one-symbol replacement reaching \(C_b(n)\) must replace some \(g\) by \(g+t\). Thus the degree of \(x\) into \(C_b(n)\) is exactly \(r(x)\); summing degrees over the source class and using step 1 proves that every pair of distinct classes has \(B\) connecting edges.

## Verification

A standard-library-only Python verifier, `support_spectrum_check.py`, directly enumerates multiplicity vectors and syndrome/support profiles, calculates the predicted profile independently from the explicit integer Möbius/order formula, and checks the prime specialization and the balance criterion. It covers 100 group-length settings across cyclic groups and noncyclic products, with 27,824 enumerated vectors. In 15 additional settings it constructs one-symbol transfer neighbors and verifies their distinctness, syndrome targets and aggregate edge count. Exact integer equality passes throughout; recorded output is in `support_spectrum_check.out`. These finite computations corroborate the theorem but are not an exhaustive proof for unbounded \(n\) or arbitrary groups; the preceding character-theoretic argument supplies that proof.

Two exact illustrations:

* For \(G=\mathbb Z/5\mathbb Z\) and \(n=5\), \(W_{0,5}(u)=5u+20u^3+u^5\), while each nonzero syndrome has \(W_{a,5}(u)=10u^2+10u^3+5u^4\). All five classes have the same total shadow occupancy \(W'_{a,5}(1)=70\), although their size and support profiles differ.
* For \(q=n=4\), cyclic \(G=\mathbb Z/4\mathbb Z\) has three profile types: \(4u+2u^2+4u^3\), \(4u^2+4u^3\), and \(8u^2+u^4\). The Klein group \(G=(\mathbb Z/2\mathbb Z)^2\), despite the same alphabet size, instead has only two: \(4u+6u^2+u^4\) and \(4u^2+4u^3\). This shows that the group structure, rather than alphabet size alone, can govern the distribution.

## Relationship to prior work

Kreindel, Essayag and Zabokritskiy's 2026 *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results* defines the single-deletion sum-modulo construction (Section 5.1) and derives syndrome **cardinalities** by an unweighted character filter (Proposition 14 and Appendix B). Its Proposition 16 and Appendix C explicitly treat the **support size** as the number of distinct one-deletion outputs and use the unrestricted counts \(\binom qr\binom{n-1}{r-1}\) in a shadow-packing bound. Those statements motivate the missing *syndrome-conditioned* distribution, but the inspected text does not determine its coefficientwise profile, its exact balance criterion, or its group-sensitive character-order formula. The present theorem keeps the support-size variable through Fourier filtering; setting \(u=1\) recovers the known cardinalities. The sum-modulo construction and its correctness are prior art, not new claims.

Kreindel, Essayag and Zabokritskiy's March 2026 *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes* develops different polynomial-syndrome constructions and counts **same-length metric-ball** volumes and pair distances in the whole multiset simplex (Sections 3–4). It does not, in the inspected sections and enumerators, condition the *one-sided deletion-shadow* size on the full-group additive syndrome. General polynomial-code alphabet-to-group maps need not be bijections, and are outside the theorem's hypotheses.

Kovačević and Tan's foundational *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments* studies geometric deletion bounds; Theorem 17 uses the number of nonzero multiplicity coordinates and the unrestricted count of each support size, but does not provide a class-by-class additive-syndrome support enumerator. The derivation also uses standard finite-abelian character orthogonality and elementary Möbius inversion; novelty is not claimed for these tools individually.

## Limitations

No finite-length optimality of the additive-syndrome classes among *all* one-deletion codes is claimed. The profile determines exact branching and shadow occupancy of these specific code classes, not the performance of an arbitrary nonlinear multiset code. No formula for two or more deletions or for alphabet labels not bijectively identified with the syndrome group is proved. The equal inter-class edge count concerns one-symbol replacements, not an equitable partition with constant vertex degree. No improvement in rate, error correction radius, or decoding complexity is asserted. An implicit equivalent profile could exist in older enumerative/cyclotomic literature; independent priority and mathematical audit remain outstanding.

## References

1. A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first publicly submitted 2026-01-09; Sections 5.1, Appendix B, Appendix C. https://arxiv.org/html/2601.05636v2
2. A. Kreindel, I. B. Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1, first publicly submitted 2026-03-18; Sections 2–4. https://arxiv.org/abs/2603.18322
3. V. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837, 2016; in particular Lemma 3 and Theorem 17. https://arxiv.org/abs/1612.08837
