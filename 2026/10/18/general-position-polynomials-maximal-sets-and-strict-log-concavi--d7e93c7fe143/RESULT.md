# Inclusion-maximal general-position sets of cycle complements

## Finding

For each integer \(n\ge5\), let \(M_n(z)\) count inclusion-maximal geodesic general-position sets of the labeled graph \(\overline{C_n}\) by size. Then
\[
M_n(z)=
\begin{cases}
5z^3,& n=5,\\
3z^2+8z^3,& n=6,\\
nz^3+\displaystyle\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}
\frac{n}{k}\binom{k}{n-2k}z^k,& n\ge7.
\end{cases}
\]
In set-system terms, start with all maximal independent sets of the original cycle and all consecutive triples. Delete the five independent pairs only at \(n=5\). In particular, at \(n=6\) the three opposite pairs are the only maximal two-vertex sets, and no other \(n\ge5\) has maximal two-vertex sets. Thus the smallest maximal general-position set has size three except at \(n=6\), when it has size two.

## Assumptions and scope

Vertices are labeled by \(\mathbb Z/n\mathbb Z\), with the original cycle edges between consecutive labels. A set is in geodesic general position when no three of its vertices lie on a common shortest path. A set is inclusion-maximal if it has no proper general-position superset, which is not the same as having maximum cardinality. Counts are of labeled subsets, not up to rotation or reflection.

## Proof

First recall the ordinary general-position set-system reduction. In the complement of \(C_n\), each pair of consecutive cycle vertices has a common neighbor (their closed neighborhoods in the cycle cover at most four vertices), so the complement has diameter two. A set is in general position exactly when it induces no three-vertex path in the complement. Induced graphs with no three-vertex path have clique components: otherwise a shortest internal path between a pair of nonadjacent vertices of one component would contain such a path. Taking complements shows equivalently that \(C_n[S]\) must be complete multipartite. If \(C_n[S]\) contains any edge then triangle-freeness forces two nonempty parts, and the degree bound forces each part to have size at most two. Both parts of size two would give an induced four-cycle, impossible for \(n\ge5\). Consequently the eligible sets are the independent sets of \(C_n\), the cycle-edge pairs, and the consecutive triples. This ordinary family description is also a special case of the general degree-two deletion characterization referenced below.

To pass from eligible sets to **inclusion-maximal** ones, consider what can contain each type. Every consecutive triple is maximal: an extension contains an edge and has at least four vertices, of which there are no eligible sets in this cycle. An edge pair is not maximal, since it lies in a consecutive triple. A cycle-independent set with at least three vertices has only cycle-independent proper extensions among eligible sets, and so is maximal in general position exactly when it is maximal independent in the cycle. Nonmaximal independent sets of any size can extend in the cycle-independent family and are never maximal in general position. The only remaining issue is whether any maximal independent pair is contained in an edge-containing eligible set of size three.

A maximal independent set of size \(k\) has only gaps of two or three cycle edges between successive marked vertices: independence excludes a gap of one, and a gap of at least four leaves an unmarked vertex with no marked neighbor. Conversely, all gaps two or three imply both independence and maximality. There must be \(n-2k\) gaps of length three. Counting a chosen starting marked vertex gives \(n\binom{k}{n-2k}\) rooted placements in the fixed cyclic direction. Dividing by the \(k\) possible roots for each set gives the count in the formula and the range \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\).

There are no maximal independent singletons for \(n\ge5\), and independent maximal pairs are possible only at \(n=5,6\) by the gap bound. At \(n=5\), the gaps of a maximal pair are two and three; its members are the endpoints of a length-two path in the cycle, so that the pair extends to the consecutive triple containing that path. This eliminates all five pairs. At \(n=6\), the gaps of a maximal pair are three and three, so its opposite vertices do not occur in any consecutive triple. All three such pairs remain maximal in general position. The cycle also has the two alternating independent triples in this case. Adding the \(n\) distinct consecutive triples in each case establishes the result.

## Relation to existing results

The general structural criterion for geodesic general position is treated by Anand et al. ([arXiv:1812.08460](https://arxiv.org/abs/1812.08460)). *Exact general-position polynomials and strict log-concavity after degree-two edge deletion* ([result](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-general-position-polynomials-and-strict-log-concavity-afte--6fabfeea792b/RESULT.md)) gives the ordinary set-family structure, ordinary polynomial and strict coefficient result in a larger class. Di Stefano et al. ([arXiv:2306.09965](https://arxiv.org/abs/2306.09965)) study the smallest size of maximal sets, with a general criterion for maximal pairs. Counts of maximal independent sets of cycles are classical; the total by cycle order is the Perrin sequence ([OEIS A001608](https://oeis.org/A001608)). The assertion here is the complete size-refined census for maximal **general-position** sets in antiholes. Counting all eligible sets by size does not see which sets can be extended; it is the overlap with consecutive triples that removes the otherwise maximal independent pairs of the five-cycle.

## Verification and limitations

Run `python3 check_maximal.py` for an exact finite comparison against shortest-path enumeration for \(5\le n\le16\). The proof above supplies the full range. The result is only for complements of simple cycles of order at least five. The comparison with known ordinary general-position and independent-set counting results does not establish historical priority for the maximal-set formula.
