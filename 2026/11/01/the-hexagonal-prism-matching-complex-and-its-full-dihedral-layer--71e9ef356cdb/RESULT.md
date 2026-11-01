# The hexagonal prism matching complex and its full dihedral-layer homology character

## Finding
Let \(G=C_6\square K_2\) be the hexagonal prism graph, and let \(\mathcal M(G)\) be its **ordinary matching complex**: every collection of pairwise vertex-disjoint edges of \(G\) is a face, including those not extendable to a perfect matching. Then
\[
|\mathcal M(G)|\simeq\bigvee^{12}S^3.
\]
The full graph automorphism group is \(\operatorname{Aut}(G)\cong D_6\times C_2\). Writing \(r\) for one-step rotation, \(s\) for reflection of the hexagon, and \(t\) for exchange of the two layers, the complete rational homology character \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_3(\mathcal M(G);\mathbb Q))\) is as follows. In each row entries correspond to \(a=0,1,2,3,4,5\) for \(g=r^a s^b t^c\):

| \(b\) | \(c\) | \(\chi(r^a s^b t^c)\), \(a=0,\ldots,5\) |
|---:|---:|---|
| 0 | 0 | \((12,0,0,6,0,0)\) |
| 0 | 1 | \((-2,-2,-2,4,-2,-2)\) |
| 1 | 0 | \((0,-2,0,-2,0,-2)\) |
| 1 | 1 | \((2,4,2,4,2,4)\) |

Let \(A_{\eta,\epsilon}\) be the one-dimensional representation of \(D_6\) on which \(r\) acts by \(\eta\in\{\pm1\}\) and \(s\) by \(\epsilon\in\{\pm1\}\). Let \(E_j\), \(j=1,2\), be its rational irreducible two-dimensional representation with \(\chi_{E_j}(r^a)=2\cos(2\pi ja/6)\) and \(\chi_{E_j}(r^as)=0\), and write \(T_\zeta\) for the one-dimensional representation of the layer-exchange \(C_2\) where \(t\) acts by \(\zeta\). Then the homology representation is
\[
(A_{+,+}\boxtimes T_+)
\oplus 2(A_{+,-}\boxtimes T_-)
\oplus(A_{-,+}\boxtimes T_-)
\oplus(E_1\boxtimes T_-)
\oplus2(E_2\boxtimes T_+)
\oplus(E_2\boxtimes T_-).
\]
In particular, layer exchange has \(+1\) and \(-1\) eigenspace dimensions \(5\) and \(7\), and the full graph automorphism group fixes a unique one-dimensional subspace of third rational homology.

## Assumptions and scope
Use graph vertices \((i,\ell)\) with \(i\in\mathbb Z/6\mathbb Z\) and \(\ell\in\{0,1\}\). Its 18 graph edges are the twelve rim edges \(\{(i,\ell),(i+1,\ell)\}\) and six rung edges \(\{(i,0),(i,1)\}\). No cycles, surface cells, or other edges are added. The simplices of \(\mathcal M(G)\) are subsets of **graph edges**, not subsets of graph vertices. Its empty face is included in augmented enumeration but not treated as a CW cell. All integral homotopy and rational representation assertions concern precisely this twelve-vertex graph, not an infinite prism family.

The graph automorphism group has precisely 24 elements: every rung belongs to two graph-theoretic quadrilaterals, while every rim edge belongs to one; hence automorphisms preserve the six rungs. On the rung adjacency cycle they induce a dihedral permutation. After this choice, connectivity across rim edges forces the choice of layer swap to be global. Conversely every element of \(D_6\times C_2\) so obtained is an automorphism.

## Proof
**Exact finite face enumeration.** Index the 18 graph edges by rim layer zero in cyclic order, rim layer one in cyclic order, then rungs in cyclic order. Represent an edge subset by an eighteen-bit nonnegative integer, and accept it exactly when the selected graph edges have disjoint endpoints. The complete enumeration has 1,104 faces including the empty face and dimension-wise nonempty counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,336,420,192,20).
\]
An independent matching-polynomial computation by vertex deletion, \(P_H(z)=P_{H-v}(z)+z\sum_{w\sim v}P_{H-\{v,w\}}(z)\), recovers the coefficients \((1,18,117,336,420,192,20)\). Thus the reduced Euler characteristic is \(-12\).

