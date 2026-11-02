# A sharp Lucas-number cyclic covering theorem for Fibonacci words

## Finding

Let \(\mathcal F_n\) be the set of all binary words of length \(n\) containing no contiguous occurrence of \(00\). A circular word \(W\) *covers* \(\mathcal F_n\) when every word in \(\mathcal F_n\) occurs as one of its indexed cyclic windows of length \(n\), with repetitions allowed. For every integer \(n\ge2\), the smallest possible length of such a circular word is

\[
\ell_n=F_{n+2}+F_n-1=L_{n+1}-1,
\]

where \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\). In particular, exactly \(F_n-1\) cyclic windows beyond the \(F_{n+2}\) required distinct ones are necessary and sufficient. An optimal cover can itself have no cyclic occurrence of \(00\).

The first optimum lengths, for \(n=2,\ldots,12\), are \(3,6,10,17,28,46,75,122,198,321,520\).

## Assumptions and scope

The alphabet is \(\{0,1\}\). The forbidden pattern is applied to each required *linear* word; it is **not** a cyclic prohibition on that word. In particular, \(010\in\mathcal F_3\). The covering word is cyclic and can use arbitrary additional windows. Its cyclic windows are indexed by their starting positions, modulo the covering length. The theorem optimizes over every circular binary word, without a prior avoidance constraint. The winning construction satisfies the stronger avoidance constraint automatically.

## Proof

**1. Mandatory transitions.** In the order-\((n-1)\) binary de Bruijn directed graph, vertices are binary words of length \(h=n-1\), and the arc labeled by an \(n\)-word \(w\) runs from its length-\(h\) prefix to its length-\(h\) suffix. Every circular word gives a closed walk in this graph with one arc per indexed window. Covering \(\mathcal F_n\) forces at least one use of each mandatory arc labeled by \(w\in\mathcal F_n\). The usual first-symbol decomposition gives \(|\mathcal F_n|=F_{n+2}\).

For a length-\(h\) vertex \(v\) avoiding \(00\), its mandatory outdegree is \(1\) if it ends in \(0\) and \(2\) if it ends in \(1\). Its mandatory indegree is \(1\) if it begins with \(0\) and \(2\) if it begins with \(1\). Thus the mandatory outdegree-minus-indegree imbalance is \(+1\) at each vertex beginning in \(0\) and ending in \(1\), \(-1\) at each vertex beginning in \(1\) and ending in \(0\), and zero otherwise. Vertices containing \(00\) have no mandatory incident arcs.

**2. Universal lower bound.** Call a vertex with imbalance \(-1\) a source and a vertex with imbalance \(+1\) a sink, referring to the *additional* arcs needed to repair the imbalance. Every source is uniquely of the form \(v=1^r0u\), where \(r\ge1\) is the length of its initial run of ones, and \(u\) is empty or begins with \(1\) and ends with \(0\). Additional arcs of any covering walk form a nonnegative integer flow with one unit of supply at every source and one unit of demand at every sink. Such a flow decomposes into source-to-sink directed paths and directed cycles. The initial \(r\) symbols of \(v\) are all ones, so after fewer than \(r\) de Bruijn shifts the leading symbol remains one. Hence **any** path from this source to **any** sink, which begins with zero, uses at least \(r\) arcs. Summing over the source-started flow paths gives the lower bound \(\sum_{v\text{ source}}r(v)\) additional windows. This argument allows additional arcs containing \(00\): it bounds completely unrestricted covering words.

**3. Matching upper bound and covering construction.** For each source \(v=1^r0u\), append \(1\) exactly \(r\) times in the de Bruijn graph, shifting off its first \(r\) ones. The resulting vertex is \(0u1^r\), which is a sink. Each additional \(n\)-word is formed by appending \(1\) to a vertex without \(00\), so no added arc contains \(00\). These paths connect sources to sinks bijectively: given any sink \(0u1^r\), take \(r\) to be its entire trailing run of ones; then \(u\) is empty or ends in zero and, if nonempty, starts with one, so \(1^r0u\) is its unique source. Adding all these directed paths to the mandatory arcs balances every vertex.

The mandatory subgraph on \(00\)-avoiding vertices is strongly connected: from any such vertex append \(1\) repeatedly to reach \(1^h\), then append the symbols of any desired admissible vertex. Every intermediate window still avoids \(00\). Therefore the augmented directed multigraph has an Euler circuit. Reading its edge labels gives a circular cover with exactly \(F_{n+2}+\sum_v r(v)\) windows, and the cover contains no cyclic \(00\).

