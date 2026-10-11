# Two-particle Petersen configuration homology as an \(S_5\)-module

## Finding

For the Petersen graph \(P=KG(5,2)\) and its unordered two-point configuration space \(B_2(P)\), \(H_1(B_2(P);\mathbb Z)\cong\mathbb Z^6\oplus\mathbb Z/2\) and \(H_2(B_2(P);\mathbb Z)\cong\mathbb Z^5\), with no higher homology. Under \(\operatorname{Aut}(P)\cong S_5\), the rational homology modules are \(H_1(B_2(P);\mathbb Q)\cong S^{(3,1,1)}\) and \(H_2(B_2(P);\mathbb Q)\cong S^{(2,2,1)}\); their characters on cycle types \(1,(2),(2,2),(3),(4),(5),(3,2)\) are respectively \((6,0,-2,0,0,1,0)\) and \((5,-1,1,-1,1,0,-1)\).

The unique order-two torsion summand in \(H_1(B_2(P);\mathbb Z)\) is fixed by every graph automorphism, because \(\operatorname{Aut}(\mathbb Z/2)\) is trivial.

## Assumptions and scope

The Petersen graph is realized as the Kneser graph \(KG(5,2)\): its ten vertices are the two-element subsets of a five-element set, and two vertices are adjacent exactly when the corresponding subsets are disjoint. The unordered configuration space \(B_2(P)\) consists of two distinct, unlabeled points moving on the geometric realization of \(P\).

For two particles the Petersen graph satisfies the standard sufficient-subdivision criterion for Abrams' discrete configuration model: distinct essential vertices are separated by at least one edge, and every nontrivial cycle has length at least three (in fact the girth is five). Hence the unordered discrete configuration complex \(UD_2(P)\) is a deformation retract of \(B_2(P)\).

No statement is made for three or more particles, for ordered configurations, or for integral decomposition of the free homology as a \(\mathbb Z[S_5]\)-module.

## Proof

The cells of \(UD_2(P)\) are pairs of mutually disjoint open cells of \(P\). There are \(45\) zero-cells (unordered pairs of distinct graph vertices), \(120\) one-cells (an oriented graph edge together with a vertex not incident to it), and \(75\) two-cells (unordered pairs of vertex-disjoint graph edges). With lexicographic orientations this gives a cellular chain complex
\[
0\longrightarrow \mathbb Z^{75}\xrightarrow{\partial_2}\mathbb Z^{120}\xrightarrow{\partial_1}\mathbb Z^{45}\longrightarrow0.
\]
The supplied verifier reconstructs every cell and every signed boundary and checks \(\partial_1\partial_2=0\).

The one-skeleton is connected. A deterministic spanning tree uses \(44\) one-cells, so the remaining \(76\) chord coordinates identify \(\ker(\partial_1)\) with \(\mathbb Z^{76}\). In those coordinates \(\partial_2\) is a \(76\times75\) integer matrix \(M\). A displayed certificate selects a \(70\times70\) minor with determinant of absolute value \(2\), while exact elimination modulo \(2\) gives rank \(69\) and modulo \(3\) gives rank \(70\). Consequently \(M\) has rational rank \(70\), and every maximal minor is even while one has determinant \(\pm2\); its top determinantal divisor is therefore \(2\). Thus the nonzero Smith factors are \(69\) copies of \(1\) and one copy of \(2\), giving
\[
H_1(B_2(P);\mathbb Z)\cong \mathbb Z^6\oplus\mathbb Z/2.
\]
An explicit \(75\times5\) integer matrix in the certificate lies in \(\ker(\partial_2)\); a selected \(5\times5\) row minor has determinant \(-1\). These five cycles are independent. Together with the rank-
\(70\) lower bound above they force \(\ker(\partial_2)\cong\mathbb Z^5\), so
\[
H_2(B_2(P);\mathbb Z)\cong\mathbb Z^5.
\]
There are no cells above dimension two.

The natural permutation of the underlying five-element set gives an action of \(S_5\) on \(KG(5,2)\). Conversely, the complement of \(P\) is the line graph of \(K_5\); its five maximal four-cliques are exactly the five stars of \(K_5\), so every automorphism permutes these five cliques faithfully. Hence \(\operatorname{Aut}(P)\cong S_5\).

For each of all \(120\) elements of \(S_5\), the verifier acts on the oriented cellular chains and on the explicit integral basis of \(H_2\). The resulting \(H_2\)-trace is computed directly. The \(H_1\)-trace then follows from the Hopf trace identity
\[
\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2)
=1-\operatorname{tr}(g\mid H_1)+\operatorname{tr}(g\mid H_2).
\]
On the cycle types \(1,(2),(2,2),(3),(4),(5),(3,2)\), this gives the two characters
\[
(6,0,-2,0,0,1,0),\qquad (5,-1,1,-1,1,0,-1).
\]
Their character inner products with themselves are one and with each other are zero. Comparison with the standard rational character table of \(S_5\) identifies them as \(S^{(3,1,1)}\) and \(S^{(2,2,1)}\), respectively.

## Verification

Run `python3 verification.py` beside `verification_certificate.json`. It reconstructs the Petersen graph and \(UD_2(P)\), all boundary maps, the spanning-tree presentation, the certified determinant, modular ranks, the five integral two-cycles, the five maximal four-cliques proving the automorphism-group identification, and all \(120\) symmetry actions. A successful replay ends with `VERIFY_OK`.

The determinant and modular-rank checks are exact integer calculations; the representation check uses exact rational arithmetic. No numerical approximation or probabilistic computation enters the claim.

## Relationship to prior work

An and Knudsen develop second homology of graph configuration spaces and emphasize that systematic unstable homology remains sparse. Their main theorem treats planar graphs, while their introduction explicitly asks what additional generators are required for non-planar graphs; the Petersen graph is non-planar, so that theorem does not imply the result here. Their paper also uses the general Świątkowski model, which supplies context but no Petersen-specific homology or \(S_5\)-module calculation.

General results of Ko and Park on first homology of graph braid groups can cover the nonequivariant abelian-group aspect of \(H_1\) in broad families; accordingly, the novelty claim here is not that a rank/torsion formula for first homology exists in isolation. The new statement assessed here is the combined exact two-particle Petersen calculation through degree two together with the full rational \(S_5\)-module decomposition. Targeted searches for the Petersen configuration space, the two Specht labels, and automorphism-representation formulations did not locate a published statement with these characters.

The nearest published database findings found by semantic search concern different functors on the Petersen graph (matching, Morse, and cut complexes) or three-particle configuration homology of generalized theta graphs; none implies the two-particle Petersen configuration-space representation.

## Limitations

The calculation is specific to two unordered particles on the Petersen graph. It does not determine the ring structure, graph-braid fundamental group, integral extension data beyond the displayed abelian groups, or configuration spaces with more particles. Search-based originality evidence is necessarily incomplete; a specialized unindexed computation could exist, although no decisive covering source was found in the inspected literature and database searches.

## References

1. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, first public 2020-08-24.
2. B. H. An, G. C. Drummond-Cole, and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351.
3. T. Maciążek, *Non-abelian quantum statistics on graphs*, Communications in Mathematical Physics 375 (2020), 743–769, DOI 10.1007/s00220-019-03583-5.
4. D. R. Wood, *Proof Without Words: The Automorphism Group of the Petersen Graph Is Isomorphic to \(S_5\)*, Mathematics Magazine 90 (2017).
5. GroupNames, *Character table of \(S_5\)*, consulted for the irreducible-character labels.
