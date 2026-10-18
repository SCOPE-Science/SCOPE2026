# A sharp simplicial-collapse plateau in the Heawood higher-independence filtration

## Finding
Let \(H\) be the Heawood graph, with point vertices \(p_i\) and line vertices \(\ell_j\) indexed by \(\mathbb Z/7\mathbb Z\), where \(p_i\) is adjacent to \(\ell_j\) precisely when \(i-j\in\{0,1,3\}\). For every positive integer \(r\), let \(\mathcal I_r=\operatorname{Ind}_r(H)\) consist of the vertex subsets whose induced connected components each have at most \(r\) vertices.

There are **actual elementary simplicial collapses**
\[
\boxed{\mathcal I_5\searrow\mathcal I_4\searrow\mathcal I_3\simeq S^6.}
\]
The first collapse consists of exactly \(840\) free-face/coface removals and the second of \(784\). Thus both natural inclusions \(\mathcal I_3\hookrightarrow\mathcal I_4\hookrightarrow\mathcal I_5\) are simple-homotopy equivalences and induce integral homology isomorphisms. In particular, for each \(r\in\{3,4,5\}\),
\[
\widetilde H_j(\mathcal I_r;\mathbb Z)\cong
\begin{cases}\mathbb Z,&j=6,\\0,&j\ne6.\end{cases}
\]
The interval of consecutive stages is maximal at both ends in the sense of homotopy equivalence: the adjacent Euler characteristics are
\[
\chi(\mathcal I_2)=-12,\qquad
\chi(\mathcal I_3)=\chi(\mathcal I_4)=\chi(\mathcal I_5)=2,\qquad
\chi(\mathcal I_6)=-19.
\]
Therefore neither adjoining inclusion, from threshold \(2\) to \(3\) or from \(5\) to \(6\), is a homotopy equivalence.

## Assumptions and scope
The graph is the simple undirected point–line incidence graph of the Fano plane, with exactly \(14\) vertices and \(21\) edges, represented by vertex labels \(0,\dots,6\) for points and \(7,\dots,13\) for lines. Each line with index \(j\) contains the points \(j,j+1,j+3\) modulo \(7\). The component bound is on **the number of vertices**, not the diameter, maximum degree, edge count, or size of the largest connected subgraph chosen after deleting edges. The asserted equivalences concern the indicated thresholds of this one graph.

A simplicial collapse \(K\searrow L\) is a finite sequence deleting a simplex \(\sigma\) together with its unique codimension-one coface \(\tau\) whenever \(\sigma\) is a free face and \(\tau\) is maximal in the current complex; the empty face is never removed. Here \(L\) is an actual subcomplex of \(K\), so the reverse inclusions are the original inclusion maps.

## Proof
**Face enumeration.** A vertex set belongs to \(\mathcal I_r\) if and only if it contains no induced connected \((r+1)\)-vertex set. Indeed, any connected induced component of size at least \(r+1\) has a connected induced subset with exactly \(r+1\) vertices, obtained by growing a connected vertex set one adjacent vertex at a time. The verifier checks this obstruction criterion independently against direct connected-component traversal for all \(2^{14}\) labeled subsets at each \(r\in\{2,3,4,5,6\}\). With the empty face omitted, the respective face counts are \(2256,4622,6190,7870,9683\). Alternating the face vectors gives the displayed Euler characteristics.

**The sphere at threshold three.** Represent a nonempty face \(\sigma\) by \(m(\sigma)=\sum_{i\in\sigma}2^i\). Begin with all \(4622\) nonempty faces of \(\mathcal I_3\). For the vertex-pivot order
\[
(8,12,10,6,3,9,13,5,11,1,2,7,0,4),
\]
at each pivot pair every currently unpaired face not containing that vertex with its one-vertex extension, if that extension is currently unpaired; inspect faces in ascending bitmask order. This produces exactly \(2310\) disjoint face/coface pairs and leaves just the vertex-mask \(256\) and the seven-vertex-mask \(10454\) unpaired. The latter represents a \(6\)-simplex. Directly orient each of all \(23884\) Hasse cover incidences downward except the matched ones, which are oriented upward. The resulting finite directed graph is acyclic (verified by a complete topological sort). Discrete Morse theory consequently provides a CW model with one zero-cell and one six-cell and no other cells. Its unique attaching map lands in a point, hence \(\mathcal I_3\simeq S^6\).

