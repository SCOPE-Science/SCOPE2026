# A vanishing Hopf obstruction for the bidirected hexagon multipath complex

## Finding
Let \(D\) be the bidirected six-cycle, with arcs in both directions on every edge of \(C_6\). Let \(X(D)\) be the simplicial complex of arc sets whose connected components are directed simple paths or isolated vertices. Then
\[
X(D)\simeq S^2\vee S^4\vee S^4.
\]
This is an integral homotopy equivalence, not merely an equality of Betti numbers. In the notation of Caputi--Collari--Smith, \(D={\tt BP}_5\).

## Assumptions and scope
The graph has precisely six vertices, \(0,1,2,3,4,5\), with indices modulo six. Its twelve ordered arc labels are
\[
a_i=(i,i+1),\quad b_i=(i+1,i),\qquad 0\le i<6,
\]
numbered \(0,\ldots,5\) for the \(a_i\) and \(6,\ldots,11\) for the \(b_i\). A simplex is a nonempty arc subset in which every vertex has at most one selected incoming and one selected outgoing arc and there is no selected directed cycle; the empty simplex is included by convention. A mask \(m\) encodes the arcs with \(1\)-bits in the stated label order. All integral chain signs come from increasing arc-label order.

## Proof
**Acyclic matching and cellular reduction.** Enumerating all possible subsets under the defining condition gives the nonempty face-vector
\[
(f_0,f_1,f_2,f_3,f_4)=(12,48,76,48,12).
\]
The complete list of 96 distinct matched facet--cofacet pairs is stored in `BP5_MATCHING.json`. The verifier constructs the entire Hasse diagram on the 196 nonempty simplices, directs each matched edge upward and every other covering relation downward, and checks by an exhaustive topological ordering that this directed graph is acyclic. Every simplex belongs to exactly one pair or is one of the four critical masks
\[
3904,\quad47,\quad2624,\quad512,
\]
of dimensions \(4,4,2,0\), respectively. Forman's discrete Morse theorem therefore yields a homotopy equivalent CW complex with exactly one zero-cell, one two-cell, and two four-cells, and no other cells. Its two-skeleton is \(S^2\). The two four-cells attach by maps in \(\pi_3(S^2)\cong\mathbb Z\).

**An integral cohomology generator.** Define a degree-two simplicial cochain \(\alpha\) to have coefficient \(1\) on the eight increasingly oriented triangles with masks
\[
11,13,21,22,26,37,38,42,
\]
and coefficient \(0\) on every other triangle. Directly evaluating the oriented coboundary on each of the 48 three-simplices gives \(\delta\alpha=0\). The explicit integral two-cycle
\[
 z=-[21]+[84]-[273]-[336]+[1029]+[1092]-[1281]+[1344]
\]
(here square-bracket labels denote increasingly oriented simplices with the indicated masks) satisfies \(\partial z=0\) and \(\langle\alpha,z\rangle=-1\). As the minimal CW model shows \(H^2(X(D);\mathbb Z)\cong\mathbb Z\), the class of \(\alpha\) is its primitive generator.

**Vanishing of the Hopf obstruction.** For any increasingly ordered four-simplex with arc-label vertices \(i_0<\cdots<i_4\), the Alexander--Whitney formula reads
\[
(\alpha\smile\alpha)([i_0,\ldots,i_4])
=\alpha([i_0,i_1,i_2])\alpha([i_2,i_3,i_4]).
\]
In each of the twelve four-simplices at least one factor is zero, by the eight-term support above. Hence \(\alpha\smile\alpha=0\) as an *integral cochain*, so its cohomology class vanishes. For a simply connected CW complex with one two-cell and two four-cells, the coordinates of the square of the primitive degree-two class, paired with the two four-cell fundamental classes, are exactly the Hopf invariants of the attaching maps in \(\pi_3(S^2)\cong\mathbb Z\). Both attaching maps thus represent zero. They are null-homotopic, proving the stated wedge decomposition.

## Verification
Run `python3 verify.py` in a directory containing `verify.py` and `BP5_MATCHING.json`. Only Python's standard library is required. The checker regenerates the entire face poset from the twelve directed arcs; validates the complete matching, critical dimensions, and absence of directed gradient cycles; checks the signed integral cochain and cycle identities; and checks that all twelve Alexander--Whitney square coefficients are exactly zero. Its success marker is `VERIFY_OK`. The combinatorial checks are exhaustive for this single six-vertex graph; the topological conclusion additionally uses Forman's discrete Morse theorem and the standard identification \(\pi_3(S^2)\cong\mathbb Z\) through the Hopf invariant.

## Relationship to prior work
Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670v1, first submitted 2026-01-09), Theorem 2.10, computed the integral homology of all bidirected polygons but explicitly left their wedge-of-spheres homotopy classification open (discussion following Theorem 2.10 and Section 3). The present result resolves the precise six-cycle case in which a four-cell attachment to a two-sphere could carry a nontrivial integral Hopf invariant. Previously available homotopy calculations for larger bidirected polygons beginning at seven vertices do not imply this case. Calculations of dihedral *homology characters* likewise do not determine the attaching Hopf invariant.

## Limitations
The statement concerns only the bidirected six-cycle, not every bidirected polygon. The certificate supplies a finite complete argument for the stated simplicial complex; it does not classify equivariant homotopy types or yield an infinite-family matching. The novelty comparison is subject to the possibility of equivalent unindexed work, and the scientific result has not undergone independent external validation.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (2026), https://arxiv.org/html/2601.05670.
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90--145.
3. A. Hatcher, *Algebraic Topology* (2002), Sections 3.2 and 4.B, for cup products and the Hopf invariant, https://pi.math.cornell.edu/~hatcher/AT/AT.pdf.
