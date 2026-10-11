# Complete Rips barcodes and top-dimensional symmetry of multipartite prisms

## Finding

For \(k\ge2\) and integers \(a_1,\ldots,a_k\ge2\), consider the Cartesian graph prism
\[
P=K_{a_1,\ldots,a_k}\square K_2,
\]
where the first factor is complete multipartite. Set \(N=\sum_{i=1}^k a_i\) and \(B=\prod_{i=1}^k(a_i-1)\). With the shortest-path metric on the \(2N\) graph vertices and the inclusive Vietoris--Rips convention, the homotopy types are
\[
\operatorname{VR}_{\le}(P;r)\simeq
\begin{cases}
\bigsqcup^{2N}\mathrm{pt},&0\le r<1,\\
\bigvee^{N-1}S^1\vee\bigvee^{2B}S^{k-1},&1\le r<2,\\
\bigvee^B S^{2k-1},&2\le r<3,\\
\mathrm{pt},&r\ge3.
\end{cases}
\]
All integral homology groups are free abelian. The complete positive-dimensional persistence barcode over every field comprises \(N-1\) bars of degree one and lifetime \([1,2)\), \(2B\) bars of degree \(k-1\) and lifetime \([1,2)\), and \(B\) bars of degree \(2k-1\) and lifetime \([2,3)\). When \(k=2\), combine the two degree-one multiplicities. In degree zero, the barcode has \(2N-1\) bars \([0,1)\) and one bar \([0,\infty)\).

Furthermore, let the group \(\prod_{i=1}^k S_{a_i}\) act by permuting vertices within each part of both layers. On scale-two integral homology in degree \(2k-1\), its action is naturally
\[
\widetilde H_{2k-1}(\operatorname{VR}_{\le}(P;2);\mathbb Z)
\cong\bigotimes_{i=1}^k A_{a_i},\qquad
A_a=\ker\!\left(\mathbb Z^a\xrightarrow{\sum}\mathbb Z\right).
\]
The automorphism swapping the two layers acts by multiplication by \((-1)^k\) on this module.

## Assumptions and scope

A vertex is a triple \((i,j,h)\) with part index \(1\le i\le k\), position \(1\le j\le a_i\), and layer \(h\in\{0,1\}\). The graph has an edge between distinct vertices in the same layer from different parts, or between corresponding positions in opposite layers. Every graph vertex participates. For \(r\ge0\), an abstract simplex is a finite vertex set with every pair at shortest-path distance at most \(r\). No Euclidean embedding, genericity, equal part sizes, or coefficients restrictions are assumed.

## Proof

**Distance rule.** Any two distinct vertices in the same layer and different parts have distance one. If they lie in one part and the same layer, their distance is two, since \(k\ge2\) supplies a common neighbor in a different part. Two vertices in different parts and opposite layers are at distance two, by one cross-part move and one vertical move. Corresponding opposite-layer vertices have distance one. Noncorresponding opposite-layer vertices within the same part have distance three: cross-layer moves change no position, and every same-part position change needs at least two horizontal edges. A three-edge route exists using any other part. Thus the diameter is exactly three.

**Scale one.** A clique using both layers can contain only one vertical edge: each cross-layer edge is a matching edge, so any third vertex is not adjacent to at least one endpoint. Hence the clique complex is two copies of \(D_{a_1}*\cdots*D_{a_k}\) linked by \(N\) isolated matching edges. Here \(D_a\) is the discrete complex on \(a\) vertices. Since \(D_a\simeq\bigvee^{a-1}S^0\), iterating the join formula gives \(D_{a_1}*\cdots*D_{a_k}\simeq\bigvee^B S^{k-1}\). Both copies are path connected. Joining two connected spaces by \(N\) edges with pairwise distinct endpoints gives their homotopy wedge plus \(N-1\) additional circles (choose one bridge in a spanning tree and use paths in each connected component to close the other bridges). This proves the scale-one expression for all \(k\ge2\).

