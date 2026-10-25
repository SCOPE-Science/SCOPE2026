# Exact census and sharp rarity exponent for finite ultrahomogeneous unary maps

## Finding
Let \(u_n\) count the maps \(f:[n]\to[n]\) such that the structure with one unary operation \(f\) is ultrahomogeneous. Put \(u_0=1\). For integers \(k\ge1\) and a finite tuple \(\mathbf b=(b_0,\ldots,b_{h-1})\) of strictly positive integers, including the empty tuple when \(h=0\), define
\[
\ell_0=1,\qquad \ell_{j+1}=b_j\ell_j,\qquad
s(k,\mathbf b)=k\sum_{j=0}^{h}\ell_j,
\qquad a(k,\mathbf b)=k\prod_{j=0}^{h-1}(b_j!)^{k\ell_j}.
\]
Empty products equal one. The exact exponential generating function is
\[
\boxed{U(z)=\sum_{n\ge0}\frac{u_n}{n!}z^n
=\prod_{k\ge1}\left(1+\sum_{h\ge0}\ \sum_{\mathbf b\in\mathbb N_{>0}^{h}}
\left[\exp\left(\frac{z^{s(k,\mathbf b)}}{a(k,\mathbf b)}\right)-1\right]\right).}
\]
This infinite product and its inner sums are **formal, coefficientwise locally finite**. In addition,
\[
\boxed{u_n=n!\exp(o(n)),\qquad
\Pr_{f\text{ uniform on }[n]^{[n]}}(f\text{ ultrahomogeneous})
=\frac{u_n}{n^n}=\exp(-n+o(n)).}
\]
Thus the exact logarithmic large-deviation rate is \(-1\). The first positive-size counts, in order from \(n=1\) to \(n=12\), are
\[
1,4,15,100,575,5526,43967,511064,5396967,73824130,928413959,15140851452.
\]

## Assumptions and scope
A monounary algebra on the fixed labelled carrier \([n]=\{1,\ldots,n\}\) is a single function \(f:[n]\to[n]\). A subalgebra is closed under forward iteration. **Ultrahomogeneous** means every isomorphism between finitely generated subalgebras extends to an automorphism of the whole algebra. Labelled functions, not isomorphism types, are counted; no assumption of injectivity or absence of fixed points is made. The empty function contributes the constant term by enumerative convention.

In a finite functional digraph every connected component has one directed cycle. The parameter \(k\) is its cycle length; at distance \(j+1\) from each cycle vertex, every vertex at distance \(j\) has exactly \(b_j\) immediate noncycle predecessors, and the height is \(h\). The empty tuple corresponds to a bare directed cycle. Different cycle lengths may carry different branching profiles, but all components having the same cycle length must have the **same** profile in an ultrahomogeneous unary algebra. This last global restriction is essential to the product formula.

## Proof
**1. Structural input.** Quinn-Gregson's classification of ultrahomogeneous monounary algebras (Theorems 4.7, 4.9 and 4.10 of reference 1) implies the following finite specialization. For any fixed cycle length \(k\), either no component has a \(k\)-cycle, or all components with \(k\)-cycles are copies of one connected structure with a finite sequence \(\mathbf b\) of positive, levelwise-uniform predecessor counts. Conversely every finite disjoint union obeying this condition is ultrahomogeneous. Components of distinct cycle lengths are distinguishable by their singly generated subalgebras and can be chosen independently. The cycle-free alternative of the source classification cannot occur in a nonempty finite mapping.

**2. Component size and automorphisms.** Each of the \(k\) cycle vertices has \(\ell_j\) vertices at depth \(j\), giving \(s=k\sum_{j=0}^{h}\ell_j\). An automorphism of a connected component rotates its directed cycle in exactly \(k\) possible ways. After fixing its action on the cycle, for each of the \(k\ell_j\) vertices at depth \(j\), its \(b_j\) indistinguishable immediate children can be permuted arbitrarily, independently and recursively. Hence the component's full automorphism group has order
\[
|\operatorname{Aut}(k,\mathbf b)|=k\prod_{j=0}^{h-1}(b_j!)^{k\ell_j}=a(k,\mathbf b).
\]
There are therefore \(s!/a\) labelled realizations of this connected structure on a specified \(s\)-point carrier, giving connected exponential generating monomial \(z^s/a\). A set of exactly \(m\ge1\) indistinguishable copies has contribution \(z^{ms}/(m!a^m)\), so a nonempty set of copies contributes \(\exp(z^s/a)-1\).

**3. Exact product.** For each \(k\), one must choose either no components or one profile \(\mathbf b\) with a positive multiplicity. Its generating function is consequently
\[
1+\sum_{\mathbf b}\left(\exp(z^{s(k,\mathbf b)}/a(k,\mathbf b))-1\right).
\]
Multiplying these factors over independent cycle lengths establishes the displayed formula. For every \(n\), a term of degree at most \(n\) requires \(k\le n\), \(h<n\), and all \(b_j\le n\), so no coefficient involves infinitely many summands.

