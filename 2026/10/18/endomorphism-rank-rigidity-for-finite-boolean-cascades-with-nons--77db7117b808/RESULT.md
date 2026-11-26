# Image ranks of retractions of finite Boolean cascades

## Finding

Let \(P=A_1\oplus\cdots\oplus A_h\) be an ordinal sum of disjoint antichains, with \(h\ge2\) and \(n_i=|A_i|\ge2\). In the finite Heyting algebra \(H=\operatorname{Up}(P)\), let \(\Phi\) range over the idempotent endomorphisms. Its rank here is the cardinality of \(\Phi[H]\), not the number of points in the image of its dual map. Then
\[
\sum_{\Phi^2=\Phi} z^{|\Phi[H]|}=
\sum_{r=1}^{n_1}\binom{n_1}{r}r^{n_1-r}z^{2^r+\sum_{i=2}^h(2^{n_i}-1)}
+\sum_{j=2}^h n_j z^{2+\sum_{i=j+1}^h(2^{n_i}-1)}.
\]
All displayed exponents are distinct. More precisely, for each specified nonempty subset \(C\subseteq A_1\) of size \(r\), there are \(r^{n_1-r}\) idempotent endomorphisms whose dual map has image \(C\cup A_2\cup\cdots\cup A_h\). For each \(2\le j\le h\) and \(c\in A_j\), exactly one has dual image \(\{c\}\cup A_{j+1}\cup\cdots\cup A_h\). There are no other dual images of idempotent endomorphisms.

## Assumptions and scope

The elements of each antichain are distinguished. The Heyting operations are intersection, union, the two named bounds and implication, given by \(U\to V=\{x:\uparrow x\cap U\subseteq V\}\). A retraction here means an idempotent endomorphism, equivalently a homomorphism onto its image that fixes its image. Its dual map is an Esakia bounded morphism. The nonsingleton assumption is used in the proof and no analogous census is asserted with singleton levels.

## Proof

By finite Esakia duality [1], the endomorphisms of \(H\) are exactly the inverse-image maps of the unique self-maps \(f\) of \(P\) satisfying
\[
f(\uparrow x)=\uparrow f(x)\qquad(x\in P).
\]
The equation implies monotonicity. The equivalence with preservation of implication can also be checked pointwise: if a point \(y\ge f(x)\) is missing from \(f(\uparrow x)\), the upsets \(U=\uparrow y\), \(V=U\setminus\{y\}\) witness failure of preservation at \(x\); conversely the equation identifies the two inclusion tests for implication. By uniqueness, idempotence is precisely \(f^2=f\), which means \(f\) fixes every element of its image.

Let \(j\) be the first occupied level of \(S=f(P)\) and put \(C=S\cap A_j\). The bounded-morphism equation makes \(S\) an upset, so it contains every point above level \(j\). These points are all fixed. If \(x\in A_j\) mapped to a point of some \(A_k\), \(k>j\), then \(f(\uparrow x)\) would contain all of \(A_k\), since \(\uparrow x\) contains \(A_k\) and \(A_k\) is fixed. In contrast, \(\uparrow f(x)\) contains only \(f(x)\) in \(A_k\), contradicting \(n_k\ge2\). Hence \(f(A_j)\subseteq C\), with \(C\) fixed.

For \(j=1\), each of the \(n_1-r\) points outside \(C\) in that level can be mapped independently into \(C\); these maps satisfy the bounded-morphism equation because the full upper suffix is fixed. For \(j>1\), any \(x\) below level \(j\) has \(f(x)\le f(c)=c\) for every \(c\in C\). The lowest occupied level of \(S\) is \(j\), so \(f(x)=c\) for all \(c\in C\) and \(C\) is a singleton. All points at or below level \(j\) must map to that point, leaving exactly one map for the specified \(c\). It satisfies the equation since for such a lower source its upper cone maps onto \(\{c\}\) together with the complete suffix. This proves the classification directly for retractions.

Restricting an upset of \(P\) to \(S\) is surjective onto \(\operatorname{Up}(S)\), since \(S\) is an upset. Its inverse images under \(f\) distinguish any two different restrictions, by surjectivity onto \(S\). Consequently \(|\Phi[H]|=|\operatorname{Up}(S)|\). A nonempty upset in an ordinal sum takes an arbitrary nonempty subset from its lowest occupied level and the whole of each higher level. Including the empty upset gives \(1+\sum_i(2^{|S\cap A_i|}-1)\), proving the exponents in the finding. The exponents in the first family strictly increase with \(r\), those in the second strictly decrease with \(j\), and the smallest in the first exceeds the largest in the second by \(2^{n_2}-1\). Counting the choices of \(C\) or \(c\) gives the displayed polynomial.

## Verification and limitations

The accompanying finite checker enumerates bounded morphisms on small carriers and compares the image ranks and total idempotent counts with formulas. For example, on levels \((2,3,2)\) the retraction polynomial is \(2z^2+3z^5+2z^{12}+z^{14}\). The rank-resolved formulas and classification for arbitrary level sizes follow from the proof, not extrapolation. No publication priority or arbitrary-poset classification is asserted.

## Relationship to other work

Reference [2] already gives the complete endomorphism normal form and rank polynomial at equal level widths, and an exact suffix recursion for the all-endomorphism rank polynomial at arbitrary positive widths. Neither that census nor its nonsingleton simplification is claimed here. The invariant here counts only idempotents, resolved by image rank and by specified dual image; the fixed-image argument determines which of the endomorphisms counted by the general rank polynomial are retractions.

## References

1. G. Bezhanishvili, N. Bezhanishvili, T. Moraschini and M. Stronkowski, *Profiniteness and representability of spectra of Heyting algebras*, Theorem 2.6, https://arxiv.org/abs/2103.02530.
2. *Frontier rigidity and exact Heyting endomorphism-rank census for finite weak orders*, Resultary record 6af93dfcdf0d, https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-frontier-rigidity-and-exact-heyting-endomorphism-rank-census-for--6af93dfcdf0d.
