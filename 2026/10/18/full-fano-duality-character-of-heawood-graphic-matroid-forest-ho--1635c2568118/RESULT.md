# Full Fano-duality character of Heawood graphic-matroid forest homology

## Finding
Let \(H\) be the incidence graph of the seven points and seven lines of the Fano plane. Let \(\mathcal F(H)\) be its graphic-matroid independence complex: its vertices are the 21 graph edges and its faces are precisely the edge sets that contain no graph cycle. Then
\[
\widetilde H_i(\mathcal F(H);\mathbb Z)=
\begin{cases}\mathbb Z^{3152}&i=12,\\0&i\ne12.\end{cases}
\]
The full automorphism group \(G=\operatorname{Aut}(H)\) has order 336 and contains the incidence-preserving group \(G_+\) of order 168. The following table gives every rational degree-12 homology trace; an edge-cycle type such as \(2^8 1^5\) means eight transpositions and five fixed edges of the induced permutation on the 21 graph edges.

| Point/line exchange | Edge-cycle type | Number of automorphisms | Homology trace |
|---|---|---:|---:|
| No | \(1^{21}\) | 1 | 3152 |
| No | \(2^8 1^5\) | 21 | 0 |
| No | \(3^7\) | 56 | -4 |
| No | \(4^4 2^2 1\) | 42 | 0 |
| No | \(7^3\) | 48 | 2 |
| Yes | \(2^9 1^3\) | 28 | 60 |
| Yes | \(6^3 3\) | 56 | 0 |
| Yes | \(8^2 4 1\) | 84 | 0 |

The dimensions of the invariant spaces are
\[
\dim\widetilde H_{12}(\mathcal F(H);\mathbb Q)^G=14,\qquad
\dim\widetilde H_{12}(\mathcal F(H);\mathbb Q)^{G_+}=18.
\]
Each point-line-exchanging involution acts on the 18-dimensional \(G_+\)-fixed subspace with positive and negative eigenspace dimensions 14 and 4, respectively. This is **not** a claim that the entire 3152-dimensional module has a four-dimensional negative eigenspace.

## Assumptions and scope
Model the seven nonzero vectors of \(\mathbb F_2^3\) as the points \(1,\ldots,7\), with Fano lines \(\{a,b,a\oplus b\}\), where \(\oplus\) denotes bitwise exclusive-or on three-bit vectors. Add one graph vertex for each line and one edge for each incident point-line pair. There are 14 graph vertices, 21 graph edges, and a unique connected component. A forest is any subset of those edges inducing no cycles, including the empty subset. Use reduced simplicial chains over \(\mathbb Z\), with the empty face in degree \(-1\).

The line-preserving actions arise from all 168 invertible linear transformations of \(\mathbb F_2^3\); composing with the point/line duality defined by orthogonality produces 168 additional actions. These 336 edge permutations are distinct. Every symmetry acts simplicially on \(\mathcal F(H)\), using the orientation convention of increasing edge indices.

## Proof
**Topological concentration.** The graph is connected and bridgeless. Its graphic matroid consequently has rank \(14-1=13\) and no coloops. The matroid independence complex is shellable, by the general matroid-complex theorem of Ardila--Castillo--Samper (Theorem 1.3, with the familiar homotopy corollary stated in their introduction). It is pure of dimension 12 and homotopy equivalent to a wedge of 12-spheres, with no integral torsion. Thus the entire reduced rational Lefschetz number of an automorphism equals its character on \(\widetilde H_{12}\).

**Finite signed Lefschetz formula.** For an automorphism \(g\), decompose its 21-edge permutation into orbits \(O_1,\ldots,O_r\). A face fixed setwise by \(g\) is exactly the union of a subset of these orbits, provided that union is a forest. If \(s\) edge orbits occur in such a face, the sign of the vertex permutation on its oriented simplex is \((-1)^{|A|-s}\), and the alternating simplicial-chain sign is \((-1)^{|A|-1}\). Their product is \((-1)^{s+1}\). This also holds for the empty face, whose reduced chain is degree \(-1\). Therefore
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{12}(\mathcal F(H);\mathbb Q)\bigr)
=-\sum_{I\subseteq\{1,\ldots,r\}:\,\bigcup_{j\in I}O_j\text{ is a forest}}(-1)^{|I|}.
\]
No infinite calculation is hidden here: every summation ranges over at most 21 finite edge orbits. The forest predicate is exact, determined by disjoint-set unions and rejected precisely when an edge closes a cycle.

**Full group evaluation.** Exhausting the 168 invertible binary matrices and composing with orthogonality duality gives all 336 symmetries and precisely the eight displayed point/line-exchange and edge-cycle signatures. Evaluating the signed sum for each symmetry gives the traces and multiplicities in the table. An independent enumeration over all \(2^{21}=2,097,152\) edge masks gives 1,469,920 forests and the same traces for representatives of all eight signatures. In particular, the identity trace is 3152. The integer homology rank is thus 3152 by concentration.

**Invariant dimensions and duality.** For a finite group acting in characteristic zero, averaging traces gives fixed-space dimension. The full-group character sum is
\[
3152+56(-4)+48(2)+28(60)=4704=336\cdot14.
\]
Within the 168-element incidence-preserving subgroup it is
\[
3152+56(-4)+48(2)=3024=168\cdot18.
\]
The larger group is an index-two extension, so any incidence duality induces an involution on the 18-dimensional subgroup-fixed space. Its fixed part is the 14-dimensional full-group-fixed space, leaving a four-dimensional negative eigenspace.

## Verification
Run `python3 verify_heawood.py` for an exact enumeration of all 336 automorphisms, eight edge-orbit types and signed forest-orbit recursions. It asserts the full table and invariant dimensions. Independently compile `heawood_forest_crosscheck.cpp` with `g++ -std=c++17 -O2 heawood_forest_crosscheck.cpp -o heawood_check` and run `./heawood_check`: this searches all 2,097,152 edge subsets and independently computes 1,469,920 forests and the eight representative traces. The scripts use no network services or third-party packages; both were executed from the packaged source files before reporting this result. Standard matroid shellability supplies the infinite-dimensional/topological inference; finite checks alone are not presented as a shellability proof.

## Relationship to prior work
Ardila--Castillo--Samper establish matroid independence-complex shellability and the general wedge-of-spheres structure; this is used, not claimed as new. Moci--Pezzoli study equivariant matroid homology and provide a broad representation-theoretic framework, particularly for dual matroids and selected graph families; they do not tabulate the full Heawood graphic-forest 336-element character. Existing Heawood calculations for ordinary matching complexes and for graph-vertex independence complexes concern different face predicates: pairwise disjoint edges or independent graph vertices, respectively. Neither determines the present graphic-matroid forest character. The new contribution is the evaluated eight-type character and exact full-group and duality-invariant dimensions, not general matroid shellability.

## Limitations
The complete character is given as an eight-signature table, not an explicit irreducible-character decomposition or integral equivariant lattice classification. Ordinary group characters do not determine integral extension classes. Literature not located by the searches may contain an equivalent Heawood-specific computation. The proof requires standard established matroid-shellability results; the included finite checkers reproduce the group and alternating forest enumeration, not the general shellability theorem.

## References
1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (first public version 2014-10-14), especially Theorem 1.3 and the introduction on the independence complex.
2. L. Moci, G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (first public version 2020-01-11), especially the introduction and Sections 4 and 6.
3. J. C. Baez, *The Heawood Graph*, AMS Visual Insight, 2015-08-01, for Fano-incidence and full 336-element symmetry background.
