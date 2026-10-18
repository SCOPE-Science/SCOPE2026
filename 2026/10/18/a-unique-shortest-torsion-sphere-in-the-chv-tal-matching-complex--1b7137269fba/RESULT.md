# A unique shortest torsion sphere in the Chvátal matching complex

## Finding
Let \(G\) be the twelve-vertex, twenty-four-edge Chvátal graph given explicitly below, and let \(K=\mathcal M(G)\) be its **ordinary matching complex**. There is an integral homotopy equivalence
\[
K\simeq \left(\bigvee^{28}S^3\right)\vee M(\mathbb Z/3,3),
\]
where \(M(\mathbb Z/3,3)=S^3\cup_{\deg 3}e^4\). Thus \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{28}\oplus\mathbb Z/3\), with other reduced integral homology zero.

Exactly **423 induced eight-vertex octahedral three-spheres** are shortest possible induced supports of nonzero ambient third homology. All 423 fundamental cycles are nontrivial in ambient integral homology. **Precisely one has exact order three**, and the other 422 have infinite order. Collectively the 423 fundamental cycles **generate all** of \(\widetilde H_3(K;\mathbb Z)\) integrally.

## Assumptions and scope
The graph vertices are \(0,\ldots,11\). Its edge set, in lexicographic order, is
```
[(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
 (2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
 (5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)]
```
These are the twelve vertices and twenty-four edges of the four-regular triangle-free Chvátal graph. A vertex of \(K\) is a graph edge; a simplex is a nonempty set of mutually vertex-disjoint graph edges (the empty face is included in boundary/face-poset constructions). The inclusion \(K[W]\hookrightarrow K\) is the induced inclusion for a subset \(W\) of its twenty-four complex vertices. An **induced octahedral three-sphere** means an induced subcomplex isomorphic to \((S^0)^{*4}\), the fourfold join of two-point sets.

The unique order-three carrier is the octahedral complex on the eight graph edges partitioned into four blocks
\[
\bigl(\{0,6\},\{0,9\}\bigr),\quad
\bigl(\{1,2\},\{1,7\}\bigr),\quad
\bigl(\{3,4\},\{4,8\}\bigr),\quad
\bigl(\{5,10\},\{5,11\}\bigr).
\]
Its signed fundamental cycle is the simplicial join of the corresponding four oriented differences of vertices of \(K\). Every pair in a block meets at one graph vertex, while edges from distinct blocks are disjoint. Consequently it is an induced cross-polytope boundary, with sixteen oriented tetrahedral facets.

## Proof
**Exact finite complex and Morse model.** Enumerating all matchings produces face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(24,204,752,1175,628,52).
\]
Use the lexicographically indexed edge list above. On the face poset, successively match every eligible remaining face not containing the indexed edge to its coface under the pivot indices
```
[12,5,19,17,22,18,15,8,20,7,1,23,
 21,11,14,13,10,9,6,3,16,2,0,4]
```
Remove the empty-face pair, so that its matched vertex is critical for ordinary Morse theory. This gives 1,399 nonempty face–coface pairs and exactly one critical zero-cell, 32 critical three-cells, and four critical four-cells. Orient each Hasse incidence downwards except matched incidences, oriented upwards. `verify_chvatal.py` constructs every such incidence and confirms a complete topological ordering of the directed Hasse graph, verifying acyclicity.

**Integral attaching matrix.** For each oriented critical four-simplex, eliminate all matched three-dimensional faces by signed gradient-path recursion. The resulting exact integral Morse boundary \(B\) is a \(32\times4\) matrix. Its Smith normal form has nonzero invariants \(1,1,1,3\). A rational-rank certificate is the nonzero determinant \(-3\) in critical three-cell rows \((0,1,4,18)\) (zero-based). Exact Smith reduction independently fixes the integral invariant factors. Since there are no critical one- or two-cells and only the above higher cells, the three-skeleton is a wedge of 32 three-spheres; the four-cell attaching maps are classified by their integer degrees via \(\pi_3(\bigvee^{32} S^3)\cong\mathbb Z^{32}\). Elementary integral changes of the four-cell and three-sphere bases realize homotopy equivalences, producing 28 free three-spheres, three cancellable pairs, and one three-dimensional mod-three Moore space. This proves the asserted integral homotopy equivalence.

**Minimal eight-vertex carriers.** Any nonzero third reduced homology of a flag simplicial complex needs at least eight vertices, and an eight-vertex flag complex with nonzero third homology is an octahedral three-sphere. This standard extremal flag-sphere lemma follows inductively using deletion/link Mayer–Vietoris: select a vertex whose link carries nontrivial second homology; the link needs six vertices, and nonadjacency forces one more vertex besides the selected one, giving eight; equality iterates to a join of four two-point sets. Here \(K\) is flag because incompatible pairs of graph edges determine all nonfaces. Thus there are no smaller induced third-homology carriers.

