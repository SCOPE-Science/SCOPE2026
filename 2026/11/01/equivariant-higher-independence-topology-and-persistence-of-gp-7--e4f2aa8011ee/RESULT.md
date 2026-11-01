# Equivariant higher-independence topology and persistence of \(GP(7,2)\)

## Finding
Let \(G=GP(7,2)\) be the fourteen-vertex generalized Petersen graph. For an integer \(r\ge1\), the higher-independence complex \(K_r=\operatorname{Ind}_r(G)\) contains precisely the vertex subsets whose induced graph components have at most \(r\) vertices. Its first four stages have the **integral** homotopy types
\[
K_1\simeq S^3,\qquad K_2\simeq S^5,\qquad
K_3\simeq\bigvee^8S^5,\qquad K_4\simeq\bigvee^6S^6.
\]
The reduced positive-degree persistent homology over \(\mathbb F_2\), restricted to the four-stage filtration \(K_1\subseteq K_2\subseteq K_3\subseteq K_4\), has exactly one bar \([1,2)\) in degree three, one bar \([2,4)\) and seven bars \([3,4)\) in degree five, and six degree-six classes born at stage four and still present at the **end of this truncated filtration**. Therefore the inclusion \(K_2\hookrightarrow K_3\) has rank one on degree-five homology over \(\mathbb F_2\) and induces a nonzero, hence injective, homomorphism \(H_5(K_2;\mathbb Z)\longrightarrow H_5(K_3;\mathbb Z)\).

The natural dihedral group \(D_7=\langle\rho,\tau\rangle\) acts on these complexes. Its character on the unique nonzero reduced rational homology group at each stage, ordered on \((1,\rho,\rho^2,\rho^3,\tau)\), is respectively
\[
(1,1,1,1,1),\quad (1,1,1,1,-1),\quad
(8,1,1,1,-2),\quad (6,-1,-1,-1,0).
\]
Writing \(\varepsilon\) for the one-dimensional character trivial on rotations and negative on reflections, and \(W\) for the six-dimensional augmentation module of the natural seven-point permutation representation, the four rational modules are \(\mathbf1\), \(\varepsilon\), \(2\varepsilon\oplus W\), and \(W\), respectively.

## Assumptions and scope
The vertices are \(u_i,v_i\), for \(i\in\mathbb Z/7\mathbb Z\). Edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). In the executable realization, vertices \(u_0,\ldots,u_6\) are indexed \(0,\ldots,6\) and \(v_0,\ldots,v_6\) are indexed \(7,\ldots,13\). The group generators act by \(\rho(u_i)=u_{i+1}\), \(\rho(v_i)=v_{i+1}\), \(\tau(u_i)=u_{-i}\), and \(\tau(v_i)=v_{-i}\). The character is computed with the natural action on oriented simplices. Reduced homology is over the indicated field; the homotopy equivalences and their homology consequences are integral. Persistence statements refer **only** to cutoffs one through four; no survival beyond cutoff four is claimed. A direct check finds 49 maximal independent sets, all of cardinality five, making this a well-covered cubic example.

## Proof
**1. Complete finite face characterization.** For each of the \(2^{14}=16{,}384\) vertex subsets \(\sigma\), find the sizes of all connected components in the induced graph \(G[\sigma]\). Let \(t(\sigma)\) be the maximum, or zero for the empty set. Then the nonempty faces of \(K_r\) are exactly \(\{\sigma\neq\varnothing:t(\sigma)\le r\}\). An independent union-find routine based on the undirected edge list agrees with the bitset breadth-first search for every subset. Thus the face enumeration follows directly from the graph definition, without a model-dependent face table.

**2. Explicit acyclic matchings.** The supplied `check.py` constructs the following discrete-Morse matchings deterministically. For a stage-specific ordered list of vertices, visit each vertex \(w\) in turn and pair any still-unmatched nonempty face \(\sigma\) not containing \(w\) with its still-unmatched coface \(\sigma\cup\{w\}\), if that coface exists. The vertex orders are
\[
\begin{array}{c|l}
 r&\text{vertex order}\\\hline
1&(1,10,9,5,11,2,3,7,8,4,0,12,6,13)\\
2&(13,10,0,12,6,5,3,8,7,11,4,1,9,2)\\
3&(1,10,9,5,11,2,3,7,8,4,0,12,6,13)\\
4&(11,12,6,10,13,0,4,1,7,5,2,8,9,3).
\end{array}
\]
For each resulting matching, orient each codimension-one face incidence from the larger face to the smaller face, **except** reverse every matched incidence. A topological sort visits every vertex of each directed Hasse graph, proving there is no directed cycle and hence that the matching is acyclic. The exhaustive sizes are
\[
\begin{array}{c|r|r|r|c}
r&\text{faces including empty}&\text{matched pairs}&\text{Hasse incidences}&\text{critical dimensions/counts}\\\hline
1&435&216&1435&0:1,\ 3:1\\
2&2269&1133&10248&0:1,\ 5:1\\
3&4390&2190&22211&0:1,\ 5:8\\
4&6476&3234&35189&0:1,\ 6:6.
\end{array}
\]
These are complete combinatorial finite certificates, reconstituted and checked from the exact source graph by the standalone checker. Discrete Morse theory gives a CW complex with precisely these cells. Because each CW model has one zero-cell and its only other cells have one common dimension at least three, every attaching map lands in the zero-cell. The CW model is therefore a wedge of the indicated spheres. This proves **homotopy**, not merely field Betti numbers, and in particular its integral torsion-freeness. Independently computed simplicial boundary ranks over \(\mathbb F_2\) reproduce each homology rank.

