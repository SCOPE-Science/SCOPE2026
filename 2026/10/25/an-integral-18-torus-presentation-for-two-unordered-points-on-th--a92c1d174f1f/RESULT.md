# An integral 18-torus presentation for two unordered points on the four-by-four complete bipartite graph

## Finding
Let \(G=K_{4,4}\) be the complete bipartite graph and \(X=\operatorname{UConf}_2(|G|)\) its unordered configuration space of two distinct points. The eighteen unordered pairs of vertex-disjoint four-cycles in \(G\) define embedded product tori. Their integral fundamental classes generate \(H_2(X;\mathbb Z)\cong\mathbb Z^{12}\). Twelve explicitly specified tori form an integral basis; the six displayed relations below are a \(\mathbb Z\)-basis for *all* relations among the eighteen geometric generators. In particular, no additional non-toric integral generator is required for this graph.

## Assumptions and scope
The graph is the ordinary simple \(K_{4,4}\), with left vertices \(r_0,r_1,r_2,r_3\), right vertices \(c_0,c_1,c_2,c_3\), and all sixteen edges \(e_{ij}=r_ic_j\). Particles are *unordered* and cannot coincide anywhere. Homology is singular homology with integral coefficients. A disjoint pair of four-cycles means cycles with disjoint vertex sets, and its torus means the subspace consisting of one point on each cycle. No assertion about graphs other than this fixed \(K_{4,4}\) is included.

Each edge \(e_{ij}\) is oriented from \(r_i\) to \(c_j\), with index \(4i+j\). For a row pair \(a=\{0,k\}\), where \(k\in\{1,2,3\}\), and an arbitrary column pair \(b\subset\{0,1,2,3\}\) with \(|b|=2\), let \(t_{a,b}\) be the product torus class of the two complementary \(K_{2,2}\) four-cycles. For each four-cycle, its oriented one-cycle has coefficients \((+1,-1,-1,+1)\) on its four edges in row-major order; the two-cycle is their exterior product. There are \(3\cdot6=18\) such classes.

To list them, denote these tori by \(t_0,\ldots,t_{17}\): first order the row pairs as \((01),(02),(03)\), and within each group order the column pairs as \((01),(02),(03),(12),(13),(23)\).

## Proof
**Cellular model.** The standard equivariant deformation retract from the ordered deleted product of a graph onto its discretized cells descends under the particle swap to \(X\). The unordered cubical complex has \(28\) zero-cells (pairs of distinct vertices), \(96\) one-cells (one vertex and a nonincident edge), and \(72\) two-cells (unordered pairs of edges with disjoint endpoints). There are no higher cells. If \(e_i=[u,v]\), \(e_j=[w,z]\), and \(i<j\), its degree-two boundary is
\[
\partial_2[e_i,e_j]=[v,e_j]-[u,e_j]-[z,e_i]+[w,e_i].
\]
Thus \(H_2(X;\mathbb Z)=\ker(\partial_2:\mathbb Z^{72}\to\mathbb Z^{96})\), with no quotient by higher boundaries.

**Cycles and exact rank.** The eighteen product cycles have sixteen nonzero signed square-cell coefficients each. Their cellular boundaries vanish term by term. For the explicit \(96\times72\) boundary matrix, reduction over \(\mathbb F_3\) yields rank \(60\). Therefore \(\operatorname{rank}_{\mathbb Q}\partial_2\ge60\). Twelve product cycles have a coordinate minor of determinant \(-1\): select torus columns (zero-based)
\[
(0,1,2,3,4,6,7,8,9,10,12,13)
\]
and square-cell rows (zero-based lexicographic order of disjoint edge-index pairs)
\[
(13,67,31,34,32,37,9,57,38,29,55,14).
\]
Consequently twelve cycles are independent, forcing \(\operatorname{rank}_{\mathbb Q}\partial_2\le72-12=60\). Hence the integral second homology is free of rank exactly twelve.

