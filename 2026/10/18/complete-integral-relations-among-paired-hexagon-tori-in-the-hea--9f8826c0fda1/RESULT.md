# Complete integral relations among paired-hexagon tori in the Heawood two-point configuration space

## Finding
Let \(H\) be the point–line incidence graph of the seven-point Fano plane, and let \(X=\operatorname{UConf}_2(|H|)\) be the unordered configuration space of two distinct points on its geometric realization. There are exactly \(28\) simple hexagons in \(H\), and exactly \(42\) unordered pairs of vertex-disjoint simple cycles; every such pair consists of two hexagons. Each pair gives an embedded product torus in \(X\). These \(42\) tori form a single orbit under the \(336\)-element automorphism group of \(H\).

Let \(Q\) denote their \(42\)-element index set, and write \(e_{C,D}\) for the standard generator of \(\mathbb Z^Q\) indexed by the unordered disjoint hexagon pair \(\{C,D\}\). Choose orientations and orderings as specified below, and let \(\Phi:\mathbb Z^Q\to H_2(X;\mathbb Z)\) take each generator to the fundamental class of its torus.

For each of the \(28\) hexagons \(C\), exactly three hexagons \(D_1,D_2,D_3\) are disjoint from it. There are signs \(\epsilon_{C,j}\in\{-1,1\}\), uniquely determined up to common negation, for which
\[
 r_C=\epsilon_{C,1}e_{C,D_1}+\epsilon_{C,2}e_{C,D_2}+\epsilon_{C,3}e_{C,D_3}\in\ker\Phi.
\]
Fix these signs by the deterministic rule in `verify.py`. The sum of the \(28\) local relations is coordinatewise even, so
\[
 r_\ast=\frac12\sum_{C}r_C\in\mathbb Z^Q.
\]
**The complete integral relation module** is
\[
 \boxed{\ker\Phi=\langle r_C\ (C\text{ a hexagon}),\ r_\ast\rangle_{\mathbb Z}.}
\]
The local three-term relations are linearly independent and generate a sublattice of index **two** in \(\ker\Phi\). Thus the single global half-sum relation is indispensable: it is not an integer combination of the local relations, while twice it is. In the stated deterministic orientation, \(r_\ast\) has exactly \(22\) nonzero coefficients, consisting of \(11\) positive and \(11\) negative units. The resulting quotient is free abelian:
\[
 \boxed{\mathbb Z^{42}/\langle r_C,r_\ast\rangle\cong H_2(X;\mathbb Z)\cong\mathbb Z^{14}.}
\]
The rank and the existence of an integral basis of fourteen embedded tori are known separately. The additional statement here is the full integral presentation of **all forty-two naturally symmetric generators** and the index-two failure of the local relations to suffice.

## Assumptions and scope
Label the point vertices \(0,1,\ldots,6\) and the line vertices \(7,8,\ldots,13\). Line \(7+i\) is incident with points \(i,i+1,i+3\), with arithmetic modulo \(7\). Orient every graph edge from the smaller to the larger vertex. Every simple cycle is written starting at its smallest vertex and proceeding in the direction whose second vertex is smaller than its last vertex. Enumerate all such cycles by increasing starting vertex and the ordered depth-first traversal defined in `verify.py`; among these, list unordered vertex-disjoint pairs by increasing indices. For each pair, orient the product torus by the first cycle followed by the second. On each two-cell, order the two edge factors by their increasing edge indices and use the corresponding permutation sign.

The result concerns integral second homology of the **unordered collision-free space with two particles**, not ordered configurations, three-particle spaces, or Borel–Moore homology. It is specific to the fourteen-vertex Fano incidence graph. No general theorem for all nonplanar graphs is asserted.

## Proof
**1. Geometric model and exhaustive cycle count.** The graph has \(14\) vertices, \(21\) edges, girth \(6\), and all vertices have degree \(3\). The standard two-particle discretization applies: every simple cycle has at least three edges, and every path between distinct essential vertices has at least one edge. Thus the Abrams cubical model is a deformation retract of \(X\). Its numbers of cells in dimensions \(0,1,2\) are respectively \(91,252,168\); it has no higher-dimensional cells. Canonical simple-cycle enumeration gives cycle counts \(28,21,84,56,24\) in lengths \(6,8,10,12,14\), respectively. Precisely \(42\) unordered pairs of cycles are vertex-disjoint, all with length pair \((6,6)\). Each hexagon belongs to three pairs.

**2. Exact top-cycle lattice.** Let \(B\) be the signed cellular boundary from the free group on the \(168\) squares to the free group on the \(252\) edges. Let \(T\) be the \(168\) by \(42\) matrix whose columns are the product-torus cycles. The code constructs these matrices explicitly from the incidence edges and orientations, and verifies \(BT=0\). Exact Gaussian elimination modulo \(3\) gives \(\operatorname{rank}_{\mathbb F_3}(B)=154\), hence \(\operatorname{rank}_{\mathbb Q}(B)\ge154\). The \(14\) rows numbered \(0,2,3,5,8,16,17,19,23,48,49,54,62,65\) and the \(14\) columns numbered \(0,1,3,4,6,7,9,10,12,13,15,16,18,24\), both zero-indexed, determine a square minor of \(T\) with determinant \(+1\). Therefore \(T\) contains a primitive rank-\(14\) sublattice of the integral \(168\)-dimensional chain group. Since \(BT=0\), the rank of \(B\) is at most \(154\). Equality follows, so \(\ker_{\mathbb Z}B\) has rank \(14\). Because both \(\ker_{\mathbb Z}B\) and the lattice generated by the specified fourteen columns of \(T\) are primitive in the integral chain group and have the same rank, they coincide. In particular \(\Phi\) is onto and \(H_2(X;\mathbb Z)\cong\mathbb Z^{14}\).

