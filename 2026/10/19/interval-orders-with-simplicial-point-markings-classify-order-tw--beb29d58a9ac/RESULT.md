# Interval orders with simplicial point markings classify order-two subsequence spectra

## Finding
Let \(A\) be a fixed labeled alphabet of size \(q\geq1\). Two full-support words over \(A\) are *order-two equivalent* when they have exactly the same scattered subsequences of length at most two. Write \(\mathcal I(A)\) for the set of interval orders on the labeled set \(A\). For \(P\in\mathcal I(A)\), let \(G(P)\) be its incomparability graph. A graph vertex is *simplicial* if its open neighborhood forms a clique.

**Theorem.** The order-two equivalence classes of full-support words are in bijection with the pairs \((P,S)\) such that \(P\in\mathcal I(A)\) and \(S\subseteq A\) is an independent set consisting entirely of simplicial vertices of \(G(P)\). The minimum word length within the class corresponding to \((P,S)\) is exactly \(2q-|S|\).

The graph induced by the simplicial vertices of \(G(P)\) is a disjoint union of cliques. If their sizes are \(c_1(P),\ldots,c_{r(P)}(P)\), then the exact length-enumerator of full-support classes, counted by the minimum length of their representatives, is

\[
F_q(z)=\sum_{P\in\mathcal I(A)} z^{2q}\prod_{i=1}^{r(P)}\bigl(1+c_i(P)z^{-1}\bigr).
\]

The coefficients depend only on the alphabet size, not the particular labels. The theorem is a structural realization criterion and an enumerator; it is not an assertion that the already tabulated total number of order-two classes or the number of labeled interval orders is new.

## Assumptions and scope
A scattered subsequence is obtained by deleting zero or more positions without changing the order of the remaining positions. *Full support* means every letter of \(A\) occurs at least once. An interval order is a strict partial order representable by nonempty real intervals \(I_a=[L_a,R_a]\) with \(a<_P b\) exactly when \(R_a<L_b\); equivalently it is a finite poset with no induced \(2+2\). Two distinct letters are adjacent in \(G(P)\) exactly when they are incomparable in \(P\).

For a word \(w\) with full support, define \(f_a\) and \(\ell_a\) as its first and last positions of letter \(a\). Let \(S(w)=\{a:aa\text{ is absent as a subsequence of }w\}\), and put \(a<_{P(w)} b\) exactly when \(\ell_a<f_b\). Each \([f_a,\ell_a]\) is an interval representation of \(P(w)\), with zero-length intervals allowed for letters occurring once.

## Proof
**1. The spectrum determines \((P,S)\).** For distinct letters \(a,b\), the scattered pair \(ba\) occurs precisely when \(f_b<\ell_a\). Since distinct positions cannot coincide, \(ba\) is absent precisely when \(\ell_a<f_b\), namely when \(a<_{P(w)}b\). The repeated pair \(aa\) occurs precisely when \(f_a<\ell_a\), so its absence is equivalent to \(a\in S(w)\). The single-letter subsequences are already fixed by full support. Hence two words have the same length-at-most-two spectrum if and only if they have the same \((P,S)\).

**2. Necessity of simplicial independent markings.** If \(a\in S(w)\), then \([f_a,\ell_a]\) is the point \(\{f_a\}\). Two distinct marked points are disjoint, so their letters are comparable in \(P(w)\); thus \(S(w)\) is independent in \(G(P(w))\). Every interval whose letter is incomparable with \(a\) contains the point \(f_a\). Those neighbor intervals therefore pairwise intersect, so each marked vertex \(a\) is simplicial.

**3. Sufficiency.** Take any interval order \(P\) and an independent set \(S\) of simplicial vertices of \(G(P)\). Choose an interval representation in which all intervals are nondegenerate, all endpoints are distinct, every pair of incomparable intervals overlaps over a nonempty open segment, and all comparable intervals have positive separating gaps. Such a representation always exists: start from any finite interval representation, slightly widen its intervals to turn endpoint contacts into positive overlaps, retaining the minimum positive gap between comparable intervals, and then perturb finitely many endpoints to remove ties.

