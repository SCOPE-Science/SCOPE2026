# The full symmetric-group homology character of three unordered particles on the Petersen graph

## Finding

Write \(P=\mathrm{KG}(5,2)\) for the Petersen graph, whose ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), adjacent exactly when disjoint. The automorphism group \(\mathfrak S_5\) acts by permuting the five coordinates. Let \(B_3(P)\) denote the unordered configuration space of three distinct points of its geometric realization.

As rational \(\mathfrak S_5\)-modules,
\[
H_1(B_3(P);\mathbb Q)\cong S^{(3,1,1)},\qquad
H_2(B_3(P);\mathbb Q)\cong S^{(2,1,1,1)}\oplus2S^{(2,2,1)}\oplus S^{(3,1,1)}\oplus S^{(3,2)}.
\]
Here \(S^\lambda\) is the rational Specht representation indexed by the partition \(\lambda\) of five. In addition, \(H_0\cong\mathbb Q\) is trivial and \(H_j=0\) for \(j\ge3\). In particular, the Betti numbers are \((1,6,25)\). Neither \(H_1\) nor \(H_2\) has an invariant vector under the full automorphism group, so \(B_3(P)/\mathfrak S_5\) has no positive-degree rational homology.

In cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the complete degree-two character is
\[
\chi_2=(25,-3,1,-2,0,1,0).
\]

## Assumptions and scope

The graph is the standard ten-vertex, fifteen-edge Petersen graph; configurations are unordered, with collisions forbidden, and coefficients are rational. The \(\mathfrak S_5\) action is induced by graph automorphisms, not by permutation of particles. The asserted module decomposition is over \(\mathbb Q\). No integral decomposition, torsion classification, or other particle number is asserted.

## Proof

Use the reduced Świątkowski chain model for graph-configuration homology (References 2 and 3). For each trivalent vertex \(v\), let \(A_v\) be the rank-two augmentation lattice on its three incident half-edges. Let \(R=\mathbb Z[x_e:e\in E(P)]\), where each edge variable has weight one and homological degree zero. The reduced model is the weight-graded complex
\[
\widetilde S(P)=R\otimes\bigotimes_{v\in V(P)}(\mathbb Z\oplus A_v),\qquad
\partial(h-h_0)=x_{e(h)}-x_{e(h_0)}.
\]
Elements of \(A_v\) have homological degree and weight one, the differentials extend by the usual alternating Leibniz rule, and distinct vertex factors appear at most once. At weight three, the chain dimensions \(\dim C_j\) for \(j=0,1,2,3\) are \((680,2400,2700,960)\); there are no higher chain groups.

The standalone integer-matrix construction and exact prime-field eliminations in `verify_petersen_three.py` yield boundary ranks \((679,1715,960)\) modulo each of \(3,5,7\); modulo two the ranks are \((679,1714,960)\). They verify both boundary compositions vanish. To turn these finite-field lower bounds into rational *equalities*, observe first that \(\partial_1\) has rank at most \(680-1=679\) because its image is in the augmentation kernel, and \(\partial_3\) has rank at most \(\dim C_3=960\). Thus their rational ranks equal 679 and 960.

For \(\partial_2\), the lower bound is 1715. There is a natural map from unordered particle-configuration one-cycles to the graph cycle lattice, recording the sum of the particles' motions. For each embedded five-cycle in the Petersen graph, park two particles at vertices outside that cycle and move the third particle once around it: this realizes the given graph cycle. The twelve distinct graph five-cycles span the six-dimensional rational graph cycle space, as verified by a rank-six finite-field calculation; since its rank cannot exceed \(15-10+1=6\), this also proves rational spanning. Thus \(\dim H_1(B_3(P);\mathbb Q)\ge6\), forcing \(\mathrm{rank}_\mathbb Q(\partial_2)\le2400-679-6=1715\). Equality follows. Consequently, \(\dim H_1=6\), \(\dim H_2=2700-1715-960=25\), and \(H_3=0\).

