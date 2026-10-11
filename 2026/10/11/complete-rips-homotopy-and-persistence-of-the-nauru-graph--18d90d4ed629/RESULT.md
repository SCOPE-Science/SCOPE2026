# Complete Rips homotopy and persistence of the Nauru graph

## Finding
Let \(G=GP(12,5)\) be the 24-vertex Nauru graph, with its unit-edge shortest-path metric. Write \(K_r=\operatorname{VR}_{\leq}(V(G);r)\) for the simplicial complex of nonempty finite sets of pairwise distance at most \(r\). For every real \(r\geq0\),
\[
K_r\simeq
\begin{cases}
\bigsqcup^{24}\mathrm{pt},&0\leq r<1,\\
\bigvee^{13}S^1,&1\leq r<2,\\
T^2\vee\bigvee^{12}S^2,&2\leq r<3,\\
\bigvee^{4}S^3\vee\bigvee^{4}S^4\vee S^5,&3\leq r<4,\\
\mathrm{pt},&r\geq4,
\end{cases}
\]
where \(T^2=S^1\times S^1\). In fact \(K_3\) is simplicially the join of two twelve-vertex triangulated tori, and \(K_2\) has a relative elementary-collapse certificate proving the displayed torus-plus-spheres type.

Over **every field**, the complete positive-dimensional persistent homology barcode consists of eleven degree-one intervals \([1,2)\), two degree-one intervals \([1,3)\), thirteen degree-two intervals \([2,3)\), four degree-three intervals \([3,4)\), four degree-four intervals \([3,4)\), and one degree-five interval \([3,4)\). In degree zero there are 23 intervals \([0,1)\) and one \([0,\infty)\). All homology groups occurring at the integer scales are torsion-free.

## Assumptions and scope
Take vertices \(0,\ldots,11\) for the outer ring and \(12,\ldots,23\) for the inner ring, interpreting ring indices modulo 12. The undirected edges are \(\{i,i+1\}\), \(\{i,12+i\}\), and \(\{12+i,12+(i+5)\}\) for each \(i\in\{0,\ldots,11\}\). The graph is connected, cubic, bipartite, of diameter four. Its bipartition is
\[
A=\{1,3,5,7,9,11,12,14,16,18,20,22\},\qquad B=V(G)\setminus A.
\]
The Vietoris–Rips convention is *inclusive* distance \(\leq r\), so the four changes happen at the integers \(1,2,3,4\). The claim concerns this graph and its graph metric, not the Euclidean distances of a chosen graph embedding or the circle metric.

## Proof
**Step 1: graph distances and the first two thresholds.** Breadth-first distances from each vertex are certified by `verify.py`; every vertex has one vertex at distance zero, 3 at one, 6 at two, 9 at three, and 5 at four. Below radius one there are 24 isolated vertices. At radius one the complex is the original graph: its 24 vertices and 36 edges give a connected one-dimensional complex with cycle rank \(36-24+1=13\). At radius four every pair is joined, so the full simplex is contractible.

**Step 2: the two core tori.** Write \(K=K_2\), and let \(K[A]\) and \(K[B]\) be full induced subcomplexes. Each is two-dimensional with exactly 12 vertices, 36 edges, and 24 triangles. Every edge belongs to precisely two triangles; every vertex link is a connected six-cycle; and both underlying complexes are connected. A consistent orientation of all 24 triangles exists in each. Thus each is a connected closed orientable combinatorial surface of Euler characteristic \(12-36+24=0\), so both are triangulated \(T^2\). These are finite, directly reproducible incidence and orientation claims, not assumptions about a drawing of the graph.

**Step 3: an explicit relative collapse and its attaching maps.** The whole scale-two complex has face vector \((24,108,120,24)\), and no higher-dimensional faces. The accompanying `collapse_certificate.json` lists 108 ordered reductions relative to \(K[A]\): 24 elementary triangle–tetrahedron free-face pairs, 60 edge–triangle pairs, 12 vertex–edge pairs, and 12 deletions of maximal *critical* two-simplices. The precise chronological order is the `steps` array; `verify.py` checks each pair is an actual free-face collapse in the *currently remaining* complex and that only \(K[A]\) survives. Reversing these reductions constructs \(K\) up to homotopy from the torus by attaching exactly twelve two-cells. The 12 critical boundaries have explicit integer two-chain fillings, recorded as coefficient arrays on the sorted 24 oriented triangles of \(K[A]\). The verifier projects each critical attaching one-cycle through all subsequent elementary collapses and checks its complete signed boundary equals the boundary of the recorded two-chain. No computer-observed Betti number is used as a substitute for this attaching-map check.

