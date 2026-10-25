# Two mixed-dimensional integral transitions in the closed vertex-ball nerves of the Folkman graph

## Finding
Let \(G\) be the 20-vertex Folkman graph, presented as the subdivided double of \(K_5\), and equip its vertices with shortest-path distance. For every real radius \(r\geq0\), let \(W_r(G)\) be the nerve of the twenty finite sets \(B_r(v)=\{w\in V(G):d_G(v,w)\leq r\}\). The simplex condition is
\[
\sigma\in W_r(G)\quad\Longleftrightarrow\quad
\bigcap_{v\in\sigma}B_r(v)\ne\varnothing
\quad\Longleftrightarrow\quad
\exists w\in V(G)\;\forall v\in\sigma:\ d_G(w,v)\leq r.
\]
Then all nonzero **reduced integral** homology groups are as follows:
\[
\begin{array}{c|l}
\text{radius}&\text{nonzero reduced integral homology}\\\hline
0\leq r<1&\widetilde H_0(W_r;\mathbb Z)\cong\mathbb Z^{19}\\
1\leq r<2&\widetilde H_1(W_r;\mathbb Z)\cong\mathbb Z^{6},\quad
\widetilde H_2(W_r;\mathbb Z)\cong\mathbb Z^{15}\\
2\leq r<3&\widetilde H_3(W_r;\mathbb Z)\cong\mathbb Z^{5},\quad
\widetilde H_4(W_r;\mathbb Z)\cong\mathbb Z^{15}\\
r\geq3&0.
\end{array}
\]
Every unlisted reduced integral homology group vanishes. Thus all groups are torsion-free. The **complete reduced persistence barcode over every coefficient field** consists of 19 degree-zero bars \([0,1)\), six degree-one and fifteen degree-two bars \([1,2)\), and five degree-three and fifteen degree-four bars \([2,3)\). This statement concerns the vertex-ball nerve filtration; it does **not** classify the intervening odd scales of the conventional graph-geometric Čech filtration.

## Assumptions and scope
Write \(T_i=\{t_{i,0},t_{i,1}\}\) for \(i\in\{0,1,2,3,4\}\), and \(E=\{e_{ij}:0\leq i<j\leq4\}\). The vertex set of \(G\) is the disjoint union of the ten twin vertices and ten edge vertices. Its edges are exactly \(t_{i,s}e_{ij}\) for \(s\in\{0,1\}\) and \(j\ne i\). Thus \(G\) has 20 vertices, 40 edges and degree four at each vertex. Every edge has unit length. In this paper, the nerve uses closed balls in the **vertex shortest-path metric**, with both centers and possible intersection witnesses required to be vertices. The filtration parameter is the ball radius, not the conventional Čech scale.

For an integer \(k\geq0\), \(W_k(G)\) is canonically the even-scale graph-geometric Čech complex \(\mathcal N(G,2k)\) of Adams–Shukla–Singh [1], by their neighborhood lemma. However, \(W_r\) between integer radii is the constant vertex-metric filtration: it must not be identified with the full graph-geometric Čech complex at every real scale.

## Proof
**1. Exact graph distances and facets.** Put \(E_i=\{e_{ij}:j\ne i\}\) and \(T=\bigcup_iT_i\). Two distinct twin vertices have distance two; a twin \(t_{i,s}\) has distance one to an edge vertex \(e_{jk}\) when \(i\in\{j,k\}\) and distance three otherwise. Two distinct edge vertices have distance two when the underlying edges of \(K_5\) intersect and distance four when they are disjoint. The facts follow directly from the bipartite incidence description: all twin pairs share a subdivided edge, all intersecting edge pairs share a twin, and a shortest path between disjoint edge vertices has length four.

Therefore the **exact** radius-one and radius-two balls are
\[
\begin{aligned}
B_1(t_{i,s})&=\{t_{i,s}\}\cup E_i,&
B_1(e_{ij})&=\{e_{ij}\}\cup T_i\cup T_j,\\
B_2(t_{i,s})&=T\cup E_i,&
B_2(e_{ij})&=T_i\cup T_j\cup E_i\cup E_j.
\end{aligned}
\]
The twenty radius-one balls are distinct maximal facets, each of size five. At radius two the twin balls coincide in pairs, leaving precisely five facets of size fourteen, and the ten edge-centered balls are maximal facets of size eleven. No inclusion between these fifteen facets occurs. Thus the displayed formulas determine **every** simplex, not a sampled collection.

**2. Exhaustive elementary-collapse certificate.** The self-contained file `verify.py` independently reconstructs the graph and shortest-path distances, generates every nonempty subface of each maximal ball, then applies explicit deterministic elementary collapses. A face \(\alpha\) is paired with a face \(\beta\) obtained by adjoining one vertex only when \(\beta\) is its unique immediate coface in the *remaining* complex. This condition implies that \(\alpha\) has no other coface of any higher dimension, so the pair is a legitimate elementary simplicial collapse. The algorithm always chooses a currently eligible upper face of maximal dimension, breaking ties by its bitmask vertex label; it continues until no such pair exists. Counts and ranks are recomputed when `verify.py` is executed, not read from a saved log.

The exact complete enumerations and their collapsed residual complexes have the following dimension-ordered face vectors:

| Radius | Original nonempty faces | Collapse pairs | Residual nonempty face vector |
| --- | ---: | ---: | --- |
| \(1\) | 430 | 130 | \((20,80,70)\) |
| \(2\) | 81,233 | 39,641 | \((19,159,558,811,404)\) |

