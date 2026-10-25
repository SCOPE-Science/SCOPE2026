# The Heawood five-cut complex is a wedge of 491 eight-spheres, with a complete automorphism character

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane, and let \(X=\Delta_5(H)\) be its ordinary five-cut complex. Then
\[
X\simeq\bigvee^{491}S^8.
\]
Moreover, the rational representation of \(G=\operatorname{Aut}(H)\), of order \(336\), on \(\widetilde H_8(X;\mathbb Q)\) has the following complete character. The first column records cycle lengths of an automorphism acting on all fourteen graph vertices. Every automorphism of a stated cycle type has the stated trace:

| Vertex-cycle type | Number of elements | Eighth-homology trace |
| --- | ---: | ---: |
| \(1^{14}\) | 1 | 491 |
| \(1^6 2^4\) | 21 | -29 |
| \(1^2 2^2 4^2\) | 42 | -1 |
| \(1^2 3^4\) | 56 | 5 |
| \(2^7\) | 28 | -11 |
| \((2,4,8)\) | 84 | 1 |
| \((2,6,6)\) | 56 | 1 |
| \((7,7)\) | 48 | 1 |

The character average is zero, hence
\[
\widetilde H_j(|X|/G;\mathbb Q)=0\quad\text{for every }j.
\]
This rational quotient claim does not assert that the quotient is contractible.

## Assumptions and scope
Label the seven points by \(0,\ldots,6\) and the seven lines by \(7,\ldots,13\). Line \(7+j\) is incident to point \(i\) precisely when \(i-j\pmod 7\in\{0,1,3\}\). A five-subset \(S\) is admissible when the induced graph \(H[S]\) is disconnected; its nine-vertex complement is a facet of \(X\). All subsets of such facets are faces, including the empty face in the augmented face poset. The homotopy statement is integral; the character and quotient claims use rational coefficients.

## Proof
There are exactly \(1,750\) admissible five-subsets, among the \(2,002\) total five-subsets. Exhaustively enumerating subsets of their complementary nine-element facets yields \(14,632\) nonempty faces with dimensional counts
\[
(f_0,f_1,\ldots,f_8)=(14,91,364,1001,2002,3003,3432,2975,1750).
\]
These are exact finite counts reproduced from the Fano incidence definition by the standalone verification program.

Construct a matching of the augmented face poset in fourteen rounds. During round \(v\), for every still-unmatched face \(F\) not containing vertex \(v\) such that \(F\cup\{v\}\) is still unmatched, pair these two faces and remove both from further rounds. In each round all these pairs are vertex-disjoint and hence the order within the round does not affect the output. With vertices processed in increasing order, there are exactly \(7,071\) pairs (one contains the empty face) and exactly \(491\) unmatched faces, all eight-dimensional. Orient every matched Hasse cover upward and every other cover downward. A complete topological sort of the directed graph visits all \(14,633\) faces, proving that this matching is acyclic, rather than merely relying on the matching counts.

Remove the empty-face pair: on the ordinary face poset this leaves one critical zero-cell (the previous mate of the empty face) and the 491 critical eight-cells. Forman's discrete Morse theorem gives a CW complex with precisely those cells. Because there are no cells in dimensions one through seven, every eight-cell attaches to the point and the complex is the asserted wedge. An independent mod-two simplicial boundary calculation obtains ranks \((13,78,286,715,1287,1716,1716,1259)\) in positive chain degrees one through eight, consistent with the result. The acyclic matching proves the stronger integral homotopy assertion.

For \(g\in G\), the simplicial Lefschetz formula gives its reduced Lefschetz number as
\[
-1+\sum_{\varnothing\ne F\in X,\;gF=F}(-1)^{|F|-1}\operatorname{sgn}(g\vert_F).
\]
Because the only reduced rational homology is in even degree eight, this equals the ordinary character trace on \(\widetilde H_8(X;\mathbb Q)\). Exhaustive graph isomorphism enumeration gives \(336\) automorphisms, and the signed fixed-face sum for each yields precisely the stated eight-type table. The sum of traces over all 336 elements is zero. Averaging projects rational homology onto invariants, and finite-group rational transfer identifies homology of the quotient with coinvariants; hence the reduced rational quotient homology vanishes.

## Verification
Run `python verify.py` from the package root with Python 3 and `networkx` available. The script constructs its own Fano incidence graph and facets, independently checks all face counts, executes the complete acyclic matching and directed Hasse-graph topological sort, calculates all mod-two boundary ranks, enumerates every graph automorphism, and calculates its signed Lefschetz trace. The script prints `HEAWOOD_FIVE_CUT_COMPLETE_EXACT_CHECKS_PASSED` only if all assertions pass. The verification is finite and exhaustive, not a sample-based extrapolation.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary graph cut complexes and computed several families, including cycles, complete multipartite graphs and clique prisms. Their general face-poset results address certain complete-skeleton conditions; this graph's five-cut complex lacks a complete seven-skeleton (it has \(2,975\) seven-faces instead of \(3,003\)). Their paper does not state the Heawood five-cut homotopy type or its automorphism character. The separate high-girth sphere-wedge criterion for ordinary \(k\)-cut complexes requires graph girth at least \(k+2\); the Heawood graph has girth six and the present parameter is \(k=5\), so that implication is unavailable. Previously recorded Heawood *three*-cut or *total three*-cut results concern different complexes, and they do not imply this one. The point-line incidence model and automorphism setting are independently standard.

## Limitations
The homotopy computation concerns this finite graph and this value of the cut parameter. No infinite-family statement, integral equivariant module decomposition, quotient contractibility, or independent external audit is asserted. Searches can miss unpublished or unindexed equivalent computations; further historical priority checking is appropriate.

## References
Bayer, M., Denker, M., Jelić Milutinović, M., Rowlands, R., Sundaram, S. and Xue, L., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 26 April 2023), especially Sections 1, 6 and 7, https://arxiv.org/abs/2304.13675.

Lawrence, E. D. and Wilson, R. T., *The Structure of the Heawood Graph*, arXiv:1907.11978 (2019), https://arxiv.org/abs/1907.11978.
