# A 48-sphere Rips thickening of the Fano flag graph and its full symmetry character

## Finding
Let \(\mathcal P\) be the Fano projective plane, \(H\) its bipartite point–line incidence graph (the Heawood graph), and \(G=L(H)\) its 21-vertex line graph. Give \(V(G)\) shortest-path distance and form the inclusive radius-two Vietoris–Rips complex \(X=\operatorname{VR}_{\le2}(V(G))=\operatorname{Cl}(G^2)\). Then
\[
X\simeq\bigvee^{48}S^2,\qquad
\widetilde H_j(X;\mathbb Z)=\begin{cases}\mathbb Z^{48}&j=2,\\0&j\ne2.\end{cases}
\]
The full 336-element incidence-graph automorphism group \(W=\operatorname{Aut}(H)\) acts on \(\widetilde H_2(X;\mathbb Q)\). Its character depends only on the order of an automorphism and whether it exchanges the point and line bipartitions, as given by the following exhaustive table. A value \(0\) in the swap column means bipartition-preserving; \(1\) means bipartition-exchanging.

| Order | Swap | Number of elements | Trace on \(\widetilde H_2\) |
| ---: | ---: | ---: | ---: |
| 1 | 0 | 1 | 48 |
| 2 | 0 | 21 | 0 |
| 2 | 1 | 28 | -4 |
| 3 | 0 | 56 | 3 |
| 4 | 0 | 42 | 0 |
| 6 | 1 | 56 | -1 |
| 7 | 0 | 48 | -1 |
| 8 | 1 | 84 | 0 |

In particular, the color-preserving subgroup \(W^+\) of order \(168\) has a one-dimensional invariant subspace in \(\widetilde H_2(X;\mathbb Q)\), while the full group has none. Each point–line duality reverses the unique \(W^+\)-invariant line.

## Assumptions and scope
All graph distances are shortest-path distances on the **21 flags**, not distances on the original 14-point incidence graph. The radius includes endpoints: pairs at distance exactly two are adjacent in the square graph. The Fano lines are explicitly \(\ell_i=\{i,i+1,i+3\}\) in \(\mathbb Z/7\mathbb Z\). The flag vertices are the incident pairs \((p,\ell_i)\) with \(p\in\ell_i\). Two flags are adjacent in \(G\) precisely if they share their point or their line. The theorem concerns only this finite order-two plane and the stated symmetry action; no claim is made for arbitrary projective planes or other radii.

## Proof
**Metric and simplex enumeration.** For distinct flags \((p,\ell)\) and \((q,m)\), a path of length at most two in \(G\) exists if and only if \(p\in m\) or \(q\in\ell\). Indeed a cross-incidence produces the intermediary flag \((p,m)\) or \((q,\ell)\), and any common intermediate flag forces one of the two cross-incidences (the distance-one cases are included). Therefore the squared graph can be constructed without an arbitrary shortest-path convention. An exhaustive increasing-vertex clique enumeration using these relations finds the nonempty face-count vector
\[
(f_0,f_1,f_2,f_3,f_4)=(21,126,238,105,21).
\]
There are exactly 77 maximal faces: 56 triangles and 21 five-vertex simplices, with no simplex of higher dimension. The checker reconstructs both the graph-square adjacency and its cross-incidence description independently before enumerating all 511 nonempty simplices.

**Homotopy type.** The accompanying `fano_matching_certificate.json` specifies 231 distinct pairs \((\sigma,\tau)\) of simplices, where each \(\sigma\) is a codimension-one face of \(\tau\). Every simplex occurs in one pair except one vertex and exactly 48 two-simplices. The standalone checker constructs **every** covering relation in the full nonempty face poset. It reverses the matching edges in the downward-oriented Hasse diagram and performs an exhaustive topological sort: all 511 face-poset vertices are removed, so the matching is acyclic. By the acyclic discrete-Morse matching theorem, \(X\) is homotopy equivalent to a CW complex with exactly one zero-cell, no one-cells, and 48 two-cells, and no cells in other positive dimensions. Every attaching map of a two-cell lands in the single zero-cell; the complex is therefore a wedge of 48 two-spheres. This is an integral homotopy conclusion, not an inference from finite-field Betti numbers.