**4. Upper bound at every point inside the unit disc.** Write \(c_n=u_n/n!\). Forgetting the rule that only one profile may be used for each fixed cycle length enlarges the labelled class coefficientwise. The resulting unrestricted set of connected profiles has exponential generating function \(\exp(C(z))\), where
\[
C(z)=\sum_{k\ge1}\sum_{\mathbf b}\frac{z^{s(k,\mathbf b)}}{a(k,\mathbf b)}.
\]
For a fixed positive component size \(m\), each profile is uniquely encoded by the sequence of depth-level sizes
\[
(k,\ k\ell_1,\ldots,\ k\ell_h).
\]
It is a nondecreasing sequence of positive integers summing to \(m\), hence an integer partition of \(m\). The encoding is injective because its first term recovers \(k\) and each consecutive ratio recovers the corresponding branching factor. Thus at most \(p(m)\) connected profiles have size \(m\), where \(p(m)\) is the integer partition number. Since every \(a(k,\mathbf b)\ge1\), coefficientwise
\[
0\le U(z)\preceq\exp(C(z))\preceq
\exp\left(\sum_{m\ge1}p(m)z^m\right)
=\exp\left(\prod_{j\ge1}(1-z^j)^{-1}-1\right).
\]
For any fixed real \(0<r<1\), the expression on the right has finite value, say \(K_r\). Positivity of coefficients then yields \(c_n r^n\le K_r\), so
\[
\limsup_{n\to\infty}\frac{1}{n}\log c_n\le-\log r.
\]
Letting \(r\uparrow1\) gives an upper bound of zero.

**5. Matching lower bound and density.** Every permutation of \([n]\) is ultrahomogeneous: its components are directed cycles, and any isomorphism of finitely generated subalgebras extends by permuting cycles of matching lengths and rotating each cycle. Hence \(u_n\ge n!\), so \(c_n\ge1\) for all \(n\ge1\). Together with step 4,
\[
\lim_{n\to\infty}\frac{1}{n}\log\left(\frac{u_n}{n!}\right)=0.
\]
There are exactly \(n^n\) maps \([n]\to[n]\). Stirling's formula \(\log(n!)-n\log n=-n+o(n)\) gives
\[
\lim_{n\to\infty}\frac1n\log\frac{u_n}{n^n}=-1,
\]
as asserted. No assertion about the prefactor or an asymptotic equivalent finer than the exponential scale is made.

## Verification
The standalone `verify.py` implements the formal product using exact rational coefficients through order twelve. Independently, for each \(n\in\{1,2,3,4,5,6\}\), it enumerates all \(n^n\) maps and applies the direct one-generated criterion of Quinn-Gregson's Theorem 4.7, checking that points with the same eventual cycle length and height have the same predecessor degree. The two enumerations agree exactly. The checker prints `UH_ENUMERATION_OK`. These finite computations are not substituted for the general proof or the classification input.

## Relationship to prior work
Quinn-Gregson (reference 1), publicly available from 27 March 2026, establishes the structural classification of ultrahomogeneous monounary algebras. That classification is explicitly used as a premise: this finding does not re-prove it and does not claim its structural consequences as new. The additional claims concern an exact weighted labelled census and the sharp exponential rarity rate, which are not stated in the inspected source's classification and counting sections.

Liao (reference 2) extends the discussion to several unary operations and proves an oligomorphicity criterion for tree-like algebras; its finite counterexample and Proposition 3.9 concern different claims and give no labelled unary-map density. The related published enumeration **“Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras”** treats a different extension property, yielding the initial counts \(1,4,27,232,2285,\ldots\) for positive sizes and an exponential growth factor strictly greater than one relative to \(n!\). In contrast, the present ultrahomogeneous counts begin \(1,4,15,100,575,\ldots\) and have subexponential growth relative to \(n!\). Neither exact formula or asymptotic statement implies the other through the available classifications.

## Limitations
The result is conditional on the published structural classification of ultrahomogeneous monounary algebras; it does not independently certify that classification. The count is for one unary function on a labelled finite carrier, not a relational reduct, multiple unary functions, unlabeled isomorphism types, or polymorphism-homogeneity. The asymptotic gives only the logarithmic rate, not a sharp multiplicative constant. Search and comparison of related literature cannot exclude a prior equivalent enumeration under different terminology. Independent scientific review has not been conducted.

## References
1. T. Quinn-Gregson, “Ultrahomogeneity and \(\omega\)-categoricity of monounary algebras,” arXiv:2603.26616v1 (first submitted 27 March 2026), Sections 3–4, especially Theorems 4.7, 4.9 and 4.10. https://arxiv.org/html/2603.26616v1
2. C. Liao, “A note on ultrahomogeneous unary algebras,” arXiv:2607.02725 (first submitted 2 July 2026), Sections 2–3 and Proposition 3.9. https://arxiv.org/abs/2607.02725
3. “Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras,” publicly available mathematical finding, exact finite counts and EGF for a distinct homogeneity property.
