# Integral homology and two-connectivity of the four-cube perfect-matching complex

## Finding

Let \(Q_4\) be the graph with vertex set \(\{0,1\}^4\) and edges between binary vectors differing in one coordinate. Its perfect-matching complex \(\mathcal P(Q_4)\) has the 32 edges of \(Q_4\) as vertices; a collection of graph edges is a simplex precisely when it is contained in a perfect matching of \(Q_4\). Then its **integral reduced homology** is

\[
\widetilde H_j(\mathcal P(Q_4);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{54},&j=3,\\
\mathbb Z^{21},&j=4,\\
0,&\text{otherwise}.
\end{cases}
\]

Furthermore \(\mathcal P(Q_4)\) is **2-connected**, so \(\pi_1=\pi_2=0\), and the Hurewicz isomorphism gives \(\pi_3\cong\mathbb Z^{54}\). In particular its integral homology has no torsion. **No wedge-of-spheres homotopy classification is asserted**: the homology calculations alone do not determine potential higher attaching maps.

## Assumptions and scope

The graph is the 16-vertex four-dimensional *binary* hypercube, equivalently the Cartesian product of four copies of \(K_2\) or the 4-by-4 toroidal square grid. The complex is the *extendable perfect-matching complex*, distinct from the ordinary matching complex, independence complex, or discrete-Morse complex. Facets have eight graph edges, hence simplicial dimension seven. All homology coefficients in this statement are \(\mathbb Z\). The result is one natural finite complex, not a claim for all hypercubes.

## Proof

**Full face description.** Encode each cube vertex by an integer from zero through fifteen, and an edge as an unordered pair \(\{a,a\mathbin{\mathrm{xor}}2^i\}\) for a coordinate \(i\in\{0,1,2,3\}\). There are exactly 32 graph edges. To enumerate a perfect matching without repetitions, take the smallest unmatched vertex \(a\), pair it successively with each of its unmatched neighbors, and recursively match the remaining vertices. This exhausts all matchings because every perfect matching has exactly one incident edge at \(a\). The checker finds 272 distinct perfect matchings. Insert every submask of their eight-edge characteristic masks; the resulting 30,561 faces, including the empty face, have dimension-wise counts

\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(32,400,2496,7776,10560,6848,2176,272).
\]

**Fundamental-group and second-homotopy certificate.** `q4_verifier.py` constructs a matching on the nonempty face poset: in each round, choose the currently best available graph-edge toggle and pair every available \(\sigma\) with \(\sigma\cup\{e\}\) when both faces survive. It explicitly orients every codimension-one incidence downward except that matched incidences point upward, and checks that the entire directed incidence graph has a topological ordering. There are 150,688 covering incidences, 15,179 matched pairs, and precisely one critical 0-cell, 114 critical 3-cells, 84 critical 4-cells and three critical 5-cells. Therefore Forman's cellular discrete-Morse theorem gives a CW homotopy model with one 0-cell and no 1- or 2-cells. By cellular approximation every map from a 1- or 2-sphere into that model is null-homotopic: \(\pi_1=\pi_2=0\).

**Independent integral chain certificate.** Separately from that matching, the checker repeatedly removes a positive-dimensional free face and its unique codimension-one coface. There are exactly 10,974 certified elementary simplicial collapses. The remaining subcomplex has 8,613 faces, including the empty face, with

\[
(f_0,f_1,f_2,f_3,f_4)=(32,397,2069,3925,2189).
\]

Since every step is an elementary collapse, this subcomplex is homotopy equivalent to the original. Orient each positive-dimensional face by increasing graph-edge index. Its integral differential sends an oriented \(d\)-face to the signed alternating sum of its \((d-1)\)-faces. The checker builds all of these integer matrices and repeatedly contracts a differential coefficient \(+1\) or \(-1\), using the exact corresponding elementary integral row/column operations. Such a unit pivot splits off a contractible two-term summand and therefore preserves integral homology. Proceeding from degree four down to degree one, the exact numbers of unit cancellations are respectively 2,168; 1,703; 366; and 31. Every residual differential has **all coefficients identically zero**, not merely zero modulo a prime. The surviving integral chain groups have ranks

\[
(\operatorname{rank}C_0,\ldots,\operatorname{rank}C_4)
=(1,0,0,54,21).
\]

Thus reduced homology has exactly the announced free summands, with no uncomputed torsion. Together with 2-connectivity, Hurewicz identifies \(\pi_3\). The independent mod-two rank calculation is a cross-check, not the basis for the integral conclusion.

## Verification

Run the included standalone standard-library script via `python3 q4_verifier.py`. The included `CHECK_OUTPUT.txt` is its actual output. The program needs no external input, mathematical libraries, seed or network. It checks all face masks and directed Hasse incidences, every claimed simplicial free-face pairing, each integer pivot and every final zero differential; assertion failures abort verification. The elementary collapses and exact integer chain reduction are independent of the discrete-Morse matching used to establish 2-connectivity. The calculations establish a **finite** exact theorem, without extrapolation to higher-dimensional cubes.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega (first arXiv version 2022-09-06) define and study extendable perfect-matching complexes for honeycomb graph families. Their analyzed families are not the four-dimensional cube. Chandrakar and Singh (2024 preprint) study perfect-matching complexes of polygonal line tilings, not this toroidal 4-by-4 graph. Relevant earlier and indexed results on the ordinary matching complexes of three-cubes or planar 4-by-4 grids, or on four-cube independence complexes, are mathematically different constructions and do not imply this calculation. The comparison does not establish global uniqueness; an unindexed equivalent result remains possible.

## Limitations

This proof is computationally assisted for one explicit 16-vertex graph, though the code exhaustively certifies the finite combinatorial statements and works with signed **integer** differentials. Its two homology degrees and 2-connectivity do not determine all higher homotopy groups or homotopy attaching maps; in particular no sphere-wedge splitting or equivariant representation is claimed. The originality comparison is limited to accessed sources and searched databases. Independent external review has not been performed.

## References

1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first publicly posted September 6, 2022).
2. H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first publicly posted 2024).
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete-Morse homotopy theorem).