An octahedral carrier has four nonadjacent vertex pairs in \(K\), i.e. four pairs of graph edges meeting in one graph vertex, while all cross-block edges of \(G\) are disjoint. It is equivalent to a tiling of all twelve vertices of \(G\) by four vertex-disjoint length-two paths. `verify_chvatal.py` enumerates all 72 such paths and all disjoint four-path tilings; there are **exactly 423**, with no repeats.

**Exact ambient orders and generation.** Orient every octahedral fundamental cycle by the simplicial join of four vertex differences, including permutation signs in sorted vertex order. Project its signed sixteen-simplex chain to the 32 critical three-cell coordinates under the verified integral Morse reduction. For any resulting vector \(v\), membership in the rational image of \(B\) is decided by the inverse of the selected nonsingular \(4\times4\) minor, then checked against the entire matrix \(B\). Precisely one of the 423 vectors belongs to that rational image; it is the stated four-block cycle. Its coefficient vector is
\[
B\begin{pmatrix}-2/3\\-2/3\\1/3\\-1/3\end{pmatrix}=v.
\]
The coefficients are not all integers, but three times them are, so its class has exact order three. The other 422 vectors are outside the rational boundary image and thus have infinite order. Finally, the augmented integer matrix \([B\mid v_1\mid\cdots\mid v_{423}]\), of size \(32\times427\), has 32 unit Smith invariant factors. Hence the critical cycles together with the four boundaries span the **whole integral** Morse lattice: the 423 cycles generate \(\widetilde H_3(K;\mathbb Z)\), not merely its rationalization or a finite-index subgroup.

## Verification
Run `python3 verify_chvatal.py` and `python3 verify_modular.py` in a directory containing the packaged code, with the exact version of SymPy declared in `requirements.txt` (the modular verifier requires only Python 3). Both programs independently regenerate matchings. The first exhaustively certifies the acyclic Morse matching, signed integer reduction, integral Smith invariants, 423 shortest carriers, unique order-three vector, nonvanishing of all classes, and integral spanning. It ends with `INTEGRAL_GENERATION_SNF_32_UNITS VERIFY_OK`. The second reconstructs all simplicial boundary matrices and computes their ranks over four finite fields. In dimensions three through five, ranks over characteristics two, five and seven are \((571,576,52)\), and over three are \((571,575,52)\). This corroborates the unique three-torsion class. Finite-field ranks alone are not a proof of integral homology; the signed Morse Smith computation provides that proof.

## Relationship to prior work
Shareshian and Wachs study torsion in matching complexes of **complete** and **complete bipartite** graphs, including \(\mathcal M(K_{12})\), not this twenty-four-edge subgraph. Their complete-graph homology does not determine the matching-complex homology of an arbitrary subgraph, and it does not identify the exceptional induced octahedral cycle here. Jonsson's exact-sequence results likewise concern complete-graph matching complexes. Bayer, Jelić Milutinović and Vega prove that matching complexes of **outerplanar** graphs are contractible or wedges of spheres. The Chvátal graph is not outerplanar, since it has 24 edges whereas an outerplanar simple graph with 12 vertices has at most 21. A published computation of the icosahedral graph's ordinary matching complex gives another three-Moore-space example with a different ambient free rank; its underlying graph has 30 edges, and that result does not classify the present carrier. In contrast, the Grötzsch graph's ordinary matching complex is a torsion-free wedge of 24 three-spheres; the two canonical triangle-free four-chromatic examples behave differently. Earlier topological calculations of the Chvátal graph's **independence** or open-neighborhood complex concern different simplicial objects and do not imply this theorem.

## Limitations
The theorem is confined to the explicitly listed Chvátal graph and its ordinary matching complex; no minimum-order claim among all graph classes or general graph-family theorem is made. The 423 count and integral Morse certificates are large, but fully reconstructed by the attached scripts rather than inferred from partial sampling. The comparison with published literature does not prove absolute historical priority; equivalent less-indexed work remains possible. Independent external scientific validation has not been performed.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (public 2004-09-03), https://arxiv.org/abs/math/0409054.
2. J. Jonsson, *More Torsion in the Homology of the Matching Complex*, arXiv:1203.5641v1 (public 2012-03-26), https://arxiv.org/abs/1203.5641.
3. M. Bayer, Z. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, https://arxiv.org/abs/2411.04601.
4. *Three-torsion in the icosahedral matching complex: a planar counterexample*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a.
5. *The Grötzsch graph matching complex is a wedge of twenty-four three-spheres*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-gr-tzsch-graph-matching-complex-is-a-wedge-of-twenty-four-th--514850eb507b.
