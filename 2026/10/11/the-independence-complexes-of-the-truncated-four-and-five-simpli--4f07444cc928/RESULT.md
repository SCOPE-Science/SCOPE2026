# The independence complexes of the truncated four- and five-simplices

## Finding
Let \(T_m\) be the one-skeleton of the ordinarily truncated \((m-1)\)-simplex, for \(m\in\{5,6\}\). Then the integral homotopy types of their ordinary independence complexes are
\[
\operatorname{Ind}(T_5)\simeq \bigvee^{5}S^3\vee\bigvee^{23}S^4,
\qquad
\operatorname{Ind}(T_6)\simeq \bigvee^{6}S^4\vee\bigvee^{967}S^5.
\]
These are homotopy equivalences of spaces, not merely equalities of field homology groups. In particular, both spaces have torsion-free integral homology and nonzero reduced homology in two adjacent degrees.

## Assumptions and scope
The graph \(T_m\) has vertex set \(\{(a,b):0\leq a,b<m,\ a\ne b\}\). Two distinct vertices \((a,b)\) and \((c,d)\) are adjacent exactly when \(a=c\), or when \((c,d)=(b,a)\). This is the usual edge graph of a simplex truncated at every vertex: each original vertex gives a clique of size \(m-1\), and each original edge gives one cross-clique edge. The graph has \(m(m-1)\) vertices and \(m(m-1)^2/2\) edges. Equivalently, \(T_m\) is the line graph of the graph obtained by subdividing every edge of the complete graph \(K_m\) exactly once: the edge from original vertex \(a\) to the subdivision vertex of \(\{a,b\}\) corresponds to \((a,b)\). Thus \(\operatorname{Ind}(T_m)\) is canonically the ordinary matching complex of this once-subdivided complete graph. An independent set is equivalent to a partial function from \(\{0,\ldots,m-1\}\) to itself, with no fixed points and no directed two-cycle. We consider all such sets, including the empty set, as a simplicial complex; only nonempty simplices occur in the matching certificate.

## Proof
First, enumerate all nonempty independent sets using the explicit ordered-pair adjacency rule. For \(m=5\), the face vector, by dimensions zero through four, is \((20,150,520,815,444)\), totaling \(1949\) nonempty simplices. For \(m=6\), the face vector, by dimensions zero through five, is \((30,360,2200,7170,11700,7360)\), totaling \(28820\) nonempty simplices. This enumeration is exhaustive because every nonempty face is generated recursively by adjoining a higher-indexed vertex that is not adjacent to any previously selected vertex.

Define a matching on the nonempty face poset as follows. Process graph vertices \(j\) in the fixed lexicographic ordering of pairs. At step \(j\), among faces not removed by earlier steps, pair every face \(\sigma\) missing \(j\) with \(\sigma\cup\{j\}\) whenever both are present; remove both. The pairs are disjoint and always span one Hasse incidence. A complete enumeration of the Hasse incidences, reversing precisely the matched edges, has an acyclic topological ordering: the directed graphs have \(7340\) and \(138660\) incidences respectively. Therefore this is an acyclic Forman matching.

The unmatched critical cells, by dimension, number \((1,0,0,6,24)\) for \(m=5\) and \((1,0,0,0,7,968)\) for \(m=6\). The resulting CW models thus have one zero-cell, no cells in dimensions from one through \(m-3\), then \(m+1\) cells in dimension \(m-2\), and the indicated higher critical cells in dimension \(m-1\). With no lower positive-dimensional cells, the \((m-2)\)-skeleton is a wedge of \((m+1)\) spheres of dimension \(m-2\).

For clarity on integral attaching maps, orient every simplex by increasing ordered-pair index and give its codimension-one face obtained by deleting the \(i\)-th vertex incidence coefficient \((-1)^i\). Starting with those signed incidences, the code eliminates matched pairs by summing their signed gradient paths: for a matched lower face \(\tau\) and upper face \(\rho\), eliminate \(\tau\) using the relation \(\partial\rho=0\), with the unit coefficient of \(\tau\) in \(\partial\rho\). All coefficients remain integers. This produces the exact Morse cellular boundary matrix from critical \((m-1)\)-cells to critical \((m-2)\)-cells.

