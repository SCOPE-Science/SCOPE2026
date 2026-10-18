# Split integral homology at the critical cycle-power three-cut boundary

## Finding
For every integer \(p\ge2\), let \(G_p=C_{4p}^{p}\) be the graph on the cyclic set \(\mathbb Z/(4p)\) with adjacent distinct vertices at cyclic distance at most \(p\). Let \(\Delta_3(G_p)\) be the ordinary three-cut complex, whose facets are complements of disconnected induced three-vertex subsets of \(G_p\). Then
\[
\widetilde H_{4p-5}(\Delta_3(G_p);\mathbb Z)\supseteq_{\rm split}\mathbb Z^{p-1}.
\]
Consequently the pure \((4p-4)\)-complex \(\Delta_3(G_p)\) is not shellable. The inclusion indicates a direct summand, not an equality of complete homology groups.

## Assumptions and scope
All graphs are finite, simple, undirected. Integers \(p\ge2\) are arbitrary. The ordinary cut complex uses complements of *disconnected induced* vertex triples, not total cut complexes. Reduced homology is integral. Faces include the empty face; a simplicial map may identify vertices provided the image of a source face is a target face.

## Proof
**Alexander dual.** Put \(N=4p\) and \(K_p=\Delta_3(G_p)^\vee\), with Alexander dual taken inside the full simplex on all \(N\) vertices. A subset \(S\) is a face of \(K_p\) precisely when its complement is not a face of \(\Delta_3(G_p)\). Since the facets of the cut complex are complements of disconnected triples, this means that no disconnected triple lies in \(S\). Thus every three-element subset of \(S\) induces a connected graph. This equivalence includes faces of size less than three.

**Octagonal sphere.** For \(p=2\), a direct enumeration on \(C_8^2\) gives the nonempty face counts \((8,28,32,10)\), by vertex-cardinality \(1,2,3,4\). The accompanying standalone verifier lists and checks twenty free-face/coface pairs. After elementary simplicial collapses, the residual complex has \((8,18,12)\) faces, with every edge in exactly two triangles, every vertex link a circle, a connected one-skeleton and Euler characteristic two. Hence \(K_2\simeq S^2\) and \(H_2(K_2;\mathbb Z)=\mathbb Z\). The rotation \(r:j\mapsto j+1\) of the eight vertices has degree \(-1\) on this group: no nonempty simplex of \(K_2\) is setwise fixed by \(r\), since its vertex orbits have size eight and the full eight-set is not a simplex. Thus the unreduced Lefschetz number is zero; the homotopy type has only \(H_0\) and \(H_2\), whence \(0=1+\operatorname{tr}(r_*\mid H_2)\).

**Sections and block quotients.** For \(0\le s,t<p\), partition the \(4p\) cyclic source vertices into eight consecutive alternating blocks of lengths \(1,p-1,1,p-1,1,p-1,1,p-1\), with the first block beginning at \(s\). Denote the blocks \(B_0^{(s)},\ldots,B_7^{(s)}\), and define \(q_s:V(G_p)\to\mathbb Z/8\) by block number. Define \(e_t:\mathbb Z/8\to V(G_p)\) by
\[
e_t(2k)=t+kp,\qquad e_t(2k+1)=t+kp+1\quad(k=0,1,2,3),
\]
all source indices modulo \(4p\). Both maps take each graph edge to either an edge or one vertex: in the block quotient, moving between blocks whose cyclic indices differ by at least three requires at least \(p+1\) source steps; a source edge therefore only meets the same block or a block at cyclic distance one or two; for the section, target jumps of one or two indices map to source cyclic distances at most \(p\). A weak graph homomorphism preserves connectedness of triple images when all three image vertices differ, and images with fewer than three vertices are automatically faces. Therefore \(q_s\) and \(e_t\) induce simplicial maps \(Q_s:K_p\to K_2\) and \(E_t:K_2\to K_p\).

