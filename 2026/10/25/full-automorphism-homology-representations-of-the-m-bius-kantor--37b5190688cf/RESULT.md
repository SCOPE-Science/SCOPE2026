# Full automorphism homology representations of the Möbius–Kantor independence complex

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph and \(X=\operatorname{Ind}(M)\) its ordinary independence complex. Put \(G=\operatorname{Aut}(M)\), of order \(96\). The graph has a central involution \(z\) that sends each index \(i\) to \(i+4\) modulo \(8\), both on the outer and inner eight-cycles. The quotient graph \(M/\langle z\rangle\) is the ordinary cube. Let \(\mathcal D\) be its four unordered pairs of antipodal vertices, and let \(\pi:G\to S_4\) be the induced permutation of \(\mathcal D\). Let \(b:G\to\{\pm1\}\) equal \(+1\) when an automorphism preserves the bipartition of \(M\), and \(-1\) when it exchanges the classes. Define \(\epsilon(g)=b(g)\operatorname{sgn}(\pi(g))\).

Then, as rational \(G\)-representations,
\[
\widetilde H_3(X;\mathbb Q)\cong
\mathbb Q[\mathcal D]\otimes\mathbb Q_{\epsilon},
\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbb Q_b,
\]
and all other reduced rational homology groups vanish. Equivalently, the **complete character formula**, for every \(g\in G\), is
\[
\operatorname{tr}(g\mid\widetilde H_3)=
 b(g)\operatorname{sgn}(\pi(g))\#\operatorname{Fix}_{\mathcal D}(\pi(g)),
\qquad
\operatorname{tr}(g\mid\widetilde H_4)=b(g).
\]
The joint map \(g\mapsto(\pi(g),b(g))\) is onto \(S_4\times C_2\) with kernel \(\{1,z\}\). Consequently the quotient by the full automorphism group is rationally acyclic; the quotient by \(\ker b\) has a unique reduced rational class in degree \(4\), and the quotient by \(\ker\epsilon\) has a unique reduced rational class in degree \(3\).

## Assumptions and scope
Use vertices \(u_i,v_i\), where \(i\in\mathbb Z/8\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\). The bipartition is
\[
 A=\{u_0,u_2,u_4,u_6,v_1,v_3,v_5,v_7\},\qquad
 B=\{u_1,u_3,u_5,u_7,v_0,v_2,v_4,v_6\}.
\]
The quotient graph under \(z(u_i)=u_{i+4}\) and \(z(v_i)=v_{i+4}\) has eight vertices and twelve edges and is isomorphic to the three-cube. The four antipodal pairs are defined intrinsically by cube distance three, so the character formula does not depend on a choice of labeling for them. The symbols \(\mathbb Q_b\) and \(\mathbb Q_\epsilon\) denote the one-dimensional rational characters defined above, while \(\mathbb Q[\mathcal D]\) is the four-dimensional permutation module. All homology and quotient statements in this finding use rational coefficients.

## Proof
**Homology concentration and a nonzero rational top class.** Direct reconstruction gives \(1{,}090\) nonempty simplices and the face vector \((16,96,272,376,240,72,16,2)\) in dimensions zero through seven. With the augmented degree-\(-1\) group included, Gaussian elimination over \(\mathbb F_{101}\) gives successive boundary ranks
\[
(1,15,81,191,181,58,14,2).
\]
The reduced mod-\(101\) Betti numbers are thus \(4\) in degree three and \(1\) in degree four, with zeros elsewhere. Reduction modulo a prime bounds each rational Betti number from above. To certify nonzero rational degree-four homology, construct, by sparse elimination on the degree-four simplicial boundary, an integral four-cycle \(c\) with exactly \(100\) nonzero oriented-simplex coefficients (fifty \(+1\) and fifty \(-1\)). Its integral boundary is directly zero. The exact rational boundary \(\partial_5\) has rank \(58\), while the matrix \([\partial_5\mid c]\) has rank \(59\); hence \([c]\ne0\) rationally. The reduced Euler characteristic from the face vector is \(-3\). Thus precisely
\[
\dim_{\mathbb Q}\widetilde H_3(X)=4,\qquad
\dim_{\mathbb Q}\widetilde H_4(X)=1,
\]
with no other reduced rational homology.

**The rank-one character.** Reconstructing all graph automorphisms gives exactly \(96\). For each, apply the oriented simplicial action to \(c\); its class modulo \(\operatorname{im}\partial_5\), computed over \(\mathbb F_{101}\), is \(b(g)[c]\). The rank of \(\partial_5\) is the same over \(\mathbb Q\) and \(\mathbb F_{101}\), and \(c\) is nonzero in both quotient homologies. Because each automorphism has finite order, its rational action on the one-dimensional \(\widetilde H_4\) is \(+1\) or \(-1\). The mod-\(101\) equality therefore distinguishes these two rational possibilities and proves \(\chi_4(g)=b(g)\) for all \(g\).