Each residual is simplicially closed and is homotopy equivalent to its original complex because every removed pair is a free-face elementary collapse. Vertices disappearing from the residual are allowed: they lie in the removed elementary pairs.

**3. Exact integral boundary reductions.** Orient simplices by increasing vertex label. Construct the complete signed simplicial boundary matrices of each residual complex, with signs \((-1)^j\) on deletion of vertex position \(j\). Apply integer row and column operations using only pivots \(+1\) and \(-1\). Each such pivot separates a unit invariant factor; its Schur complement is computed with integers and preserves the remaining Smith invariants. After the stated number of unit pivots, **every remaining entry is zero**, proving that every nonzero Smith invariant factor is one. The integral boundary ranks are
\[
\begin{array}{c|rrrr}
&\operatorname{rank}\partial_1&\operatorname{rank}\partial_2&
\operatorname{rank}\partial_3&\operatorname{rank}\partial_4\\\hline
W_1&19&55&0&0\\
W_2&18&141&417&389.
\end{array}
\]
For radius one, ordinary Betti numbers are \((1,6,15)\); for radius two, they are \((1,0,0,5,15)\). These follow from the displayed face vectors and the exact boundary-rank identity \(\beta_j=f_j-\operatorname{rank}\partial_j-\operatorname{rank}\partial_{j+1}\). All homology is free abelian because the unit invariant factors make each boundary image saturated. The certificate additionally reconstructs every boundary over \(\mathbb F_2\) and independently checks each rank by binary Gaussian elimination.

**4. Endpoints and persistence.** At radius zero, every ball is a singleton, giving 20 isolated points. Each twin vertex has eccentricity three, so for radius at least three one closed vertex ball contains all twenty vertices. The nerve is then the full nineteen-simplex. Graph distances are integral, and hence no other radius introduces a new face. At adjacent nontrivial scales the nonzero reduced homology occurs in distinct degrees: degrees zero, then one and two, then three and four, and finally none. Consequently all structure maps between successive nonzero stages vanish degreewise. This gives exactly the stated integral groups and the complete barcode over fields.

## Verification
The included standard-library Python 3 file `verify.py` implements all twenty graph distances by breadth-first search, all face generators, all elementary free-face pair removals, integer unimodular boundary diagonalization, and an independent binary boundary-rank calculation. Run `python3 verify.py`. A successful execution ends with `VERIFY_OK`; its exact output is also supplied in `verification_output.txt`. The check is exhaustive for this **fixed finite graph**, not a projection from a handful of examples. The theorem makes no claim for a parametrized family of other graphs.

## Relationship to prior work
Adams, Shukla and Singh [1] define the vertex-centered graph-geometric Čech filtration and prove its even-scale ball-neighborhood description. Their explicit homotopy theorems concern hypercube graphs, and do not compute either of the two Folkman-graph complexes here. Matsushita [2] proves a broad suspension comparison for closed-neighborhood complexes and studies special graph products, but no inspected theorem supplies these exact integral groups for the Folkman graph or its radius-two vertex-ball nerve.

The published Rips filtration of once-subdivided complete graphs [3] concerns a **different** clique-complex construction. Although it is combinatorially related to the doubled-subdivision presentation used here, it does not imply the current nerve membership criterion or its integral boundary ranks. An inspected result on Steiner-design incidence graphs [4] concerns **open** neighborhood complexes of the undoubled incidence graph, not the present **closed** radius-one and radius-two ball nerves. An inspected square-completion theorem [5] assumes no three common neighbors for a vertex pair, while the two twins at any base vertex here have four common neighbors. Other inspected results on clique-fiber Čech nerves [6] and complete multipartite graphs [7] cover different graph families. This is a comparison of hypotheses and deductions, not an assertion that an unsuccessful search proves uniqueness.

## Limitations
The claim is a **finite, computer-assisted exact integral homology classification** of one natural graph. It does not establish homotopy equivalences to wedges of spheres, an equivariant classification, nor any general theorem for arbitrary semisymmetric graphs. The integral matrices and free-face steps are verified by an executable finite certificate; the result is not a statement about an infinite list of cases. The complete barcode is for the **vertex-ball nerve** (equivalently, for the even-scale subfiltration of the graph-geometric Čech nerve) and does not describe the odd-scale graph-geometric Čech stages. An older equivalent table under a different graph presentation remains a bibliographic risk. No independent mathematical audit has been performed.

## References
1. Henry Adams, Samir Shukla and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public 2022-12-12, especially Lemma 2.2 and Theorems 4.1 and 5.13. https://arxiv.org/abs/2212.05871
2. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (2025), especially Theorem 1.2 and Example 3.5. https://arxiv.org/abs/2511.12608
3. *The Rips filtration of the complete-graph subdivision has two consecutive sphere wedges*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-rips-filtration-of-the-complete-graph-subdivision-has-two-co--fb5f0359b702
4. *Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-twin-circle-wedges-in-neighborhood-complexes-of-steiner-design-i--5b757c0a694f
5. *Square-completion decomposition of scale-two graph Čech nerves*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-square-completion-decomposition-of-scale-two-graph-ech-nerves--98a5c720a71e
6. *Clique-fiber Čech nerves over graphs of girth at least five*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-fiber-ech-nerves-over-graphs-of-girth-at-least-five--bcf5b8b96c75
7. *Complete intrinsic graph Čech persistence of multipartite graphs, including their symmetry modules*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-intrinsic-graph-ech-persistence-of-multipartite-graphs--4c8b867ce9c1
