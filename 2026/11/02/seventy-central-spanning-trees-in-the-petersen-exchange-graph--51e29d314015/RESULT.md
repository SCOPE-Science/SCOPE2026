# Seventy central spanning trees in the Petersen exchange graph

## Finding
Let \(P\) be the Petersen graph with vertices the two-element subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. Its spanning-tree exchange graph \(\mathcal T(P)\) has a vertex for each spanning tree of \(P\), and joins two trees when one edge is deleted and a different edge is inserted, leaving a spanning tree. Then \(\mathcal T(P)\) is connected on exactly \(2000\) vertices, with radius \(5\), diameter \(6\), exactly \(70\) central vertices, and \(1930\) peripheral vertices. A tree is central if and only if its six-edge complement in \(P\) contains a cycle; among the central trees, \(60\) have a complementary five-cycle and \(10\) a complementary six-cycle.

The exact distance enumerator over unordered **distinct** spanning-tree pairs is
\[
28140z+222360z^2+651080z^3+748200z^4+314220z^5+35000z^6.
\]
Thus the exchange graph has \(1,999,000\) unordered pairs and Wiener index \(7,200,000\). The previously known count of \(2000\) spanning trees, the definition of the exchange graph, and the general exchange-distance identity are not claimed as new.

## Assumptions and scope
All graphs are finite, simple, and labelled as stated. Each spanning tree has exactly nine of the fifteen edges of \(P\). The exchange graph uses **unrestricted** one-edge basis exchange, not only exchanges along cycles of specified lengths. Distances are unweighted graph distances; eccentricity is the maximum distance from a vertex. A central vertex has minimum eccentricity, while a peripheral vertex has maximum eccentricity. An unordered pair is counted once and diagonal pairs are excluded.

## Proof
**General exchange distance (previously known).** For two spanning trees \(T,U\) of any connected graph on the same vertex set, every single exchange changes at most one member of \(T\setminus U\). Conversely, if \(e\in U\setminus T\), insertion into \(T\) creates a unique cycle containing some edge \(f\in T\setminus U\), and exchanging \(f\) for \(e\) reduces \(\lvert T\setminus U\rvert\) by one. Hence \(d(T,U)=\lvert T\setminus U\rvert\), an identity also stated in Dara et al., Lemma 2.3 (2016).

**Central-tree characterization.** Fix \(T\), and put \(H=E(P)\setminus T\), a six-edge spanning subgraph. The maximum number of edges of \(H\) that a spanning tree \(U\) can contain is the graphic-matroid rank \(r(H)\): an acyclic subset of \(H\) can always be extended to a spanning tree of the connected graph \(P\). Thus
\[
\operatorname{ecc}_{\mathcal T(P)}(T)=\max_U\lvert U\setminus T\rvert=r(H).
\]
The Petersen graph has girth five, so a six-edge subgraph has at most one cycle. Consequently \(r(H)=6\) for an acyclic \(H\), and \(r(H)=5\) if \(H\) contains a five- or six-cycle. Both cases occur by the constructions below.

There are exactly 12 five-cycles and 10 six-cycles in \(P\) (verified directly by the cycle enumeration in `verify_direct.py`; these classical cycle counts are also listed by Brouwer). Each five-cycle \(C\) has as its complementary induced subgraph on the other five vertices another five-cycle, with five matching edges joining the two cycles. For \(E(P)\setminus T\) to contain \(C\), the sixth deleted edge must lie on the other five-cycle: deleting a matching edge instead leaves that other cycle inside \(T\), making \(T\) non-acyclic. All five choices on the other cycle give trees (a four-edge path with five pendant edges). This yields \(12\cdot5=60\) central trees with a complementary five-cycle.

For each six-cycle \(C\), the remaining nine edges form a spanning tree. Indeed, the six vertices on \(C\) each have exactly one unused incident edge and no chord (a chord would create a triangle or four-cycle). Those six remaining edges run to the four vertices off \(C\), and the latter have three internal edges; as the graph is triangle-free, these three edges form a tree. This gives ten more central trees. No six-edge subgraph contains two distinct cycles, so the cases are disjoint. Therefore \(70\) of the \(2000\) spanning trees have eccentricity five and \(1930\) have eccentricity six. The asserted radius, diameter, and connectedness follow.

