# Nine integral four-spheres in the fully periodic five-by-five hard-square complex

## Finding
Let \(G=C_5\square C_5\) be the 25-vertex square toroidal grid, and let \(K=\operatorname{Ind}(G)\) be the simplicial complex of vertex subsets containing no adjacent pair. There is a homotopy equivalence
\[
K\simeq\bigvee^{9}S^4.
\]
In particular \(\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^9\), every other reduced integral homology group vanishes, and the integral homology has no torsion. The assertion specifies the homotopy type, not just the already studied signed independence-set count.

## Assumptions and scope
The vertices are indexed by \(v=5r+c\), for \(0\leq r,c<5\); coordinates are taken modulo \(5\). Distinct vertices \((r,c)\) and \((r',c')\) are adjacent exactly when one coordinate agrees and the other differs by \(\pm1\) modulo \(5\). The ordinary abstract simplicial complex includes all independent sets, including the empty set for enumeration; its geometric realization uses the nonempty faces. No diagonal edges or open/cylindrical boundary conditions are permitted. The result is specific to this 25-vertex graph and does not assert an all-size periodic-grid classification.

## Proof
We give a finite exhaustive acyclic discrete-Morse construction. The attached \(verify.py\) is a standalone integer/bitset implementation of every step; its loops enumerate a specified finite domain with no random choices, cutoffs, numerical tolerances, or external data.

First form a bitmask \(N(v)\) of the four neighbors of each index \(0\leq v<25\). Start with \(F_0=\{0\}\), encoding the empty face by zero, and for each \(v=0,\ldots,24\) adjoin all \(x\cup\{v\}\) where \(x\) is a previously constructed independent face and \(x\cap N(v)=\varnothing\). Induction on the maximum vertex of a face proves that the resulting bitmasks comprise **all** independent faces, with no duplicates. The exact face numbers in dimensions \(-1,0,\ldots,9\) are
\[
(1,25,250,1300,3850,6745,7100,4450,1550,250,10).
\]
Thus there are precisely \(25{,}531\) augmented faces.

Construct a matching sequentially on the augmented face poset. Let \(U\) initially contain every face. For each pivot \(v=0,\ldots,24\), pair **every** face \(x\in U\) not containing \(v\) for which \(x\cup\{v\}\in U\), and remove both endpoints immediately. For fixed \(v\), the proposed pairs have disjoint endpoints (one lacks \(v\), the other contains it), so the order of pairs within a stage is immaterial. The attached program checks membership and removes the endpoints. The 25 successive numbers of pairs are
\[
(5682,3771,1228,880,556,40,0,89,194,40,129,88,16,16,16,0,0,9,6,0,0,0,0,0,1).
\]
There are \(12{,}761\) matched pairs in the augmented face poset, leaving exactly nine unmatched five-vertex faces. The nine unmatched masks in increasing order are
\[
1196104,\ 1313284,\ 2360464,\ 2625576,\ 4235344,\ 4720898,\ 8425986,\ 8470786,\ 16850980.
\]

To establish **acyclicity**, orient every covering relation between a face \(\tau\) and a codimension-one subface \(\sigma\) as \(\sigma\to\tau\) when it is a matched pair, and as \(\tau\to\sigma\) otherwise. All such incidences are exhaustively enumerated by removing each set bit of every face. Kahn's exact topological-sort algorithm then removes all \(25{,}531\) vertices of this directed Hasse graph, so it contains no directed cycle. This is an exhaustive acyclicity verification, not merely a sample of gradient paths.

The augmented matching includes the pair consisting of the empty face and vertex \(0\). Delete that pair along with the empty face: the remaining matching on the ordinary nonempty face poset is still acyclic, since deleting vertices and edges cannot create a directed cycle. It has exactly one critical zero-cell, the singleton \(\{0\}\), and exactly nine critical four-cells; there are no other critical cells. Forman's acyclic matching theorem therefore yields a CW complex with one zero-cell and nine four-cells. As there are no positive-dimensional lower cells, all attaching maps of these four-cells land at the zero-cell and are null; hence this CW complex is \(\bigvee^9 S^4\). All stated integral homology conclusions follow.

## Verification
Execute `python3 verify.py` with a standard CPython installation. The complete face enumeration, face vector, matching-stage counts, remaining faces, and directed Hasse acyclicity are each asserted explicitly. The verifier prints `VERIFY_OK_TOROIDAL_FIVE_BY_FIVE_NINE_FOUR_SPHERES` only after all assertions pass. A sample deterministic output is supplied as `verification_output.txt`. The algorithm's finite exact enumeration and full directed-graph check are the computational certificate supporting the homotopy assertion.

## Relationship to prior work
Fendley, Schoutens and van Eerten introduced the doubly periodic hard-square model at negative activity. Jonsson's 2006 paper established the signed independent-set enumeration in terms of rhombus tilings for the **same doubly periodic grid family** and explicitly distinguished that Euler-characteristic information from complete homology. Bousquet-Mélou, Linusson and Nevo determined homotopy types for grid families with **open or cylindrical** boundary conditions, not for the present doubly periodic case. Jonsson's later study of cross-polytope cycles provides particular homology witnesses in periodic grids; the cited abstract and introduction do not establish the complete 25-vertex homotopy type. This result neither claims novelty for the known partition function nor assumes that a signed Euler count forces a wedge decomposition.

## Limitations
This is an exact finite certificate for one naturally defined toroidal graph; no general family theorem or symmetry representation is asserted. One potentially relevant 2010 article on cross-cycles was not accessible in complete form, so an unindexed equivalent calculation cannot be ruled out. The exhaustive checks have been performed with the included ordinary Python program; no external independent mathematical audit has been conducted.

## References
- P. Fendley, K. Schoutens and H. van Eerten, *Hard squares with negative activity*, arXiv:cond-mat/0408497 (public 24 August 2004), https://arxiv.org/abs/cond-mat/0408497.
- J. Jonsson, *Hard Squares with Negative Activity and Rhombus Tilings of the Plane*, Electronic Journal of Combinatorics 13 (2006), #R67, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v13i1r67/pdf/.
- M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, Journal of Algebraic Combinatorics 27 (2008), 423–450, https://arxiv.org/pdf/math/0701890.
- J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grids*, Discrete & Computational Geometry 43 (2010), 927–950, DOI:10.1007/s00454-009-9224-9.
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
