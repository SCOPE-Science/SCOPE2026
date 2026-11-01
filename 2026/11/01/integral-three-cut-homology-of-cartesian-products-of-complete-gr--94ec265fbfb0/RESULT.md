# Integral three-cut homology of Cartesian products of complete graphs

## Finding

Let \(d\ge3\), and let \(q_1,\ldots,q_d\ge2\) be integers with at least one \(q_i\ge3\). Put
\[
G=K_{q_1}\square\cdots\square K_{q_d},\qquad N=\prod_{i=1}^d q_i.
\]
For the **ordinary** three-cut complex \(\Delta_3(G)\), whose facets are complements of disconnected induced triples, define
\[
E=\frac N2\sum_i(q_i-1),\quad F=\sum_i\frac N{q_i}\binom{q_i-1}{2},\quad
S=\sum_{i<j}\frac N{q_iq_j}\binom{q_i}{2}\binom{q_j}{2},
\]
\[
\mu=N-1-E+F+S,\qquad
h=\frac N2\sum_{\substack{J\subseteq\{1,\ldots,d\}\\|J|\ge3}}\prod_{j\in J}(q_j-1).
\]
Then, integrally and without torsion,
\[
\widetilde H_t(\Delta_3(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{\mu},&t=N-5,\\
\mathbb Z^h,&t=N-4,\\
0,&\text{otherwise}.
\end{cases}
\]
Moreover its Alexander dual \(K=\Delta_3(G)^\vee\) has the **integral homotopy type**
\[
K\simeq\left(\bigvee^{\mu}S^2\right)\vee
\left(\bigvee^h S^1\right).
\]
For these parameters \(\mu\ge1\) and \(h>0\). Although \(\Delta_3(G)\) is pure of dimension \(N-4\), it is not shellable. The theorem includes every multinary Hamming graph with at least three coordinates and every mixed-alphabet Cartesian clique product; previously studied binary cubes and two-factor rook graphs are boundary cases of its construction, not claimed as new.

## Assumptions and scope

All graphs are finite, undirected and simple. A vertex of \(G\) is a word with coordinate \(i\) in \(\{0,\ldots,q_i-1\}\); two vertices are adjacent precisely when they differ in exactly one coordinate. Three vertices induce a connected graph precisely when they span either a triangle or a path with two edges. A face of the combinatorial Alexander dual \(K\) is any set all of whose three-element subsets are connected in this sense. In particular, **all** pairs of vertices are edges of \(K\), whether or not they are edges of \(G\). The reduced homology convention is integral simplicial homology; the Alexander dual is taken on the complete \(N\)-vertex ground set.

## Proof

**1. Classify every dual facet.** A clique of \(G\) lies in one *coordinate line* (a set obtained by varying one coordinate with the others fixed). Suppose a dual face contains two vertices \(a,b\) that are nonadjacent in \(G\). For every third vertex \(c\) in the face, the triple \(\{a,b,c\}\) must be connected. Thus \(c\) must be adjacent to **both** \(a\) and \(b\). If the Hamming distance between \(a,b\) is at least three, there is no such \(c\), so the pair itself is maximal. If that distance is two, the common neighbors are precisely the other two corners of the unique coordinate square with \(a,b\) as opposite corners. Consequently every such face lies in that square's four-vertex simplex. Conversely, every three vertices of a coordinate square induce a length-two path, and every three vertices of one coordinate line form a triangle. The maximal faces of \(K\) therefore are: the full simplices on coordinate lines; the tetrahedra on coordinate squares; and the isolated long edges joining vertices of distance at least three. This argument also excludes all other higher-dimensional faces.

**2. Explicit elementary collapses.** Consider a coordinate square with cyclically ordered corners \(a,b,c,e\), where its perimeter edges are graph edges and its diagonals \(ac,be\) have Hamming distance two. The triangle \(abc\) is contained in no other maximal face, so collapse the square tetrahedron against \(abc\). The diagonal edge \(ac\) is then free in triangle \(ace\), because two vertices at distance two have exactly two common neighbors, both in their unique square. Collapse this triangle against \(ac\). What remains of the tetrahedron is the two-triangle disk \(abe\cup bce\), a triangulated square filling the perimeter. No square's removed triangles or diagonal edges occur in any other square, and none occur in coordinate-line simplices. These collapses can be performed for every square independently.

For each coordinate-line simplex choose one vertex \(o\) as apex. Pair every face \(T\) avoiding \(o\), with \(|T|\ge3\), with \(T\cup\{o\}\). Perform these elementary collapses in descending order of \(|T|\). Every such \(T\) is free when processed: its other cofaces have already been removed, and triangles within one line are not shared with any square. The remaining line complex is the contractible two-dimensional fan of triangles \(\{o,a,b\}\) over every edge \(ab\) avoiding \(o\), together with all line edges. This holds also for line size two, where the fan is simply one edge.

Let \(Y\) be the resulting subcomplex after **omitting** the long edges. Its one-skeleton consists of all \(E\) edges of the Cartesian graph, together with one diagonal per square. It has exactly \(F\) coordinate-fan triangles and two triangles per square. Equivalently, \(Y\) is a two-dimensional CW complex built from the graph's one-skeleton, filling each triangle within a coordinate clique and each coordinate square. There are \(S\) squares; the diagonal plus the two triangular faces representing each square contribute a net \(+1\) to Euler characteristic.

**3. Simply connectivity and homotopy type.** First, each square diagonal in a path can be replaced, using one of its filling triangles, by two perimeter edges; hence every loop in \(Y\) is homotopic to a loop in the Cartesian graph. Any edge path in the Cartesian graph changes one coordinate at a time. The filled squares permit two successive changes in **distinct** coordinates to be interchanged up to endpoint-fixed homotopy. The filled coordinate-line fans permit successive changes in the **same** coordinate to be shortened to one edge (and backtracking to be deleted). Hence every path from a fixed base word to any other word is homotopic relative endpoints to the canonical path that updates coordinates in increasing order. Every loop contracts. Thus \(\pi_1(Y)=0\).

Since \(Y\) is connected, simply connected and two-dimensional, its integral \(H_2\) is free, with rank \(\chi(Y)-1\). Its Euler characteristic, counted using the foregoing CW cells, is
\[
\chi(Y)=N-E+F+S,
\]
so \(\operatorname{rank}H_2(Y;\mathbb Z)=\mu\). By Hurewicz, maps of \(\mu\) two-spheres represent a homology basis; their wedge is a homology equivalence between simply connected CW complexes, hence a homotopy equivalence by Whitehead's theorem. Thus \(Y\simeq\bigvee^{\mu}S^2\). The \(h\) long edges all have endpoints in connected \(Y\); attaching each such one-cell is homotopy equivalent to adding a circle. Counting unordered pairs at Hamming distance at least three gives
\[
h=\frac N2\sum_{\substack{J\subseteq[d]\\|J|\ge3}}\prod_{j\in J}(q_j-1).
\]
It follows that \(K\simeq\bigvee^{\mu}S^2\vee\bigvee^h S^1\). The construction is integral and explicitly collapsible down to a two-complex; no numerical torsion assumption is made.

**4. Transfer by combinatorial Alexander duality.** Integral combinatorial Alexander duality on the \(N\)-vertex ground set gives
\[
\widetilde H_t(\Delta_3(G);\mathbb Z)\cong
\widetilde H^{N-t-3}(K;\mathbb Z).
\]
The wedge decomposition shows that the dual's cohomology is free and nonzero only in degrees one and two, with ranks \(h\) and \(\mu\). Substitution proves the two claimed homology groups and absence of torsion. Choosing two symbols from each of three distinct coordinates exhibits the six square faces of a three-cube inside \(Y\). Their oriented sum is a nonzero integral two-cycle, and \(Y\) has no three-cells, proving \(\mu\ge1\). Since \(d\ge3\), distance-three vertex pairs exist, so \(h>0\). Every facet of \(\Delta_3(G)\) has \(N-3\) vertices, making it pure of dimension \(N-4\); its nonzero degree-\(N-5\) homology rules out shellability of a pure complex.

## Verification

The reproducible `verify.py` reconstructs the Alexander dual independently from all connected induced triples, enumerates all possible faces up through a degree large enough to exclude unlisted higher faces, and compares them with the predicted coordinate-line, square and long-edge covers. It computes simplicial boundary ranks over \(\mathbb F_2\) independently of the collapse proof and checks the predicted degrees and multiplicities for factor sets \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((3,3,3)\), \((2,3,4)\), and \((2,2,5)\). The nonbinary three-coordinate instances have respective predicted pairs \((\mu,h)=(6,12),(20,36),(53,108),(43,72),(28,40)\). Finite mod-two ranks do **not** establish torsion-freeness or the infinite family; the collapse and duality proof supplies those facts.

## Relationship to prior work

Bayer et al., *Topology of Cut Complexes of Graphs* (first posted 26 April 2023), introduced the ordinary cut complex and classified cases including the clique prism \(K_n\square K_2\); that theorem is not a classification of general products with three or more factors. *Topology of Cut Complexes II* treats path grids and disjoint unions, not Cartesian clique powers. Published work on **total** two-cut complexes of Cartesian products of cliques studies a different complex. A previously published exact ordinary three-cut computation for **two-factor rook graphs** \(K_m\square K_n\) covers the two-factor specialization, and a prior binary-cube classification covers the all-binary specialization; both are expressly excluded from the claimed new domain. Their statements do not imply the classification for products with three or more factors and a nonbinary coordinate. A related Hamming-graph Čech complex is another construction with different face conditions. Originality searches and comparisons are documented in `AUDIT.json`.

## Limitations

No homotopy classification of \(\Delta_3(G)\) itself, equivariant homology representation, torsion in other cut parameters or shellability converse is claimed. The homotopy equivalence concerns its Alexander **dual**, not the cut complex. The result is not claimed new for two-factor rook graphs or all-binary cubes. Equivalent unindexed work may remain; database nonmatches are not proof of priority. The complete infinite-family argument relies on the stated elementary-collapse and path-homotopy lemmas; finite checker runs only corroborate small instances. No independent audit has been performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public version 2023-04-26; in particular the cut-complex definition, Table 1 and Section 7.3 (clique prisms).
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public version 2024-07-11; Section 5 (rectangular path grids).
3. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first public version 2026-02-24; Section 5.4 (Cartesian products for total two-cut complexes, not ordinary three-cut complexes).
4. *Integral and equivariant homology of three-cut complexes of rook graphs*, publicly indexed mathematical research finding (record `bd50464fc17f`), theorem and proof for two-factor rook graphs, accessed 2026-10-27.
