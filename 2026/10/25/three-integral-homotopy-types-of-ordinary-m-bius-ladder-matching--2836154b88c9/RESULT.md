# Three integral homotopy types of ordinary Möbius-ladder matching complexes

## Finding

Write \(M_{2n}\) for the Möbius ladder with vertex set \(\mathbb Z/(2n)\mathbb Z\) and edges \(\{i,i+1\}\) for every cyclic index and \(\{i,i+n\}\) for \(0\le i<n\). Let \(\mathcal M(G)\) be the **ordinary matching complex**: the simplicial complex with graph edges as vertices and sets of pairwise vertex-disjoint graph edges as faces. Then the three exact, integral homotopy types are

\[
\begin{aligned}
\mathcal M(M_{12})&\simeq\bigvee^{10}S^3,\\
\mathcal M(M_{14})&\simeq\bigvee^{16}S^4,\\
\mathcal M(M_{16})&\simeq\bigvee^2 S^4\vee\bigvee^4 S^5.
\end{aligned}
\]

In particular, the third complex has essential reduced homology in two different dimensions. This is a classification of three specified sizes, not a periodicity theorem for the entire family.

## Assumptions and scope

Graphs are finite, simple and undirected. The three cases have, respectively, 12, 14 and 16 graph vertices, and 18, 21 and 24 graph edges. Every simplex is an arbitrary matching, whether or not extendable to a perfect matching. All homotopy equivalences and homology calculations are integral. An empty matching is included as the formal simplicial empty face, but is not a geometric cell.

For reproducibility, order graph edges lexicographically as sorted unordered endpoint pairs \((a,b)\) with \(0\le a<b<2n\). Encode a matching by its subset bitmask in that edge order. The program `check_mobius_matching.py` uses these conventions without an external mathematical package.

## Proof

**1. Exhaustive finite complexes.** For each \(n\in\{6,7,8\}\), enumerate all matchings by recursively adjoining only graph edges whose two endpoints are not already occupied and whose index exceeds every previously selected index. This lists every face exactly once: each matching has a unique increasing sequence of edge indices. The numbers of faces by cardinality (starting at cardinality zero) are

| \(n\) | Face counts, including the empty face |
| --- | --- |
| \(6\) | 1, 18, 117, 336, 420, 192, 18 |
| \(7\) | 1, 21, 168, 644, 1225, 1085, 371, 31 |
| \(8\) | 1, 24, 228, 1096, 2834, 3880, 2588, 696, 47 |

The verification program constructs these same face sets by a second, independent include/exclude dynamic program and checks equality of the sets.

**2. Deterministic acyclic matching.** Initially mark every face, including the formal empty face, as available. For each graph-edge index \(j\), in increasing order, scan still-available faces in increasing order of (face cardinality, integer bitmask). Whenever a face \(F\) omits \(j\) and both \(F\) and \(F\cup\{j\}\) are still available, pair those two faces and remove them from the available set. The empty face is paired with the first one-edge simplex; discard that formal pair and keep the one-edge simplex as a critical geometric vertex. All other pairs are retained as a matching on the nonempty face poset.

The program **exhaustively** constructs the complete codimension-one Hasse graph of the geometric face poset; it reverses the matched covering relations and applies Kahn's topological-sort algorithm. For \(n=6,7,8\), respectively, every one of the 3,990; 15,036; and 55,256 covering relations is processed, and the directed graph is acyclic. Consequently Forman's discrete Morse theorem produces a homotopy equivalent CW complex with exactly the following critical cells (all unlisted dimensions have none):

| \(n\) | Critical cell dimensions and counts |
| --- | --- |
| \(6\) | one 0-cell; two 2-cells; fifteen 3-cells; three 4-cells |
| \(7\) | one 0-cell; eight 3-cells; twenty-four 4-cells |
| \(8\) | one 0-cell; two 3-cells; twenty-three 4-cells; twenty-three 5-cells |

The numbers of ordinary paired geometric cell pairs are 540, 1,756 and 5,672 respectively. The code checks that each nonempty cell is either matched exactly once or is one of the displayed critical cells.

**3. Exact signed Morse boundaries.** Fix the orientation of every simplex by increasing graph-edge indices. For an oriented simplex \(U\), deleting the vertex at index position \(t\), counted from zero, has incidence sign \((-1)^t\). If a lower simplex \(L\) is matched upward to \(U\), eliminate its generator using the integral boundary relation \(\partial U=0\): substitute

\[
L=-[U:L]^{-1}\sum_{L'\ne L}[U:L']L',\qquad [U:L]\in\{+1,-1\}.
\]

Iterating these substitutions along the acyclic gradient paths and discarding cells that are matched as upper members computes the induced signed Morse differential. The file `check_mobius_matching.py` implements this precisely and also checks that the resulting differential squares to zero. The nontrivial integral boundary maps have the following sizes and **unit-pivot** ranks:

