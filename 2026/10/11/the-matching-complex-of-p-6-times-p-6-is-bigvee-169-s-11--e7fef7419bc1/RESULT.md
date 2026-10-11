# The matching complex of \(P_6\times P_6\) is \(\bigvee^{169}S^{11}\)
## Finding
Let \(P_6\) be the path graph on six vertices and let \(P_6\times P_6\) denote the categorical graph product. Then its matching complex satisfies \(\mathsf{M}(P_6\times P_6)\simeq\bigvee^{169}S^{11}\). More precisely, \(P_6\times P_6\) is the disjoint union of two isomorphic connected components \(C\), each with 18 vertices and 25 edges, and \(\mathsf{M}(C)\simeq\bigvee^{13}S^5\); the join decomposition of the matching complex therefore gives the stated wedge of 169 eleven-spheres.

This is the first unordered parameter pair with both path factors at least six in the categorical-product family: every pair with a smaller factor is already covered, after swapping factors when necessary, by the cases with second factor at most five established in the cited source.

## Assumptions and scope
Here \(P_6\) is the simple path on vertex set \(\{0,1,2,3,4,5}\). The categorical product has vertex set \(V(P_6)\times V(P_6)\), and \((i,j)\) is adjacent to \((i',j')\) exactly when \(|i-i'|=|j-j'|=1\). The matching complex \(\mathsf{M}(G)\) has one vertex for each edge of \(G\), with simplices the pairwise vertex-disjoint edge sets.

The claim concerns only the finite graph \(P_6\times P_6\); it does not assert the all-parameter conjecture for larger categorical products.

## Proof
Every categorical-product edge changes both coordinates by one, so the parity of \(i+j\) is preserved. Exact reconstruction gives two connected parity components, each with 18 vertices and 25 edges. Reflection \((i,j)\mapsto(i,5-j)\) is an explicit isomorphism between them; call either component \(C\).

The complete matching complex \(\mathsf{M}(C)\) has 12,900 nonempty faces and face vector
\[
(25,244,1195,3139,4377,3001,846,72,1).
\]
A staged element matching pairs 6,443 face-poset cover relations. Orienting every unmatched Hasse cover downward and every matched cover upward produces a directed graph on all 12,900 nonempty faces. A complete topological sort of all 63,027 Hasse covers succeeds, proving that this is an acyclic discrete-Morse matching. Its critical simplices consist of one \(0\)-simplex and thirteen \(5\)-simplices, with no other critical simplices. Forman's theorem therefore gives
\[
\mathsf{M}(C)\simeq\bigvee^{13}S^5.
\]

For a disjoint union, a matching is uniquely the union of a matching from each component, hence
\[
\mathsf{M}(C\sqcup C)=\mathsf{M}(C)*\mathsf{M}(C).
\]
Using \(X*Y\simeq\Sigma(X\wedge Y)\) for the connected based CW complexes here,
\[
\left(\bigvee^{13}S^5\right)*\left(\bigvee^{13}S^5\right)
\simeq
\bigvee^{169}S^{11}.
\]
Since \(P_6\times P_6\cong C\sqcup C\), the result follows.

## Verification
The accompanying script `verify_p6p6_matching.py` reconstructs the graph from the categorical-product definition, checks that the two parity classes are connected and isomorphic, enumerates every matching of one component, rebuilds every Hasse cover, replays the fixed staged matching, and topologically sorts the resulting directed Hasse graph.

As an independent algebraic cross-check, it constructs every mod-\(2\) simplicial boundary matrix of \(\mathsf{M}(C)\). Their ranks are
\[
(24,220,975,2164,2213,775,71,1)
\]
in dimensions \(1\) through \(8\), yielding reduced Betti rank 13 only in degree \(5\) and zero in all other degrees. The Euler characteristic is \(-12\), consistent with \(\bigvee^{13}S^5\). The saved verifier output ends with the successful exact certificate summary.

## Relationship to prior work
Gupta, Sarkar, Sawant, and Shukla study exactly the categorical products \(P_n\times P_m\). Their Theorem 1.3 proves wedge-of-spheres homotopy types for \(3\le m\le5\), while their Conjecture 6.2 proposes the wedge-of-spheres conclusion for \(n\ge3\) and \(m\ge6\). By commutativity of the categorical product, all unordered parameter pairs with one factor below six are covered by their established small-width cases or the separately handled widths one and two. Thus \((6,6)\) is the first genuinely new symmetric boundary case of the conjectured regime.

Searches using the aliases categorical product, tensor product, direct product, Kronecker product, and the line-graph independence-complex formulation found no published exact evaluation of \(\mathsf{M}(P_6\times P_6)\). Nearby work on Cartesian small grids and polygonal line tilings concerns different graph families and does not imply this case.

## Limitations
The computation is exhaustive only for \(P_6\times P_6\). It does not provide a recurrence for larger widths, prove Conjecture 6.2 in general, or determine whether the same Morse pattern persists. The originality comparison is limited by the coverage of searchable published literature; an unindexed thesis, table, or finite computation could in principle contain the same isolated case.

## References
1. R. K. Gupta, S. Sarkar, S. S. Sawant, and S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298, first public 2024-03-22; later published in *Journal of Applied and Computational Topology*, DOI 10.1007/s41468-026-00238-y.
2. B. Braun and W. K. Hough, *Matching and independence complexes related to small grids*, *Electronic Journal of Combinatorics* 24(4) (2017), DOI 10.37236/6212.
3. T. Matsushita, *Matching complexes of small grids*, *Electronic Journal of Combinatorics* 26(3) (2019), DOI 10.37236/8480.
4. M. Bayer, M. Jelić Milutinović, and J. Vega, *General polygonal line tilings and their matching complexes*, *Discrete Mathematics* 346(7) (2023), 113428, DOI 10.1016/j.disc.2023.113428.
