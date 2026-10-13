# Degree-factorization of the strong-odd coloring polynomial of forests

## Finding

For any finite simple forest \(F\) and integer \(q\ge 2\), let \(SO_F(q)\) count all **proper strong-odd** vertex colorings \(\varphi:V(F)\to\{1,\ldots,q\}\), allowing unused palette colors. A coloring is strong-odd if, for each vertex \(v\), every color represented in the open neighborhood \(N_F(v)\) is represented an odd number of times. Isolated vertices satisfy this condition vacuously.

For positive integers \(d\), put
\[
f_d(q)=(d-1)!\,[z^{d-1}]\cosh(z)\bigl(1+\sinh(z)\bigr)^{q-2}.
\]
Write \(s(F)\) for the number of isolated vertices and \(c_+(F)\) for the number of connected components containing an edge. **The exact strong-odd counting formula is**
\[
SO_F(q)=q^{s(F)}\bigl(q(q-1)\bigr)^{c_+(F)}\prod_{v:\,\deg_F(v)\ge1} f_{\deg_F(v)}(q).
\]
In particular, **the complete strong-odd coloring polynomial of a forest depends only on its multiset of vertex degrees**, even when the forests are not isomorphic. For every tree \(T\) having at least one edge, the exact count of named-palette three-colorings simplifies to
\[
SO_T(3)=6\prod_{v:\,\deg_T(v)\text{ even}}2^{\deg_T(v)-2}.
\]
At \(q=2\), the formula returns two colorings of each nontrivial tree with all degrees odd and zero otherwise, consistent with the previously known minimum-color theorem.

## Assumptions and scope

All graphs are finite, simple, and undirected; the statement covers disconnected forests and empty graphs. The palette is the specified set of \(q\) **named** colors and a coloring need not use every color. The coefficient-extraction notation \([z^k]\) means the coefficient of \(z^k\) in a formal power series with rational coefficients. In the formula, \(f_d(q)\) is a nonnegative integer for each integer \(q\ge2\), and each component with an edge has at least two vertices. For an edgeless forest of \(s\) vertices the product and component factors are empty, giving \(SO_F(q)=q^s\). For the empty forest the count is one. No claim is made for graphs containing cycles.

The factor is polynomial in the palette variable: to extract the coefficient of \(z^{d-1}\), only terms of bounded degree are needed, and \(\binom{q-2}{j}\) is polynomial in \(q\). Thus the displayed identity for all integers \(q\ge2\) determines a genuine counting polynomial.

## Proof

Consider a tree component \(T\) with an edge. Fix an arbitrary edge \(ab\), and regard \(a\) and \(b\) as two roots connected by the designated edge. Direct every other tree edge away from this pair. Choose distinct colors on \(a\) and \(b\); there are exactly \(q(q-1)\) choices, with properness on their shared edge.

Each vertex \(v\) now has exactly one **designated predecessor neighbor**: its partner across \(ab\) if \(v\in\{a,b\}\), and its parent otherwise. The colors of \(v\) and this predecessor have already been fixed and are distinct whenever the yet uncolored children of \(v\) are reached. There are exactly \(d-1\) such children if \(\deg_T(v)=d\).

Properness forbids the children from using the color of \(v\), but imposes no restrictions among different children. The predecessor's color already occurs **once** in \(N_T(v)\), so this same color must appear an **even** additional number of times among the children. Every one of the other \(q-2\) eligible palette colors must appear either zero or an **odd** number of times. The labeled-child exponential generating function is accordingly \(\cosh(z)(1+\sinh(z))^{q-2}\); multiplying its coefficient of \(z^{d-1}\) by \((d-1)!\) gives precisely \(f_d(q)\).

These choices depend only on \(d\) and \(q\), not on the identities of the two fixed colors. The children of different vertices are disjoint, and tree acyclicity ensures that every vertex other than the two roots is colored exactly once by its parent. Thus each choice in the product produces a unique proper strong-odd coloring, and conversely each such coloring has exactly this unique decomposition. The number on \(T\) is \(q(q-1)\prod_{v\in V(T)} f_{\deg_T(v)}(q)\). Multiply over components, with an independent factor \(q\) per isolated vertex, proving the identity.

For \(q=3\), the local generating function is
\[
\cosh(z)\bigl(1+\sinh(z)\bigr)=\cosh(z)+\tfrac12\sinh(2z).
\]
It follows that \(f_d(3)=1\) if \(d\) is odd, and \(f_d(3)=2^{d-2}\) if \(d\) is even; substitution gives the three-color count. For \(q=2\), \(f_d(2)=(d-1)![z^{d-1}]\cosh(z)\) equals one for odd \(d\) and zero for even \(d\). Finally, the entire right side depends only on the multiset of degrees, completing the structural consequence.

## Verification

The supplied standalone Python 3 file `verify.py` uses no external dependencies. Run `python3 verify.py` to recompute the checks. It enumerates proper color assignments directly, tests each actual open-neighborhood multiplicity, and compares against the degree-product formula; separately it compares the local-factor finite sum against exact rational formal-series coefficients and checks the three-color closed form.

One completed execution returned `VERIFY_OK`, with **4,516 direct brute-force versus product comparisons**, across every labeled tree of orders two through six for the included palettes and selected larger trees through order nine; **297,098 accepted color assignments** were counted across those comparisons. The three-color simplification was additionally checked for all **18,248 labeled trees of orders two through seven**. The finite checks corroborate rather than replace the all-order bijective proof.

## Relationship to prior work

Kwon and Park introduced proper strong-odd coloring in the first public version of arXiv:2401.11653 (2024-01-22), classified under MSC 05C15. Caro, Petruševski, Škrekovski and Tuza, in arXiv:2410.02336v1 (2024-10-03), prove in Proposition 2.1 that each tree admits a strong-odd coloring with at most three colors, and characterize exactly when two colors suffice. Their result is a **minimum-color existence theorem** and a linear-time construction; it neither gives the number of colorings with a prescribed palette nor forces a degree-multiset factorization. The later arXiv:2610.01441v1 establishes a minimum-color algorithm for block graphs, encompassing trees but still not an all-coloring enumerator. This result adds the full all-palette enumeration, with the older chromatic-number statements recovered only as consequences.

## Limitations

Only acyclic graphs are treated; the proof relies on uniquely assigning each nonroot vertex to a preceding neighbor. The counting polynomial uses named colors and includes unused colors, so it should not be confused with counts of colorings up to color permutation. The literature comparison cannot establish absolute priority against every unindexed or inaccessible publication. Independent audit has not been performed; all finite verification is computational corroboration of a symbolic argument.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653v1 (first publicly submitted 2024-01-22), https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1 (first publicly submitted 2024-10-03), https://arxiv.org/abs/2410.02336; published in Discrete Mathematics 348 (2025), article 114601.
3. *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441v1 (2026-10-01), https://arxiv.org/abs/2610.01441.
