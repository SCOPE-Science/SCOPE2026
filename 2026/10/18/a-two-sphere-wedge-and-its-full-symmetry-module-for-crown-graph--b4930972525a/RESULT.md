# A two-sphere wedge and its full symmetry module for crown-graph two-independence complexes

## Finding
For every integer \(n\ge 4\), let \(G_n\) be the crown graph obtained from \(K_{n,n}\) by removing a perfect matching. Define \(X_n=\operatorname{Ind}_2(G_n)\) as the simplicial complex of all vertex sets whose **induced connected components contain at most two vertices**. Then
\[
X_n\simeq\bigvee^{\binom{n-1}{2}}S^2.
\]
In particular, \(\widetilde H_2(X_n;\mathbb Z)\cong\mathbb Z^{\binom{n-1}{2}}\), all other reduced integral homology vanishes, and there is no integral torsion.

The full natural graph-symmetry action is also determined. Diagonal permutations \(\sigma\in S_n\) of the matched pairs, together with the bipartition exchange \(\tau\) of order two, act on integral second homology as
\[
\widetilde H_2(X_n;\mathbb Z)\ \cong\ H_1(K_n^{(1)};\mathbb Z)\otimes\varepsilon,
\]
where \(K_n^{(1)}\) is the complete graph as a one-dimensional CW complex, \(S_n\) permutes its vertices, and \(\varepsilon\) is the sign representation of the bipartition exchange. Over \(\mathbb Q\), the first factor is \(\bigwedge^2 U_n\), where \(U_n=\{(x_1,\ldots,x_n)\in\mathbb Q^n:\sum x_i=0\}\). The complete rational character is
\[
\operatorname{tr}(\sigma\tau^e\mid\widetilde H_2(X_n;\mathbb Q))
=(-1)^e\frac{(f(\sigma)-1)^2-(f(\sigma^2)-1)}{2},
\]
for \(e\in\{0,1\}\), with \(f(\pi)\) the number of fixed points of \(\pi\) on the matched-pair indices.

## Assumptions and scope
Write the vertex bipartition as \(A=\{a_i:1\le i\le n\}\) and \(B=\{b_i:1\le i\le n\}\). The edges are precisely \(\{a_i,b_j\}\) with \(i\ne j\). All spaces are finite abstract simplicial complexes with their geometric realizations. The statement holds for every integer \(n\ge4\), with no parity assumption. The boundary case \(n=3\) also follows by the same construction, but is not used for the claimed infinite family. The group action is a statement about **integral homology representations**, not a claim of an equivariant homotopy equivalence.

## Proof
**1. Classification of faces.** Every subset of \(A\), and every subset of \(B\), is a face. A mixed face contains at most two vertices from each bipartition class: any opposite vertex is adjacent to at least two members of a three-element subset in one class, producing a connected component of size at least three. A mixed face with two vertices from one class and one from the other is allowed exactly when the singleton index equals one of the two opposite-side indices. A mixed face with two vertices in each class is allowed exactly when the two index sets coincide: if they differ, one opposite-side vertex has two neighbors and creates a component containing at least three vertices. All mixed faces with just one vertex on each side are automatically allowed. Thus every mixed face is contained in one of the four-vertex simplices
\[
T_{ij}=\Delta\{a_i,a_j,b_i,b_j\},\qquad 1\le i<j\le n.
\]
Every \(T_{ij}\) is indeed a simplex: its induced graph is two disjoint edges. Consequently the two full simplices \(\Delta A,\Delta B\) together with all \(T_{ij}\) form a cover of \(X_n\).

**2. First nerve.** Every nonempty finite intersection of these cover members is a full simplex on its common vertices, hence contractible. The two full simplices \(\Delta A\) and \(\Delta B\) have empty intersection. A family of distinct \(T_{ij}\) has nonempty intersection exactly when their index pairs share a common index. Such an intersection contains both \(a_i\) and \(b_i\) for a common index \(i\), and its intersections with either \(\Delta A\) or \(\Delta B\) remain nonempty. Every \(T_{ij}\) meets both full simplices. By the simplicial nerve lemma, the first cover nerve is
\[
N= S^0*P=\Sigma P,
\]
where \(P\) has one vertex \(e_{ij}\) for each unordered pair \(\{i,j\}\), and a set of these vertices spans a simplex precisely when all its corresponding pairs have a common endpoint. The two vertices of \(S^0\) correspond to \(\Delta A,\Delta B\).