**The four-dimensional character.** For any \(g\), the signed fixed-simplex formula for the reduced Lefschetz number is
\[
\widetilde L(g)=-1+\sum_{\substack{\varnothing\ne F\in X\\gF=F}}
(-1)^{\dim F}\operatorname{sgn}(g\vert_F),
\]
where the last sign is computed from the induced permutation in increasing vertex order. Exhaustive exact evaluation of all \(96\) automorphisms gives
\[
\widetilde L(g)=b(g)-b(g)\operatorname{sgn}(\pi(g))
\#\operatorname{Fix}_{\mathcal D}(\pi(g)).
\]
Only degrees three and four have nonzero reduced homology, so \(\widetilde L(g)=\chi_4(g)-\chi_3(g)\). Substituting the known \(\chi_4\) proves the displayed formula for \(\chi_3\). The right-hand character is exactly that of the explicitly defined twisted permutation module. Semisimplicity of rational representations of finite groups therefore proves the claimed module isomorphism.

**Quotients.** Exhaustive graph-automorphism enumeration also verifies that every pair \((\sigma,t)\in S_4\times\{\pm1\}\) occurs exactly twice as \((\pi(g),b(g))\). The invariants of the full group in both modules are zero. Under \(\ker b\), the top line is trivial and the degree-three module becomes the sign-twisted four-point permutation module, with no invariants. Under \(\ker\epsilon\), the degree-three module becomes the ordinary transitive four-point permutation module, with a one-dimensional invariant, whereas the top line has no invariants. For a finite simplicial group action, barycentric subdivision and averaging over \(\mathbb Q\) identify quotient rational homology with invariants. This yields all three quotient assertions.

## Verification
Run `python verify.py` with Python 3, NetworkX and SymPy. The verifier reconstructs the graph, its independent simplices, exact oriented boundary columns, all \(96\) automorphisms and the cube quotient. It computes all mod-\(101\) boundary ranks; produces and integrally checks the sparse degree-four cycle; verifies the two exact rational matrix ranks; checks the induced top action on that nonzero cycle and the signed Lefschetz identity for every automorphism; verifies that the action on four cube diagonals together with bipartition parity is onto \(S_4\times C_2\); and checks the three invariant-subspace dimensions. Successful completion prints `MK_FULL_AUTOMORPHISM_CHARACTER_VERIFIED`. Mod-prime computations alone are not used as a rational nonboundary proof: the two exact rational ranks supply that step. The stated representation concerns rational, not integral equivariant, homology.

## Relationship to prior work
Bıyıkoğlu and Civan's earlier calculation gives the underlying nonequivariant homotopy type \(\operatorname{Ind}(M)\simeq\bigvee^4 S^3\vee S^4\), not its automorphism action. Berghoff's work develops general techniques for homology of independence complexes but does not classify this example's full graph-automorphism module. A previously published calculation of the natural order-eight rotation on this same independence complex determines only the restriction to a cyclic subgroup; that restriction cannot determine the joint \(96\)-element character. A separate study of Lefschetz numbers of the Möbius–Kantor *graph itself* treats the graph as a one-dimensional complex, not its higher-dimensional independence complex. The present statement isolates the previously undetermined full rational symmetry module and its quotient consequences.

## Limitations
The assertion is for the specific sixteen-vertex graph, with rational homology only; it neither classifies a generalized Petersen graph family nor proves integral equivariant module decomposition. The irreducible decomposition is expressed as a natural twisted permutation representation instead of by a presentation of every irreducible of the abstract automorphism group. Exact finite enumeration is a proof of this finite claim, not an extrapolation. An equivalent unindexed calculation could exist; the available full text of the 2015 preprint and the closest full published results were compared, but the corresponding 2019 publisher-hosted article was not fully readable. No independent mathematical audit has been performed.

## References
1. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267v1 (first public 2020-08-14); later *Combinatorial Theory* 2 (2022), DOI:10.5070/C62156880; primary MSC2020 55U10.
2. T. Bıyıkoğlu and Y. Civan, *Castelnuovo-Mumford regularity of graphs*, arXiv:1503.06018v1 (first public 2015-03-20), Example 3.9.
3. T. Bıyıkoğlu and Y. Civan, *Prime graphs, matchings and the Castelnuovo-Mumford regularity*, *Journal of Commutative Algebra* 11 (2019), DOI:10.1216/JCA-2019-11-1-1.
4. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799v1 (first public 2026-05-29); graph-level, rather than independence-complex, Lefschetz numbers.
