# Two-degree sphere splittings and integral symmetry modules for clique bouquets

## Finding
Fix integers \(r\ge2\) and \(t\ge3\), and integers \(a_1,\ldots,a_r\ge1\). Form the simple graph \(W(a_1,\ldots,a_r)\) from \(r\) complete graphs \(K_{a_i+1}\) by identifying exactly one vertex \(v\) of each, with no other identifications or edges between their private vertex sets. Write \(\mathsf{CF}_t(W)\) for the simplicial complex whose faces are vertex subsets spanning no clique of order \(t\).

Put
\[
 d_{\mathrm{hi}}=r(t-1)-1,\qquad d_{\mathrm{lo}}=r(t-2),\qquad
 M_{\mathrm{hi}}=\prod_{i=1}^r\binom{a_i-1}{t-1},\qquad
 M_{\mathrm{lo}}=\prod_{i=1}^r\binom{a_i-1}{t-2}.
\]
Then there is an **integral homotopy equivalence**
\[
 \mathsf{CF}_t(W)\simeq
 \left(\bigvee^{M_{\mathrm{hi}}}S^{d_{\mathrm{hi}}}\right)
 \vee\left(\bigvee^{M_{\mathrm{lo}}}S^{d_{\mathrm{lo}}}\right).
\]
A zero-fold wedge is understood as a point. The lower multiplicity is positive exactly when every \(a_i\ge t-1\), and the upper multiplicity is positive exactly when every \(a_i\ge t\). If any \(a_i\le t-2\), both vanish and the complex is contractible. When present, the two sphere dimensions differ by \(r-1\).

There is also a natural **integral homology-module refinement**. Let \(A_i\) be the private vertices of clique \(i\), let \(U_i=\ker(\mathbb Z^{A_i}\xrightarrow{\mathrm{sum}}\mathbb Z)\), and let \(\Gamma=\prod_{i=1}^r S_{a_i}\) permute private vertices within each clique while fixing \(v\). Then, as integral \(\Gamma\)-lattices,
\[
 \widetilde H_{d_{\mathrm{hi}}}(\mathsf{CF}_t(W);\mathbb Z)
 \cong\bigotimes_{i=1}^r\bigwedge^{t-1}U_i,
 \qquad
 \widetilde H_{d_{\mathrm{lo}}}(\mathsf{CF}_t(W);\mathbb Z)
 \cong\bigotimes_{i=1}^r\bigwedge^{t-2}U_i.
\]
Every other reduced integral homology group is zero. Only the homology isomorphisms, not an equivariant wedge-space equivalence, are asserted to be \(\Gamma\)-equivariant.

For example, when \(r=2\), \(t=3\), and \((a_1,a_2)=(3,4)\), the complex is \(\bigvee^3S^3\vee\bigvee^6S^2\). When \(r=3\), \(t=3\), and all three private-part sizes equal \(3\), it is \(S^5\vee\bigvee^8S^3\).

## Assumptions and scope
All graphs are finite, simple, loopless and undirected. The graph is a one-vertex bouquet of complete blocks, not a complete graph join of its blocks. The assumptions \(r\ge2\), \(t\ge3\), and \(a_i\ge1\) define the full nontrivial bouquet setting covered here; smaller private cliques are included through the contractible case. The convention \(\binom nk=0\) for \(k>n\) is used. The result classifies ordinary homotopy types and their natural *within-block* leaf-permutation integral homology; it does not classify the full automorphism action when distinct blocks can be exchanged.

