# Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types

## Finding
Let \(S\) be the Shrikhande graph and \(R\) the \(4\times4\) rook graph. Then
\[
\operatorname{Ind}(S)\simeq\bigvee^{23}S^2,\qquad
\operatorname{Ind}(R)\simeq\bigvee^{15}S^2.
\]
Thus \(\widetilde H_2(\operatorname{Ind}(S);\mathbb Z)\cong\mathbb Z^{23}\) and \(\widetilde H_2(\operatorname{Ind}(R);\mathbb Z)\cong\mathbb Z^{15}\), with every other reduced integral homology group zero. Both graphs have \(16\) vertices, valency \(6\), and exactly \(2\) common neighbors for every pair of distinct vertices, so the distinction is invisible to their strongly regular parameters and adjacency spectra.

## Assumptions and scope
These are finite, undirected, loopless simple graphs. For each \((i,j)\in(\mathbb Z/4\mathbb Z)^2\), label its vertex by the integer \(4i+j\) (with coordinate representatives \(0,1,2,3\)). In \(S\), the difference between adjacent vertices belongs to
\[
D=\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
For \(R\), two distinct vertices are adjacent exactly when their first or second coordinate agrees. For any graph \(G\), \(\operatorname{Ind}(G)\) has the independent vertex subsets as faces, including the empty face; we use its ordinary geometric realization and integral homotopy type. No claim is made for larger Doob, Hamming, or rook graph families.

## Proof
**Graph verification.** Construct the two explicit adjacency masks in `verify_twins.py`. Exhaustive loops check symmetry, zero diagonals, degree \(6\) at every vertex, and exactly two shared neighbors for each unordered pair. Consequently both presentations realize strongly regular graphs with parameters \((16,6,2,2)\). Their local neighborhoods are respectively a six-cycle and two disjoint triangles; the graphs are not isomorphic.

**Complete face enumeration.** Represent a vertex subset by a \(16\)-bit integer. Iterate all masks in the exact range \(0\le m<2^{16}\); a mask is retained if and only if it contains no adjacent vertex pair. The numbers of nonempty faces by dimensions \(0,1,2,3\) are
\[
(16,72,96,16)\quad\text{for }S,\qquad
(16,72,96,24)\quad\text{for }R.
\]
No higher-dimensional faces occur. The total numbers of nonempty simplices are \(200\) and \(208\), respectively. An independent vertex-deletion recurrence, \(I_G(t)=I_{G-v}(t)+tI_{G-N[v]}(t)\), checks the full independence polynomials
\[
I_S(t)=1+16t+72t^2+96t^3+16t^4,\quad
I_R(t)=1+16t+72t^2+96t^3+24t^4.
\]

**Explicit discrete-Morse matchings.** Discard only the empty face from the matching poset. For a specified ordered list of vertices, visit each vertex \(v\) in order. Among currently unmatched nonempty faces, traverse in ascending dimension and then ascending bit mask; whenever \(v\notin F\), and both \(F\) and \(F\cup\{v\}\) remain unmatched, pair those faces and remove both. The vertex order for \(S\) is \((0,1,\ldots,15)\). For \(R\) it is
\[
(7,9,5,6,14,10,12,8,1,2,13,15,4,11,0,3).
\]
This produces \(88\) face pairs for \(S\) and \(96\) for \(R\). The unmatched cells are exactly one vertex and \(23\) two-simplices for \(S\), and exactly one vertex and \(15\) two-simplices for \(R\).

**Exhaustive acyclicity certificate.** Form the directed Hasse diagram on all nonempty faces. For each codimension-one incidence \(F\subset F\cup\{v\}\), direct the arrow from the larger to the smaller face unless the incidence is matched, in which case reverse it. The implementation builds *every* such incidence: \(496\) arrows among \(200\) faces for \(S\), and \(528\) arrows among \(208\) faces for \(R\). Kahn's topological-sort algorithm removes all \(200\) and all \(208\) vertices, respectively, with no residual directed circuit. Thus the matchings are acyclic in Forman's sense. Both matchings exhaustively cover their respective face posets except for the stated critical cells.

**Homotopy deduction.** By the finite acyclic-matching theorem of discrete Morse theory, each independence complex is homotopy equivalent to a CW complex with exactly the indicated critical cells. Such a CW complex has one zero-cell, no one-cells, and respectively \(23\) or \(15\) two-cells, with no cells in other positive dimensions. All attaching maps are constant into the unique zero-cell, giving wedges of two-spheres with precisely those multiplicities. In particular, integral torsion and all higher attaching-map ambiguities are excluded by the actual CW structure, rather than inferred from field homology.

## Verification
Run `python3 verify_twins.py` and `python3 verify_independence_polynomials.py` with standard Python 3; there are no external software dependencies or data files. The first program independently checks the graph parameters, all faces, each pair, the full directed Hasse graph, and mod-two simplicial boundary ranks. Its terminal marker is `SHRIKHANDE_ROOK_INDEPENDENCE_VERIFY_OK`. The second computes independence polynomials by recursive vertex deletion and returns `POLYNOMIAL_RECURSION_OK`. In particular, both programs check the top-dimensional simplex counts by distinct methods.

## Relationship to prior work
Barmak's *Star clusters in independence complexes of graphs* (arXiv:1007.0418) provides the topological framework and studies chessboard/matching complexes and several global connectivity principles. Its triangle-free suspension theorem does not apply to \(S\), which has triangles. Its claw-free theorem does not apply to \(S\) either: every open neighborhood induces a six-cycle, containing three mutually nonadjacent vertices and hence an induced claw with its center. No asserted result there computes this graph's independence-complex homotopy type.

The rook graph is \(L(K_{4,4})\), so its independence complex is precisely the classical \(4\)-by-\(4\) chessboard complex; extensive earlier results concern that object, and this comparison does not present rook-topology computations as the novel half. Shareshian and Wachs's chessboard homology results concern that rook half and do not imply topology for \(S\). Earlier work by Bodnar and collaborators distinguishes the same strongly regular pair via **clique complexes of the original graphs**, whereas here \(\operatorname{Ind}(G)=\operatorname{Cl}(\overline G)\) is the clique complex of the **complement**, a different construction. Cioabă and coauthors' computed first homology for the Shrikhande *clique* complex is likewise not a computation of its independence complex. The present additional content is the explicit homotopy reduction of the Shrikhande independence complex and its precise comparison with the rook analogue.

## Limitations
The statement is finite and restricted to two graphs on \(16\) vertices; it asserts neither a classification of all strongly regular graphs nor a first-ever distinction of these already known nonisomorphic graphs. The source comparison does not rule out equivalent computations hidden in unindexed or unpublished literature. Computed mod-two homology is a cross-check, not the reason the integral homotopy type follows. No independent external mathematical review is claimed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2010), https://arxiv.org/abs/1007.0418. The publicly available first version lists primary MSC 57M15.
2. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, https://arxiv.org/abs/math/0409054.
3. C. Bodnar et al., *Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks* (2021), https://arxiv.org/abs/2103.03212; Figure 3 compares the same graphs' clique complexes.
4. S. M. Cioabă and coauthors, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328, https://arxiv.org/abs/2606.27328.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Standard acyclic matching theorem.
