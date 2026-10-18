# Point-exchange geodesics for ternary projective-plane transversals

## Finding
Let \(\Pi=\operatorname{PG}(2,3)\), the projective plane with thirteen points and thirteen four-point lines. Define a *line transversal* to be any set of points meeting every line; transversals containing a whole line are **included**. For \(0\leq k\leq13\), let \(\mathcal T_k\) be the transversals with \(k\) points, and let \(G_k\) be their point-exchange graph: two sets are adjacent when their symmetric difference has two points.

**Exact geodesic theorem.** For every integer \(6\leq k\leq13\), and every \(S,T\in\mathcal T_k\),
\[
 d_{G_k}(S,T)=k-|S\cap T|.
\]
Thus each \(G_k\) in this range is an isometric subgraph of the Johnson graph \(J(13,k)\). The threshold is sharp: \(G_5\) is the disjoint union of thirteen copies of \(K_9\), \(G_4\) consists of thirteen isolated vertices, and no transversals of size at most three exist.

At the first connected level \(k=6\), there are exactly \(702\) vertices and \(7{,}488\) edges. The \(468\) vertices containing a line have degree \(23\) and eccentricity \(5\); the \(234\) others have degree \(18\) and eccentricity \(6\). Consequently, \(G_6\) has radius \(5\) and diameter \(6\). The complete radius-diameter pairs \((\operatorname{rad}G_k,\operatorname{diam}G_k)\) for \(k=6,7,8,9,10,11,12,13\) are respectively
\[
 (5,6),\ (6,6),\ (5,5),\ (4,4),\ (3,3),\ (2,2),\ (1,1),\ (0,0).
\]
The respective numbers of vertices at these levels are \(702,1248,1170,702,286,78,13,1\).

## Assumptions and scope
The point set consists of one-dimensional subspaces of \(\mathbb F_3^3\); every line is a kernel of a nonzero linear functional, with scalar multiples identified. A transversal is defined solely by meeting all thirteen lines, whether or not it contains a complete line. A legal move simultaneously removes exactly one selected point and adds one unselected point, retaining the cardinality and the transversal condition. Distances are graph distances in the resulting finite, simple, undirected graphs. No assertion is made about planes of other orders, about moves of different cardinality, or about transversals that are required to contain no line.

## Proof
Every line of \(\Pi\) has four points and meets each other line, hence the thirteen lines are transversals. Exhaustive checking of the \(2^{13}=8192\) point subsets shows that no smaller transversal exists and that these are all size-four transversals. Every size-five transversal contains exactly one line; therefore it has the form \(L\cup\{p\}\) with \(p\notin L\). For each fixed \(L\), the nine choices of \(p\) form a clique \(K_9\); transversals with distinct contained lines cannot differ in one point. This proves the disconnected assertions.

At size six, a line-containing transversal is a line together with two points from its nine-point complement. No six-point set contains two lines, because two distinct four-point lines have seven points in their union. Thus there are \(13\binom92=468\) line-containing six-point transversals. The other \(234\) are exactly the sets of six nonvertex points on the three sides of a projective triangle. There are \(\binom{13}{3}-13\binom43=234\) triples of nonconcurrent lines, and the checker verifies that these yield distinct transversals and exhaust every six-point transversal containing no line. This geometric classification is a computed finite input, not claimed as a new classification of minimal blocking sets.

For any two \(k\)-sets \(S,T\), each point exchange increases \(|S\cap T|\) by at most one, so every path from \(S\) to \(T\) has length at least \(k-|S\cap T|\). For the reverse inequality, the finite *target-directed exchange property* is checked exhaustively: for every \(k\in\{6,\ldots,13\}\) and every distinct ordered pair \((S,T)\in\mathcal T_k^2\), there exist \(a\in S\setminus T\) and \(b\in T\setminus S\) for which \((S\setminus\{a\})\cup\{b\}\in\mathcal T_k\). The checker performs this test directly on all \(3{,}995{,}862\) distinct ordered pairs, not on a sample. Iterating the certified exchange decreases the intersection deficit by exactly one until reaching \(T\), proving the distance identity by induction on \(k-|S\cap T|\).