| \(n\) | Morse boundary | Matrix size | Integral unit-pivot rank |
| --- | --- | --- | --- |
| \(6\) | \(\partial_3:C_3\to C_2\) | 2 by 15 | 2 |
| \(6\) | \(\partial_4:C_4\to C_3\) | 15 by 3 | 3 |
| \(7\) | \(\partial_4:C_4\to C_3\) | 8 by 24 | 8 |
| \(8\) | \(\partial_4:C_4\to C_3\) | 2 by 23 | 2 |
| \(8\) | \(\partial_5:C_5\to C_4\) | 23 by 23 | 19 |

These are not merely rational ranks: the verifier reduces each displayed integer matrix to a diagonal consisting exclusively of \(\pm1\) units and zeros, using only integral row/column permutations and additions, and asserts that the residual matrix is zero. Therefore no non-unit Smith invariant factors occur. The program publishes SHA-256 digests of each actual signed Morse matrix alongside the deterministic matrix construction for reproducibility.

**4. Integral homotopy inference.** Each Morse complex has exactly one vertex and no 1-cells, hence is simply connected. The lowest positive-dimensional cells are 2-cells for \(n=6\) and 3-cells for \(n=7,8\). In all three cases, the boundary from the next dimension onto these lowest cells has full row rank and only unit Smith factors. Attaching maps in the first nontrivial dimension are therefore classified by their integral degrees. Elementary changes of cellular bases and homotopy cell cancellations kill all the lowest cells and equally many cells one dimension higher.

The resulting CW complexes have, respectively, 13 three-cells and 3 four-cells; 16 four-cells and no other positive-dimensional cells; and 21 four-cells and 23 five-cells. The surviving attaching maps from the next dimension are again determined entirely by their integral degree matrices, since \(\pi_d(\bigvee S^d)\cong\mathbb Z^r\) for \(d\ge2\). The remaining unit Smith factors cancel 3, 0 and 19 further neighboring cell pairs. The residual critical generators consist of ten 3-cells; sixteen 4-cells; and two 4-cells together with four 5-cells. All are attached trivially, proving exactly the three asserted sphere-wedge homotopy equivalences. In particular, higher homotopy attaching ambiguities cannot arise at these adjacent dimensions after the indicated cancellations.

## Verification

Run `python3 check_mobius_matching.py` with Python 3.8 or later and no third-party dependencies. Its exact stdout is `CHECK_OUTPUT.txt`. The program reconstructs every face, validates a second face-enumeration method, verifies every matched and unmatched codimension-one relation, tests acyclicity, computes signed Morse differentials, confirms \(\partial^2=0\), and performs integral unit-pivot reduction. Independently of Morse reduction, it computes all reduced mod-two Betti numbers using Gaussian elimination on the complete simplicial boundary matrices; these are, in order, ranks 10 in degree 3, 16 in degree 4, and ranks 2 and 4 in degrees 4 and 5, with no other nonzero reduced ranks. This mod-two agreement is corroborative, not a substitute for the integral proof and unit-pivot checks.

## Relationship to prior work

Agarwal and Basak, arXiv:2608.30601 (first submitted 31 August 2026; revised 14 September 2026), give homotopy classifications of the **independence** and **perfect matching** complexes of Möbius and circular ladders. Their Section 6, Problem 26 explicitly proposes studying the **ordinary matching** complexes as a distinct problem. None of their stated matching-complex theorems gives the present three types. For comparison, their even-width perfect-matching result for \(n=6,8\) has two spheres in degree \((n-2)/2\), unlike the ordinary matching results here.

The separately recorded ordinary matching complex of the eight-vertex Wagner graph and the ten-vertex Möbius ladder have smaller graph orders; they do not imply the three graph orders treated here. General polygonal line tilings (Bayer, Jelić Milutinović and Vega) concern open strings of polygons, not the closed twisted Möbius seam. Matsushita's grid-family result is for line graphs of open small grids and their stated extensions, not the graph family with a twisted cycle closure. The outerplanar matching-complex theorem is inapplicable because Möbius ladders are nonplanar. A separately indexed Heawood-graph matching complex also has sixteen four-spheres, but the Heawood graph has girth six while the fourteen-vertex Möbius ladder has four-cycles; equality of a Betti multiplicity does not identify the complexes. These relationships delimit the present finite computation; they do not establish novelty against every possible unindexed source.

## Limitations

Only the exact orders \(n=6,7,8\) are covered. There is no assertion of a formula, periodicity or universal sphere-wedge behavior for all Möbius ladders. The finite computations are exhaustive for the three stated complexes; numerical checks at these sizes are not an infinite-family proof. Potential unpublished, unindexed or inaccessible overlapping work remains a bibliographic risk. These results have undergone a self-review but **no independent audit**.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 2026-08-31, especially §§1, 3, 5–6. https://arxiv.org/html/2608.30601v2
2. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Mathematics 346 (2023), article 113428, DOI 10.1016/j.disc.2023.113428; preprint arXiv:2211.12559. https://doi.org/10.1016/j.disc.2023.113428
3. T. Matsushita, *Matching complexes of small grids*, Electronic Journal of Combinatorics 26 (2019), #P3.1, arXiv:1812.11000. https://arxiv.org/abs/1812.11000
4. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first public version 2024-11-07. https://arxiv.org/abs/2411.04601
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; standard acyclic matching and Morse CW-complex theory.