**Two genuine relative collapses.** For either consecutive pair \(L=\mathcal I_{r-1}\subset K=\mathcal I_r\), with \(r=4\) or \(5\), form the set of nonempty relative simplices \(K\setminus L\). In increasing vertex order \((0,1,\dots,13)\), perform the same toggle pairing on the *remaining relative simplices*, again visiting face masks in increasing order. At threshold \(4\), the relative set contains \(1568\) simplices, exhausted by \(784\) disjoint pairs; at threshold \(5\), it contains \(1680\), exhausted by \(840\) pairs. In each case the directed relative Hasse graph is acyclic.

More strongly, the verifier actually deletes all these pairs **from the full current simplicial complex**, one at a time: it selects an available matched lower face whose *only currently present immediate coface* is its matched upper face, additionally checks the latter has no coface, and deletes both. It completes \(784\) and \(840\) legal elementary collapses respectively, without deleting any face of \(L\), and the final face set equals \(L\) exactly. This gives the two claimed simplicial collapses, not merely abstract homology isomorphisms.

**Sharpness.** The independently checked face vectors for thresholds \(2\) and \(6\) have Euler characteristics \(-12\) and \(-19\), whereas the middle stages have Euler characteristic \(2\). Homotopy equivalences preserve Euler characteristic of finite complexes, so the block cannot extend to either adjacent threshold.

## Verification
Run `python3 verify_heawood_filtration.py` with Python \(3.10\) or newer; no third-party packages are required. The checker constructs the Fano incidence graph directly, independently enumerates faces by connectivity and forbidden connected subsets, validates all five face vectors and Euler characteristics, checks the complete directed Hasse graphs for cycles, and **replays every relative free-face collapse** on the ambient face sets. It terminates with `HEAWOOD_IND3_TO_IND5_PLATEAU_AND_BOUNDARIES_VERIFIED` only after all assertions pass. The code and its outputs are finite exhaustive certificates for the stated fourteen-vertex graph, not a proof for an unbounded graph family.

## Relationship to prior work
Deshpande and Singh introduced systematic homotopy computations of higher-independence complexes for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. Deshpande, Shukla, and Singh also established connectivity bounds and wedge results for chordal graphs; Abdelmalek and collaborators studied shellability for chordal families. The Heawood graph is neither chordal nor complete bipartite, and these stated theorems do not compute the present inclusions. Earlier Heawood calculations at component bound \(2\) and for an **induced-forest maximum-degree filtration** concern adjacent or different complexes, not the two collapse maps here. For instance, the induced four-vertex path on \(\{p_0,p_1,\ell_0,\ell_1\}\) is allowed by the degree-two forest condition but not by \(\mathcal I_3\), while the induced star on \(\{p_0,p_1,p_3,\ell_0\}\) is admitted to \(\mathcal I_4\) but not that degree-two forest complex. Equality of individual homotopy types would not establish these natural simple-homotopy equivalences.

## Limitations
The result is specific to the Fano-plane incidence graph and the thresholds stated. It does not determine the homotopy type of \(\mathcal I_6\) or a general family of projective-plane incidence graphs. The novelty comparison covers accessible published work and mathematical research records but cannot rule out unindexed equivalent results. No independent mathematical audit is asserted.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted 2020-01-15, https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, first posted 2020-01-19, https://arxiv.org/abs/2001.06775.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first posted 2021-06-21, https://arxiv.org/abs/2106.10863.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
