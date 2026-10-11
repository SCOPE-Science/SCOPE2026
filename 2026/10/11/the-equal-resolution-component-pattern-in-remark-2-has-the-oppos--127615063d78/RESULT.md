# The equal-resolution component pattern in Remark 2 has the opposite sign

## Finding
For an ordinary unoriented skein triple \(L,L_0,L_1\), obtained by replacing the local crossing/tangle connection of four boundary points by the other two pairings, there is an integer \(c\) such that the three component counts have multiset
\[
\{c,c,c+1\}.
\]
Consequently the hypothesis
\[
|L_0|=|L_1|=|L|+1
\]
printed in Remark 2 of Huang, arXiv:2609.38117v1, cannot occur. If the two resolutions have equal component count, then necessarily
\[
|L_0|=|L_1|=|L|-1.
\]

There is an independent rank check. After localization, Hendricks--Lipshitz--Sarkar identify the equivariant Floer group of a link with \(d\) components as a free module of rank \(2^{d-1}\). Under the printed plus-one hypothesis, the localized exact sequence of Huang's Theorem 1.3 would therefore have consecutive ranks
\[
r,\ 2r,\ 2r,\ r.
\]
Remark 2 also says that the middle map is zero. Exactness would then force a surjection from rank \(r\) to rank \(2r\), and simultaneously an injection from rank \(2r\) to rank \(r\), which is impossible after passage to the fraction field. Under the only possible equal-resolution pattern, the ranks instead have the dimensionally compatible form
\[
2r,\ r,\ r,\ 2r.
\]

Thus the source-specific component-count condition in Remark 2 has the opposite sign from the realizable equal-resolution pattern. This statement does not assert that replacing \(+1\) by \(-1\) by itself proves every localized map formula in that remark.
## Assumptions and scope
The statement concerns the ordinary unoriented skein move used in Huang's Theorems 1.2 and 1.3: outside a small three-ball the link is fixed, while inside the ball the three local pictures connect the same four boundary points in the three possible pairings. The notation \(|L|\) denotes the number of link components, as in the localization formula quoted in the source.

No orientation assumption is needed for the component-count argument. Closed components lying entirely outside the skein ball are allowed and simply contribute the same additive constant to all three counts.

The second part uses only the localized free rank supplied by Hendricks--Lipshitz--Sarkar and exactness of Huang's sequence. It is a consistency check, not a reconstruction of the cobordism maps.
## Proof
Remove the skein ball. The portion of the link outside the ball is a compact one-manifold with four boundary points together with possibly some closed components. Its two interval components pair the four boundary points; call this perfect matching \(O\). Let \(P\) be one of the three possible local pairings placed back inside the ball.

Consider the graph on the four boundary points whose edges are the two pairs of \(O\) together with the two pairs of \(P\). If \(P=O\), this graph is the disjoint union of two doubled edges, so the part of the closed link meeting the ball has two components. If \(P\ne O\), the union of the two distinct perfect matchings is a single four-cycle, so the part meeting the ball has one component.

Exactly one of the three local pairings equals \(O\). Hence exactly one of the three closed links has one more component than the other two. Adding the fixed number of closed components disjoint from the ball gives the multiset \(\{c,c,c+1\}\).

The two resolutions \(L_0\) and \(L_1\) correspond to distinct local pairings. If they have the same number of components, neither can be the unique pairing equal to \(O\). Therefore the remaining local picture \(L\) is the unique larger closure, and
\[
|L_0|=|L_1|=|L|-1.
\]
This proves the topological assertion and shows that the printed plus-one condition is empty.

For the rank check, localize further to a field if necessary. Hendricks--Lipshitz--Sarkar Proposition 6.3 gives localized rank \(2^{|J|-1}\) for a link \(J\). Under the printed hypothesis, write \(r=2^{|L|-1}\). Huang's exact sequence would have ranks \(r,2r,2r,r\), while Remark 2 declares the middle map zero. Exactness at the first rank-\(2r\) term forces the preceding rank-\(r\) map to be surjective, impossible by dimension. Exactness at the second rank-\(2r\) term likewise forces the following map into rank \(r\) to be injective. This independently detects the same sign inconsistency.
## Verification
The component-count proof is exhaustive because there are exactly three perfect matchings on four labeled boundary points. For a fixed outside matching, one local matching is equal to it and the other two are distinct from it; their unions are respectively two two-cycles and one four-cycle. No finite experiment is used to infer a general case.

The primary full text was checked at Theorems 1.2 and 1.3 and Remark 2. Theorem 1.2 specifies the ordinary unoriented \(0\)- and \(1\)-resolutions in a three-ball. Theorem 1.3 gives the exact sequence in the order \(L\to L_1\to L_0\to L\). Remark 2 prints \(|L_0|=|L_1|=|L|+1\) and states that the localized \(L_1\to L_0\) map is zero.

The Hendricks--Lipshitz--Sarkar full text was checked at Proposition 6.3, which supplies the localized rank \(2^{d-1}\) for a \(d\)-component based link, and at Lemma 6.11, the lemma cited by Huang for localized cobordism maps.
## Relationship to prior work
Huang's arXiv:2609.38117v1 proves an equivariant Floer exact triangle and gives the component-count hypothesis in Remark 2. The paper does not note that the displayed plus-one condition is incompatible with the elementary topology of the three local pairings. Its own localization formula also supplies the rank data used in the independent consistency check.

Hendricks--Lipshitz--Sarkar develop the localization theorem and describe localized cobordism maps. Their results imply the rank constraint used above, but they predate Huang's remark and do not state the source-specific vacuity or sign correction.

Targeted searches for the exact arXiv identifier together with “Remark 2,” the printed component-count equation, skein component-count aliases, and localized-rank formulations located no published statement identifying this particular hypothesis as empty. The mathematical pairing lemma itself is elementary and standard in spirit; the original content assessed here is the precise consequence for this newly stated hypothesis and its localized exact-sequence consistency.
## Limitations
The finding concerns Remark 2 as written in arXiv:2609.38117v1. It does not challenge Huang's main exact-triangle or spectral-sequence theorems. It does not assert the author's intended sign, although \(-1\) is the only realizable sign when the two resolutions have equal component count and is dimensionally compatible with the stated localized vanishing.

The argument does not independently prove the two explicit localized map descriptions or the vanishing map after replacing \(+1\) by \(-1\). A later revision may correct the remark. An unindexed contemporaneous note or informal communication could also have observed the same source-specific issue.
## References
1. J. Huang, *Exact triangle and Spectral sequence of the equivariant Floer homology of double branched covers*, arXiv:2609.38117v1, first submitted 2026-09-29; Theorems 1.2--1.3 and Remark 2.
2. K. Hendricks, R. Lipshitz, and S. Sarkar, *A flexible construction of equivariant Floer homology and applications*, arXiv:1510.02449v2; J. Topol. 9 (2016), 1153--1236; Proposition 6.3 and Lemma 6.11.
