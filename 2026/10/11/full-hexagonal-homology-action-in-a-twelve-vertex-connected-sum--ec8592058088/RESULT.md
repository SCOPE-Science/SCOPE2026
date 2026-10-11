# Full hexagonal homology action in a twelve-vertex connected-sum triangulation
## Finding
Let \(K\) be the twelve-vertex triangulation `manifold_3_12_13_4` from the Lutz manifold tables. The exact facet presentation reconstructs
\[
f(K)=(12,66,108,54),
\]
and the tables identify its topology as
\[
(S^2\times S^1)\#(S^2\times S^1)
\]
with
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2.
\]

The full simplicial automorphism group has order \(24\). In an explicit integral basis of first homology, its induced image in \(GL(2,\mathbb Z)\) has order \(12\), and every image matrix is realized by exactly two simplicial automorphisms. The image is exactly the full integral isometry group of
\[
q(x,y)=x^2+xy+y^2.
\]
Equivalently, the simplicial symmetries realize the complete dihedral symmetry group of the hexagonal rank-two lattice on first homology. The kernel of the integral homology action therefore has order \(2\).

Reduction modulo \(2\) maps those twelve integral matrices onto all six elements of
\[
GL(2,\mathbf F_2),
\]
so the mod-two homology action is surjective and its kernel in the simplicial automorphism group has order \(4\).

## Assumptions and scope
The claim concerns the fixed labelled complex `manifold_3_12_13_4`. The phrase “full simplicial automorphism group” means all vertex permutations preserving its tetrahedral facet set. The homology basis is constructed from two graph cycles after collapsing the star spanning tree at vertex \(1\); it is not imported from the source table.

The quadratic form \(q\) is a homology-coordinate invariant only up to integral change of basis. Thus the intrinsic statement is that the image is conjugate in \(GL(2,\mathbb Z)\) to the full integral isometry group of the hexagonal lattice.

## Proof
From the fifty-four tetrahedra one obtains all \(66\) edges of the complete graph on twelve vertices and \(108\) triangular faces. Collapse the star tree at vertex \(1\). The integral graph-cycle lattice then has one coordinate for each of the remaining \(55\) edges.

The package gives two explicit integral one-cocycles \(w_1,w_2\) in these cotree coordinates and verifies that both annihilate every one of the \(108\) oriented facial triangle boundaries. A selected \(53\)-by-\(53\) minor of the facial-boundary relation matrix has determinant \(1\). Hence the relation lattice has rank at least \(53\) and is primitive. The two independent cocycles give rank at most \(53\). Consequently
\[
H_1(K;\mathbb Z)\cong\mathbb Z^{55}/B_1\cong\mathbb Z^2
\]
with no torsion, independently reproducing the published homology.

The cotree cycles associated with edges \(23\) and \(26\) have cocycle-pairing matrix
\[
\begin{pmatrix}-1&-1\\-1&0\end{pmatrix},
\]
whose determinant is \(-1\). They therefore form an integral homology basis.

To determine the full simplicial automorphism group, the verifier performs an exact backtracking enumeration of vertex permutations. As soon as three assigned vertices are available it enforces preservation of triangular-face status, and as soon as four are available it enforces preservation of tetrahedral-facet status. Exactly \(24\) complete permutations survive, and their orbit on vertex \(1\) contains all twelve vertices.

Each of those \(24\) automorphisms is applied to the two basis cycles, and the resulting cycles are evaluated against \(w_1,w_2\). Converting the two pairing columns back through the unimodular pairing matrix gives the induced integral \(2\)-by-\(2\) homology matrix. Exactly twelve distinct matrices occur, each twice.

Every resulting matrix preserves \(q(x,y)=x^2+xy+y^2\). Conversely, if an integral matrix preserves \(q\), each column has \(q\)-norm one. Since
\[
4q(x,y)=(2x+y)^2+3y^2,
\]
any integral norm-one vector has both coordinates in \(\{-1,0,1\}\). Exhausting these finitely many possibilities gives exactly twelve invertible isometries, identical to the twelve matrices induced by the simplicial automorphisms. Thus the homology image is the full integral isometry group of \(q\).

Reducing the twelve matrices modulo \(2\) gives six distinct invertible matrices, exactly all of \(GL(2,\mathbf F_2)\). The integral identity matrix has two simplicial preimages, while the mod-two identity has four, giving the two kernel orders.

## Verification
The standalone `verify.py` uses only the Python standard library. It rebuilds the face sets, replays the determinant-one boundary certificate by fraction-free Bareiss elimination, verifies the cocycles, exhausts the full automorphism backtracking tree, computes all integral homology matrices, exhausts the integral isometry group of \(q\), and checks the complete mod-two image.

Its exact successful output is:

`VERIFY_OK f=12,66,108,54 aut=24 H1_Z=Z^2 boundary_minor_det=1 H1_image=O(x^2+xy+y^2,Z):12 action_multiplicity=2 kernel_Z=2 mod2_image=GL(2,2):6 kernel_F2=4`

All enumerated domains are finite and exhausted. No random search or sampled automorphism computation is used in the proof.

## Relationship to prior work
Köhler and Lutz classify vertex-transitive combinatorial manifolds on at most thirteen vertices. Their enumeration framework determines automorphism groups while processing transitive group actions, and the Lutz manifold tables supply this exact complex, its topology, and its homology. Those facts are treated as prior.

The inspected literature and exact databases did not locate a statement describing the induced action of the full simplicial automorphism group of this exact twelve-vertex complex on \(H_1\), nor the identification of its image with the complete hexagonal-lattice isometry group. The closest owned result involving \(S^2\times S^1\) concerns a different ten-vertex triangulation and the vertex support of its second-homology generator; it does not imply an automorphism representation on rank-two first homology.

## Limitations
The result is specific to this one vertex-transitive triangulation. It does not classify the homology representations of the other twelve-vertex triangulations of the same topological manifold, nor does it determine the full mapping-class-group action. The originality conclusion is literature-based; an unindexed historical computation could contain the same twelve homology matrices.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24, primary MSC `57Q15`.
2. F. H. Lutz, *The Manifold Page*, exact datasets `3_manifolds.txt`, `3_manifolds_type.txt`, and `3_manifolds_hom.txt`, entry `manifold_3_12_13_4`.