**Integral degree matrix.** Consider the composition on the eight target vertices. Up to the rotation by two positions induced by translating source indices by \(p\), and with all shift differences reduced modulo \(p\), one has the following complete trichotomy. If \(t=s\), then \(q_s e_t\) is the identity; if \(t=s-1\pmod p\), it is rotation by one position (possibly composed with an even rotation); in every other case, the image of the entire eight-vertex target belongs to a single four-vertex parity class (either \(\{1,3,5,7\}\) or \(\{0,2,4,6\}\)), and thus factors through its simplex. Both parity classes form simplices of \(K_2\), since each of their three-vertex subsets is connected in \(C_8^2\). Thus on \(H_2(K_2;\mathbb Z)=\mathbb Z\),
\[
\deg(Q_sE_t)=\mathbf 1_{s=t}-\mathbf 1_{t=s-1\pmod p}.
\]
The first term is degree \(+1\), the second is degree \(-1\), and all other composites have degree zero. The formula also holds at \(p=2\). It can be verified directly from eight residues for each relative shift; the checker performs the exact integral signed test for \(2\le p\le16\), while this trichotomy proves it for all \(p\ge2\).

Let \(E:\mathbb Z^p\to H_2(K_p;\mathbb Z)\) be the direct sum of the \((E_t)_*\), and let \(Q:H_2(K_p;\mathbb Z)\to\mathbb Z^p\) be the product of the \((Q_s)_*\). Their composite is the \(p\times p\) integer matrix \(D=(\mathbf 1_{s=t}-\mathbf 1_{t=s-1\pmod p})\). Its principal \((p-1)\times(p-1)\) minor obtained by dropping the last row and last column is unit triangular, of determinant one. Projection onto the first \(p-1\) coordinates, composed with \(Q\), therefore restricts to an isomorphism on the free subgroup generated by \((E_0)_*,\ldots,(E_{p-2})_*\). This gives an *integrally split* copy of \(\mathbb Z^{p-1}\) in \(H_2(K_p;\mathbb Z)\).

**Duality and shellability.** Integral combinatorial Alexander duality gives
\[
\widetilde H_{N-5}(\Delta_3(G_p);\mathbb Z)\cong \widetilde H^2(K_p;\mathbb Z).
\]
By the integral universal coefficient theorem, the split free summand just exhibited injects as a direct summand in degree-two cohomology. Every facet of the cut complex has size \(N-3\), hence its dimension is \(N-4\). A pure shellable complex has vanishing reduced integral homology below its top dimension; here the next-to-top group is nonzero. Therefore \(\Delta_3(C_{4p}^{p})\) is not shellable for every \(p\ge2\).

## Verification
Run `python3 verify.py` using only Python's standard library. It enumerates and checks all 78 nonempty faces of \(K_2\), performs and certifies twenty elementary free-face cancellations, verifies the closed-surface sphere criterion, tests the relevant weak graph maps for \(2\le p\le64\), and recomputes every signed degree entry for \(2\le p\le16\). The finite tests do not replace the all-parameter block argument or duality proof.

## Relationship to prior work
Chauhan and Shukla (2026), arXiv:2603.23155v1, establish shellability for \(n\ge6p-3\) and discuss the unsettled low-\(n\) boundary for cycle powers. Chauhan, Shukla and Vinayak (2024), arXiv:2406.01979v1, formulate an exact wedge-of-spheres homotopy conjecture at \(n=4p\), including the putative rank \(p-1\) in the next-to-top degree. The present result proves that conjecture's **non-shellability implication** for every \(p\ge3\), and an integral split lower bound, not the conjectured full homotopy equivalence or exact Betti number. Finite cases previously tabulated are not claimed as new.

## Limitations
The result determines neither the complete integral homology nor possible torsion, and does not prove a wedge-of-spheres decomposition. No claim is made for arbitrary \(n\ne4p\), or for total cut complexes. Finite checker ranges are independent consistency evidence; the universal quantifier rests on the symbolic block and duality proof. Other unindexed or inaccessible literature could already contain an equivalent argument.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1 (first public March 24, 2026).
2. P. Chauhan, S. Shukla and Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979v1 (first public June 4, 2024), Conjecture 4.2.
3. Standard combinatorial Alexander duality and the universal coefficient theorem for simplicial complexes.
