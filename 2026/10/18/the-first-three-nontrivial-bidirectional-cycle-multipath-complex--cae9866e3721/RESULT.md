# The first three nontrivial bidirectional-cycle multipath complexes are wedges of spheres

## Finding

Let \(B_n\) be the bidirected cycle on \(n+1\) vertices, with both arcs between consecutive vertices, and let \(X(B_n)\) be its multipath complex. For the three values \(n\in\{3,4,5\}\), there are integral homotopy equivalences
\[
\begin{aligned}
X(B_3)&\simeq \bigvee^{3}S^1\vee\bigvee^{2}S^2,\\
X(B_4)&\simeq S^2\vee\bigvee^{2}S^3,\\
X(B_5)&\simeq S^2\vee\bigvee^{2}S^4.
\end{aligned}
\]
In particular, these three cases satisfy the wedge-of-spheres conjecture posed for bidirectional polygonal multipath complexes by Caputi, Collari, and Smith. This theorem does not assert that the conjecture holds for other lengths.

## Assumptions and scope

For \(n\in\{3,4,5\}\), put \(N=n+1\) and take vertices \(0,\ldots,N-1\), modulo \(N\). Arc indices are \(2i\) for \(i\to i+1\) and \(2i+1\) for \(i+1\to i\), for \(0\leq i<N\). A face is a set of arcs with in-degree and out-degree each at most one at every graph vertex and no directed cycle. Consequently, each weak connected component is a directed path or an isolated vertex. The empty face is used for augmented discrete-Morse enumeration, but geometric realization is the ordinary nonempty simplicial complex. Orient simplices by increasing arc index; use integral simplicial chains and cochains.

All three cases concern the complete bidirectional cycles, not oriented cycles obtained by choosing just one arc along each edge, and not the cycle-free chessboard complex of a complete directed graph.

## Proof

**1. Exact discrete-Morse reduction.** The standalone verifier enumerates *every* subset of the \(2N\) arcs and retains precisely those that satisfy the preceding face definition. For each value of \(N\), it considers all remaining unmatched faces in increasing integer-mask order and pairs \(F\) with \(F\cup\{e_j\}\) when both faces are still unmatched, sequentially for the pivot order recorded below. The elementary matching is an acyclic matching in Forman's sense: the verifier reverses each matching incidence in the complete oriented Hasse diagram and topologically sorts **all** vertices. A completed sort is an exhaustive certificate of absence of closed gradient paths. It includes the empty face, which pairs with a vertex; deleting this augmented pair leaves that vertex as the single critical ordinary zero-cell and leaves the other critical dimensions unchanged.

For \(N=4\), use pivot indices \((0,1,2,3,4,5,6,7)\): there are \(33\) augmented faces, \(14\) matching pairs, and critical positive-dimensional cells \(3\) in degree \(1\), \(2\) in degree \(2\). The directed Hasse graph has \(64\) incidences. For \(N=5\), use \((0,4,9,7,6,1,8,5,2,3)\): there are \(81\) faces, \(39\) pairs, one critical degree-\(2\) cell and two degree-\(3\) cells, with \(200\) incidences. For \(N=6\), use \((0,1,2,3,4,5,6,7,8,9,10,11)\): there are \(197\) faces, \(97\) pairs, one critical degree-\(2\) cell and two degree-\(4\) cells, with \(588\) incidences. Each directed graph is verified acyclic by complete enumeration. Hence each complex has a CW model with exactly the displayed cells and one zero-cell.

**2. The four-vertex cycle.** For \(N=4\), all eight triangles are the three-element subsets of either the four forward arcs or the four reverse arcs. These form two disjoint tetrahedral boundaries, each homeomorphic to \(S^2\). There are exactly four mixed edges, with eight distinct endpoints; they connect the two sphere components by four parallel bridges, up to homotopy. A spanning-tree contraction shows that the result is \(\bigvee^{2}S^2\vee\bigvee^{3}S^1\).

**3. The five-vertex cycle.** For \(N=5\), every four-element face is a four-element subset of one of the two coherently oriented five-arc cycles. No five-element face exists. The two oriented simplex boundaries therefore give independent integral cycles in \(H_3\), as there are no degree-\(4\) boundaries and their supports are disjoint. The Morse CW model has only two degree-\(3\) cells, so its integral degree-\(3\) cellular differential into the sole degree-\(2\) cell is the zero map. Its two three-cell attaching maps have zero degrees in \(\pi_2(S^2)\cong\mathbb Z\), hence are null-homotopic. This gives \(S^2\vee\bigvee^2 S^3\).