**Pair-distance polynomial.** For each forest \(F\subseteq E(P)\), let \(\tau_F\) be the number of spanning trees containing all edges of \(F\); if \(F\) is cyclic, put \(\tau_F=0\). Contraction and the Matrix–Tree Theorem give \(\tau_F=\tau(P/F)\), counting parallel edges with multiplicity. Define
\[
A_j=\sum_{\substack{F\subseteq E(P)\\\lvert F\rvert=j}}\tau_F^2.
\]
The exact reduced-Laplacian determinants, exhaustively computed for all \(2^{15}\) edge subsets by `verify_contraction.py`, give
\[
(A_0,\ldots,A_9)=(4000000,21600000,49464000,62475840,47399640,22052160,6159040,966960,74280,2000).
\]
The identity
\[
\sum_{T,U}y^{\lvert T\cap U\rvert}
=\sum_{F\subseteq E(P)}\tau_F^2(y-1)^{\lvert F\rvert}
=\sum_{j=0}^{9} A_j(y-1)^j
\]
follows by expanding \(y^{\lvert T\cap U\rvert}=(1+(y-1))^{\lvert T\cap U\rvert}\) and interchanging the finite sums. Converting intersection size \(s\) to distance \(9-s\), discarding the 2000 diagonal pairs and dividing the remaining ordered counts by two, gives exactly the asserted distance polynomial. The sum of its coefficients is \(1,999,000=\binom{2000}{2}\), and its derivative at \(z=1\) is \(7,200,000\).

## Verification
Run `python verify_direct.py` and `python verify_contraction.py` with Python 3 and no third-party dependencies. The first enumerates all \(\binom{15}{9}=5005\) nine-edge subsets, checks connectivity with a union-find rank calculation, counts all \(\binom{2000}{2}\) tree pairs, and independently enumerates the five- and six-cycles and central configurations. The second enumerates all \(2^{15}\) edge subsets and applies a fraction-free Bareiss determinant algorithm to every contracted graph. It verifies all ten forest moments and the resulting complete pair-distance histogram. Both executables terminated with explicit PASS messages. Each checks a finite *exhaustive* universe; no sampled extrapolation or assertion about other graph families is involved.

## Relationship to prior work
Cummins introduced tree graphs in 1966. Dara, Hegde, Deva, Rao and Zaslavsky (arXiv:1601.01041, first submitted January 6, 2016) prove the general edge-exchange distance identity and study forest-graph operator dynamics, without evaluating the Petersen-specific radius, centers, or pair-distance polynomial. Brouwer's Petersen graph description gives its model, symmetry and classical cycle census; it does not state these exchange-graph statistics. Kim and Oum (2025) prove Hamiltonicity and pancyclicity results for general matroid basis graphs, which likewise do not determine the present metric census. The historical 2000-tree count and any general base-exchange theorem are expressly excluded from the novelty claim.

## Limitations
This is an exact result for one canonical finite graph, not a formula for arbitrary cubic graphs or generalized Petersen graphs. The computational portion is supported by two reproducible exhaustive algorithms, not by a formally checked proof. An equivalent historical computation might exist in an unindexed table or manuscript, including the partially accessible paper *The Petersen Matroid*; no absolute priority claim is made. No mixing-time or spectral-gap theorem for a random exchange walk is asserted.

## References
1. S. Dara, S. M. Hegde, V. Deva, S. B. Rao, T. Zaslavsky, *The Dynamics of the Forest Graph Operator*, arXiv:1601.01041 (2016), especially Lemma 2.3. https://arxiv.org/abs/1601.01041
2. A. E. Brouwer, *The Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (classical structural and cycle data).
3. D. Kim and S.-il Oum, *Note on Hamiltonicity of Basis Graphs of Even Delta-Matroids*, Journal of Graph Theory 109 (2025), 446–453. https://doi.org/10.1002/jgt.23237
4. T. A. Al-Hawary, *The Petersen Matroid*, a relevant partially accessible manuscript. https://www.researchgate.net/publication/266273614_The_Petersen_matroid
