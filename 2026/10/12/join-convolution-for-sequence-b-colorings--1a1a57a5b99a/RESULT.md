# Join decomposition and labeled convolution for sequence b-colorings

## Finding
Let \(G\) and \(H\) be nonempty finite simple connected graphs, and let \(S=(s_1,\ldots,s_k)\) be a non-increasing sequence of positive integers. For \(I=\{i_1<\cdots<i_p\}\subseteq[k]\), write \(S_I=(s_{i_1},\ldots,s_{i_p})\).

**Join realization theorem.** The join \(G\vee H\) realizes \(S\) as a sequence b-coloring if and only if there exists a nonempty proper subset \(I\subsetneq[k]\) such that \(G\) realizes \(S_I\) and \(H\) realizes \(S_{[k]\setminus I}\).

Write \(B_G(S)\) for the number of surjective proper colorings of \(G\) by the *labeled* colors \(1,\ldots,k\) in which, for each \(i\), color class \(i\) contains at least \(s_i\) color-dominating vertices. Then
\[
\boxed{B_{G\vee H}(S)=\sum_{\emptyset\ne I\subsetneq[k]}B_G(S_I)B_H(S_{[k]\setminus I}).}
\tag{1}
\]
The factors on the right use the inherited label order of their respective subsequences. Both sides are zero if there are too few colors for nonempty factors.

The formula iterates. For nonempty connected graphs \(G_1,\ldots,G_r\), \(r\ge2\), the number of labeled sequence b-colorings of their join is
\[
B_{G_1\vee\cdots\vee G_r}(S)
=\sum_{[k]=I_1\sqcup\cdots\sqcup I_r\atop I_j\ne\emptyset}
\prod_{j=1}^{r} B_{G_j}(S_{I_j}),
\tag{2}
\]
where the sum is over ordered partitions of the label set into nonempty blocks. In particular, realization holds exactly when at least one such ordered partition has every factor realizable.

## Assumptions and definitions
A proper coloring is a **b-coloring** if every used color class contains a color-dominating vertex (CDV), whose closed neighborhood meets every used color. A sequence b-coloring realizes \(S\) when its color class \(i\) contains at least \(s_i\) CDVs. Sequences are indexed by *actual labeled colors*: permutations of labels generally change the sequence requirements. The join is formed on vertex-disjoint copies of its factors, adding every possible edge between distinct factors. The graphs are nonempty so a proper coloring uses at least one color on each factor. The connectedness restriction is consistent with the initiating sequence-b-coloring setting; the proof itself only needs nonemptiness.

## Proof
Consider any proper coloring \(c\) of \(G\vee H\). Since every vertex of \(G\) is adjacent to every vertex of \(H\), no color can occur in both factors. Thus \(c\) gives a *unique* partition \([k]=I\sqcup([k]\setminus I)\) into the nonempty sets of labels used on each side.

For \(v\in V(G)\), the join's closed neighborhood is
\[
N_{G\vee H}[v]=N_G[v]\cup V(H).
\]
The vertices of \(H\) supply **all** colors used in \(H\). It follows that \(v\) sees all global colors if and only if \(v\) sees all colors used in its own factor under \(c|_G\). Therefore \(v\) is a CDV of the join coloring if and only if it is a CDV of the restricted \(G\)-coloring. The same equivalence holds for \(H\).

For the fixed label set \(I\), restricting a labeled join coloring is therefore a bijection onto ordered pairs of realizing colorings of \(G\) with labels \(I\) and of \(H\) with complementary labels. Conversely, any such pair combines to a proper join coloring; all CDV multiplicities in every color class are preserved exactly. Consequently, the existence criterion follows, and the cardinality of the fiber of this restriction is \(B_G(S_I)B_H(S_{[k]\setminus I})\). Distinct choices of \(I\) are disjoint, so their sum yields (1).

To prove (2), apply the same closed-neighborhood argument simultaneously to every factor. Every proper global coloring defines a unique ordered partition of the label set by factors; CDV status is preserved in every restricted coloring, and the restriction/combination bijection yields the product. Summation over ordered partitions completes the proof.

## Verification and reproducibility
The argument is valid for arbitrary finite factor sizes and does not depend on computation. An independent direct finite check constructed joins using \(K_1\), \(K_2\), and the three-vertex path, enumerated labeled proper colorings, calculated CDV counts from closed neighborhoods, and compared the full profiles with those predicted by the factor restriction bijection. It found agreement, including joins of \(K_1\) with the three-vertex path, \(K_2\) with the three-vertex path, and \(K_2\) with itself. The existing `artifacts/verify.py` independently contains a broader exhaustive check for connected factor graphs through order three. These checks corroborate, rather than prove, the general statement.

## Relation to earlier results
Jakovac and Lang introduced sequence b-colorings and the \(S\)-spectrum in 2026. General results on the **ordinary** b-chromatic number of joins and cographs address the existence of a CDV in each color class but do not, by themselves, track the full vector of CDV multiplicities or give the labeled convolution (1).

A previously published exact sequence-b-coloring classification of complete multipartite graphs includes a full realization criterion, unique maximal sequence, and labeled counting product. Those results are **not** claimed here. They concern a special graph family; they do not state or imply the arbitrary-factor join decomposition and its exact ordered-palette convolution. Formula (1) is the sole main contribution, with (2) as its direct iteration. The exact decomposition gives reusable input to calculations on graph joins whenever the factor sequence-count data are available.

## Limits
The factor data \(B_{G_j}\) need not be easy to compute; this is a precise structural factorization, not a claim of efficient general-purpose computation. A b-coloring of a join cannot reuse colors between nonempty factors. Neither the formula nor the proof extends without modification to graph operations without complete adjacency between factors. A differently phrased earlier CDV-multiplicity join formula could exist in less-accessible literature. The small-case enumerations do not prove the theorem, which rests on the restriction bijection.

## References
1. M. Jakovac and M. S. Lang, *Sequence b-colorings in graphs*, arXiv:2609.08484v1, September 2026.
2. *Sequence b-colorings of complete multipartite graphs are rigid*, published October 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sequence-b-colorings-of-complete-multipartite-graphs-are-rigid--3d19e234dc3b.
3. M. Jakovac and I. Peterin, *The b-chromatic number and related topics—A survey*, Discrete Applied Mathematics 235 (2018), 184–201, DOI 10.1016/j.dam.2017.08.008.
4. F. Bonomo, G. Durán, F. Maffray, J. Marenco, M. Valencia-Pabon, *On the b-coloring of cographs and P4-sparse graphs*, Graphs and Combinatorics 25 (2009), 153–167, DOI 10.1007/s00373-008-0829-1.