The one-dimensional fundamental group of the target torus is \(\pi_1(T^2)=\mathbb Z^2\). On a torus, a closed attaching loop is nullhomotopic if and only if its integral homology class vanishes. Each of the twelve projected attaching loops is a boundary in \(K[A]\), hence is nullhomotopic. Attaching a two-cell along a nullhomotopic map contributes a wedge summand \(S^2\). The relative collapse and all twelve fillings therefore prove
\[
K_2\simeq T^2\vee\bigvee^{12}S^2.
\]
In particular the first homology is \(\mathbb Z^2\), the second is \(\mathbb Z^{13}\), and all other reduced homology vanishes.

**Step 4: the join at radius three.** Every pair of vertices from opposite bipartition classes is at odd distance, either one or three. Every pair within a bipartition class has even distance, either two or four. Consequently, at radius three **all cross-part edges** are present, while the induced complex within either part is still exactly the radius-two torus triangulation. The flag-complex definition then gives the simplicial identity
\[
K_3=K[A]*K[B]\cong T^2*T^2.
\]
The join is the suspension of the smash product, \(T^2*T^2\simeq\Sigma(T^2\wedge T^2)\). The standard natural suspension splitting of products of circles (applied to the four circle factors, retaining terms meeting each of the two torus factors) yields four \(S^3\) summands, four \(S^4\) summands, and one \(S^5\) summand. This proves the stated radius-three homotopy type; the verifier independently checks the corresponding exact mod-two Betti numbers \((1,0,0,4,4,1)\).

**Step 5: persistence.** Every radius-two edge spans an original length-two graph path. The triangle consisting of the new edge and that path shows the map \(H_1(K_1;F)\to H_1(K_2;F)\) is surjective for any field \(F\). Its domain has dimension 13 and codomain dimension two, so exactly two degree-one classes persist through scale two. At scale three both \(H_1\) and \(H_2\) vanish, and all positive-dimensional homology vanishes again at scale four. The claimed intervals follow from these ranks and the interval decomposition of a finite persistence module. The integral wedge and join decompositions also establish torsion-freeness.

## Verification
Run `python3 verify.py` with `collapse_certificate.json` beside it using the Python standard library (no packages or network needed). Successful execution prints exactly `VERIFY_OK vertices=24 radius2_faces=276 relative_pairs=96 critical_2cells=12 radius3_faces=5328`. The checker recomputes all 24 graph distance rows, enumerates the 276 nonempty radius-two simplices, verifies both triangulated tori including orientability and all vertex links, checks every listed free-face collapse and critical face, verifies all 12 *signed integral* two-chain boundaries, and checks the radius-three join and mod-two homology by exact boundary rank elimination. The finite certificate is exhaustive for this precisely specified 24-vertex complex; the standard topological implications in Steps 2–5 are separate mathematical arguments.

## Relationship to prior work
Eppstein described the Nauru graph, its generalized Petersen and star-transposition models, and a toroidal hexagon embedding in 2007. This previously known toroidal embedding is acknowledged, not claimed as new. Kawamura (2011), Theorems 2.2 and 3.3, gives general graph-square relations for bipartite graphs and low-degree topology; the results do not provide the full graph-specific twelve two-sphere attachments or complete higher-scale join. Adamaszek (2011) studies powers of graphs and includes high-girth collapse conditions and classifications of cycle powers, not this girth-six cubic graph. Adamaszek–Adams (arXiv:1503.03669, first public 2015-03-12) classifies circle-metric Rips complexes, not the Nauru graph metric; its published version lists 55U10 as primary MSC. The present result is a distinct explicit graph-metric computation with an integral attaching-map certificate, not a restatement of the graph's known torus embedding.

## Limitations
No general classification for all generalized Petersen graphs, star-transposition graphs, or other graph metrics follows from this one example. The homotopy splitting uses the certified finite combinatorics and standard facts about orientable surfaces and suspensions. Computational checks alone would establish only finite combinatorics, not a statement about an unbounded family. Published and indexed literature comparisons do not exclude an equivalent result in unindexed work; originality has not been independently audited. This analysis establishes ordinary persistent homology, not enhanced multiplicative or equivariant persistent invariants.

## References
1. D. Eppstein, *The many faces of the Nauru graph* (2007-12-12), https://11011110.github.io/blog/2007/12/12/many-faces-of.html .
2. K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs* (2011), https://cdm.ucalgary.ca/article/download/62059/46707/177343 .
3. M. Adamaszek, *Clique complexes and graph powers* (2011), arXiv:1104.0433, https://arxiv.org/abs/1104.0433 .
4. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first public 2015-03-12); *Pacific Journal of Mathematics* 290 (2017), 1–40, https://arxiv.org/abs/1503.03669 .