**3. The local relation lattice.** Order the \(28\) hexagons by their canonical enumeration. For each one, write its three product-torus columns in the canonical pair order and choose the unique sign vector among \((1,1,-1)\), \((1,-1,-1)\), \((1,1,1)\), and \((1,-1,1)\) that makes their sum zero. Let \(R\) be the resulting \(42\) by \(28\) integral matrix. Direct chain multiplication gives \(TR=0\). Its square submatrix on the zero-indexed row set
\[
 \{0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,19,21,24,25,26,27,28,30,31,33,36\}
\]
has determinant \(-2\). Exact elimination modulo \(2\) gives \(\operatorname{rank}_{\mathbb F_2}(R)=27\). Hence \(R\) has rational rank \(28\), every maximal minor of \(R\) is even, and the gcd of the maximal minors is exactly \(2\). Its column lattice therefore has index two in its saturation. The relation module \(\ker_{\mathbb Z}T\) is saturated as the kernel of a homomorphism between free abelian groups. Because both lattices have rank \(42-14=28\), this saturation equals \(\ker_{\mathbb Z}T\).

**4. The necessary global relation.** Every pair of hexagons belongs to exactly two of the local relations, each with coefficient \(+1\) or \(-1\); hence their sum is coordinatewise even and \(r_\ast\) is integral. Because \(R\) has independent columns, \(r_\ast\) has unique rational coordinates \((1/2,\ldots,1/2)\) relative to those columns, and thus cannot be in their integral span. But its double lies in that span. By the index-two calculation it fills precisely the missing coset and produces the full relation lattice. The indicated chain-level orientation shows its \(22\)-term support.

**5. Symmetry.** The \(168\) permutations of the seven points that preserve the Fano line triples induce incidence-preserving permutations of all fourteen graph vertices. Together with the point–line duality sending point \(i\) to line \(7-i\) and line \(7+j\) to point \(-j\), indices modulo \(7\), they give \(336\) graph automorphisms. The graph is connected and bipartite with the seven points and seven lines as its unique bipartition up to interchange; every automorphism preserving the parts is determined by its point permutation, which must preserve the Fano lines. Thus these \(336\) permutations are the full automorphism group. Their induced action on the \(42\) unordered disjoint-hexagon pairs has one orbit. The verified generators and relations are accordingly a complete, symmetry-natural description of the integral torus presentation; orientation signs are part of the chain convention.

## Verification
The complete deterministic reconstruction is provided by `verify.py` and pinned Python dependencies in `requirements.txt`. Run `python3 verify.py` after installing those dependencies. The script recomputes the Fano incidence graph and all simple cycles, builds the oriented cubical boundary and all forty-two product-torus cycles, checks the signed relations, verifies both displayed integer determinants and the modular ranks, checks the half-sum, and enumerates the full \(336\)-element automorphism group. All determinant computations use exact integer arithmetic. No external saved matrices or graph tables are required.

## Relationship to prior work
Farley and Sabalka's discrete graph-configuration framework supplies the topological setting; the cellular discretization follows Abrams's construction. Barnett–Farber and Farber–Hanbury study the ordered two-particle configuration space and its intersection forms; these results do not state the present integral relations among all unordered Fano-incidence product tori. An and Knudsen's planar graph-braid homology theorem explicitly identifies relations in degree two as an outstanding mathematical question; its planarity hypothesis does not cover the nonplanar Heawood graph. The classical combinatorial Coxeter graph has \(28\) vertices corresponding to the Heawood hexagons and \(42\) edges corresponding to disjoint pairs, but this graph data alone does not determine the topological integral relation lattice.

The prior rank-\(14\) homology and existence of a fourteen-torus basis are not novelty claims. Neither those facts nor the Coxeter graph census imply the complete integral kernel presentation above: the distinguishing feature is the index-two difference between locally generated relations and the full saturated relation lattice.

## Limitations
The result is a complete finite calculation for one canonical nonplanar graph, not a universal presentation for arbitrary graphs. The literature comparisons cannot exclude every unindexed equivalent result. The searchable full text of Barnett’s 2010 Durham thesis was inspected in its general construction chapters and in the chapter on complete and complete-bipartite graphs; it contains related intersection-form and relation arguments for different graphs, but no identified calculation of the Fano incidence graph or its forty-two torus syzygies. The repository PDF images were not independently rendered, and unindexed equivalent treatments elsewhere remain a bibliographic risk.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first posted 25 October 2004); *Algebraic & Geometric Topology* 5 (2005), 1075–1109. https://arxiv.org/abs/math/0410539
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (12 March 2009); *Algebraic & Geometric Topology* 9 (2009), 593–624. https://doi.org/10.2140/agt.2009.9.593
3. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (13 May 2010); *Algebraic & Geometric Topology* 10 (2010), 2203–2227. https://arxiv.org/abs/1005.2300
4. K. Barnett, *The Configuration Space of Two Particles Moving on a Graph*, Durham University thesis (2010), full-text thesis. https://etheses.durham.ac.uk/293/
5. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (2020), especially Section 1.1 and Section 3. https://arxiv.org/abs/2008.10371