**4. Exact cost.** Let \(A_h\) be the number of length-\(h\) sources, and \(E_h\) the sum of their initial-one-run lengths. Here \(A_1=0\), \(A_h=F_{h-1}\) for \(h\ge2\), \(E_1=0\), and \(E_2=1\). Splitting sources of length \(h\ge3\) according to whether they begin \(11\) or \(10\) gives

\[
E_h=E_{h-1}+A_{h-1}+A_{h-2}=E_{h-1}+F_{h-1}.
\]

By the Fibonacci sum identity, \(E_h=F_{h+1}-1\) for all \(h\ge1\). Substituting \(h=n-1\) proves that the necessary and sufficient additional-arc count is \(F_n-1\). Finally \(F_{n+2}+F_n=L_{n+1}\), proving the stated formula. The length-\(n=2\) boundary case has no sources and gives the same formula. \(\square\)

## Verification

The standard-library program `verify.py` implements the source-to-sink augmentation, balances the multigraph, computes an Euler tour, checks every cyclic length-\(n\) window, and verifies both the Lucas length and the absence of \(00\). It passed for \(2\le n\le12\); it also enumerates every shorter circular binary candidate for \(2\le n\le5\) and verifies none covers all mandatory words. Examples of optimum covering strings (rotation is immaterial) are `110` for \(n=2\), `110101` for \(n=3\), `1111011010` for \(n=4\), and `11110111011010101` for \(n=5\).

The separately implemented `flow_check.py`, using NetworkX network simplex, independently solves the unconstrained minimum-cost flow relaxation for every \(n\) from \(2\) through \(12\), permitting all binary arcs including those containing \(00\). It reports the same additional costs \(0,1,2,4,7,12,20,33,54,88,143\). These computations test the construction and reduction; the infinite statement follows from the proof, not extrapolation.

## Relationship to prior work

Moreno and Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695, first arXiv version 12 November 2007), formulate restricted-language de Bruijn cycles using **periodically admissible** words. Their definition requires the repeated word to avoid the forbidden pattern, and their target is an Eulerian cycle with one occurrence of each cyclically admissible word. This differs from covering **all linearly admissible words**, including those with first and last symbols zero, while minimizing repeats. Their Euler-circuit framework is useful context but does not directly give the present shortest-cover formula.

Sawada and Gabrić, *Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random* (arXiv:2510.16545, Section 4.5), likewise construct cycles over necklace classes that **cyclically** avoid a forbidden run. Their target alphabet of required windows is not \(\mathcal F_n\), and their results concern random Eulerian-cycle generation, not the optimal augmentation of the nonbalanced graph of linearly admissible windows.

Chee, Etzion, Ta, and Vu, *On de Bruijn Covering Sequences and Arrays* (arXiv:2404.13674, introduction), minimize sequences whose windows form a Hamming covering code of specified radius over the **full** word space; it does not state the selective exact-cover problem solved here. Chen, Kitaev, and Sun (arXiv:1908.01116) study existence of exact universal cycles after deleting selected words, primarily low-order exceptional cases; the present result is an optimal cover **with repeats** of a structured Fibonacci-sized set.

The exact Lucas formula was not found in the inspected sources or in targeted research-record searches. Absence of a retrieved match does not prove historical priority; older or differently named superstring and constrained-sequence results may exist.

## Limitations

The theorem applies only to the binary no-adjacent-zero language and cyclic coverage of all **linearly** valid length-\(n\) words. It does not count or classify optimal cyclic covers, provide an amortized-constant-time generator, or resolve forbidden patterns of greater length or larger alphabets. Independent literature-priority verification is not performed. Some related constrained-code papers were inspected only at the abstract/bibliographic level owing to unavailable full text.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (2007), https://arxiv.org/abs/0711.1695.
2. J. Sawada and D. Gabrić, *Las Vegas Algorithms to Generate Universal Cycles and de Bruijn Sequences Uniformly at Random*, arXiv:2510.16545 (2025), https://arxiv.org/abs/2510.16545.
3. Y. M. Chee, T. Etzion, H. Ta, and V. K. Vu, *On de Bruijn Covering Sequences and Arrays*, arXiv:2404.13674 (2024), https://arxiv.org/abs/2404.13674.
4. H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *On the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, arXiv:1908.01116 (2019), https://arxiv.org/abs/1908.01116.
5. Y. M. Chee et al., *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications*, arXiv:2005.03102 (2020), https://arxiv.org/abs/2005.03102 (abstract inspected).