**3. Second nerve.** The complex \(P\) is covered by the \(n\) simplices \(C_i=\Delta\{e_{ij}:j\ne i\}\). Each pairwise intersection \(C_i\cap C_j\) is exactly the vertex \(e_{ij}\), while every triple intersection is empty. Thus its good-cover nerve is the complete graph \(K_n^{(1)}\), without filled triangles. Hence
\[
P\simeq K_n^{(1)}\simeq\bigvee^{\binom n2-n+1}S^1
=\bigvee^{\binom{n-1}{2}}S^1.
\]
Suspension of a wedge of circles yields the asserted wedge of two-spheres. This proves the integral homotopy statement for all \(n\), not just those tested computationally.

**4. Full symmetry representation.** The group \(S_n\times C_2\) preserves the original graph and first cover, permuting \(T_{ij}\) and either preserving or exchanging the two full-side simplices. The second cover of \(P\) is \(S_n\)-invariant. The augmentations in the simplicial Čech double complexes of these two covers are natural for these permutation actions. Since every nonempty cover intersection is a simplex, the vertical homology is concentrated in degree zero; its horizontal differential is the respective nerve differential. Therefore the resulting homology identifications are integral and equivariant. Interchanging the two suspension vertices induces multiplication by \(-1\) on suspension-reduced homology; a diagonal pair permutation induces the usual permutation action on \(H_1(K_n^{(1)};\mathbb Z)\). This proves the stated integral module identification.

For completeness, the rational vertex permutation module of the complete graph decomposes as \(\mathbb Q^n=\mathbf1\oplus U_n\). Its oriented-edge chain module is \(\bigwedge^2\mathbb Q^n=U_n\oplus\bigwedge^2 U_n\), and the graph boundary maps the first summand isomorphically onto the reduced vertex chain module, with kernel \(\bigwedge^2 U_n\). Finally, the exterior-square trace identity \(\operatorname{tr}(\bigwedge^2 T)=((\operatorname{tr}T)^2-\operatorname{tr}(T^2))/2\) and \(\operatorname{tr}(\sigma\mid U_n)=f(\sigma)-1\) give the displayed character formula. The exchange \(\tau\) multiplies it by \(-1\), completing the proof.

## Verification
The included `verify.py` independently checks the bounded-component definition for every vertex subset against the proposed face classification, verifies the entire maximal-face list, and reduces actual simplicial boundary matrices modulo two. It checks all \(2n!\) natural automorphisms for \(n=3,4,5,6\) and selected nontrivial automorphisms for \(n=7,8\), evaluating signs on oriented faces to compare reduced Lefschetz traces with the theoretical character. All runs for \(3\le n\le8\) passed. Use `python3 verify.py --max-n 8`; no nonstandard dependencies are needed. Detailed output appears in `verification_output.txt`. Finite checks corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Deshpande and Singh (2020, arXiv:2001.05448v1) define this bounded-component convention and classify higher-independence complexes for complete multipartite graphs, whiskered graphs, paths, cycles, and perfect rooted trees. For \(n\ge4\), the crown graph is not itself complete multipartite (the deleted cross-pairs obstruct that property), and their inspected family results do not directly determine this complex. Abdelmalek and coauthors (2021, arXiv:2106.10863v1) treat chordal graphs and related classes, whereas a crown graph has induced cycles of length at least four and is not chordal. Related neighborhood complexes whose decompositions involve crown graphs describe a different face condition; they do not imply the present result. The precise two-stage nerve decomposition and the complete symmetry character are the contributions established here.

## Limitations
The theorem treats only the two-independence stage and crowns with at least four matched pairs; it does not determine higher component bounds or a classification for arbitrary matching-deleted bipartite graphs. The displayed homotopy equivalence need not respect all group actions, though the stated integral homology isomorphism does. Searches of accessible literature cannot exclude an unindexed equivalent theorem. A separate independent mathematical review has not been performed.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first public 2020-01-15), https://arxiv.org/abs/2001.05448.
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1, https://arxiv.org/abs/2106.10863.
3. *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710v1, https://arxiv.org/abs/2510.25710 (different indexing conventions for higher independence are noted).