The sum-of-motions map onto \(H_1(P;\mathbb Q)\) is equivariant, and equality of dimensions makes it an isomorphism. With orientations chosen for graph edges, its character is
\[
\chi_1(g)=1-\#\mathrm{Fix}_V(g)+\sum_{e\,\mathrm{setwise\ fixed}}\mathrm{orientation\_sign}(g|_e).
\]
In the indicated seven cycle-type order this equals \((6,0,-2,0,0,0,1)\), the character of \(S^{(3,1,1)}\).

The alternating trace of the reduced chain complex is the graded Lefschetz character \(L(g)=1-\chi_1(g)+\chi_2(g)\). It can be computed two independent ways: directly by the signed action on each of the 6,740 chain basis elements, and from the orbit generating function
\[
L(g)=[t^3]\,\frac{\prod_{O\in V(P)/\langle g\rangle}(1-\alpha_Ot^{|O|})}{\prod_{F\in E(P)/\langle g\rangle}(1-t^{|F|})},
\qquad \alpha_O=\operatorname{tr}\big(g^{|O|}\mid A_v\big)
=\#\mathrm{Fix}\big(g^{|O|}\mid H(v)\big)-1
\]
for any \(v\) in the vertex orbit \(O\). The directly computed values of \(L\) are \((20,-2,4,-1,1,2,0)\). Hence \(\chi_2=L-1+\chi_1=(25,-3,1,-2,0,1,0)\). Applying character orthogonality and the Murnaghan–Nakayama rule to the seven conjugacy classes gives multiplicities one for \(S^{(2,1,1,1)}\), two for \(S^{(2,2,1)}\), one for \(S^{(3,1,1)}\), and one for \(S^{(3,2)}\), zero for the other irreducibles. Their dimensions add to 25. The trivial representation does not appear in either positive degree. Finally, finite-group averaging identifies the rational homology of the orbit space with the invariants, proving the quotient statement.

## Verification

Run `python3 verify_petersen_three.py` using Python 3's standard library, with no external packages. It constructs the reduced chain matrices from the graph definition, proves \(\partial^2=0\) by exact integer arithmetic, checks ranks in four characteristics, enumerates every five-cycle and its cycle-space rank, computes all seven \(\mathfrak S_5\) conjugacy-class traces directly and via the independent orbit formula, and decomposes the character using exact integer character arithmetic. The checked output is embedded in `verification_output.txt`; the final line is `VERIFY_OK`.

## Relationship to prior work

Ko and Park (2011, Reference 1) determine general first homology for graph braid groups, consistent with the six-dimensional rational first homology here. The reduced Świątkowski model and graph-configuration homological methods are established in References 2 and 3 and are used here, not claimed as new. Maciążek and Sawicki (2019, Reference 3) also present nonequivariant degree-two and degree-three homology data for graphs in the Petersen family; no novelty is claimed for a tabulated Betti number. The contribution here is instead the complete natural \(\mathfrak S_5\)-representation on degree-two rational homology, including the absence of invariants, for three unordered particles. Two-particle Petersen representations do not determine this different particle-weight case.

## Limitations

The proof determines rational representations and dimensions, not the integral homology groups or the torsion action. The 2019 Petersen-family table was examined through the available article text and table context; some tabular entries were not extractable as text. Although the literature comparison revealed no equivalent equivariant three-particle result, unindexed or inaccessible equivalents are possible. Independent mathematical validation has not been performed.

## References

1. Ki Hyoung Ko and Hyo Won Park, *Characteristics of graph braid groups*, first made public January 13, 2011, https://arxiv.org/abs/1101.2648.
2. Byung Hee An, Gabriel C. Drummond-Cole, Ben Knudsen, *Subdivisional spaces and graph braid groups*, 2019, https://doi.org/10.4171/DM/709.
3. Tomasz Maciążek and Adam Sawicki, *Non-abelian quantum statistics on graphs*, Communications in Mathematical Physics (2019), https://doi.org/10.1007/s00220-019-03583-5, Sections 4 and 5 and Table 2.