For \(a\in S\), consider its interval and those of all vertices incomparable with \(a\). By simpliciality every two of these intervals overlap, and in the chosen representation they overlap in an open segment. The interval Helly property gives a nonempty common open segment. Choose a point \(p_a\) in that common segment and replace \(I_a\) by \(\{p_a\}\). This preserves each comparison and incomparison incident with \(a\). Two letters in \(S\) are comparable, hence their original intervals are disjoint; modifying their intervals therefore causes no interference. We obtain the same interval order \(P\) with precisely the specified members of \(S\) represented by points and every other letter represented by a nondegenerate interval. Choose any remaining endpoints and marked points pairwise distinct, without changing comparisons. Reading the resulting endpoints from left to right, writing each unmarked letter at both endpoints and each marked letter at its single point, yields a full-support word with \((P(w),S(w))=(P,S)\).

**4. Minimum representative length.** In every word with this spectrum, each letter in \(S\) appears exactly once and each other letter at least twice. This gives the lower bound \(2q-|S|\). In the word just constructed, each unmarked letter occurs exactly twice and each marked letter once, attaining the bound. Alternatively, starting from an arbitrary representative, keeping only the first and last occurrences of each letter preserves all pairs of distinct letters and the presence/absence of repeated-letter pairs.

**5. The generating function.** If \(a,b\) are adjacent simplicial vertices in any graph, their closed neighborhoods coincide: every neighbor of one is a neighbor of the other by the simplicial clique condition. Consequently adjacency is transitive among simplicial vertices, and their induced graph is a disjoint union of cliques of sizes \(c_i(P)\). An independent set of simplicial vertices selects either no vertex or exactly one of the \(c_i(P)\) vertices from each clique. Its minimum-length contribution is \(z^{2q-|S|}\). Multiplication over the cliques and summation over labeled interval orders gives the displayed enumerator.

## Verification
The standalone \(\texttt{check.py}\) independently enumerates every labeled interval order from all double-occurrence endpoint words and every permitted simplicial independent marking. A separate breadth-first traversal of all reachable order-two subsequence signatures records the shortest representative of each signature. The two methods agree, for every alphabet size \(1\leq q\leq5\). The number of labeled interval orders at these sizes is \(1,3,19,207,3451\), consistent with OEIS A079144. The full-support class counts are \(2,11,112,1803,41876\). For \(q=5\), the coefficients by shortest length \(5,6,7,8,9,10\) are respectively \(120,1800,8400,15720,12385,3451\). These are finite consistency checks; the proof above applies to every finite alphabet size.

## Relationship to prior work
Simon's level-two relation and class counting were investigated by Karandikar, Kufleitner, and Schnoebelen, who published the total number of classes over alphabets of several sizes (arXiv:1310.1278, Appendix B). Praveen, Schnoebelen, Veron, and Vialard studied piecewise-complexity and minimal representatives of Simon classes (arXiv:2311.15431). Fleischmann, Höfer, Huch, and Nowotka investigated binary Simon classes using a different factorization (arXiv:2306.14192). The interval-order counts themselves have an existing combinatorial literature (OEIS A079144). None of the relevant inspected proofs gives the present bijection with independently chosen simplicial point markings, the exact shortest-representative length by markings, or the resulting general full-support length enumerator. The previously known class totals do not imply a unique geometric realization condition. This comparison is a literature-based originality assessment, not a universal uniqueness guarantee.

## Limitations
The result concerns scattered subsequences of length at most two, not longer subsequences or contiguous factors. It gives an exact finite combinatorial sum over labeled interval orders, not a simplified closed form or fast enumeration algorithm for arbitrarily large alphabets. The small-alphabet coefficient values are computational checks rather than an exhaustive proof of the arbitrary-alphabet statement. Equivalent formulations may exist in unindexed literature; the broader published literature on interval graphs, interval orders, and Simon classes is large.

## References
1. M. Praveen, Ph. Schnoebelen, J. Veron, and I. Vialard, *On the piecewise complexity of words and periodic words*, arXiv:2311.15431v1 (public November 26, 2023), https://arxiv.org/html/2311.15431v1.
2. P. Karandikar, M. Kufleitner, and Ph. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278 (2013), https://arxiv.org/html/1310.1278v5.
3. P. Fleischmann, J. Höfer, A. Huch, and D. Nowotka, *Alpha-beta-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192 (2023), https://arxiv.org/abs/2306.14192.
4. OEIS A229954, *The index of Simon's piecewise testability congruence*, https://oeis.org/A229954.
5. OEIS A079144, *Number of labeled interval orders*, https://oeis.org/A079144.