The stated radii and diameters follow by maximizing the proved explicit distance formula over the completely enumerated families. At size six, independent breadth-first searches from every one of the \(702\) vertices corroborate each individual distance and yield the two eccentricity classes. The edge and degree counts follow from the exact adjacency census.

## Verification
Run `python verify_pg3.py` with Python 3.9 or later; no third-party packages or downloaded tables are required. The script builds the projective plane twice: once using homogeneous-coordinate dot products, and again using nine affine points, twelve affine lines, four directions at infinity, and the line at infinity. It constructs an explicit point bijection and checks agreement of the two incidence relations and their complete transversal enumerations. It then checks the universal target-directed exchange property for every directed pair at each \(k\), enumerates the size-five components, verifies the size-six triangle classification, counts size-six edges and degrees, and independently compares all size-six breadth-first-search distances to the proposed Johnson distances. `certificate.json` records the successful exact counts, and is reproducible by redirecting the script output.

The finite verification of a universal statement over at most thirteen points is exhaustive; it makes no infinite-family inference. In particular, the proof relies on the explicitly supplied source code and its reproducible execution, not on a log alone.

## Relationship to prior work
Work on projective-plane blocking sets established their static geometry and minimum-size theory long before this calculation. In particular, the published classification of minimal blocking sets in planes of order at most eight by Coolsaet, Botteldoorn and Fack is a close static comparator; the line and triangle census above is not claimed as new. The contribution is instead the *entire target-directed point-exchange property*, its isometric Johnson distances across all cardinalities from six through thirteen, and the exact sharp disconnected-to-isometric threshold and metric profile. Static classifications of minimal transversals do not alone assert this all-pairs shortest-path property. General token-jumping results on claw-free graphs concern independent sets, not arbitrary hypergraph line transversals; they do not yield the stated geometry-specific geodesics. Nor is this a direct application of the matroid basis-exchange theorem: for the six-transversal family, the strong basis-exchange axiom fails, as the reproducible program verifies using the masks `63` and `1182` and removal of point index `0`. The weaker *existence of some target-directed move* nevertheless holds for every pair. The closest accessible sources and access limitations are described in `REVIEW.md` and `AUDIT.json`.

## Limitations
The theorem is for the unique projective plane of order three, not a uniform statement for other prime powers. The isometry test is a finite computer-assisted proof through a transparent complete case analysis, rather than an algebraic formula for selecting each move without reference to the thirteen-point incidence table. The full text of one relevant published static classification was not available through the attempted lawful access routes; an unstated exchange corollary there or in unindexed work remains an originality risk. No independent external audit has occurred.

## References
1. A. A. Bruen, “Blocking Sets in Finite Projective Planes,” *SIAM Journal on Applied Mathematics* 21 (1971), 380–392. DOI: 10.1137/0121041.
2. P. Sziklai and G. Van de Voorde, “A small minimal blocking set in \(\operatorname{PG}(n,p^t)\), spanning a \((t-1)\)-space, is linear,” arXiv:1210.1003v1 (first public version, 2012-10-03), https://arxiv.org/abs/1210.1003.
3. P. Bonsma, M. Kamiński and M. Wrochna, “Reconfiguring Independent Sets in Claw-Free Graphs,” arXiv:1403.0359v1 (first public version, 2014-03-03), https://arxiv.org/abs/1403.0359.
4. K. Coolsaet, A. Botteldoorn and V. Fack, “Classification of minimal blocking sets in small Desarguesian projective planes,” *Journal of Combinatorial Designs* 30 (2022), 561–580. DOI: 10.1002/jcd.21842.
5. T. Ito et al., “On the complexity of reconfiguration problems,” *Theoretical Computer Science* 412 (2011), 1054–1065. DOI: 10.1016/j.tcs.2010.12.005.
