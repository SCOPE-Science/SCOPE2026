# The Frucht graph independence complex and its complete vertex-deletion classification

## Finding
Let \(F\) be the classical twelve-vertex cubic Frucht graph with the vertex labeling specified below. Write \(K=\operatorname{Ind}(F)\) for the simplicial complex of independent vertex sets. Then
\[
K\simeq\bigvee^{3}S^{2}.
\]
Moreover, **all twelve vertex-deletion and link homotopy types** fall into exactly three groups, with vertex labels fixed by the edge list below:

- For \(A=\{0,1,5,7,9,10\}\), each \(v\in A\) satisfies \(K-v\simeq\bigvee^{2}S^{2}\) and \(\operatorname{lk}_K(v)\simeq S^{1}\).
- For \(B=\{2,8\}\), each \(v\in B\) satisfies \(K-v\simeq\bigvee^{4}S^{2}\) and \(\operatorname{lk}_K(v)\simeq S^{2}\).
- For \(C=\{3,4,6,11\}\), each \(v\in C\) satisfies \(K-v\simeq\bigvee^{3}S^{2}\), its link is simplicially collapsible, and the natural inclusion \(K-v\hookrightarrow K\) is a homotopy equivalence.

Thus deletion changes the homotopy type at exactly eight of the twelve vertices, despite the Frucht graph's trivial automorphism group.

## Assumptions and scope
Here \(F\) is the **simple undirected graph** on labeled vertices \(\{0,1,\ldots,11\}\) with its 18 edges given by the following reproducible Python literal:

```python
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

This is the standard Frucht graph: in the reference cyclic LCF labeling \(0,\ldots,11\), its LCF jumps are `[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]`; the isomorphism sends our vertices to LCF vertices by `old_to_lcf = {4:0,3:1,2:2,1:3,7:4,0:5,6:6,5:7,10:8,11:9,8:10,9:11}`. Both representations are implemented and checked in the certificates. For any \(v\), \(K-v=\operatorname{Ind}(F-v)\) is the induced subcomplex obtained by removing vertex \(v\); its link \(\operatorname{lk}_K(v)=\operatorname{Ind}(F-N_F[v])\), where \(N_F[v]\) is the closed graph neighborhood. All homotopy equivalences concern geometric realizations; integral homology follows accordingly.

## Proof
The complete independence complex has \(168\) nonempty simplices and face vector \((12,48,73,34,1)\) in dimensions \(0\) through \(4\). Exhaustive enumeration visits every subset of the twelve vertices and retains exactly those containing no edge of \(F\).

The certificate `verify_frucht.py` constructs a discrete Morse matching on the **full face poset**, first including the empty face. For each vertex index in its stated permutation, it matches every currently unmatched face \(\sigma\) without that vertex to \(\sigma\cup\{v\}\), whenever both faces are still unmatched, and removes the pair before proceeding. The empty-to-vertex pair is subsequently discarded, leaving that vertex as the unique critical zero-cell. This procedure is fully deterministic once the order is fixed, and the attached verifier spells out each order for the full complex, all deletions, and all links. The matching has \(82\) pairs on the ordinary full complex, and its critical cells are exactly one zero-cell and three two-cells. The verifier constructs the entire directed Hasse diagram by reversing matched incidences and topologically sorts **all 456 incidences**; all cells are removed, proving there is no directed cycle. By discrete Morse theory, the complex has the homotopy type of a CW complex with one zero-cell and three two-cells, which is \(\bigvee^{3}S^{2}\), since each attaching map from a circle to a point is constant.

The same exhaustive matching method separately checks each of the twelve induced deletions and twelve induced links. In each deletion, only one critical zero-cell and \(2\), \(3\), or \(4\) critical two-cells remain, according to the groups above. In each link for \(A\), exactly one critical zero-cell and one critical one-cell remain, giving \(S^1\); each link for \(B\) has one zero-cell and one two-cell, giving \(S^2\). For \(C\), each link has a matching with one critical zero-cell, and the verifier independently constructs an exhaustive sequence of elementary free-face collapses down to that vertex: each link is **simplicially collapsible**, not merely acyclic. Full acyclicity verification covers all \(5,376\) oriented face incidences across the complete collection of \(25\) complexes.

Finally, for every vertex the elementary decomposition
\[
K=(K-v)\cup\bigl(v*\operatorname{lk}_K(v)\bigr),\qquad
(K-v)\cap\bigl(v*\operatorname{lk}_K(v)\bigr)=\operatorname{lk}_K(v)
\]
is a union of simplicial subcomplexes. When the link is contractible, the attached cone is homotopically inessential, so the inclusion \(K-v\hookrightarrow K\) is a homotopy equivalence. For the remaining vertices, the second reduced integral Betti ranks are \(2\) or \(4\), as against \(3\) for \(K\), proving these inclusions cannot be homotopy equivalences. This completes the classification.

## Verification
Run `python3 verify_frucht.py` and `python3 verify_homology.py` using Python's standard library; both scripts are provided in full. The first enumerates all \(25\) complexes, checks every Morse matching against every codimension-one face incidence, performs full topological sorts and verifies all four elementary-collapse certificates. It returns `FRUCHT_MORSE_CERTIFICATE_OK` only after all assertions pass. The second constructs the graph independently from its LCF Hamiltonian-cycle representation, checks the stated isomorphism, and computes complete mod-two simplicial boundary ranks for the full complex and each deletion/link. It returns `FRUCHT_INDEPENDENT_HOMOLOGY_OK`. The independent homology computation checks, but does not substitute for, the discrete Morse homotopy proof.

## Relationship to prior work
The graph is standard and already documented in the graph literature (Weisstein's *Frucht Graph* entry gives its LCF representation). Barmak's 2010 star-cluster theorem establishes a suspension result when a graph has a vertex lying in no triangle. That hypothesis **does apply here**: vertices \(2\), \(8\), and \(11\) lie in no triangle. However, that theorem by itself supplies neither the exact three-sphere multiplicity nor the complete deletion/link classification. Goyal–Shukla–Singh's exact results concern generalized Mycielskians of complete graphs and categorical products of complete graphs, not this graph; Nilakantan–Shukla treat a specified family of regular bipartite graphs, whereas the Frucht graph contains triangles. Ehrenborg–Hetyei's sphere/contractibility results include forests, but the Frucht graph contains cycles. No inspected theorem determines these full graph-specific deletion and link data. The result makes no claim about any uninspected or unpublished literature.

## Limitations
The theorem concerns this single graph with the given labeling and exactly its one-vertex deletions/links. It does not claim a general theorem for all cubic graphs, Halin graphs, or asymmetric graphs. The finite certificates are exhaustive for these \(25\) complexes, but they do not establish global bibliographic uniqueness; an unindexed equivalent classification could exist. Verification and homotopy proof have been checked without a separate independent scientific audit.

## References
1. R. Frucht, *Herstellung von Graphen mit vorgegebener abstrakter Gruppe*, Compositio Mathematica 6 (1939), 239–250; graph data also catalogued by E. W. Weisstein, “Frucht Graph,” https://mathworld.wolfram.com/FruchtGraph.html.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2 July 2010), especially Theorems 3.4–3.5, https://arxiv.org/abs/1007.0418.
3. S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, https://arxiv.org/abs/1905.06926.
4. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789, https://arxiv.org/abs/1709.04789.
5. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, doi:10.1016/j.ejc.2005.04.010.
6. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