**4. The six-vertex cycle and the unstable attaching obstruction.** For \(N=6\), the same face-classification argument identifies every five-element face as an omission of exactly one arc from one of the two consistently oriented six-arc cycles, and there are no six-element faces. The CW model has one zero-cell, one two-cell and two four-cells; therefore it is obtained from \(S^2\) by attaching two degree-\(4\) cells along maps \(S^3\to S^2\). Unlike the previous case, vanishing cellular differentials alone says nothing about these maps, since \(\pi_3(S^2)\cong\mathbb Z\). We now show that both Hopf coefficients vanish.

Define an integral simplicial two-cochain \(\phi\), indexed by increasing triples of arc labels. It takes value \(+1\) on
\[
(0,2,4),\ (0,2,6),\ (2,4,8),\ (2,6,8),\ (2,4,10),\ (2,6,10),
\]
value \(-1\) on \((0,4,9)\), and zero otherwise. The verifier evaluates the signed coboundary on **every** three-simplex and obtains \(\delta\phi=0\) identically over \(\mathbb Z\). It also checks via complete binary Gaussian elimination that the mod-two class of \(\phi\) is not a coboundary (the degree-one coboundary image has rank \(37\) in the \(76\)-dimensional triangle-cochain space). Since \(H^2\cong\mathbb Z\) from the Morse CW model, \([\phi]\) is an odd multiple of its integral generator \(u\).

For every four-simplex with increasing vertices \((a_0,\ldots,a_4)\), the Alexander–Whitney square evaluates as
\[
(\phi\smile\phi)(a_0,a_1,a_2,a_3,a_4)=
\phi(a_0,a_1,a_2)\,\phi(a_2,a_3,a_4)=0.
\]
The verifier checks this equality on **all** four-simplices, so the square is the zero cochain, not just a numerically small cohomology class. The Morse CW model gives \(H^4\cong\mathbb Z^2\), which is torsion-free; since \([\phi]=k u\) for a nonzero odd integer \(k\), \(k^2u^2=0\) implies \(u^2=0\). By the classical Hopf-invariant calculation for two four-cells attached to a two-sphere, the coefficients of the two classes in \(\pi_3(S^2)\) are exactly the coordinates of \(u^2\) evaluated on the two top cellular homology generators, up to orientation signs. Both vanish, so both attaching maps are null-homotopic. Hence \(X(B_5)\simeq S^2\vee\bigvee^2S^4\).

## Verification

Run `python3 verify_bidirectional_multipaths.py` with Python 3 and no dependencies beyond its standard library. The complete face enumerations have cardinalities \(33,81,197\); the three exact directed-Hasse checks contain \(64,200,588\) incidences. The independent top-cycle tests identify the complete sets of highest-dimensional simplices for \(N=5,6\). The last case additionally verifies an integral cocycle, a nonzero mod-two class, and vanishing of its integral Alexander–Whitney cup square on every top-dimensional simplex. A successful run ends with `VERIFY_OK: exact discrete Morse, top-cycle and Hopf-cup certificates`. The code itself is a fully specified finite mathematical certificate for all three graph orders, not a sample of a larger conjectural range.

## Relationship to prior work

Caputi, Collari, and Smith, *Multipath complexes of bidirectional polygonal digraphs* (first public preprint 9 January 2026, arXiv:2601.05670), determine connectivity and integral homology for all lengths but explicitly leave the homotopy type and proposed wedge-of-spheres property unresolved (introduction, Theorem 2.10, Section 3). For the three cases here their homology computations agree with the displayed homotopy types but do not determine the unstable attaching maps. The seven-term integral two-cocycle and its vanishing cup square settle that ambiguity at six graph vertices.

Caputi, Collari, Di Trani, and Smith, *On the homotopy type of multipath complexes* (Mathematika 70 (2024), e12235, Section 4.2), give wedge decompositions for **oriented polygonal graphs without bidirectional edges**; their theorem does not imply the present bidirectional results. The classification of cycle-free chessboard complexes concerns complete digraphs and also does not supply these homotopy equivalences.

## Limitations

This is a complete classification only for \(n\in\{3,4,5\}\); it does not establish the wedge conjecture for arbitrary bidirectional cycles. The \(n=2\) complex is outside the stated result and can be disconnected. For the first case above, the fundamental group is free; the proof does not provide a preferred or symmetry-equivariant choice of sphere generators. It does not give simple-homotopy equivalences for every displayed wedge decomposition, nor identify the geometric automorphism actions on homology. Completeness of the finite computations depends on the explicit, reproducible code provided; the all-length theorem is not claimed.

## References

1. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 [math.CO], publicly posted 9 January 2026. https://arxiv.org/abs/2601.05670 . Theorem 2.10 and Section 3.
2. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, Mathematika 70 (2024), e12235. DOI 10.1112/mtk.12235; lawful author-accepted manuscript https://irep.ntu.ac.uk/id/eprint/50523/1/1844094_Smih.pdf . Section 4.2.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete-Morse CW reduction.
4. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), Chapter 4 and Section 3.2. Classification of \(\pi_3(S^2)\), Hopf invariant, and cup products.
