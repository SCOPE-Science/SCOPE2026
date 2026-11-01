# A third-dimensional sphere-wedge theorem for Hamiltonian-cycle-deleted complete bipartite graphs

## Finding

For each integer \(n\ge4\), take disjoint vertex classes \(A=\{a_0,\ldots,a_{n-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\), with indices modulo \(n\). Define \(G_n\) by retaining the edge \(a_ib_j\) of \(K_{n,n}\) exactly when \(j\notin\{i,i+1\}\). Thus \(G_n\) is obtained by deleting the alternating Hamiltonian cycle consisting of the nonedges \(a_ib_i\) and \(a_ib_{i+1}\).

Let \(X_n=\operatorname{Ind}_2(G_n)\) be the simplicial complex of subsets whose induced subgraphs have components of order at most two, equivalently maximum induced degree at most one. Then

\[
X_n\simeq\bigvee^{n^2-3n-1}S^3\qquad(n\ge4).
\]

In particular its reduced integral homology is free of rank \(n^2-3n-1\) in degree three and zero in all other degrees. The initial ranks for \(n=4,5,6,7,8\) are \(3,9,17,27,39\). For \(n=3\), the graph is a matching and \(X_3\) is a simplex, hence contractible. The isolated \(n=4\) case also follows from the previously known cycle-graph calculation; the uniform deleted-cycle family is the new scope.

## Assumptions and scope

All graphs are finite, simple and unweighted. The complex includes the empty simplex, but the discrete-Morse face poset omits it. Indices are interpreted modulo \(n\), and the vertex ordering used below is \(a_0,a_1,\ldots,a_{n-1},b_0,b_1,\ldots,b_{n-1}\). The theorem is an ordinary nonequivariant homotopy equivalence, not an equivariant one. No claim concerns higher-independence parameter greater than two.

For \(T\subseteq B\), let \(L_T\) denote the family of \(S\subseteq A\) with \(S\cup T\in X_n\). When \(T\ne\varnothing\), the empty \(S\) belongs to \(L_T\). Write \(P_j=\{a_{j-1},a_j\}\), the two nonneighbors of \(b_j\) in \(G_n\). A set \(S\cup T\) is a face exactly when each selected vertex has at most one neighbor across the two classes.

## Proof

**Step 1: an acyclic element matching.** Process the vertices in the displayed order. At each vertex \(v\), pair every *currently unpaired* face \(F\) not containing \(v\) with \(F\cup\{v\}\), if the latter is also currently unpaired. Remove both from later consideration. The union of these element matchings is acyclic by the sequential-element-matching proposition (Deshpande–Singh, Proposition 2.10, based on the standard discrete-Morse matching lemma). Thus it suffices to identify the unpaired faces. Faces in distinct fixed-\(T\) fibers never interact during the \(A\)-vertex stages.

**Step 2: the fibers while matching \(A\).** For \(T=\varnothing\), the whole \(A\)-simplex is paired except for the vertex \(a_0\). For \(|T|=1\), say \(T=\{b_j\}\), the family \(L_T\) is the join of the simplex on \(P_j\) and the discrete complex of subsets of \(A\setminus P_j\) of size at most one. It is a cone, and toggling the earliest vertex in \(P_j\) perfectly matches the entire fiber.

For \(T=\{b_j,b_k\}\), both selected \(B\)-vertices allow an \(A\)-vertex exactly when it lies in \(P_j\cup P_k\). If \(j,k\) are consecutive in the cycle \(C_n\), the pairs \(P_j,P_k\) overlap in one vertex, and \(L_T\) is the full triangle on their three-element union: no critical face remains. If \(j,k\) are not consecutive, the two \(P\)-pairs are disjoint, and \(L_T\) is the four-cycle whose edges choose one endpoint from each pair. Sequential matching of this four-cycle leaves one edge, containing the later (larger numerical index) member of each \(P\)-pair. Therefore one four-vertex critical candidate \(S\cup T\) survives for each *nonconsecutive* unordered \(B\)-pair, and their count is \(\binom n2-n=n(n-3)/2\).

If \(|T|=3\), an allowed selected \(a_i\) must have both of its missing neighbors \(b_i,b_{i+1}\) in \(T\). These eligible \(a_i\) (at most two) span a simplex whenever nonempty, so that fiber is perfectly paired. If no consecutive \(B\)-pair occurs in \(T\), only the face \(T\) remains. If \(|T|\ge4\), no vertex of \(A\) may be selected, so again only \(T\) remains. Consequently the survivors after the \(A\) stages are exactly: \(a_0\); one four-element mixed face for every nonconsecutive \(B\)-pair; all pure \(B\)-faces of size at least four; and the pure \(B\)-triples that are independent in \(C_n\). (A face containing a nonempty \(T\) has at most three selected \(A\)-vertices, justifying the complete case split.)

**Step 3: matching \(B\).** The mixed survivors have exactly two \(B\)-vertices, and no face obtained by adding or deleting a \(B\)-vertex survives Step 2. They are therefore untouched, as is \(a_0\). On the pure \(B\)-survivors, the \(b_0\)-matching eliminates every set without \(b_0\), every pure face of size at least five, and every four-set containing \(b_0\) whose three other indices are independent in the path \(1,2,\ldots,n-1\). More precisely, the remaining pure faces are (i) independent triples \(\{b_0,b_i,b_j\}\) of the cyclic graph and (ii) four-sets \(\{b_0,b_i,b_j,b_k\}\) for which \(\{i,j,k\}\) contains a consecutive pair in the index path.

Any triple of type (i) has \(2\le i<j\le n-2\) and \(j\ge i+2\). At stages \(b_1,\ldots,b_{i-2}\), its possible four-set partners were already removed by the \(b_0\)-matching, because their three nonzero indices are independent in the path. At stage \(b_{i-1}\) it is paired with \(\{b_0,b_{i-1},b_i,b_j\}\), which survived the \(b_0\)-matching and contains no earlier nonzero vertex. This pairs *all* remaining triples with distinct four-sets, leaving only four-vertex faces (dimension three).

To count these, the number of type-(ii) four-sets before the later \(B\)-stages is

\[
\binom{n-1}{3}-\binom{n-3}{3}.
\]

Indeed the excluded three-subsets of the \(n-1\) nonzero indices are precisely the independent triples of the path, whose count is \(\binom{n-3}{3}\). The number of type-(i) triples, and hence the number of removed four-sets, is \(\binom{n-4}{2}\), by choosing two nonconsecutive indices in \(2,3,\ldots,n-2\). Binomial coefficients with an upper argument smaller than the lower are interpreted as zero. The number of surviving pure four-sets is therefore

\[
\binom{n-1}{3}-\binom{n-3}{3}-\binom{n-4}{2}
=\frac{n^2-3n-2}{2}.
\]

Adding the \(n(n-3)/2\) mixed four-sets gives exactly \(n^2-3n-1\) unmatched three-dimensional simplices, plus the single unmatched vertex \(a_0\).

**Step 4: topology.** The matching is acyclic for every \(n\ge4\), by the cited general element-matching proposition; Steps 2–3 identify *all* critical simplices for every such \(n\). Forman's discrete Morse theorem gives a CW model with one zero-cell and exactly \(n^2-3n-1\) three-cells, with no cells of dimensions one or two. All three-cells therefore attach trivially to the point, giving the asserted wedge of three-spheres integrally. For \(n=3\), the complement of the deleted six-cycle consists of three disjoint edges, so every vertex subset induces maximum degree at most one and \(X_3\) is the full five-simplex.

## Verification

The standalone `verify.py` reconstructs every face using a cyclic-index predicate; compares this with an independently built graph-adjacency test over every vertex subset for \(3\le n\le8\); enumerates the element matching and independently checks directed-Hasse acyclicity and both critical-face descriptions for \(4\le n\le12\); and computes mod-two boundary ranks for \(4\le n\le8\). Its recorded output in `verification_output.txt` ends with `ALL_CHECKS_PASS`. These finite computations check the formula and implementation; the infinite quantifier rests on the explicit case analysis in the proof and on the general matching theorem, not on extrapolation.

## Relationship to prior work

Taylan's path-devoid-complex theory proves homotopy descriptions for paths, cycles and forests; it supplies the earlier cycle specialization but not the present dense cycle-deleted bipartite family. Deshpande and Singh's Theorem 3.5 concerns *complete* multipartite graphs. At parameter two their theorem gives \(\operatorname{Ind}_2(K_{n,n})\simeq\bigvee^{n^2-1}S^1\). Deleting an entire alternating Hamiltonian cycle creates a genuinely different graph, changing both the homotopy dimension and the multiplicity. Their Proposition 2.10 supplies the standard acyclicity tool, not the critical-face classification proved here. The ordinary independence complex of the same edge-deleted graph is a different invariant and does not imply the present first higher-independence calculation.

## Limitations

The theorem concerns the first higher-independence parameter only and the specific deletion of one alternating Hamiltonian cycle. No equivariant homotopy classification, generalization to arbitrary degree-two deleted bipartite factors, or complete publication-priority guarantee is claimed. Independent mathematical validation has not been performed.

## References

1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first posted 2015-01-27), especially Theorems 3.10, 3.14 and 5.2. https://arxiv.org/abs/1501.06754
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020-01-15), especially Proposition 2.10 and Theorem 3.5. https://arxiv.org/abs/2001.05448
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
