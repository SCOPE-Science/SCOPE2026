# Inverse antipodes at the first eccentricity split of the derangement switch graph

## Finding
Let \(G_n\), for \(n\ge4\), be the graph whose vertices are the derangements of \(\{0,1,\ldots,n-1\}\). Two derangements are adjacent when one is obtained from the other by interchanging its images at two positions, while remaining a derangement. All distances below refer to the **simple, loopless** graph, without lazy Markov-chain self-loops.

**Theorem (exact first eccentricity split).** The graphs \(G_4\) and \(G_5\) are both self-centered, with radius and diameter equal to \(3\) and \(4\), respectively. However, \(G_6\) has \(265\) vertices and \(1260\) edges, and
\[
\operatorname{rad}(G_6)=5,\qquad \operatorname{diam}(G_6)=6.
\]
Precisely \(40\) vertices have eccentricity \(6\), namely the derangements of cycle type \((3,3)\); the other \(225\) have eccentricity \(5\). Each derangement \(\sigma\) of type \((3,3)\) has **exactly one** vertex at distance \(6\), and that vertex is \(\sigma^{-1}\). Thus the diameter is realized by exactly \(20\) unordered inverse pairs.

For complete quantitative specificity, the unordered-pair distance distribution of \(G_6\) is
\[
\#\{\{\sigma,\tau\}: d(\sigma,\tau)=k\}
=(1260,5310,11490,12100,4800,20)
\]
for \(k=1,2,3,4,5,6\), respectively. The sum is \(\binom{265}{2}=34980\). The n=4 and n=5 pair distributions, at positive distances, are \((12,18,6)\) and \((120,300,360,166)\), respectively.

## Assumptions and scope
A derangement is a permutation \(\sigma\) with \(\sigma(i)\ne i\) for every position \(i\). One move at positions \(i<j\) gives \(\tau(i)=\sigma(j)\), \(\tau(j)=\sigma(i)\), leaving all other images untouched. Its necessary and sufficient legality conditions are
\[
\sigma(i)\ne j,\qquad \sigma(j)\ne i.
\]
No other moves, including three-cycles, simultaneous disjoint transpositions, or visits through permutations with fixed points, are allowed. The phrase *first* refers to the connected orders \(4\le n\le6\) only; no assertion about radius or diameter for \(n\ge7\) is made. The case \(n=3\) has two isolated derangements and is excluded from this connected-graph comparison.

## Proof
**Step 1 (exhaustive finite state and edge sets).** Every \(G_n\)-vertex corresponds bijectively to a perfect matching of the bipartite graph \(K_{n,n}\) with the \(n\) diagonal edges removed, by recording the column matched to each row. In a matching, an alternating four-cycle switch replaces two edges \((i,\sigma(i))\), \((j,\sigma(j))\) by \((i,\sigma(j))\), \((j,\sigma(i))\). The two replacement edges are present if and only if the displayed legality conditions hold. Enumerating bijective assignments by recursion, or equivalently generating all \(n!\) permutations and filtering the diagonal, is therefore exhaustive for both vertices and edges. This gives \(9,44,265\) vertices and \(12,120,1260\) edges for \(n=4,5,6\).

**Step 2 (conjugacy symmetry reduces the eccentricity proof to eight roots).** Simultaneous relabeling by any permutation \(\pi\) sends \(\sigma\mapsto\pi\sigma\pi^{-1}\). It preserves fixed-point-freeness, and sends each permitted pair of swapped positions to the conjugately relabeled pair. Hence it is an automorphism of \(G_n\). Its orbits are exactly the derangement cycle types, so eccentricity is constant within each type. There are two types each for \(n=4,5\), and four types for \(n=6\). Counting permutations of each type gives, at \(n=6\), \(15\) of type \((2,2,2)\), \(90\) of type \((4,2)\), \(40\) of type \((3,3)\), and \(120\) of type \((6)\).

**Step 3 (checkable exact distance certificates).** The included `orbit_distance_certificate.json` fixes one lexicographically first root for each of the eight types and records integer distance labels to **every vertex**, indexed by the lexicographic list of derangements. The standalone `verify_distance_certificate.py` recomputes the complete legal edge set and validates for every root \(r\) and every vertex \(v\): \(d(r)=0\); \(d(v)\ge0\); labels across every edge differ by at most one; and each \(v\ne r\) has a neighbor with label \(d(v)-1\). These are logically sufficient, not heuristic: edge-Lipschitzness proves every path from \(r\) to \(v\) has at least \(d(v)\) edges, while descending neighbors construct a path of exactly \(d(v)\) edges. Hence the labels are **exact** shortest-path distances, without relying on log text or sampling.

The certificate gives the following complete distance-shell profiles (including the root itself at distance zero) for \(G_6\):