For \(m=5\) this integral matrix has size \(6\times24\), and for \(m=6\) size \(7\times968\). In each case the signed entries belong to \(\{-1,0,1\}\), at least one entry has absolute value one, and every two-by-two minor vanishes (the verifier checks the equivalent complete cross-product identities). Thus each matrix has rank exactly one and its only nonzero Smith invariant factor is one. Integer row and column operations put it in diagonal form with one unit and all remaining entries zero.

Because \(m-2\geq3\), the attaching maps of \((m-1)\)-cells to a wedge of \((m-2)\)-spheres are classified up to homotopy by their integer degree vectors: the Hurewicz map \(\pi_{m-2}\to H_{m-2}\) is an isomorphism. Unimodular changes of bases of these spheres and the attaching cells realize the Smith reduction; a unit attaching map cancels one lower/higher cell pair. Each remaining cell has zero attaching degree vector and hence a null-homotopic attaching map. The resulting wedge contains \(6-1=5\) lower-dimensional spheres and \(24-1=23\) higher-dimensional spheres for \(m=5\), and \(7-1=6\) lower-dimensional spheres and \(968-1=967\) higher-dimensional spheres for \(m=6\), as asserted.

## Verification
The standalone standard-library script `verify_morse.py` reproduces each graph, enumerates all faces, constructs the explicit matching, checks every Hasse arrow by a full topological sort, and calculates the signed integral Morse boundary by exact integer arithmetic and signed gradient-path recursion. Its expected checks include the face vectors, matching sizes \(959\) and \(13922\), counts of critical cells, unit pivots, and vanishing two-by-two minors. Run with `python verify_morse.py`.

Independently, `verify_homology.py` uses enumeration of partial functions rather than the graph search and computes simplicial boundary ranks modulo \(2\), \(3\), and \(5\). It obtains reduced Betti numbers \((0,0,0,5,23)\) and \((0,0,0,0,6,967)\) over all three fields. Run with `python verify_homology.py`. This second check supports, but by itself does not establish, the integral homotopy statement; the signed acyclic-Morse argument does that.

## Relationship to prior work
Engström's *Independence complexes of claw-free graphs* establishes connectivity theorems, including quantitative bounds, for a class containing \(T_5\) and \(T_6\): every graph vertex here has a neighborhood that is a clique plus a single reverse-edge neighbor. Those general bounds do not specify the two integral wedge decompositions above. Barmak's *Star clusters in independence complexes of graphs* develops homotopy reductions for graph independence complexes, including a triangle-free suspension result; these truncated-simplex graphs contain cliques of size at least four and are not covered by that special case. Goyal, Shukla, and Singh determine homotopy types for several other graph families and constructions, not these two ordered-pair graphs. Research-index comparisons with exact sphere multiplicities, directed-arc and partial-function descriptions, and the equivalent matching complexes of once-subdivided complete graphs identified no statement implying this result. Barmak’s §5 matching-complex connectivity theorems also supply bounds, not these two exact integral types. Results on higher matching complexes of unsubdivided complete graphs concern different simplicial complexes. These searches do not constitute proof of priority.

## Limitations
The theorem is an exhaustive exact determination only for the two dimensions specified. It does not assert a closed-form homotopy type for all truncated simplices, nor a proof that all members of the family are wedges of spheres. The signed Morse algorithm is a finite exhaustive proof for these two input graphs, not an infinite-family certificate. An equivalent calculation in unindexed literature remains a residual bibliographic risk; independent review has not been performed.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1 (17 December 2005), https://arxiv.org/html/math/0512420v1 .
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2 July 2010), https://arxiv.org/html/1007.0418v1 .
3. S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1 (16 May 2019), https://arxiv.org/html/1905.06926v1 .