**Discrete-Morse matching.** Starting from all 1,104 augmented faces, process the 18 edges in the indicated order. At stage \(j\), for every still-unmatched face \(\sigma\) not containing edge \(j\), pair it with \(\sigma\cup\{j\}\) whenever the latter is also still-unmatched. These pairs are disjoint. The augmented process yields 546 pairs and exactly twelve unmatched four-element faces. Its first pair is the empty face with the one-edge face \(\{e_0\}\). Discard that first pair and the empty face; this leaves a discrete-Morse matching of the *ordinary nonempty face poset* with 545 pairs and thirteen critical cells: one zero-cell and twelve three-cells.

To verify acyclicity without invoking an unproved generic matching lemma, enumerate every nonempty codimension-one face incidence, orient matched incidences from smaller to larger and all others from larger to smaller, and topologically sort this finite digraph. The provided standalone verifier checks all 4,002 incidences among all 1,103 nonempty faces and successfully visits every vertex. A directed cycle would prevent a complete topological sort, so the matching is acyclic. Forman's discrete-Morse theorem yields a homotopy equivalent CW complex with exactly one 0-cell and twelve 3-cells. Each three-cell attaches along a map from \(S^2\) to a point, necessarily trivial. This establishes the asserted wedge of twelve three-spheres integrally; in particular the only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{12}\).

**Action on rational homology.** For a graph automorphism \(g\), its action on an oriented matching simplex permutes the selected edges with the induced orientation sign. Since reduced rational homology is concentrated in degree three, the reduced Lefschetz formula gives
\[
\chi(g)=\sum_{\substack{\sigma\in\mathcal M(G)\\g\sigma=\sigma}}(-1)^{|\sigma|}\operatorname{sgn}(g|_\sigma),
\]
with the empty face contributing \(+1\). For \(g=r^as^bt^c\), the verifier explicitly permutes the 18 graph edges, enumerates all invariant matchings, evaluates each sign by inversion parity in the sorted edge list, and obtains the four six-entry rows above. This computation has no dependence on equivariance of the Morse matching.

For each of the eight one-dimensional and four two-dimensional irreducible characters of \(D_6\times C_2\), the usual character inner product \(\frac1{24}\sum_g\chi(g)\overline{\psi(g)}\) yields precisely the displayed multiplicities (all other multiplicities zero). The sum of dimension-weighted multiplicities is 12. The layer-swap trace is \(-2\), so its eigenspace dimensions are \((12-2)/2=5\) and \((12+2)/2=7\). The multiplicity of the trivial character is one, giving the unique fixed rational homology line.

## Verification
Run `python3 verify.py` in the directory containing this file and the standalone checker. It reconstructs the graph from the edge formula, enumerates all faces, independently verifies the face vector by matching-polynomial recursion, constructs the full Morse matching, checks every directed Hasse incidence and global acyclicity, performs independent mod-two simplicial-boundary elimination, computes all 24 signed Lefschetz traces, and calculates their exact irreducible multiplicities. The checks execute using only the Python standard library. No numerical floating-point comparison or unexamined external dataset is needed.

## Relationship to prior work
Agarwal and Basak's 2026 work on Möbius and circular ladders (arXiv:2608.30601, first publicly posted 2026-08-31) studies **independence complexes of the original graphs** and **perfect-matching complexes**. Neither is the ordinary matching complex considered here: for instance, this complex has six maximal four-edge matchings that are not contained in any perfect matching, in addition to 72 maximal five-edge and 20 perfect six-edge matchings. The accessible full text of the first version and the updated second-version abstract do not state the ordinary hexagonal-prism matching homotopy or its \(D_6\times C_2\) character.

The outerplanar-graph matching-complex theorem of Bayer, Jelić Milutinović and Vega (arXiv:2411.04601) does not apply: every outerplanar graph is 2-degenerate, whereas this prism is 3-regular. Matsushita's small-grid results concern the nonperiodic rectangular ladder rather than its cyclic closure. A published calculation for the *total three-cut complex* of the same hexagonal prism concerns a different simplicial complex and does not imply this matching-complex result. These are mathematical coverage comparisons rather than assertions that unsuccessful searches prove novelty.

## Limitations
The proof classifies one finite graph; it does not determine matching-complex homotopy for all circular ladders or the integral automorphism-module lattice. The latest version of the relevant 2026 primary paper could be inspected only through its abstract, although detailed first-version text was inspected. A similar calculation in an unexamined section or unindexed source cannot be ruled out. The finite verification is independently reproducible from the embedded checker but has not received an independent mathematical audit.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 2026-08-31, revised 2026-09-14. https://arxiv.org/abs/2608.30601
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first public 2024-11-07. https://arxiv.org/abs/2411.04601
3. T. Matsushita, *Matching Complexes of Small Grids*, Electron. J. Combin. 26(3) (2019), #P3.1, doi:10.37236/8480.
4. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
