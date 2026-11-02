# All optimal majority C-colourings of the ternary Hamming three-cube

## Finding

Let \(H=K_3\square K_3\square K_3\) be the 27-vertex Hamming graph on triples in \(\{0,1,2\}^3\): two vertices are adjacent if their triples differ in exactly one coordinate. A majority C-colouring is a partition into nonempty classes \(S\) with \(\deg_{H[S]}(v)\ge 3\) for each \(v\in S\). The maximum of four classes was established previously by Lu (2026); it is not claimed here as new.

**Complete classification and census.** In every four-class majority C-colouring of \(H\), the class sizes are exactly \(6,6,6,9\). Each six-vertex class is a coordinate box with respective coordinate sizes \(3,2,1\), and **all three six-vertex classes have the same full-length coordinate axis**. In fact all four classes are cylinders along that axis. Projecting onto the other two coordinates produces a partition of a \(3\times3\) rook graph into three disjoint adjacent pairs and one triple whose induced subgraph has no isolated vertex. Conversely every such projected partition, lifted along any of the three axes, is a four-class majority C-colouring.

There are precisely **288** such partitions into unordered classes, or **6912** onto colourings with four prescribed named colours. Under the full graph automorphism group of order \(1296\), the \(288\) partitions form exactly **three orbits of sizes \(18,54,216\)**. Among projected partitions, the nine-vertex class corresponds to a straight three-cell line in \(72\) cases (over all three axes), forming the first two orbits, and to an L-shaped three-cell triple in \(216\) cases, forming the last orbit.

## Assumptions and scope

The graph is the *ordinary* Cartesian product of three copies of \(K_3\), not the distinct Hamming-distance-two threshold graph. No proper-colouring condition is imposed: same-colour neighbors are required, not forbidden. Each vertex of \(H\) has degree six; the weak-majority condition is therefore exactly three or more same-class neighbors. Distinct named colours are counted as different functions, whereas the \(288\) partitions do not distinguish permutations of colours. No general claim for other alphabet sizes or dimensions is made.

## Proof

**1. Exhaustive local-class lemma.** Index the \(27\) triples lexicographically as \(v_0,\dots,v_{26}\). Let \(A_i\) be the exact six-neighbor bit mask of \(v_i\). For any nonzero bit mask \(S\), define
\[
Q(S)\quad\Longleftrightarrow\quad
\forall i\ (v_i\in S\implies \operatorname{popcount}(A_i\mathbin{\&}S)\ge3).
\]
The companion `verify.py` iterates, without sampling or pruning, all \(\binom{27}{j}\) subsets for every \(1\le j\le7\); there are exactly \(1,285,623\) tests. The resulting exact valid counts for sizes \(1,\ldots,7\) are \((0,0,0,0,0,54,0)\). It independently constructs the \(54\) distinct boxes with coordinate sizes \((3,2,1)\) in any coordinate order: choose the full-length axis in three ways, the two-value axis in two ways, the one-value coordinate in three ways, and the two selected values in three ways. Its exact comparison of their bit masks with the entire size-six solution set proves that **all** six-vertex majority classes are precisely these boxes, and that no seven-vertex majority class exists. The finite search is a complete, auditable exhaustive proof of this fixed graph's lemma; no truncated computation or extrapolation is used.

**2. Exhaustion of four classes and common-axis rigidity.** Each nonempty colour class has at least six vertices, and five classes would need at least \(30>27\) vertices. In any four-class partition, the size restrictions together with the absence of size-seven classes force the multiset \((6,6,6,9)\). There are exactly \(\binom{54}{3}\) candidate triples of size-six boxes. The verifier enumerates every such triple, rejects intersections, and checks \(Q\) on the nine-vertex complement. There are \(540\), \(972\), and \(54\) pairwise-disjoint triples using respectively one, two, or three distinct full-length axes. Exactly \(288\), \(0\), and \(0\) have majority-valid complements. Thus all optimal four-class partitions, and only those, use one common full-length axis. In the complement the same axis is necessarily full-length too. This also proves the total \(288\) without an assumption about axis alignment.

**3. Independent quotient count and structural description.** Fix the common full-length axis. Every class is a cylinder over a subset of the remaining \(3\times3\) rook graph. A vertex in a cylinder already has two same-colour neighbors from the full-length axis, so the majority condition becomes: every occupied quotient cell must have at least one adjacent cell in its own quotient part. Every six-vertex class projects to an adjacent pair. The residual three quotient cells likewise form a subgraph without isolates: either a straight line (six choices) or a right-angle path / L (36 choices). Direct enumeration of the rook-graph edges shows that, conditional on a fixed residual straight line, the complementary six cells have four unordered matchings into three rook edges; conditional on an L, they have two. Therefore there are \(6\cdot4+36\cdot2=96\) partitions per axis, and \(3\cdot96=288\) total, independently agreeing with the direct 27-vertex census.

