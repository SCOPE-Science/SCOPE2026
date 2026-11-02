# A Möbius–annulus parity law for two-defect token-sliding complexes of cycle powers

## Finding
Let \(k\ge2\), \(m\ge2\), \(q=k+1\), and \(n=qm+2\). Let \(G=C_n^k\), the graph on \(\mathbb Z/n\mathbb Z\) joining distinct vertices at circular distance at most \(k\). Form \(\mathcal R\) from all maximum independent sets of \(G\): two sets are adjacent if one token moves along an edge of \(G\) while the set remains independent. Form a two-dimensional polygonal cell complex \(X\) by attaching a separate closed 2-cell along **each** graph-theoretic triangle and each simple four-cycle of \(\mathcal R\).

**Theorem.** The graph \(\mathcal R\) is connected and 4-regular, with
\[
 |V(\mathcal R)|=\frac{n(m+1)}2,\qquad |E(\mathcal R)|=n(m+1),
 \qquad N_3=n,\qquad N_4=\frac{n(m-1)}2,
\]
where \(N_j\) is the number of undirected simple \(j\)-cycles (not merely a chosen face set). The attached complex \(X\) is a compact connected surface with boundary and Euler characteristic zero. Its boundary is a disjoint union of \(\gcd(2,q)\) cycles, each of length \(n/\gcd(2,q)\). Thus \(X\) is a Möbius band for even \(k\) and an annulus for odd \(k\). In particular the topology changes with the parity of the separation threshold, while the cell counts have uniform formulas.

## Assumptions and scope
All vertices of the underlying cycle are individually labelled; all independent sets are unordered vertex subsets. There are exactly \(m\) selected vertices, and the extra cyclic spacing beyond the mandatory separation \(q\) is exactly two. Both one- and two-position moves are permitted because \(k\ge2\), but no valid move may travel farther than two positions in either cyclic direction. Distinct simple three- and four-cycles give distinct polygonal 2-cells even if their boundaries have common edges. The theorem is for every integer \(k,m\ge2\), not an extrapolation from finite experiments.

## Proof
**1. Gap encoding and exhaustive moves.** List a maximum independent set as \(x_0<x_1<\cdots <x_{m-1}<x_0+n\) on the lifted circle. Its cyclic gaps are \(x_{i+1}-x_i=q+s_i\), with indices modulo \(m\), \(s_i\ge0\), and \(\sum_i s_i=2\). The independence number is exactly \(m\): every pair of successive tokens requires a gap of at least \(q\), and the displayed construction attains \(m\). Every configuration therefore has either one gap containing two excess positions (type A) or two gaps each containing one (type B). Moving a token clockwise by \(d\) subtracts \(d\) from the following excess gap and adds \(d\) to the preceding one; counterclockwise movement reverses this transfer. Since the total excess is two, only \(d=1,2\) can occur, and every such transfer is a legal slide along an edge of \(C_n^k\). Each type A state has two unit-transfer and two double-transfer neighbors. Each type B state has four unit-transfer neighbors. These are distinct, so the graph is 4-regular.

**2. Exact state count.** For a choice of distinguished first token there are \(n\binom{m+1}{2}\) cyclic excess-gap lists, obtained by placing two indistinguishable excess units in \(m\) gaps. Every unordered token set is represented exactly \(m\) times. Hence \(|V|=n(m+1)/2\). Exactly one long gap can occur in a type A state. Its preceding token may be any \(x\in\mathbb Z/n\mathbb Z\), uniquely determining that state, denoted \(A_x\). Thus there are \(n\) type A states and \(n(m-1)/2\) type B states.

**3. Exhaustive local short-cycle check.** This is a finite *symbolic* case analysis valid for every \(m\). Write \((i,i)\) for both excess units in gap \(i\) and \((i,j)\), \(i\ne j\), for separated units; indices are cyclic gap labels, not fixed physical sites. A unit move transports one excess unit to a neighboring gap; a double move transports both together and is possible only at \((i,i)\). A simple triangle must use one double move and two unit moves: it is precisely \((i,i)\leftrightarrow(i,i+1)\leftrightarrow(i+1,i+1)\leftrightarrow(i,i)\). If no double move occurs, the unit-transfer graph has no triangles (every step changes the parity of the sum of lifted token positions). For a four-cycle, canceling the net changes of two excess units shows that it is precisely a commuting pair of unit transfers (possibly with a boundary coalescence), with no additional four-cycles involving double moves. This last statement also follows by checking the four possible directions of transfer for each of the two excess units: a return in four moves cannot include a double transfer without either repeating a vertex or closing the three-cycle just described. The complete local incidence table for *all* triangles and four-cycles is:

