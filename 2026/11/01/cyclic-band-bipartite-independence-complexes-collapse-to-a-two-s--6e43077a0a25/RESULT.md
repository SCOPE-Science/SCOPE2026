# Cyclic-band bipartite independence complexes collapse to a two-sphere

## Finding
For integers \(t\ge 2\) and \(n\ge 2t-1\), write \(G_{n,t}\) for the graph obtained from \(K_{n,n}\) by deleting the \(t\) consecutive cyclic perfect matchings: its vertices are \(a_i,b_i\), with indices in \(\mathbb Z/n\mathbb Z\), and \(a_i\) and \(b_j\) are adjacent exactly when \((j-i)\bmod n\notin\{0,1,\ldots,t-1\}\). Define \(K_{n,t}=\operatorname{Ind}(G_{n,t})\). Then
\[
K_{n,t}\searrow K_{n,2}\simeq S^2.
\]
The first step consists of exactly \(n(t2^{t-2}-2)\) elementary simplicial free-face collapses. Including the empty face, the number of faces is exactly \(2^{n+1}-1+nt2^{t-1}\).

## Assumptions and scope
Throughout, \(n,t\) are integers satisfying \(t\ge2\) and \(n\ge2t-1\). An independence complex contains the empty face. A simplicial collapse removes a codimension-one free face together with its unique maximal coface. The asserted equivalence to a sphere is a homotopy equivalence, not a claim that the full simplicial complex is a triangulated sphere. No assertion is made below the specified stable range.

## Proof
**Step 1: the complement description.** Since \(G_{n,t}\) is bipartite, \(K_{n,t}\) is the clique complex of a graph with one complete clique on all \(a_i\), one complete clique on all \(b_i\), and mixed edges \(a_i b_{i+q}\) for \(0\le q<t\). Construct these mixed edges in increasing order of \(q\), and within each layer in order of \(i\). All additions in the same layer can be processed independently as described below.

**Step 2: the link at a newly inserted edge.** Fix a layer \(s\in\{3,\ldots,t\}\) and an index \(i\), and add the mixed edge \(e=\{a_i,b_{i+s-1}\}\). Immediately before insertion, the common neighbors of its endpoints are precisely
\[
A_r=a_{i+r}\ (1\le r\le s-1),\qquad B_q=b_{i+q}\ (0\le q\le s-2).
\]
All the \(A_r\) are pairwise adjacent, as are all the \(B_q\); their mixed adjacency is \(A_rB_q\) if and only if \(r\le q\). Here the condition \(n\ge2s-1\) prevents modular wraparound from introducing any additional common neighbors or mixed edges. Earlier edges in the same layer have different endpoints and introduce no extra edge among the displayed common neighbors. Therefore, the link of \(e\) in the enlarged clique complex is the flag complex \(L_s\) on these \(2s-2\) vertices, consisting of the two cliques and the Ferrers cross-adjacencies \(r\le q\).

**Step 3: explicit relative collapses.** In \(L_s\), for each \(r=2,\ldots,s-1\), the closed neighborhood of \(A_r\) is contained in that of \(A_1\). Removing \(A_r\) via the standard dominated-vertex simplicial collapse gives a strong deformation retraction. In the resulting complex, for each \(q=0,\ldots,s-3\), the closed neighborhood of \(B_q\) is contained in that of \(B_{s-2}\), so these vertices can likewise be deleted. What remains is the single edge \(\{A_1,B_{s-2}\}\), which collapses to a vertex and then to the empty face **relative to the newly inserted edge**: for each collapse pair \((\sigma,\tau)\) in the link, remove \((e\cup\sigma,e\cup\tau)\). In the last two pairs, remove \((e\cup\{A_1\},e\cup\{A_1,B_{s-2}\})\) and then \((e,e\cup\{B_{s-2}\})\). Each lower face is free in the current complex because every face containing \(e\) is newly created by this edge insertion. Thus the enlarged complex simplicially collapses onto the pre-insertion complex. This argument is uniform over every \(s\) and \(i\).