**4. Orbit census.** The full automorphism group is \((S_3)^3\rtimes S_3\), acting by independent alphabet permutations and coordinate permutations, of order \((3!)^3(3!)=1296\). This is the full group: an automorphism is determined by the image of one vertex (27 possibilities) and its induced action on that vertex's neighborhood (at most \(3!\,2^3=48\), since the neighborhood induces three disjoint edges), which subsequently determines all vertices at distance two and three by their adjacency relationships. The verifier constructs all \(1296\) distinct permutations explicitly and tests adjacency preservation. It acts on every one of the \(288\) unordered partitions and removes complete orbits; the sizes are exactly \(18,54,216\). Of these, \(18+54=72\) have a straight residual triple, and \(216\) have an L-shaped residual triple. The \(4!\) possible bijections of the four classes with four named colours finally give \(288\cdot24=6912\) onto four-colour functions.

**5. Existence witness.** For \((x,y,z)\in\{0,1,2\}^3\), let its colour be the entry in row \(x\), column \(y\) of the array
\[
\begin{pmatrix}0&1&0\\3&1&3\\0&2&2\end{pmatrix}.
\]
This uses four colours and each same-colour degree is at least three, as checked directly on the original graph. This confirms existence without depending on the prior scalar theorem.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter; no packages, downloaded data, or external files are needed. The checker separately constructs the original graph adjacency masks; exhaustively tests all \(1,285,623\) vertex subsets up to size seven; classifies all \(54\) six-vertex majority classes; examines every three-box selection and every permissible nine-vertex complement; independently counts perfect-matchings on the rook quotient; validates the explicit four-colour witness; constructs every full graph automorphism and computes every partition orbit. Expected final output includes `ALL_OPTIMAL_UNLABELLED_PARTITIONS_OK 288`, `FULL_AUTOMORPHISM_ORBIT_CENSUS_OK [18, 54, 216]`, `NAMED_FOUR_COLOURINGS_OK 6912`, and `VERIFY_OK`. Exact integer and bitwise operations are used throughout. This is a complete finite certificate for this 27-vertex case, not a claim of independent external certification.

## Relationship to prior work

Bujtás, Dettlaff, Furmańczyk, and Laskowska (2026), *Majority C-coloring of graphs* [1], define the majority C-colouring parameter and related alliance formulations. Their subsequent paper *Majority C-coloring in Cartesian products* [2] asks for the optimal number of classes in odd-dimensional balanced Hamming products. **Lu (2026) [3] already determines the exact maximum for all balanced odd-dimensional Hamming graphs**, and his theorem gives four for the ternary three-cube. His paper also constructs optimal rectangular partitions and proves minimum-class-size bounds. The present result does not claim priority for the four-class value, the underlying class-size lower bound, or existence of one rectangular construction: it instead classifies **all** extremal partitions in the ternary three-cube, proves common-axis rigidity, counts all named and unnamed optima, and identifies the complete automorphism orbit profile. The inspected primary texts do not state that complete enumeration or orbit classification. Related strong-defensive-alliance partitions are equivalent formulations, not independent new invariants.

## Limitations

The result is an exact finite classification for \(H=K_3\square K_3\square K_3\). The executable exhaustive certificate is essential to the small-class and mixed-axis exclusion lemmas; it has not been replaced by a purely symbolic family-wide classification. Its result does not transfer to higher dimensions, other alphabets, or distance-two Hamming graphs. The available primary sources and indexed mathematical records provide evidence for originality of the optimizer census, not a proof of historical uniqueness. Independent mathematical audit has not been performed.

## References

[1] Z. Bujtás, M. Dettlaff, H. Furmańczyk, and M. Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752 (first public version April 22, 2026).

[2] Z. Bujtás, M. Dettlaff, H. Furmańczyk, M. Laskowska, and Z. Tuza (revised version), *Majority C-coloring in Cartesian products*, arXiv:2608.27669 (first public version August 27, 2026).

[3] ZeHua Lu, *Exact majority C-colourings of balanced Hamming graphs and grids*, arXiv:2609.31674 (first public version September 16, 2026), Theorem 1 and Sections 2–4, 7.