**Integral saturation.** The displayed determinant \(-1\) means the twelve chosen torus columns generate a primitive rank-twelve sublattice of the ambient cellular group \(\mathbb Z^{72}\). Their lattice lies in \(\ker\partial_2\), also of rank twelve. The quotient of these two lattices is finite, but injects into the torsion-free quotient of \(\mathbb Z^{72}\) by the primitive sublattice. It is therefore zero. The twelve tori are an *integral* basis of \(H_2(X;\mathbb Z)\); rational spanning alone would not suffice for this conclusion.

**Complete presentation.** In the indexing above, all six following relations hold as equalities of signed cellular two-chains, not just modulo homology:
\[
\begin{aligned}
R_1:&\quad t_0-t_1+t_2+t_3-t_4+t_5=0,\\
R_2:&\quad t_6-t_7+t_8+t_9-t_{10}+t_{11}=0,\\
R_3:&\quad t_0-t_1+t_2-t_6+t_7-t_8+t_{12}-t_{13}+t_{14}=0,\\
R_4:&\quad t_0-t_1+t_3-t_6+t_7-t_9+t_{12}-t_{13}+t_{15}=0,\\
R_5:&\quad -t_1+t_4+t_7-t_{10}-t_{13}+t_{16}=0,\\
R_6:&\quad -2t_0+t_1-t_2-t_3+t_4+2t_6-t_7+t_8+t_9-t_{10}-t_{12}+t_{17}=0.
\end{aligned}
\]
Their coefficients at the omitted generator indices \((5,11,14,15,16,17)\) form the identity matrix, and no other omitted indices appear in each corresponding relation. Thus every omitted torus is an integral linear combination of the twelve basis tori. Since the full relation module has rank \(18-12=6\), these six independent relations generate it integrally: any additional relation may first be reduced to one on the twelve basis vectors, which is necessarily zero.

## Verification
Run `python3 verify.py` using Python 3.9 or later, with no third-party libraries. The program independently builds all 72 oriented square cells, the degree-two boundary, and the eighteen signed product tori; verifies every boundary and each of the six integral relations; computes the boundary rank over both \(\mathbb F_3\) and \(\mathbb F_5\); and evaluates the explicit determinant using integer fraction-free elimination. The required terminal marker is `VERIFY_OK_K44_UNORDERED_INTEGRAL_TORUS_PRESENTATION`. See `verification_output.txt` for the actual check output.

## Relationship to prior work
Barnett–Farber (2009, arXiv:0903.2180v1) prove the ordered deleted-product deformation retract and establish the ordered graph-configuration intersection framework. Farber–Hanbury (2010, arXiv:1005.2300) establish maturity of complete bipartite graphs and derive **ordered** second Betti numbers, not the integral geometric generators of this unordered space. Ramos–Yun (2026, arXiv:2606.13813), Section 3.3 (especially Theorem 3.17, Example 3.18 and Proposition 3.19), provide the closest comparison: rational representations of ordered and unordered configurations for \(K_{n,n}\), and *rational* toric subrepresentations of the **ordered** \(K_{4,4}\) configuration space. Those statements do not establish integral saturation or an explicit complete relation lattice for the eighteen unordered product tori. An–Knudsen (2020, arXiv:2008.10371) concern general generation of second homology for planar graph braid groups, whereas \(K_{4,4}\) is nonplanar.

## Limitations
This result concerns exactly two unordered particles on the fixed unsubdivided graph realization \(|K_{4,4}|\); graph subdivision does not alter the underlying topological space but the displayed finite cell basis uses the chosen graph. The statement does not classify larger complete bipartite graphs or all graph configuration spaces, and does not claim independence of a separate scientific audit. The corresponding results for ordered configurations and for rational toric submodules are explicitly prior work. Bibliographic risk remains from a not fully accessible 2010 dissertation and potentially unindexed equivalent integral presentations. The exact chain calculation establishes the mathematics, not bibliographic uniqueness.

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1 (first submitted 2009-03-12), especially Lemma 1.1 and the cellular deleted-product model. https://arxiv.org/abs/0903.2180
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (2010), especially Proposition 22 and Corollary 24. https://arxiv.org/abs/1005.2300
3. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (2026), Section 3.3, Example 3.18 and Proposition 3.19. https://arxiv.org/abs/2606.13813
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020). https://arxiv.org/abs/2008.10371
