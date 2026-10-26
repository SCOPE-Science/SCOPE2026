# Five disconnected metric-basis exchange components of the Desargues graph

## Finding

Let \(D\) be the Desargues graph, equivalently the generalized Petersen graph \(GP(10,3)\) or the bipartite double cover of the Petersen graph. Its metric dimension is \(3\). Every metric basis has three vertices whose projections to the Petersen graph are three distinct edges of a common star of \(K_5\), with either of the two covering signs selected independently on each edge. Conversely, every such signed star triple is a metric basis. There are exactly \(160\) metric bases.

Let \(\mathcal B(D)\) have these bases as vertices, with two bases adjacent precisely when one landmark is replaced and the resulting set remains a metric basis. Then
\[
\mathcal B(D)=\bigsqcup_{x\in[5]}\mathcal B_x,
\]
where the five components are indexed by star centers \(x\). Every component has \(32\) vertices, is \(9\)-regular with \(144\) edges, and has radius and diameter \(3\); the whole exchange graph has \(720\) edges. From every basis, the numbers of bases at graph distances \(0,1,2,3\) in its component are respectively \(1,9,15,7\).

More precisely, for any two bases \(S,T\) with the same center,
\[
\operatorname{dist}_{\mathcal B_x}(S,T)=3-|S\cap T|.
\]
No sequence of one-landmark replacements connects bases with different centers.

## Assumptions and scope

All graphs are finite, undirected and simple. Write \([5]=\{0,1,2,3,4\}\), and let \(\binom{[5]}2\) be the ten two-element subsets. The Petersen graph \(P\) has vertex set \(\binom{[5]}2\) and joins disjoint pairs. Define the Desargues graph \(D\) on the twenty vertices \((\epsilon,A)\), \(\epsilon\in\{0,1\}\), \(A\in\binom{[5]}2\), with \((\epsilon,A)\sim(1-\epsilon,B)\) precisely when \(A\cap B=\varnothing\).

A vertex set \(S\) resolves a connected graph when the vectors of distances to \(S\) distinguish all graph vertices. Its minimum possible size is the metric dimension; a minimum resolving set is a metric basis. The exchange graph uses unordered vertex sets and an edge exactly when \(|S\setminus T|=|T\setminus S|=1\). These definitions do not require a designated ordering of the landmarks or any orientation on edges.

## Proof

**Distance-transfer lemma.** For \(A,B\in\binom{[5]}2\), their Petersen distance is \(0\) when equal, \(1\) when disjoint, and \(2\) when distinct and intersecting. With the three entries indexed by these Petersen distances, distances in \(D\) satisfy
\[
d_D((\epsilon,A),(\delta,B))=
\begin{cases}
(0,4,2)_{d_P(A,B)},&\epsilon=\delta,\\
(5,1,3)_{d_P(A,B)},&\epsilon\ne\delta.
\end{cases}
\]
Indeed, paths in the double cover correspond to walks of the same length in \(P\), with path length parity fixed by the endpoint signs. Shortest even lengths for Petersen distances \(0,1,2\) are \(0,4,2\); shortest odd lengths are \(5,1,3\). The first nonzero same-vertex odd walk has length five because \(P\) has girth five, and an adjacent pair has a length-four even walk through its five-cycle. Every intersecting distinct pair has a length-two path and a length-three path; the explicit construction in \(P=KG(5,2)\), or direct inspection of its ten vertices, supplies both. These minima are also verified by an independently reconstructed breadth-first-search distance table in `verify_kneser_lift.py`.

Thus two vertices of \(D\) in opposite sign classes always have distance vectors of opposite entrywise parity to every fixed landmark. Within a fixed sign class, each landmark's distance is an injective function of the corresponding Petersen distance, irrespective of the landmark's own sign. Therefore a set of landmarks resolves \(D\) **if and only if** its projected pairs resolve \(P\). Repeated projected pairs add no information.

**Classification of Petersen triples.** A pair of vertices never resolves \(P\). Under the permutations of \([5]\), two landmark edges are either intersecting, represented by \(01,02\), or disjoint, represented by \(01,23\). The distinct vertices \(03,04\) have the same signature in the first case; \(02,03\) do in the second. The empty set and singletons cannot resolve either. Every resolving triple therefore consists of three distinct edges of \(K_5\).

Up to relabelling, an unordered triple of different \(K_5\) edges is a three-edge star, a triangle, a three-edge path, or a disjoint union of a two-edge path and one edge. Each non-star case fails: for triangle landmarks \(01,02,12\), witnesses \(03,04\) have identical signatures; for path landmarks \(01,12,23\), witnesses \(02,13\) do; for landmarks \(01,12,34\), witnesses \(03,04\) do. In the star case \(01,02,03\), the three landmark edges have distinct signatures containing a zero. The remaining seven pairs have the distinct signatures
\[
04:(2,2,2),\quad 12:(2,2,1),\quad 13:(2,1,2),\quad 23:(1,2,2),
\]
\[
14:(2,1,1),\quad 24:(1,2,1),\quad 34:(1,1,2).
\]
Hence the Petersen resolving triples are exactly the three-edge stars. There are \(5\binom43=20\) such triples. By the distance-transfer lemma, each has \(2^3\) distinct lifts to \(D\), with independent signs. This proves \(\dim(D)=3\) and the total \(160\).