**3. All dihedral character values.** For any automorphism \(g\), let
\[
L_r(g)=\sum_{\substack{\varnothing\neq\sigma\in K_r\\g\sigma=\sigma}}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
Here \(\operatorname{sgn}(g|_\sigma)\) is the orientation sign of the induced permutation on the vertices of \(\sigma\); the displayed formula is the simplicial Lefschetz number. The complex is connected and its only other homology group is in dimension \(d_r\in\{3,5,5,6\}\), so
\[
\operatorname{tr}(g|\widetilde H_{d_r}(K_r;\mathbb Q))=(-1)^{d_r}(L_r(g)-1).
\]
The checker verifies every generator's edge preservation and evaluates this **signed fixed-simplex sum** for the identity, three nontrivial rotation conjugacy classes, and a reflection. It obtains the four five-entry characters in the statement. For odd seven, all nonidentity rotations of a fixed order form pairs of inverse conjugacy classes and all reflections are conjugate, so these five values specify the full character. Finally \(W\) has character \((6,-1,-1,-1,0)\) and \(\varepsilon\) has \((1,1,1,1,-1)\); the stated rational decompositions follow by subtraction of characters.

**4. Inclusion maps and truncated barcode.** List the nonempty faces in increasing order of their exact birth parameter \(t(\sigma)\), then dimension, then vertex-mask index. This ordering puts every boundary face before its coface. Perform ordinary persistence column reduction over \(\mathbb F_2\) on the resulting entire boundary matrix, retaining simplex birth times and recording nonzero-length pairs. The exhaustive reduction over the 6,475 nonempty faces of \(K_4\) returns exactly the bars in the finding, as well as six unpaired degree-six classes born at stage four. A second computation reduces the simplicial boundary separately at every cutoff, independently checking all Betti numbers. The unique degree-five bar born at cutoff two survives cutoff three; hence the induced map on \(H_5(-;\mathbb F_2)\) has rank one. The preceding integral homotopy types give \(H_5(K_2;\mathbb Z)\cong\mathbb Z\) and \(H_5(K_3;\mathbb Z)\cong\mathbb Z^8\). A homomorphism between these free groups whose mod-two reduction is nonzero is itself nonzero, and every nonzero map from \(\mathbb Z\) to a free abelian group is injective. No primitivity assertion is made for its image.

## Verification
Execute `python3 check.py` with Python 3 and no external dependencies. The script checks independent induced-component algorithms for all 16,384 masks; regenerates and verifies every directed matching and critical-cell count; independently computes mod-two boundary ranks and the complete four-stage barcode; verifies the graph symmetries and exact fixed-simplex Lefschetz traces; and emits canonical JSON. A successful run ends in `GP7_2_EQUIVARIANT_HIGHER_INDEPENDENCE_PERSISTENCE_OK`. The exact expected output is embedded as `verification.json`. These finite exhaustive tests are proof certificates for **the named finite graph and four cutoffs**, not evidence for a generalized-Petersen all-parameter theorem.

## Relationship to prior work
Deshpande and Singh's *Higher Independence Complexes of graphs and their homotopy types* (2020) develops the higher-independence construction and treats several explicit families, including cycles, whiskered graphs, complete multipartite graphs and perfect rooted trees. Abdelmalek and collaborators' *Chordal graphs, higher independence and vertex decomposable complexes* (2021) gives structure under chordal hypotheses. Here the induced outer seven-cycle makes \(GP(7,2)\) nonchordal and neither published family theorem supplies the homotopy types, inclusion ranks or dihedral characters above. Existing Petersen-graph cutoff-two calculations concern the **ten-vertex** \(GP(5,2)\), not this fourteen-vertex graph; generalized-Petersen graph-power Rips calculations concern a different simplicial construction. Searches under aliases including dissociation complex, induced component bound two, higher independence, generalized Petersen and well-covered cubic graph found no statement implying this entire four-stage equivariant/persistent classification. That failure of retrieval does not prove absolute novelty.

## Limitations
The result is exact for \(GP(7,2)\) and only \(1\le r\le4\). It does not classify cutoffs five or larger, generalized Petersen graphs at other parameters, integral persistence image indices, or any infinite family. The character decompositions are over \(\mathbb Q\); integral equivariant lattices are not classified. A previous unindexed calculation or a less explicitly formulated general theorem could supersede part of the statement.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public version 2020-01-15), https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first public version 2021-06-21), https://arxiv.org/abs/2106.10863.
3. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, https://arxiv.org/abs/1104.0433 (a different simplicial construction used for scope comparison).