| Cycle type | Orbit size | Certified shells in increasing distance |
|---|---:|---|
| \((2,2,2)\) | 15 | \((1,12,46,86,88,32)\) |
| \((4,2)\) | 90 | \((1,10,41,89,88,36)\) |
| \((3,3)\) | 40 | \((1,9,36,87,92,39,1)\) |
| \((6)\) | 120 | \((1,9,40,85,94,36)\) |

The two certificate roots for \(G_4\) have shells \((1,4,2,2)\) and \((1,2,5,1)\); those for \(G_5\) have shells \((1,6,12,18,7)\) and \((1,5,15,15,8)\). Thus the three radii and diameters, and the n=6 eccentricity split, follow by conjugacy. The pair-distance distribution additionally follows by summing the distances over the finite state space and dividing the ordered totals by two; two independent full-graph enumerators reproduce the displayed counts.

**Step 4 (unique inverse antipodes).** For the representative \(\sigma=(1,2,0,4,5,3)\) of type \((3,3)\), the certificate's single distance-six label occurs at \(\sigma^{-1}=(2,0,1,5,3,4)\). For every other type the maximum distance is five, so there are no further diameter pairs. Conjugation commutes with inversion; therefore, for every type-\((3,3)\) derangement, the unique antipode is its inverse. These permutations are not involutions, so \(40/2=20\) unordered pairs result.

There is also a conceptual obstruction to shorter inverse paths. In the unrestricted symmetric-group transposition graph, the distance from a type-\((3,3)\) permutation \(\sigma\) to \(\sigma^{-1}\) is four, since \(\sigma^2\) consists of two three-cycles. Any four-step geodesic must begin by transposing two positions within a cycle of \(\sigma^2\), but that cycle has the same support as a cycle of \(\sigma\). Such a swap fixes one of those positions, so it is forbidden in \(G_6\). Thus distance four is impossible; transposition parity rules out odd distances, giving a lower bound of six. A legal six-switch witness, with permutations in one-line notation in successive order, is
\[
(1,2,0,4,5,3)\to(1,2,3,4,5,0)\to(1,0,3,4,5,2)\to(1,0,3,2,5,4)
\]
\[
\to(1,0,3,5,2,4)\to(2,0,3,5,1,4)\to(2,0,1,5,3,4).
\]
The general uniqueness statement uses the complete exact labels, not this single path alone.

## Verification
The exact set and edge enumerator is `verify_one_line.py`. The independently organized bipartite perfect-matching and alternating-four-cycle enumerator is `verify_bipartite_matchings.py`. They exhaust every root of each graph for \(n=4,5,6\), reconstruct the full unordered distance histograms, and check every claimed diameter pair. Their recorded stdout is `one_line_output.txt` and `matching_output.txt`. The certificate producer `make_orbit_certificate.py` and its independently checking local-distance verifier `verify_distance_certificate.py` supply a third exact finite validation path; the checker needs only the certificate and the finite definition of edges, and its recorded output is `certificate_output.txt`. All programs use only Python's standard library and are run as `python <script>` (the certificate checker accepts the certificate path as its first argument).

## Relationship to prior work
Smith's 2013 preprint [1] studies the random-transposition Markov chain on precisely the restricted state space of derangements, but its main results concern comparison inequalities and spectral/mixing bounds, not these exact \(n=6\) graph distances. Jain's treatment of the same graph as \(\alpha(n)\) [2] proves connectivity, degrees, and shortest **spanning walks**, but a shortest spanning walk does not determine shortest paths between prescribed pairs, eccentricity, or inverse antipodes. Mendonça [3] uses the same legal transposition condition in a sampling context; Baril and Vajnovszki [4] study Gray codes with a wider move repertoire. The previously studied all-order four-cycle census of this derangement-switch graph concerns local closed walks, not the global shortest-path metric and its first asymmetric eccentricity layer.

## Limitations
The statement is exact for \(n=4,5,6\), with the structural split at \(n=6\); it makes no larger-order claim. The work supplies a finite proof certificate, not a general asymptotic diameter theorem or mixing-time estimate. A mathematically equivalent calculation might appear in unindexed databases or supplementary computations; no independent external review has been performed. The full finite verifications require faithfully implementing the stated zero-based permutation convention and legality condition.

## References
1. A. Smith, *Comparison Theory for Markov Chains on Different State Spaces and Application to Random Walk on Derangements*, arXiv:1301.7357v1, first submitted 2013-01-30. https://arxiv.org/abs/1301.7357
2. P. Jain, *Transpositions in Derangements*, preprint (2021-09-12), DOI:10.13140/RG.2.2.35817.42088. https://www.researchgate.net/publication/354533290_Transpositions_in_Derangements
3. J. R. G. Mendonça, *Efficient generation of random derangements with expected distribution of cycle lengths*, arXiv:1809.04571v1, 2018-09-12. https://arxiv.org/abs/1809.04571
4. J.-L. Baril and V. Vajnovszki, *Gray code for derangements*, Discrete Applied Mathematics, DOI:10.1016/j.dam.2003.06.002. https://jl.baril.u-bourgogne.fr/derange.pdf
