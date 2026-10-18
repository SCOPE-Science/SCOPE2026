# The complete frustration and symmetry spectrum of signed dodecahedral graphs

## Finding

For the dodecahedral graph \(D\cong\operatorname{GP}(10,2)\), let \(\sigma:E(D)\to\{+1,-1\}\) be an arbitrary signing. Vertex switching reverses all incident signs, and \(\ell(\sigma)\) denotes the minimum number of negative edges in its switching class, equivalently the line index of imbalance or frustration index. Each of the \(2^{11}=2048\) switching classes is counted once with its edges and vertices distinguished.

The complete frustration enumerator is

\[
F_D(z)=\sum_{[\sigma]}z^{\ell(\sigma)}
=1+30z+315z^2+1058z^3+577z^4+66z^5+z^6.
\]

Under the full automorphism group of \(D\), the corresponding numbers of switching-isomorphism classes at frustration values \(0,1,2,3,4,5,6\) are, respectively,

\[
(1,1,7,20,13,3,1),
\]

for a total of \(46\) symmetry types. The **unique** switching class with frustration \(6\) is represented by the all-negative signing (every pentagonal face has negative cycle sign). It contains exactly \(125\) minimal six-negative-edge edge sets, in bijection with the perfect matchings of the dual icosahedron. The maximum frustration value \(6\) itself is not claimed new; the complete distribution, symmetry refinement, uniqueness and minimizer correspondence are the retained findings.

More finely, if \(t\) is the number of negatively signed face boundaries (necessarily even), the counts of switching classes by \((t,\ell)\) are

| Negative faces \(t\) | Frustration \(\ell\) and number of classes |
|---|---|
| \(0\) | \(0:1\) |
| \(2\) | \(1:30,\ 2:30,\ 3:6\) |
| \(4\) | \(2:285,\ 3:210\) |
| \(6\) | \(3:842,\ 4:82\) |
| \(8\) | \(4:495\) |
| \(10\) | \(5:66\) |
| \(12\) | \(6:1\) |

## Assumptions and scope

All graphs are finite, simple, and undirected. \(D\) is the usual planar dodecahedral graph with \(20\) vertices, \(30\) edges, and \(12\) pentagonal faces. Its planar dual \(I=D^*\) is the icosahedral graph with \(12\) vertices, \(30\) edges, and degree \(5\). The face signs are products of primal edge signs along the facial boundaries. Vertex switching leaves all cycle signs invariant. Two signings are switching-isomorphic if a graph automorphism carries one into a switching-equivalent signing. No parallel-edge, weighted-signing, orientation, or embedding-variant claims are intended.

The dual \(I\) used for reproducibility has vertices \(0,1,\dots,11\). With \(u_i=1+i\) and \(v_i=6+i\), for \(i\in\mathbb Z/5\mathbb Z\), its edges are \(0u_i\), \(11v_i\), \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\), and \(u_iv_{i-1}\). All index arithmetic in these last expressions is modulo \(5\). The face-sign parity mask is the twelve-bit integer with the bit of each negative face set to \(1\).

## Proof

**Switching classification.** A switching class fixes the sign of every cycle. For a connected plane graph, the face boundaries generate its binary cycle space, with precisely the one dependence that their sum is zero. Hence the twelve face signs satisfy the single relation that their product is \(+1\), and otherwise determine the switching class uniquely. Conversely, every even subset \(T\subseteq V(I)\) of negative faces occurs: the edge-to-face-boundary map has rank \(11\), because the connected dual graph has vertex-edge incidence rank \(11\). Consequently there are exactly \(2^{11}=2048\) classes, indexed by even subsets \(T\).

**Frustration as a \(T\)-join.** Represent a negative primal edge by its corresponding dual edge. The odd-degree vertex set (modulo two) of the resulting dual edge set is exactly \(T\). Conversely, every dual \(T\)-join is the negative-edge set of a signing having the given face signs, thus belonging to the specified switching class. Therefore \(\ell(T)\) is the minimum number of dual edges in a \(T\)-join. Any \(T\)-join decomposes into trails pairing members of \(T\), together with closed trails, so its edge count is at least the sum of shortest-path distances for one such pairing. Conversely, select shortest paths for a pairing and take their symmetric difference. This produces a \(T\)-join with no more edges than the sum of their lengths. Thus equality holds in the shortest-path pairing formula.

**Exhaustive finite evaluation, without sampling.** Index vertices of \(I\) by \(0,\dots,11\). Define \(L(\varnothing)=0\). For each nonempty even set \(T\), let \(i\) be its least vertex, and set

\[
L(T)=\min_{j\in T\setminus\{i\}}\Bigl(d_I(i,j)+L(T\setminus\{i,j\})\Bigr),
\]

