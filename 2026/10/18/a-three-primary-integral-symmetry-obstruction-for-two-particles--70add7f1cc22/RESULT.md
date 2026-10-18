# A three-primary integral symmetry obstruction for two particles on the cube graph

## Finding
Let \(Q_3\) be the graph on the eight binary triples with edges between triples differing in exactly one coordinate. Write \(X=\operatorname{UConf}_2(|Q_3|)\) for unordered configurations of two distinct points in its geometric realization, and let \(G=\operatorname{Aut}(Q_3)=(C_2)^3\rtimes S_3\), of order \(48\). For the canonical total-motion map \(p\), there is an exact sequence of **integral** \(G\)-modules
\[
0\longrightarrow\mathbb Z_{\det}\longrightarrow H_1(X;\mathbb Z)\xrightarrow{p}H_1(Q_3;\mathbb Z)\longrightarrow0.
\]
Here \(\det(g)\) is the sign of the signed coordinate permutation representing \(g\), and the left-hand generator is a particle-exchange loop around a trivalent junction. **This extension does not split over the integers, although it has a unique rational equivariant section.** Its class has exact order three: it splits over \(\mathbb Z[1/3]\) and does not split over \(\mathbb Z\).

The integral homology is \(H_0(X;\mathbb Z)=\mathbb Z\), \(H_1(X;\mathbb Z)=\mathbb Z^6\), \(H_2(X;\mathbb Z)=\mathbb Z^3\), and \(H_i(X;\mathbb Z)=0\) for \(i\ge3\). The three opposite-face product tori form an integral basis for \(H_2\), on which a cube symmetry \(g=(t,\pi)\) takes basis vector \(e_k\) to \((-1)^{t_{\pi(k)}}e_{\pi(k)}\), where \(t\in(C_2)^3\) is the translation and \(\pi\in S_3\) permutes coordinates. Central antipodal inversion has rank-three plus and minus eigensublattices on \(H_1\), with their sum of index four.

## Assumptions and scope
All homology is ordinary singular homology with indicated coefficients. The graph has twelve edges, eight trivalent vertices and six square faces. The standard unordered deleted-product cubical model has cells of type unordered distinct vertices, edge plus nonincident vertex, and unordered disjoint edges. For two particles on this simple graph, the sufficient-subdivision condition is satisfied (one edge between essential vertices and at least three edges around a circuit), so the model is a homotopy model for the genuine configuration space. Edges \((a,b)\) have the increasing-numerical orientation. In the oriented square \((e_i,e_j)\), order edges by their enumeration, assigning the product orientation. All group actions are induced by actual graph automorphisms, not arbitrary homotopy equivalences.

The total-motion map \(p\) sends an edge-plus-vertex cell to the oriented graph edge traversed by its moving particle, and a vertex-pair cell to zero. This is a chain map to the one-dimensional cellular graph complex, inducing \(p\) on \(H_1\). Both particles contribute positively, so the construction is well-defined for unlabeled configurations and natural under graph automorphisms.

## Proof
**Integral homology and the exact sequence.** The cell counts are \((c_0,c_1,c_2)=(28,72,42)\). An exact spanning-tree reduction of the connected \(1\)-skeleton identifies its integral cycle group with \(\mathbb Z^{45}\). The six explicit cycle generators \(B_1,\ldots,B_5,L\) are as follows: for each \(B_i\), keep one particle at the indicated vertex while the other traverses a closed cube walk; these pairs (walk; station) are

- \((2,0,1,3,2);4\), \((4,0,1,5,4);2\), \((4,0,2,6,4);1\), \((5,1,3,7,5);0\), and \((6,2,0,1,3,7,6);4\).

The exchange \(L\) traverses unordered vertex pairs \((1,2),(0,2),(4,2),(4,0),(4,1),(0,1),(2,1)\). In the integral \(45\)-coordinate cycle lattice, the \(39\) specified boundary columns together with the six named cycles form a \(45\)-square matrix of determinant \(-1\). The columns and row coordinates are deterministically reconstructed by `verify.py` from the transparent `projection.json` certificate; the program verifies this determinant and checks the projection annihilates **every** of the \(42\) square boundaries, not merely the \(39\) selected ones. Accordingly the image of the second boundary is primitive of rank \(39\), giving torsion-free \(H_1\) of rank \(6\) with this precise integral basis. The five fundamental graph cycle coordinates are the negatives of the first five corresponding \(B_i\)-coordinates, while \(p(L)=0\); hence \(p\) is surjective and its kernel is exactly \(\mathbb Z L\).

