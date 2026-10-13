# Equality cases for the \(S_5\) Cayley code at distance \(3\)
## Finding
Let \(d_C(\pi,\sigma)\) be the minimum number of arbitrary transpositions needed to change \(\pi\in S_5\) into \(\sigma\in S_5\), and let \(C(5,3)\) be the maximum cardinality of a subset having pairwise Cayley distance at least \(3\). Then
\[
C(5,3)=10.
\]
There are exactly \(144\) labeled maximum codes. After left translation so that the identity lies in a maximum code, its five even permutations form an order-\(5\) subgroup \(H\), while its five odd permutations form one of the two generator cosets of the cyclic quotient \(N_{S_5}(H)/H\cong C_4\). Conversely, all such normalized unions occur. Thus there are exactly \(12\) normalized maxima, two for each of the six order-\(5\) subgroups of \(S_5\).

Every maximum code has the same pair structure: among its \(45\) unordered pairs, \(25\) relative permutations have cycle type \((4,1)\), hence distance \(3\), and \(20\) have cycle type \((5)\), hence distance \(4\). Under the explicit \(28{,}800\)-element isometry group consisting of maps \(x\mapsto axb\) and \(x\mapsto ax^{-1}b\), all \(144\) maxima form one orbit; the stabilizer of a maximum has order \(200\).

## Assumptions and scope
Permutations act on \(\{1,2,3,4,5\}\), composition is function composition, and a transposition may exchange any two symbols. Codes are arbitrary subsets of \(S_5\); no subgroup or linearity assumption is imposed. “Labeled” means that the five symbols are fixed and no quotient by equivalence is taken. The displayed isometry group is an explicitly verified group of isometries; it is not asserted to be the full isometry group of the metric space.

## Proof
For \(\tau\in S_5\), let \(c(\tau)\) be its number of cycles, including fixed points. The Cayley distance satisfies
\[
d_C(\pi,\sigma)=5-c(\pi^{-1}\sigma).
\]
The parity of this distance is the parity difference between \(\pi\) and \(\sigma\). Therefore two distinct codewords of the same parity in a distance-\(3\) code must be at even distance at least \(3\), hence at distance exactly \(4\). Their relative permutation is consequently a \(5\)-cycle and has no fixed point.

If two one-line permutations \(\pi\) and \(\sigma\) agree in a coordinate, then \(\pi^{-1}\sigma\) has a fixed point. Thus codewords of the same parity in a distance-\(3\) code disagree in every coordinate. Looking at any one fixed coordinate, the symbols used by one parity class must all be distinct, so each parity class has at most five elements. Hence every such code has size at most \(10\).

The bound is attained. In one-line notation, a representative is
\[
\{12345,13524,23451,24135,34512,35241,41352,45123,51234,52413\}.
\]
Equivalently, let \(H=\langle(1\,2\,3\,4\,5)\rangle\), and let \(g\) be the permutation with one-line form \(13524\). Then the representative is \(H\cup gH\), and direct evaluation gives minimum Cayley distance \(3\).

For completeness of the equality classification, normalize a maximum by left translating one codeword to the identity. Exactly \(74\) other permutations are then eligible, namely those at distance at least \(3\) from the identity. Join two eligible permutations when their mutual distance is at least \(3\). Exhaustive maximal-clique enumeration of this finite graph finds exactly \(12\) cliques of size \(9\), and no larger clique. Adding the identity gives the \(12\) normalized maxima.

In every normalized maximum, the even half is closed under multiplication and is an order-\(5\) subgroup \(H\). The odd half is simultaneously a left and right coset \(gH=Hg\), its elements normalize \(H\), and its image in \(N_{S_5}(H)/H\) is a generator. Conversely the two generator cosets for each of the six possible \(H\) give the twelve normalized maxima. Left translating and deduplicating them gives exactly \(144\) labeled maxima. The same exhaustive data verify the common pair-type profile.

Finally, left multiplication, right multiplication, and inversion preserve Cayley distance. The maps \(x\mapsto axb\) and \(x\mapsto ax^{-1}b\) give \(28{,}800\) distinct isometries. Applying generators of this explicit group to one representative reaches all \(144\) maxima, so they form one orbit and the stabilizer order is \(28{,}800/144=200\).

## Verification
The accompanying `verify.py` uses only the Python standard library. It independently reconstructs Cayley distances by breadth-first search in the transposition Cayley graph and checks the cycle-count formula. It then constructs the normalized compatibility graph, exhaustively enumerates all maximal cliques by Bron–Kerbosch search, verifies the subgroup/normalizer-coset description of every maximum, generates and deduplicates all labeled maxima, verifies the pair-cycle profile, constructs the stated isometry action, and checks the single orbit and stabilizer order.

The exact maximal-clique histogram in the normalized compatibility graph is
\[
4:1250,\qquad 5:6480,\qquad 6:2520,\qquad 9:12.
\]
The last entry yields the twelve normalized maxima. A successful replay ends with a line beginning `VERIFY_OK` and reports `labeled_maxima=144`, `c5_subgroups=6`, `isometry_group_size=28800`, `orbits=1`, and `stabilizer=200`.

## Relationship to prior work
Cameron and Wu’s 2006 preprint surveys the Cayley metric on permutation groups and studies weight-complexity questions; it defines Cayley distance as the minimum number of transpositions and notes its left invariance. That work concerns computational problems for subgroup weights, not maximum arbitrary subset codes or finite equality cases.

Chee and Vu’s 2014 work studies permutation codes in generalized Kendall and Cayley metrics and develops breakpoint-based constructions. Its publicly accessible abstract and bibliographic record establish direct subject overlap, but do not state this \(S_5\), distance-\(3\) equality classification.

Nguyen’s 2024 paper directly defines \(C(n,d)\) as the maximum size of a Cayley permutation code and studies general and asymptotic bounds. The full public text was inspected: it gives the code definition, general Gilbert–Varshamov and sphere-packing bounds, and asymptotic improvements, but does not state a \(C(5,3)\) equality-case census or the normalizer-coset classification above.

Targeted searches for the exact parameter, its transposition-distance aliases, equality cases, subgroup-normalizer formulations, and stronger finite classifications found no source whose statement implies the complete result here. The nearest indexed finite permutation-family result located concerns even-intersecting families in \(S_5\), a different adjacency condition and a different extremal size.

## Limitations
The theorem is only for length \(5\) and minimum Cayley distance \(3\). The finite classification is exhaustive for this parameter but does not imply a classification at other lengths or distances. The explicit \(28{,}800\)-element isometry group is sufficient for the stated orbit result, but no assertion is made that it is the full isometry group. Literature search cannot eliminate the residual possibility of an obscure or unindexed prior finite census; the strongest inspected direct source on \(C(n,d)\) is asymptotic rather than an exact \(n=5\) table.

## References
1. P. J. Cameron and T. Wu, “The complexity of the Weight Problem for permutation and matrix groups,” preprint dated 20 September 2006, https://webspace.maths.qmul.ac.uk/p.j.cameron/preprints/Metrics3.pdf.
2. Y. M. Chee and V. K. Vu, “Breakpoint analysis and permutation codes in generalized Kendall tau and Cayley metrics,” IEEE ISIT 2014, pp. 2959–2963, DOI 10.1109/ISIT.2014.6875376.
3. T. Nguyen, “Improving the Gilbert-Varshamov bound for permutation Codes in the Cayley metric and Kendall \(\tau\)-Metric,” arXiv:2404.15126.
