# Third-power cycle neighborhood complexes collapse to parity-twisted sphere bundles

## Finding
For every integer \(n\ge13\), let \(G_n=C_n^{(3)}\) be the simple graph on \(\mathbb Z/n\mathbb Z\) in which two different vertices are adjacent precisely when their cyclic distance is \(1\), \(2\), or \(3\). Let \(\mathcal N(G_n)\) be the **open** Lovász neighborhood complex: a nonempty subset is a simplex exactly when it has a common graph neighbor. There is an explicit sequence of \(10n\) elementary simplicial collapses
\[
 \mathcal N(G_n)\searrow M_n,
\]
where \(M_n\) is a closed combinatorial three-manifold whose tetrahedra are all the cyclic translates of the five templates
\[
\{0,1,2,6\},\quad\{0,1,5,6\},\quad\{0,2,3,4\},\quad\{0,2,4,5\},\quad\{0,2,5,6\}.
\]
This triangulation has face vector \((n,6n,10n,5n)\) and is PL homeomorphic to the sphere bundle
\[
 |M_n|\cong_{\rm PL}
 \begin{cases}
 S^2\times S^1,&n\text{ even},\\
 S^2\widetilde{\times}S^1,&n\text{ odd},
 \end{cases}
\]
where the latter is the nonorientable, orientation-reversing \(S^2\)-bundle over \(S^1\). Consequently \(\pi_1(\mathcal N(G_n))\cong\mathbb Z\), and the **integral** homology is
\[
H_i(\mathcal N(G_n);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
\mathbb Z,&i=2,3\text{ and }n\text{ even},\\
\mathbb Z/2\mathbb Z,&i=2\text{ and }n\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]
The orientable and nonorientable cases are therefore distinguished by genuine integral two-torsion, although they have identical mod-two Betti numbers.

## Assumptions and scope
All graphs are finite, simple, and undirected. The power is the ordinary **graph power**, not the geometric metric Rips complex and not the total cut complex. Cyclic indices are residues modulo \(n\). The lower bound \(n\ge13\) is essential to the proof because it makes the twelve positive and negative offsets \(\pm1,\ldots,\pm6\) distinct in each vertex link. The claim does not classify smaller orders, other cycle powers, or other six-regular circulants.

## Proof
**1. Uniform elementary collapse.** Each maximal simplex of \(\mathcal N(G_n)\) is a subset of a graph open neighborhood \(\{i-3,i-2,i-1,i+1,i+2,i+3\}\); in fact the full six-element neighborhoods are the distinct maximal facets. Starting with these facets, perform the following **ten ordered families**. In each row the left face is free in the unique right coface, and the same pair is removed after every simultaneous cyclic translation. Entries with negative signs mean residues modulo \(n\):

| Family | Free face | Unique coface |
|:--:|:--|:--|
| 1 | \(\{0,1,2,4,5\}\) | \(\{0,1,2,4,5,6\}\) |
| 2 | \(\{0,1,2,4\}\) | \(\{0,1,2,4,6\}\) |
| 3 | \(\{0,1,2,5\}\) | \(\{0,1,2,5,6\}\) |
| 4 | \(\{0,1,3,4\}\) | \(\{0,1,3,4,5\}\) |
| 5 | \(\{0,1,2,-3\}\) | \(\{0,1,2,-4,-3\}\) |
| 6 | \(\{0,1,2,-4\}\) | \(\{0,1,2,-4,-2\}\) |
| 7 | \(\{0,1,3\}\) | \(\{0,1,3,5\}\) |
| 8 | \(\{0,2,-3\}\) | \(\{0,2,-4,-3\}\) |
| 9 | \(\{0,1,4\}\) | \(\{0,1,4,5\}\) |
| 10 | \(\{0,2,-4\}\) | \(\{0,2,-4,-2\}\) |

These are genuine elementary collapses: each left face has exactly one remaining maximal coface when its family is reached, and no two cyclic translates use the same coface. Direct coface inspection using the six-element neighborhoods verifies these finite local identities. Cyclic coincidences can only affect cases \(13\le n\le24\), checked separately; when \(n\ge25\), any two neighborhoods meeting a fixed face have centers within six cyclic steps and all relevant relative offset configurations occur without wraparound in a window of length at most thirteen. This gives the same ten local checks on the integer line for every larger \(n\). All translates of each family can thus be removed, in any order. Listing the remaining maximal faces gives precisely the five tetrahedral templates above, each with \(n\) distinct translates. This establishes the collapse count and face vector.

**2. Closed three-manifold.** Each triangle of the resulting pure three-complex belongs to exactly two tetrahedra. Every vertex link consists of twelve distinct vertices, thirty edges, and twenty triangles, with all link edges in two triangles and a connected triangle-adjacency graph. Hence every link is a triangulated two-sphere (in fact the icosahedral link), and \(M_n\) is a closed combinatorial three-manifold.

**3. A spherical fiber in the integer cover.** Let \(\widetilde M\) have vertex set \(\mathbb Z\) and every integer translate of the same five tetrahedral templates. Because \(n\ge13\), reduction modulo \(n\) is a combinatorial covering map \(\widetilde M\to M_n\) with deck generator \(i\mapsto i+n\). Extend the height \(h(i)=i\) affinely on each tetrahedron. The lower link at any vertex is a six-vertex two-ball with five triangles, ten edges, and five boundary edges; the upper link is another such ball. For example, at vertex zero the upper-link triangles are
\[
(1,2,6),\ (1,5,6),\ (2,3,4),\ (2,4,5),\ (2,5,6).
\]
The corresponding lower-link triangles are
\[
(-6,-5,-4),\ (-6,-5,-1),\ (-6,-4,-1),\ (-5,-3,-1),\ (-4,-2,-1).
\]
These link-disk tests show that the PL height has no critical vertices; outside vertex heights it is linear on simplices and has no critical points. Thus crossing an integer level changes the level surface only by a PL isotopy, and slabs between consecutive half-integer levels are products. At height \(1/2\), the level intersects twenty-seven tetrahedra in triangles or quadrilaterals. The resulting closed connected surface has twenty-one vertices, forty-six edges, and twenty-seven polygons, so its Euler characteristic is \(21-46+27=2\): it is \(S^2\). The proper height map therefore identifies \(\widetilde M\) PL with \(S^2\times\mathbb R\), with the integer shift acting fiberwise as a homeomorphism of \(S^2\) covering translation of \(\mathbb R\).

**4. Monodromy orientation.** Number the five tetrahedral templates in their displayed order. For the tetrahedron with template number \(j\) translated by \(i\), assign to its increasing-vertex ordering the coefficient \((-1)^i c_j\), where \((c_1,c_2,c_3,c_4,c_5)=(1,-1,1,1,1)\). For every shared triangle the two induced boundary orientations cancel, so this orients \(\widetilde M\). Translation \(i\mapsto i+1\) reverses this orientation. Because height translation preserves orientation of the base line, its map on a spherical fiber has degree \(-1\). The deck generator \(i\mapsto i+n\) therefore has spherical degree \((-1)^n\). Orientation-preserving self-homeomorphisms of \(S^2\) are isotopic to the identity, and orientation-reversing ones to a reflection. The two possible mapping tori give exactly the claimed product and twisted sphere bundles.

**5. Algebraic consequences.** The fibration over \(S^1\) has simply connected spherical fiber, whence its fundamental group is \(\mathbb Z\). The Wang sequence for the monodromy \((-1)^n\) acting on \(H_2(S^2;\mathbb Z)\) gives \(H_2=\operatorname{coker}(1-(-1)^n)\) and \(H_3=\ker(1-(-1)^n)\), proving the displayed integral homology groups. No claim of an infinite homology calculation is based solely on the finite checks below.

## Verification
The independently executable standard-library script `verify.py` reconstructs every neighborhood complex for orders \(13\) through \(36\), executes the prescribed ten translate-orbit free-face cancellations in order, and checks the surviving tetrahedral orbits and face vectors. It then tests every vertex link, the local lower and upper link disks, the twenty-seven-section polygon count, connectivity of the section, and the orientation propagation sign in the integer cover. Run `python3 verify.py`; the checked package produced `VERIFY_OK` on both lines. The universal conclusions follow from the written local-width and PL arguments, not from extrapolating finitely many examples.

## Relationship to prior work
Matsushita [1] provides the combinatorial description of fundamental groups of neighborhood complexes, not a simplicial collapse or integral three-dimensional classification of \(\mathcal N(C_n^{(3)})\). Shukla [2] classifies neighborhood complexes for graphs with maximum degree at most three and **four-regular** circulant graphs, so his results do not apply directly to the six-regular graph used here. Bagchi–Datta [3] determine general minimal-triangulation phenomena for sphere bundles over \(S^1\); the topology of a sphere bundle is therefore not itself claimed to be newly discovered, and their construction does not identify these complexes as neighborhood complexes of third-power cycles. The present contribution is the explicit graph-to-manifold simplicial collapse and the all-order parity-sensitive classification.

## Limitations
The exact result is restricted to \(n\ge13\) and graph power three. This is a self-review, not an independent audit. The manuscript does not assert that the surviving abstract triangulations are new as standalone triangulations: they may be isomorphic to previously catalogued sphere-bundle triangulations. A more obscure equivalent neighborhood-complex computation cannot be ruled out conclusively by the inspected literature. No numerical test establishes a statement beyond its enumerated finite range without the proof above.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, first public version 2012-10-10, arXiv:1210.2803. Published version, J. Math. Sci. Univ. Tokyo 24 (2017), 321–353; MSC 55Q05.

[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, Electronic Journal of Combinatorics 26 (2019), P2.4.

[3] B. Bagchi and B. Datta, *Minimal triangulations of sphere bundles over the circle*, arXiv:math/0610829 (2006), Journal of Combinatorial Theory A 115 (2008), 737–752.