**Exchange components.** Every minimum basis has a unique center: the common element of its three distinct projected pairs. Adjacent bases share two signed landmarks, whose two distinct projected pairs determine their unique common endpoint. Hence an exchange cannot change this center.

Fix a center \(x\). Its four spoke classes \(\{(0,\{x,y\}),(1,\{x,y\})\}\), \(y\ne x\), are each two-element classes. A basis chooses exactly one signed vertex from each of exactly three of the four classes. There are \(4\cdot2^3=32\) possibilities. From each basis, one may flip any of its three signs or replace any of its three chosen spokes by either sign of the one omitted spoke. These are all and only the \(3+3\cdot2=9\) valid exchanges, so every component is \(9\)-regular and has \(32\cdot9/2=144\) edges.

For two bases \(S,T\) centered at \(x\), each exchange can increase \(|S\cap T|\) by at most one, giving the lower bound \(3-|S\cap T|\). The reverse inequality follows constructively: first replace any selected spoke absent from the target by the target's absent spoke if the omitted spoke differs; then correct the sign of each remaining common spoke. Each step introduces a distinct required target vertex without repeating a spoke class. This uses exactly \(3-|S\cap T|\) exchanges. (Equivalently, these are bases of a rank-three truncation of a four-part partition matroid.)

For a fixed basis, keeping its omitted spoke yields \(\binom{3}{r}\) bases at distance \(r\) for \(0\le r\le3\). Omitting instead one of its three selected spokes yields, for each such choice, \(2\binom{2}{3-r}\) bases at distance \(r\) for \(1\le r\le3\). Thus the complete numbers at distances \(0,1,2,3\) are \(1,9,15,7\). In particular each component has diameter and radius three. The five disconnected components have \(5\cdot144=720\) edges in total.

## Verification

Execute `python3 verify_kneser_lift.py` and `python3 verify_gp103.py` in a directory containing these scripts; no nonstandard package is needed. Compare their JSON output to `verify_kneser_lift.out` and `verify_gp103.out`, respectively. The first reconstructs the bipartite Kneser cover, checks the \(400\) ordered vertex-pair distances against the transfer formula, searches all \(\binom{20}{3}=1140\) triples, verifies the exact star-lift classification, and computes all component distance profiles. The second constructs \(GP(10,3)\) independently, establishes that no one- or two-landmark set resolves, searches all \(1140\) triples, and verifies an explicit isomorphism between its graph and the signed-pair model. The recorded outputs agree on all aggregate counts and component distances.

The argument above, not the enumeration alone, establishes the classification, component decomposition and exact shortest-path formula. The independent computations check the finite base cases and the concrete graph-model equivalence.

## Relationship to prior work

Boutin's study of resolving sets and the exchange property describes a three-edge-star resolving set for the Petersen graph and gives an example obstructing a global resolving-set exchange property. That is a motivating precursor, **not** a classification of all signed metric bases of the Desargues graph or their five exchange components. Imran, Baig, Shafiq and Tomescu investigate metric dimension in the generalized Petersen family \(GP(n,3)\). Shao, Sheikholeslami, Wu and Liu already establish \(\dim(GP(10,3))=3\), so that scalar value is not claimed as new. The contribution here is the complete minimum-basis classification in the bipartite double cover, the explicit component invariant, and exact exchange distances. Published topological calculations concerning the Desargues graph have different objects/invariants and do not imply this classification.

## Limitations

The theorem is specific to the Desargues graph; it does not classify resolving sets of nonminimum size, other generalized Petersen graphs, or other double covers. The claimed originality is based on the inspected accessible primary literature and targeted research-index searches, not an exhaustive proof of publication priority. Some relevant papers were inspected at selected theorem/proof sections rather than every page. No independent external audit has been performed.

## References

1. D. Boutin, *Determining sets, resolving sets, and the exchange property*, arXiv:0808.1427v1, first posted August 10, 2008. https://arxiv.org/abs/0808.1427
2. M. Imran, A. Q. Baig, M. K. Shafiq, and I. Tomescu, *On Metric Dimension of Generalized Petersen Graphs P(n,3)*, Ars Combinatoria **117** (2014), 113–130.
3. Z. Shao, S. M. Sheikholeslami, P. Wu, and J. B. Liu, *The Metric Dimension of Some Generalized Petersen Graphs*, Discrete Dynamics in Nature and Society (2018), Article ID 4531958. DOI: 10.1155/2018/4531958.
