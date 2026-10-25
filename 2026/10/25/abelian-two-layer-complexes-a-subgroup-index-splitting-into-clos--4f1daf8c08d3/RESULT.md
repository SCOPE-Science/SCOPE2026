# Abelian two-layer complexes: a subgroup-index splitting into closed surfaces and circles

## Finding
Let \(A\) be a finite abelian group of order \(q\), let \(d\in A\setminus\{0\}\), and put \(h=\operatorname{ord}(d)\) and \(g=[A:\langle d\rangle]=q/h\). Assume \(g\ge2\). Form a two-dimensional colorful simplicial complex \(K(A,d)\) on three disjoint labeled copies of \(A\): its maximal faces are the triples \(\{(0,a),(1,b),(2,c)\}\) for which \(a+b+c\in\{0,d\}\). Then the complete homotopy type is
\[
 |K(A,d)|\simeq
 \left(\bigvee^{g^2}\Sigma_{(h-1)(h-2)/2}\right)
 \vee \bigvee^{(g-1)(3q-g-1)}S^1,
\]
where \(\Sigma_j\) is the closed, connected, orientable genus-\(j\) surface, including \(\Sigma_0=S^2\). In particular,
\[
 \widetilde H_2(K(A,d);\mathbb Z)\cong\mathbb Z^{g^2},\qquad
 \widetilde H_1(K(A,d);\mathbb Z)\cong\mathbb Z^{q^2-3q+1+g^2},
\]
with all other reduced integral homology zero. Every vertex link has exactly \(g\) connected components, each a cycle of length \(2h\). Hence for \(g>1\) this is a connected pure two-dimensional complex whose edges each belong to two triangles, but whose vertex links are disconnected and whose facets are not strongly connected through edges.

For \(A=\mathbb Z/6\mathbb Z\), the three nonzero gap classes give an illustrative same-face-vector contrast: a generating gap has a closed genus-ten surface, gap \(d=2\) yields four tori wedged with fifteen circles, and gap \(d=3\) yields nine two-spheres wedged with twenty-eight circles. All three have face vector \((18,108,72)\). The generating-gap genus-ten description is recalled only for comparison; the theorem above concerns nongenerating gaps.

## Assumptions and scope
The group is finite and abelian; its operation is written additively. The order \(h\ge2\) of a nonzero element divides \(q\). The index \(g\ge2\) is the distinct, nongenerating-gap regime. Faces are the subsets of the declared colorful triples, including the empty face. In particular every edge joining distinct colors is present and no same-color edge occurs. All surfaces in the homotopy decomposition are orientable, and the circles are homotopy wedge summands, not embedded disjoint topological components.

## Proof
**1. Every colorful edge has two incident triangles.** Fixing the entries in any two colors uniquely determines the third entry for sum \(0\), and uniquely determines it for sum \(d\). These are distinct because \(d\ne0\). Hence there are \(3q\) vertices, \(3q^2\) edges, and \(2q^2\) triangular faces; each edge is in exactly one face of each sum level. Each pair of different colors spans a complete bipartite subgraph, so the complex is connected.

**2. Partition triangles into \(g^2\) surface pieces.** Write \(H=\langle d\rangle\) and let \(Q=A/H\). Each allowed triangle satisfies \(\bar a+\bar b+\bar c=0\) in \(Q\). For \((u,v)\in Q^2\), let \(P_{u,v}\) contain exactly the triangles with \(\bar a=u\), \(\bar b=v\), and therefore \(\bar c=-u-v\), together with their faces. There are \(g^2\) such subcomplexes, each of which has exactly \(h\) vertices of each color, \(3h^2\) edges and \(2h^2\) triangles. Every full-complex edge belongs to exactly one piece, because any two colored vertex cosets force the third. Thus different pieces meet only in vertices. Each piece is connected, since its three color classes span complete bipartite edge sets within the piece.

Choose representatives \(a_0\), \(b_0\) of the two fixed cosets and put \(c_0=-a_0-b_0\). Every vertex of the piece is uniquely \(a_0+id\), \(b_0+jd\), or \(c_0+kd\), where \(i,j,k\in\mathbb Z/h\mathbb Z\). The triangular condition becomes \(i+j+k\in\{0,1\}\pmod h\). Thus all pieces are isomorphic to the same two-level cyclic Latin complex \(K(\mathbb Z/h\mathbb Z,1)\).

**3. Each piece is a closed orientable surface.** At a vertex, the incident triangles alternate between sum levels \(0\) and \(1\). Its link is a connected \(2h\)-cycle: proceeding through two consecutive incident triangles translates the free neighboring coordinate by \(1\) modulo \(h\), and this generates the whole neighboring color class. Links at every vertex are therefore circles. Every edge is in exactly two triangles, so this connected two-complex is a closed triangulated surface. Orient sum-zero triangles in color order \((0,1,2)\) and sum-one triangles in the opposite order. Since any edge has one incident triangle of each level, their induced edge orientations cancel; hence the surface is orientable. Its Euler characteristic is \(3h-3h^2+2h^2=3h-h^2\). The orientable surface classification therefore gives genus \(\gamma=(h-1)(h-2)/2\).