**Scale two.** The distance rule shows that vertices in different parts are always adjacent in the scale-two graph. Within one part of size \(a\), all pairs in each of its layers are adjacent; across its layers only corresponding vertices are adjacent. Therefore the scale-two clique complex is *exactly* the abstract simplicial join
\[
\operatorname{VR}_{\le}(P;2)=\operatorname{Cl}(Q_{a_1})*\cdots*\operatorname{Cl}(Q_{a_k}),\qquad Q_a=K_a\square K_2.
\]
Each \(\operatorname{Cl}(Q_a)\) consists of two disjoint full simplices and the \(a\) vertical matching edges between them, with no other mixed-layer simplices. Contracting the two disjoint simplices to two points gives a graph with \(a\) parallel edges, a homotopy equivalence of finite CW complexes because the contracted subcomplexes are contractible. Thus \(\operatorname{Cl}(Q_a)\simeq\bigvee^{a-1}S^1\). The join of \(k\) such complexes has the claimed type \(\bigvee^B S^{2k-1}\). At scale three every pair is adjacent, so the result is a full simplex.

**Persistence.** The only nonzero positive-dimensional reduced homology at scale two has degree \(2k-1\). Its degree is distinct from both \(1\) and \(k-1\) for every \(k\ge2\). Thus the maps from scales one to two in all positive degrees are zero, independently of coefficients. All classes at scale two die at scale three. The zero-dimensional intervals follow from the graph being connected at scale one. This determines every interval and its endpoints, with no unproved persistence-map assumption.

**Integral action.** The two contracted simplices of \(\operatorname{Cl}(Q_a)\) have a connecting family of \(a\) matching edges. Orient these from layer zero to layer one; a cycle is described by integer matching-edge coefficients summing to zero. This identifies \(H_1(\operatorname{Cl}(Q_a);\mathbb Z)\) with the augmentation lattice \(A_a\), equivariantly for permutations of matching-edge labels. Under interchange of the two layers, every oriented matching edge reverses, so the action on this \(H_1\) is \(-1\). By the integral Künneth formula for joins, with no torsion, scale-two top homology is the tensor product of these \(k\) lattices. The layer swap acts as the product of \(k\) negatives, namely \((-1)^k\). All identifications are integral.

## Verification

The accompanying `verify.py` requires only Python 3's standard library. It builds each graph from its edge definition, uses independent breadth-first searches to calculate all metric distances, checks the scale-two join adjacency, and exhaustively computes simplices and mod-two boundary ranks for six small multipartite sizes at both relevant scales. It also checks metric formulas in six larger examples, with up to five partite classes. Run `python3 verify.py` and require its final output to be `VERIFY_OK`. These finite checks are corroboration; the preceding distance and join arguments, rather than extrapolation, prove the all-parameter statement and integral equivariance.

## Relationship to prior work

Adamaszek's *Clique complexes and graph powers* develops clique complexes of graph powers, including graph-metric Vietoris--Rips complexes and structural results for high-girth graphs and cycles. The present multipartite prisms contain short cycles, and the reviewed graph-power theorems do not give this complete multipartite factorization or its persistence maps. Adamaszek and Adams' *The Vietoris--Rips complexes of a circle* classifies cyclic metric complexes; its circle statements do not imply results for two-layer complete multipartite graph metrics. Work on toroidal grid Rips filtrations concerns Cartesian products of cycles rather than complete multipartite prisms.

The boundary example \(K_{2,2}\square K_2=C_4\square K_2\), the cube, has been treated separately in the literature. The present claim does not assert novelty for that single small case; it supplies a uniform all-part-size, all-number-of-parts barcode and a natural integral top-homology representation. The parameter-uniform barcode and symmetry statement is the subject of the present result.

## Limitations

This theorem concerns the finite *vertex* metric of the Cartesian graph prism and inclusive integer thresholds, not a continuous metric realization or geometric Euclidean point configuration. It assumes \(k\ge2\) and every part size at least two. It does not classify arbitrary graph products or extend the result to weighted edges. The code's mod-two computations alone cannot prove torsion-freeness or an infinite-family result; those statements follow from the structural proof.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, Israel Journal of Mathematics 196 (2013), 295--319; preprint arXiv:1104.0433, https://arxiv.org/abs/1104.0433.
2. M. Adamaszek and H. Adams, *The Vietoris--Rips complexes of a circle*, Pacific Journal of Mathematics 290 (2017), 1--40; first public preprint arXiv:1503.03669v1 (2015-03-12), https://arxiv.org/abs/1503.03669.
3. Work on graph-metric Rips complexes of toroidal grids: arXiv:2502.07134, https://arxiv.org/abs/2502.07134 (comparison of different Cartesian factors).