## Proof
**1. Exact face decomposition.** Every clique of order at least three in \(W\) is contained in one of its complete blocks. Indeed, two private vertices from distinct blocks are never adjacent. A vertex subset \(F\) avoiding \(t\)-cliques therefore satisfies \(|F\cap A_i|\le t-1\) for all \(i\) if \(v\notin F\), and \(|F\cap A_i|\le t-2\) for all \(i\) if \(v\in F\). Denote the \(q\)-skeleton of the simplex on \(A_i\) by \(E_i(q)\). Define
\[
 K_0=E_1(t-2)*\cdots*E_r(t-2),\qquad
 L=E_1(t-3)*\cdots*E_r(t-3).
\]
The simplicial identities, including the intersection, are exact even when some private blocks are too small to contain a forbidden clique:
\[
 \mathsf{CF}_t(W)=K_0\cup\bigl(v*L\bigr),\qquad K_0\cap(v*L)=L.
\]
Thus the sought space is the homotopy cofiber of the inclusion \(L\hookrightarrow K_0\). Moreover, if some \(a_i\le t-2\), every private vertex in that block can be freely added to every face, so the complex is a cone; both proposed multiplicities are then zero. For the remaining proof of the noncontractible formula, assume every \(a_i\ge t-1\).

**2. Skeleton lemma with integral symmetry.** For \(a\ge q+2\), the \(q\)-skeleton of a simplex on \(a\) vertices has homotopy type \(\bigvee^{\binom{a-1}{q+1}}S^q\). One direct proof chooses a distinguished vertex \(w\) and pairs every nonempty face not containing \(w\) of size at most \(q\) with its union with \(w\). This is an acyclic matching (toggle a fixed vertex), leaving the vertex \(w\) and the \(\binom{a-1}{q+1}\) faces of size \(q+1\) avoiding \(w\); these are its only critical cells. For \(q=0\) the formula simply counts the remaining isolated points. For \(a\le q+1\), the skeleton is a full simplex and contractible, agreeing with the zero-multiplicity convention.

For the integral module statement, order the vertex set \(A\) and identify the oriented augmented simplicial chain group in degree \(q\) with \(\bigwedge^{q+1}\mathbb Z^A\). The boundary is contraction by the augmentation covector \(\epsilon\) that sums coordinates. The full simplex's augmented chain complex is exact, so the top reduced homology of its \(q\)-skeleton is \(\ker\bigl(\iota_\epsilon:\bigwedge^{q+1}\mathbb Z^A\to\bigwedge^q\mathbb Z^A\bigr)\). Splitting \(\mathbb Z^A=U\oplus\mathbb Ze_w\) (where \(\epsilon(e_w)=1\)) identifies this kernel naturally with \(\bigwedge^{q+1}U\), which is independent of the temporary splitting and respects the entire vertex-permutation action.

**3. Homotopy types of the two joins.** A join of \(r\) nonempty complexes homotopy equivalent to wedges of spheres all of dimensions \(q_i\) is a wedge of spheres of dimension \(\sum_i(q_i+1)-1\), with multiplicity the product of the original multiplicities. If one factor is contractible, the join is contractible. Applying the skeleton lemma gives
\[
 K_0\simeq\bigvee^{M_{\mathrm{hi}}}S^{d_{\mathrm{hi}}},\qquad
 L\simeq\bigvee^{M_{\mathrm{lo}}}S^{d_{\mathrm{lo}}-1}.
\]
Here \(L\) is nonempty and path connected: each factor is nonempty and \(r\ge2\). All homology statements in this step hold over \(\mathbb Z\), without torsion, by the join chain-Künneth isomorphism.

**4. Null attaching map and splitting.** If \(K_0\) is not contractible, it is \((d_{\mathrm{hi}}-1)\)-connected by step 3. But \(L\) has geometric dimension \(d_{\mathrm{lo}}-1\), and
\[
 (d_{\mathrm{hi}}-1)-(d_{\mathrm{lo}}-1)=r-1\ge1.
\]
Thus every map from \(L\) into \(K_0\), in particular its inclusion, is nullhomotopic by cellular obstruction theory (or the CW dimension/connectivity criterion). When \(K_0\) is contractible the inclusion is nullhomotopic as well. Because \(L\hookrightarrow K_0\) is a simplicial cofibration, the homotopy cofiber of this null map is \(K_0\vee\Sigma L\). Substituting step 3 yields exactly the asserted ordinary integral wedge decomposition. No computation of homology alone is being used to infer the homotopy splitting.