**Automorphism group and character.** Every automorphism of the connected bipartite graph \(H\) either preserves both bipartitions or exchanges them. The point-preserving case is determined by a permutation of the seven points carrying the seven Fano lines to themselves. An exhaustive check of all 5040 point permutations yields 168 possibilities. A point–line polarity exists and is explicitly found by the checker, so composition yields the other 168 automorphisms. They induce 336 distinct permutations of the 21 flags.

For a simplicial automorphism \(g\), write \(\operatorname{sgn}(g|_\sigma)\) for the orientation sign of its permutation of a simplex \(\sigma\) that is fixed setwise. The simplicial Lefschetz identity gives
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(X;\mathbb Q)\bigr)
=\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma)-1.
\]
Here the subtraction of one removes the trace of \(H_0\), while the homotopy result proves that all other rational homology groups vanish. The checker evaluates this signed sum over all 511 simplices for each of the 336 induced automorphisms, computes its order and bipartition parity, and obtains the eight exhaustive rows displayed above. Finally, character averaging gives invariant dimensions \(168/168=1\) for \(W^+\), and \(0/336=0\) for \(W\). The nontrivial coset must consequently act by minus one on the \(W^+\)-invariant line.

## Verification
Run `python verify_fano_flag_rips.py` with `fano_matching_certificate.json` in the same directory; the script requires Python 3.9 or later and no nonstandard packages. It verifies the Fano incidence axioms, both definitions of the squared line graph, complete face and facet enumeration, an explicit matching partition, acyclicity of the entire directed Hasse diagram, and every group-element Lefschetz calculation. Independently of the Morse certificate, exact rank elimination over \(\mathbb F_2\) gives boundary ranks \((20,106,84,21)\) in dimensions one through four, consistent with the homotopy result. The emitted reference output is `verification_output.txt`.

## Relationship to prior work
Adamaszek, *Clique complexes and graph powers* (arXiv:1104.0433, publicly posted 2011-04-03), studies precisely the distance-power construction. Its Proposition 2.2 ensures collapse to the original graph under a **girth-at-least-seven** hypothesis for radius two; it cannot be applied to the present input \(G=L(H)\), which contains triangles. Section 5 relates \(\operatorname{Cl}(L(H))\) (radius one) to \(H\), and also treats the square of the *edge-subdivision graph* (the total graph), not the square of \(L(H)\).

Goyal, Shukla and Singh, *Topology of Clique Complexes of Line Graphs* (arXiv:2009.12130), prove \(\operatorname{Cl}(L(H))\simeq H\) in the triangle-free case; since \(H\) has graph-cycle rank eight, that earlier radius-one complex is a wedge of eight circles. Their full-text definition and theorems concern \(\operatorname{Cl}(L(H))\), not the radius-two graph power or its rational symmetry character. The 2009 paper by Larrión, Pizaña and Villarroel-Flores (*The fundamental group of the clique graph*, DOI:10.1016/j.ejc.2007.12.006) studies related graph/square fundamental-group comparisons, not the presently calculated higher-dimensional homotopy type and representation. The difference in the underlying simplicial complexes matters; shared words "line graph" or "square" do not imply an equivalent result.

## Limitations
This is a finite, explicitly certified calculation for the unique order-two projective plane. The group character is over \(\mathbb Q\); no integral decomposition of the 48-dimensional automorphism lattice is asserted. No generalization to arbitrary projective-plane orders or further Rips stages is proved. Literature and indexed-result searches found no equivalent statement for \(\operatorname{Cl}(L(H)^2)\), but unindexed equivalent work remains a bibliographic risk. No independent external scientific audit has been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (initial public posting 2011-04-03), Sections 2 and 5. https://arxiv.org/abs/1104.0433
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (initial public posting 2020-09-25), Sections 2–4. https://arxiv.org/abs/2009.12130
3. F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The fundamental group of the clique graph*, European Journal of Combinatorics 30 (2009), 288–294, DOI:10.1016/j.ejc.2007.12.006.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic-matching-to-CW principle).