The number of faces of \(L_s\), including empty, is \((s+1)2^{s-2}\): the two full cliques contribute \(2^s-1\) distinct faces, and the mixed faces contribute \((s-3)2^{s-2}+1\). Each collapse pair removes two newly added faces, giving \((s+1)2^{s-3}\) relative collapse pairs per edge. Hence the number for all layers is
\[
n\sum_{s=3}^{t}(s+1)2^{s-3}=n(t2^{t-2}-2).
\]
For \(t=2\) the sum is empty and equals zero. Starting from \(K_{n,2}\), whose two pure simplices and mixed annulus contribute \(2^{n+1}-1+4n\) faces including empty, the face increment at layer \(s\) is \(n(s+1)2^{s-2}\); telescoping gives \(2^{n+1}-1+nt2^{t-1}\).

**Step 4: identify the base homotopy type.** In \(K_{n,2}\), the mixed faces form a triangulated annulus, with precisely the triangles
\[
\{a_i,b_i,b_{i+1}\},\qquad \{a_i,a_{i-1},b_i\}\quad(i\in\mathbb Z/n\mathbb Z).
\]
Its boundary consists of the two polygonal cycles on the \(a\)- and \(b\)-vertices. The remaining pure faces are the two full simplices \(\Delta_A\) and \(\Delta_B\), each glued along the corresponding boundary circle. Replacing each full simplex by the fan triangulated disk on its cyclic boundary changes neither the homotopy type of the simplex nor its boundary inclusion; both inclusions are homotopy equivalences of pairs by standard relative deformation/gluing. The annulus capped by these two disks is the two-sphere. Hence \(K_{n,2}\simeq S^2\), proving the claim.

## Verification
The self-contained `verify.py` reconstructs the independence complexes as exact bitset face collections, checks every intermediate Ferrers link against the link in the actual graph, then explicitly replays every free-face collapse in the complete complex, requiring a unique codimension-one coface and verifying maximality. It compares the exact remainder with \(K_{n,2}\) and checks the formula for face count and collapse length. Exhaustive cases cover every \(5\le n\le11\) and \(2\le t\le\lfloor(n+1)/2\rfloor\), plus \(n=3,4\) at \(t=2\). The final line of its recorded run is `CYCLIC_BAND_COLLAPSE_OK`. The infinite-range conclusion is established by the uniform link proof above, not inferred from these finite tests.

## Relationship to prior work
Adamaszek's 2015 work studies the independence complexes of chordal graphs using dismantling; the graphs in this theorem are not generally chordal, and that theorem does not supply this parameter-uniform collapse. General sphere-or-contractible results for other restricted graph families, and analyses of independence complexes of circle graphs, do not specify this cyclic deleted-matching family or its exact elementary collapse count. In particular, the 2023 and 2024 circle-graph studies address broader but different structural questions and do not state the present classification. Published graph-invariant results for crown graphs concern distinct invariants. The nearest published related result describing the Rips complex of a low-degree-deleted complete bipartite graph identifies the independence complex of the **deleted-edge graph**, whereas here the object is the independence complex of the **retained-edge graph**. Those are generally different, so that identity does not imply the stated sphere result.

## Limitations
The result does not assert that \(K_{n,t}\) is homeomorphic to a sphere, nor does it determine its symmetry quotient, equivariant homology, or the homotopy types at \(n<2t-1\). Finite checks are supplementary to the stated combinatorial argument. Publication-priority uncertainty remains for unindexed equivalent work; independent mathematical validation has not been performed.

## References
- M. Adamaszek, *A note on independence complexes of chordal graphs and dismantling*, arXiv:1508.02426v1, first public 2015-08-10.
- S. Chakraborty, *On bipartite circle graphs and Khovanov homology*, arXiv:2302.02527v1, 2023-02-06.
- P. Bakshi et al., *Independence complexes of circle graphs*, arXiv:2412.01125v1, 2024-12-02.
- *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, doi:10.1016/j.ejc.2005.04.010.