**5. Natural integral representations.** For each clique, step 2 identifies the skeleton's top integral homology, naturally under \(S_{a_i}\), with an exterior power of \(U_i\). The canonical reduced join Künneth isomorphisms identify the unique possible upper homology of \(K_0\) and the top homology of \(L\) with the corresponding tensor products. Since \(d_{\mathrm{hi}}>d_{\mathrm{lo}}\), the long exact homology sequence of the pair \((K_0\cup(v*L),K_0)\) identifies the upper group with \(\widetilde H_{d_{\mathrm{hi}}}(K_0)\) and the lower group with \(\widetilde H_{d_{\mathrm{lo}}-1}(L)\). These identifications commute with within-block permutations: the central cone vertex is fixed and the pair, inclusion and connecting maps are natural. This gives the two displayed integral \(\Gamma\)-module isomorphisms and concludes the proof.

## Verification
The accompanying standalone `verify.py` enumerates vertex subsets independently in two ways: by the quota characterization in step 1 and by literal adjacency tests of every \(t\)-clique in the generated graph. For 23 parameter configurations it computes *all* reduced mod-two Betti numbers using simplicial boundary matrices and checks the two claimed degrees and multiplicities. It additionally computes signed Lefschetz numbers of within-block leaf permutations from the actual oriented simplices and compares them against the traces of the exterior-power augmentation representations. The deterministic output is in `verify_output.txt`. The run checks 7,278 nonempty faces and 235 signed symmetry cases. These are finite corroborating calculations only; the all-parameter integral result follows from steps 1–5.

## Relationship to prior work
Ghosh and Selvaraja (arXiv:2602.09623v1, first posted 2026-02-10) prove that \(t\)-clique-free complexes of block graphs are shellable (Corollary 3.4); the clique bouquets above are block graphs. That qualitative theorem does not specify the two homology degrees, exact sphere multiplicities, or integral leaf-permutation lattices. Their Theorem 4.2 addresses preservation of shellability under clique attachments, not a homotopy formula. Khosh-Ahang and Moradi (2019) prove vertex-decomposability statements for related \(t\)-clique ideals, including complements of certain trees, but do not supply this bouquet classification. Published results for *open-neighborhood complexes* of windmills and block graphs study a different simplicial complex: sets with a common neighbor rather than sets avoiding an order-\(t\) clique. Their homotopy statements do not imply the present formula. Existing calculations of matching or multipath complexes of windmills likewise use edge or arc subsets, not these vertex subsets. Focused semantic and keyword searches for the graph, clique-free construction, cone decomposition, integral representation and exact binomial-product formula did not identify equivalent or dominating coverage; absence from searches alone is not proof of priority.

## Limitations
This result does not classify arbitrary block graphs with multiple articulation vertices, general clique sums along an edge, or all automorphisms that exchange entire blocks. No equivariant homotopy equivalence or simple-homotopy equivalence is asserted. An elementary or differently indexed pre-existing formula could remain undiscovered. The finite verifier does not establish any assertion for parameters outside its declared cases, and its mod-two calculations cannot rule out integral torsion by themselves; torsion-freeness and the homotopy type follow from the explicit proof.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first public posting 2026-02-10. https://arxiv.org/pdf/2602.09623.
2. F. Khosh-Ahang and S. Moradi, *Some algebraic properties of t-clique ideals*, Communications in Algebra 47 (2019), DOI 10.1080/00927872.2018.1541462.
3. *Clique joins suspend Lovász neighborhood complexes*, publicly available mathematical record, 2026-10-11. The associated neighborhood construction differs from clique avoidance.
4. *Blockwise sphere bouquets in neighborhood complexes of block graphs*, publicly available mathematical record, 2026-10-11. The block-graph domain overlaps, but the simplicial functor does not.