| State type | Neighbor count | Triangles at state | Four-cycles at state | Link in polygonal complex |
|---|---:|---:|---:|---|
| A, any \(m\ge2\) | 4 | 2 | 1 | Path on four vertices |
| B, \(m=2\) | 4 | 2 | 2 | Circle on four vertices |
| B, \(m\ge3\), occupied gaps cyclically adjacent | 4 | 1 | 3 | Circle on four vertices |
| B, \(m\ge4\), occupied gaps nonadjacent | 4 | 0 | 4 | Circle on four vertices |

To reconstruct the links, order the four neighbors of a type B state by moving the first excess unit left/right and the second excess unit left/right; consecutive directions close the four elementary faces, except that when gaps are adjacent a coalescence changes one square into a triangle. For type A, the two double moves and two unit moves have consecutive links from two triangles and one square, leaving the edge between the two double-move neighbors absent from the link. For \(m=2\), both cyclic directions lead to the same other gap but distinct physical token moves; the separate row avoids double-counting their two triangles. Each elementary face uses distinct vertices. The same transfer-direction check shows every graph edge belongs to exactly two polygonal faces, except the double-transfer edges connecting two type A states, each of which belongs to exactly one triangle. Thus all local vertex links are circles (B) or intervals (A): \(X\) is a 2-manifold with boundary.

**4. Short-cycle and Euler counts.** Every triangle contains exactly two A states, while each A state belongs to two triangles. Therefore \(N_3=n\). The total graph edge count is \(2|V|=n(m+1)\). There are exactly \(n\) boundary edges by the preceding link check. Counting the total incidences of polygon edges gives \(3N_3+4N_4=2|E|-n\), so \(N_4=n(m-1)/2\) and
\[
 \chi(X)=|V|-|E|+N_3+N_4=0.
\]

**5. Boundary, connectedness, and surface type.** The type A states are \(A_x\) as in step 2. Their sole mutual edges are \(A_xA_{x+q}\) and \(A_xA_{x-q}\), obtained by moving either token bordering the long gap by two positions. Thus the entire boundary is the step-\(q\) graph on \(\mathbb Z/n\mathbb Z\); it consists of \(\gcd(n,q)=\gcd(2,q)\) cycles of equal length. The full reconfiguration graph is connected: unit transfers can first gather the two excess units into one gap. To connect any two A states, transport *one* of the two excess units once around all \(m\) gaps using successive unit transfers, keeping the other in place; each token advances once, transforming \(A_x\) into \(A_{x+1}\). Repeating this connects the A states, hence all configurations. A compact connected surface of Euler characteristic zero with one boundary component is a Möbius band; one with two boundary components is an annulus, by classification of compact surfaces. Since \(q=k+1\), these cases correspond respectively to even and odd \(k\).

## Verification
Two independent finite-state programs accompany this statement. `verify_direct.py` directly enumerates independent vertex subsets of the actual power graph, constructs token-sliding adjacency using every underlying graph edge, enumerates every triangle and simple four-cycle, checks every vertex link and boundary component, and checks connectedness. `verify_gaps.py` generates configurations independently from excess-gap compositions and reconstructs slides by gap transfers, verifying the local incidence table and the exact boundary successor \(x\mapsto x\pm q\). The programs check multiple values of \(k\) and \(m\), including both parities and all boundary cases. These checks do not replace the symbolic all-parameter proof.

## Relationship to prior work
The definition of token sliding and the reachability framework are classical; Bonsma, Kamiński and Wrochna studied claw-free graphs in their preprint of March 3, 2014. Avis and Hoang later investigated structural properties of independent-set token-sliding graphs, including explicit girth results for ordinary cycles. The present family concerns **powers** of cycles at exactly two spare positions, and the new invariant is the surface obtained by filling *all* short cycles. An ordinary-cycle theorem cannot imply this parity-dependent surface calculation: for ordinary cycles, two-position token slides are not edges. The parameter restriction is motivated by the two-defect (first nontrivial interacting-vacancy) sector of the close-packed exclusion system, rather than a prescribed small numerical example.

## Limitations
The theorem does not treat arbitrary numbers of excess positions, the \(k=1\) case (where two-position moves are forbidden), or all independent-set sizes. The square–triangle filling is a specific combinatorial 2-complex, not the clique complex of the graph. The novelty comparison is based on the inspected accessible literature and mathematical-record searches; unindexed equivalent descriptions from exclusion processes or configuration-space topology remain a residual risk. No independent scholarly audit has been performed.

## References
- P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359, initial public version 2014-03-03, https://arxiv.org/abs/1403.0359.
- D. Avis, D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, initial public version 2022-03-31, https://arxiv.org/abs/2203.16861.
- E. D. Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576, initial public version 2014-06-25, https://arxiv.org/abs/1406.6576.