where \(d_I\) is the ordinary shortest-path distance in \(I\). By the previous paragraph, \(L(T)=\ell(T)\). This recursion visits every one of the \(2048\) even masks; the standalone program `code/verify_pairing.py` specifies the entire graph, recurrence, integer arithmetic, and exhaustive assertions. Independent breadth-first search over the \(2048\)-vertex parity state graph, whose transitions toggle exactly the endpoints of one dual edge, computes the same distance for each mask. `code/verify_bfs.py` implements that different method. The complete pointwise distances and symmetry-orbit representatives are recorded in `data/frustration_distances.csv` and `data/icosahedron_orbits.csv`. The two calculations agree for all masks, establishing the coefficient table, degree-of-frustration maxima, and the unique maximizing face mask \(T=V(I)\).

**Symmetry type count.** The second phase of `code/verify_bfs.py` takes three explicit permutations preserving the specified icosahedron adjacency and closes them under composition. It obtains \(120\) distinct automorphisms. This is the full group: an automorphism of the triangulated icosahedral graph is fixed by the image of an oriented triangular flag; there are at most \(12\cdot5\cdot2=120\) choices. The group preserves parity and frustration and its orbits on all \(2048\) masks are exhaustively enumerated. There are \(46\) orbits, with frustration multiplicities \((1,1,7,20,13,3,1)\). This is a classification by the *actual induced* graph symmetries, not simply by the number of negative faces.

**The 125-minimizer correspondence.** The all-negative primal signing has odd face sign on every pentagon; hence its class is \(T=V(I)\). Any \(T\)-join on twelve odd-degree vertices uses at least six edges. A six-edge \(T\)-join necessarily gives degree exactly one at each dual vertex, hence is a perfect matching; conversely every perfect matching supplies such a \(T\)-join. Applying the standard perfect-matching subset recurrence

\[
M(S)=\sum_{j\in N_I(i)\cap(S\setminus\{i\})}M(S\setminus\{i,j\}),
\qquad M(\varnothing)=1
\]

with \(i\) the least member of the even set \(S\), gives \(M(V(I))=125\). The standalone second implementation computes this exact count. Uniqueness of the maximizing switching class follows from the complete \(T\)-join table, not merely the existence of a six-edge matching.

## Verification

Use Python 3 with only the standard library. Starting in this package's root directory run `python3 code/verify_bfs.py`, then `python3 code/verify_pairing.py`. The first program generates the two CSV certificates in `data/`; the second independently reconstructs the icosahedron using adjacency sets, computes all-pairs graph distances and minimum pairing costs, and compares each of the 2048 resulting rows against the generated CSV. The expected textual outputs are `data/bfs_output.txt` and `data/pairing_output.txt`. Every count, recurrence, finite enumerative boundary, and the 120-element permutation group are machine-checkable from the supplied scripts. A completed exhaustive finite-state calculation proves a statement about this **fixed** 20-vertex graph; it is not an extrapolation to arbitrary generalized Petersen graphs.

## Relationship to prior work

Solé and Zaslavsky, *A Coding Approach to Signed Graphs* (1994), introduce the cut-code/switching-class equivalence and planar duality; their results also make the maximum-frustration value six accessible through dual Hamiltonicity. These reductions are not presented as new. Zaslavsky's 2012 signed-Petersen paper classifies the signings of the distinct ten-vertex **Petersen** graph rather than this twenty-vertex dodecahedron. Bowlin's 2012 maximum-frustration paper concerns bipartite signed graphs; \(D\) is not bipartite. Sehrawat and Bhattacharjya's 2019 signed generalized-Petersen paper studies maximum-frustration bounds, and its relevant bounds do not imply the per-class or automorphism-orbit enumerators here. Neither relevant accessible article was found to state the displayed dodecahedral distribution, its exact 46 symmetry classes, or the unique 125-minimizer worst class. Searches of mathematical research records likewise identified no prior claim entailing these exact statements; absence from searched databases alone cannot certify priority.

## Limitations

This is a complete classification for **one finite graph**, not an infinite-family theorem or an independent priority certificate. The classical correspondence of switchings, cuts, and dual \(T\)-joins, and the maximum frustration value six, predate this work. Relevant signed-graph computations may be present in older unindexed code, notes, books, or supplementary tables; a complete literature census is not asserted. The public source first-date field tracks a verified online public date, not a claim that the 1994 journal article was first disseminated that year. Independent scientific assessment has not been performed.

## References

1. Patrick Solé and Thomas Zaslavsky, *A Coding Approach to Signed Graphs*, SIAM Journal on Discrete Mathematics 7 (1994), 544–553. DOI: https://doi.org/10.1137/S0895480189174374. Author-hosted accessible full text: https://people.math.binghamton.edu/zaslav/Tpapers/cas.sidma1994.pdf.
2. Thomas Zaslavsky, *Six signed Petersen graphs, and their automorphisms*, Discrete Mathematics (2012). DOI: https://doi.org/10.1016/j.disc.2011.12.010.
3. Garry S. Bowlin, *Maximum Frustration in Bipartite Signed Graphs*, Electronic Journal of Combinatorics (2012). DOI: https://doi.org/10.37236/2204.
4. Deepak Sehrawat and Bikash Bhattacharjya, *Maximum Frustration in Signed Generalized Petersen Graphs* (2019), arXiv:1905.05548, https://arxiv.org/abs/1905.05548.