**Naturality and nonsplitting.** A cube automorphism is the map \(g(x)=\pi(x)\oplus t\) on bit triples. Its cellular action on all \(72\) oriented one-cells gives a \(6\)-square integral matrix \(M_g\) in the basis above. The verifier reconstructs these matrices without floating-point arithmetic, and checks the composition law for all \(48^2\) ordered pairs. They have block form
\[
M_g=\begin{pmatrix}A_g&0\\ b_g&\delta_g\end{pmatrix},\qquad\delta_g=\operatorname{sgn}(\pi)(-1)^{|t|}.
\]
Thus \(L\) has the determinant character \(\delta\). A section of the quotient, necessarily of the form \(v\mapsto(v,uv)\) for a row \(u\) of five coefficients, is equivariant precisely when
\[
 uA_g-\delta_g u=b_g.
\]
For the three generating automorphisms (flip the first bit, swap coordinates zero and one, and cycle the three coordinates), the fifteen equations have the **unique** rational solution
\[
\boxed{u=\tfrac13(-1,1,-1,1,-2).}
\]
The code supplies the full generator matrices and exactly solves the fifteen linear equations using rational arithmetic. No integral equivariant section can exist, since the rational one is unique and nonintegral; conversely the displayed section is defined over \(\mathbb Z[1/3]\). Multiplication by three clears its denominators, making the extension class three-torsion, and its nonsplitting shows that the order is exactly three.

**Second homology and antipodal gluing.** Opposite square faces normal to axis \(k\) are disjoint cycles; their oriented product defines a degree-two cycle \(T_k\). There are exactly three. Their \(3\)-square coordinate minor using rows \((0,3,7)\) has determinant one. Since \(\operatorname{rank}\partial_2=39\), the top kernel has rank three; the unimodular minor forces the \(T_k\) to be an **integral** basis, proving \(H_2\cong\mathbb Z^3\). The signed face-orientation transformation gives the stated coordinate-permutation rule. In degree one, the central antipodal involution has integral plus/minus eigensublattices of ranks three and three; explicit primitive generators are in `verify.py`. The determinant of their combined six-column matrix is four, establishing index four exactly.

## Verification
Running `python3 verify.py` with `projection.json` in the same directory reconstructs all cells and signed integer boundaries; verifies \(\partial_1\partial_2=0\), connectivity, the determinant-\(-1\) \(45\)-column quotient certificate, the integral three-torus basis, all \(48\) automorphism matrices and all \(2304\) multiplication identities, the exact rational solution with denominator three, and the index-four antipodal lattice certificate. The successful actual run printed `VERIFY_OK cells=28,72,42 H=(1,6,3) G=48 quotient_unit_minor=-1 torus_basis=3 extension_denominator=3 central_gluing_index=4`. All calculations use exact integer or rational arithmetic in Python's standard library. Every finite verification concerns the exhaustively specified finite CW complex; there is no extrapolation to other graphs.

## Relationship to prior work
Abrams and Ghrist introduce graph configuration spaces and their discrete cubical models. Barnett and Farber compute ordinary **ordered** two-particle graph homology and planar face-product classes. An and Maciążek's graph braid presentations and Maciążek and Sawicki's treatment of three-connected planar graph braid homology explain the known **abstract** free rank of degree one and junction generators. These results do not specify the **integral equivariant** splitting class of the canonical total-motion exact sequence. Rational rank or character data cannot determine whether this integral extension has order three; the present nonsplitting calculation makes a separate assertion. A related published rational symmetry classification for the *cuboctahedral* graph applies to \(L(Q_3)\), not \(Q_3\). An earlier general exchange-sign Borel–Moore result concerns twisted local coefficients and does not determine ordinary singular \(H_1(X;\mathbb Z)\). The comparisons distinguish objects, coefficient theories, and actual statement implications, not merely keywords.

## Limitations
The order-three nonsplitting is proved for the **unordered two-point** configuration space of the three-dimensional cube. This does not classify other cube dimensions, other particle numbers, general planar graphs, integral cohomology rings or homotopy types. The known abstract degree-one group structure alone is not new. The rational section is unique for the specified natural extension, not a claim of unique non-equivariant splittings. Although material primary literature and indexed equivalents were compared, an unindexed alternative presentation of the same integral extension remains possible. No independent scientific audit has been performed.

## References
1. A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118v1, first public 2000-09-12, especially discussion of graph configuration cubical models. https://arxiv.org/abs/math/0009118
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (2009), especially the ordered deleted-product model and homology of planar graph configurations. https://arxiv.org/abs/0903.2180
3. B. H. An and T. Maciążek, *Geometric presentations of braid groups for particles on a graph*, arXiv:2006.15256 (2020), especially the sufficient-subdivision criterion and exchange generators. https://arxiv.org/abs/2006.15256
4. T. Maciążek and A. Sawicki, *Non-abelian quantum statistics on graphs*, arXiv:1806.02846 (2018), especially the planar graph braid-group first-homology discussion. https://arxiv.org/abs/1806.02846