**4. Compute the homotopy type of the vertex gluing.** Let \(\mathcal B\) be the bipartite incidence graph with one node for each surface piece, one node for each original colored vertex, and an edge whenever that surface contains that vertex. Each surface contributes \(3h\) incidence edges, so \(\mathcal B\) has \(g^2+3q\) vertices and \(3g^2h=3gq\) edges. It is connected: otherwise the original complex, obtained by gluing the connected pieces along precisely these vertices, would be disconnected, contrary to Step 1. Its graph cycle rank is
\[
 \beta_1(\mathcal B)=3gq-g^2-3q+1=(g-1)(3q-g-1).
\]
Replace each original common vertex by a contractible star joining a distinct copy of that vertex in every incident surface. Collapsing the stars recovers \(|K(A,d)|\), so this graph of spaces is homotopy equivalent to the original complex. The attaching maps are from discrete point sets into connected surfaces. Homotoping each attaching point within its surface to one chosen basepoint does not change the homotopy type of the graph of spaces (use mapping cylinders for the attachment maps). After this replacement, each surface is attached at one point to the graph \(\mathcal B\). Contracting a spanning tree of \(\mathcal B\) gives the asserted wedge of the \(g^2\) surfaces with \(\beta_1(\mathcal B)\) circles. The first homology is therefore free of rank \(2g^2\gamma+\beta_1(\mathcal B)=q^2-3q+1+g^2\); the second is free of rank \(g^2\), and there is no higher homology.

**5. Singular links in the full complex.** At a vertex, the neighboring vertices split according to their image in \(Q=A/H\); the two triangular levels link within a fixed pair of complementary cosets, never between distinct cosets. Each coset contributes the \(2h\)-cycle of Step 3, and there are exactly \(g\) cosets. This proves the local-link assertion and shows precisely why the nongenerating regime is not a manifold.

## Verification
The self-contained `verify.py` independently reconstructs every colored face, partitions triangles by quotient cosets, verifies full and piecewise edge-incidence multiplicities, checks the surface-piece vertex links and incidence-graph connectivity, and computes boundary ranks over two finite fields. The source-code run tested 42 nongenerating elements across cyclic groups of orders \(4,5,6,8,9,10,12\) and products \(C_2\times C_2\), \(C_2\times C_3\), \(C_2\times C_4\), \(C_3\times C_3\), also checking generating cases where present. For group orders through ten it independently computed homology over \(\mathbb F_2\) and \(\mathbb F_{1009}\). The computed case \((A,d)=(\mathbb Z/6,3)\) has \((\beta_1,\beta_2)=(28,9)\). Finite tests do not prove the all-group theorem; Steps 1–5 do.

## Relationship to prior work
Ayzenberg and Khoroshavkina, arXiv:2602.08694v1, prove homotopy-wedge decompositions for globally flabby generalized inflations. The nonflabby two-level selection here is not covered by their global hypothesis. An earlier publicly indexed calculation, *Two adjacent affine layers force integral homology in two neighboring degrees* (2026), computes integral homology for \(n\) coordinates over \(\mathbb Z/q\mathbb Z\) with the two **adjacent** permitted sum levels \(0,1\). At \(n=3\), that result has only one top integral class. It explicitly leaves nongenerating differences untreated and does not determine their homotopy types. The new feature here is the quotient-subgroup-index decomposition when \(\langle d\rangle\) is proper, producing \(g^2>1\) top homology classes, singular vertex links, nontrivial higher-genus surface wedge factors, and exact extra-circle rank. Classical Latin-bitrade surface theory provides related background but is not invoked as an implication of the claimed decomposition.

## Limitations
The theorem assumes finite abelian groups, two distinct sum levels, exactly three colors and a nongenerating difference \(g\ge2\). It gives an unpointed homotopy decomposition and integral homology, not a canonical equivariant splitting, embedding classification of singularities, or a theorem for nonabelian groups, more than two levels, or higher numbers of colors. It does not claim novelty for the generating-gap surface. Relevant indexed primary results were compared, but equivalent unindexed Latin-trade or singular-surface descriptions remain a residual originality risk. Independent scientific validation has not been performed.

## References
1. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (first posted 2026-02-09), https://arxiv.org/abs/2602.08694; Theorem 1.2, Sections 4–7.
2. *Two adjacent affine layers force integral homology in two neighboring degrees*, publicly indexed research record dated 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-adjacent-affine-layers-force-integral-homology-in-two-neighb--b693290149ba (exact adjacent-level scope and stated nongenerating-gap limitation).
3. V. de Silva et al., *Dowker's theorem for higher-order relations*, arXiv:2506.10909 (2025), https://arxiv.org/abs/2506.10909; general context for ternary relations, not an asserted source of this homotopy formula.
4. N. J. Cavenagh and I. M. Wanless, *Latin trades in groups defined on planar triangulations*, arXiv:0807.2707 (2008); background on links between Latin trades, group labels and surfaces.
