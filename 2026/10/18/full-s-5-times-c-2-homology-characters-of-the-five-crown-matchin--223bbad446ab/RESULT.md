# Full \(S_5\times C_2\) homology characters of the five-crown matching complex

## Finding

Let \(H\) be the *five-crown graph* with bipartition \(\{u_1,\ldots,u_5\}\sqcup\{v_1,\ldots,v_5\}\), with an edge \(u_i v_j\) exactly when \(i\ne j\). Write \(K=\mathcal M(H)\) for its ordinary matching complex. Equivalently, \(K\) is the nonattacking-rook complex of the \(5\times5\) chessboard after deleting its main diagonal. Its full graph-automorphism group is \(G=S_5\times C_2\): the symmetric group relabels rows and columns simultaneously, and the generator \(\tau\) of \(C_2\) interchanges the bipartition, acting on rook squares by \((i,j)\mapsto(j,i)\).

Over the rational numbers, the only nonzero reduced homology is in degrees \(2\) and \(3\), and the **complete equivariant decomposition** is

\[
\widetilde H_2(K;\mathbb Q)\cong \mathbf1_{S_5}\boxtimes\varepsilon,
\qquad
\widetilde H_3(K;\mathbb Q)\cong
\bigl(S^{(4,1)}\oplus S^{(3,2)}\bigr)\boxtimes\mathbf1_{C_2}
\oplus S^{(2,1,1,1)}\boxtimes\varepsilon.
\]

Here \(S^\lambda\) is the rational Specht module of the partition \(\lambda\), \(\mathbf1\) is the trivial character, and \(\varepsilon(\tau)=-1\). Thus the second-homology generator is fixed by every simultaneous relabeling but negated by board transposition. In degree three, transposition has even and odd eigenspace dimensions \(9\) and \(4\), respectively. In particular, \(\widetilde H_i(K;\mathbb Q)^G=0\) for every \(i\).

The corresponding rational reduced Betti numbers are \(\widetilde\beta_2=1\), \(\widetilde\beta_3=13\), and zero otherwise. The non-equivariant degree-two rank was already tabulated by Björner--Welker and recorded in Shareshian--Wachs; the **new claim** is the complete joint permutation-and-transposition representation, not the previously recorded existence of degree-two homology.

## Assumptions and scope

All faces are *unoriented* partial injections \(f:I\hookrightarrow[5]\) with \(i\ne f(i)\) on their domain. An oriented face of size \(k\) is represented by its \(k\) rook squares ordered lexicographically by \((i,j)\). Boundary maps use the alternating deletion convention; group actions include the sign of the induced permutation of the oriented face. Homology coefficients for the representation theorem are \(\mathbb Q\). No assertion is made about an equivariant homotopy splitting or an integral lattice decomposition.

The graph automorphism group has order \(240\). Indeed, its two graph bipartition classes are intrinsic since the graph is connected and bipartite. An automorphism preserving those classes must use the same permutation on their five indices because the deleted perfect matching is intrinsic; every interchange automorphism is a preserving one composed with \(\tau\).

## Proof

**1. Exact rational Betti numbers.** The face numbers in dimensions \(-1,0,1,2,3,4\) are

\[
(1,20,130,320,265,44).
\]

They are obtained by enumerating all partial injections avoiding five diagonal cells; the accompanying verifier does this from the definition. The reduced simplicial boundary matrices from degrees \(1,2,3,4\) to the immediately lower degrees have rational ranks

\[
(19,111,208,44).
\]

Here is an independent, finite and exact justification, which does not assume that prime-field ranks automatically equal rational ranks. Elimination over \(\mathbb F_{101}\) gives these four numbers as lower bounds on rational ranks. The degree-one rank is at most \(20-1=19\) because column sums vanish; hence it is exactly \(19\). The degree-two rank is at most \(130-19=111\) by the chain-complex identity; hence it is exactly \(111\). The degree-four rank is at most \(44\), giving equality.

To bound the degree-three rank from above, let \(a_1,b_1,a_2,b_2,a_3,b_3\) be the six rook squares

\[
(1,2),(1,3),(2,4),(2,5),(3,1),(4,1).
\]

Each pair \(\{a_j,b_j\}\) consists of attacking squares, whereas choices from *different* pairs never attack. The join of the three oriented zero-spheres gives an integral simplicial two-cycle \(z\) with exactly eight nonzero oriented triangles. The accompanying `verify.py` uses zero-based rook coordinates, so these six squares there have coordinates \((0,1),(0,2),(1,3),(1,4),(2,0),(3,0)\). A companion exact file `cocycle.json` defines an integral two-cochain \(\phi\): its entries are pairs \((\text{triangle index},\pm1)\), using the lexicographically ordered triangle basis. The verifier checks, over the integers,

\[
\partial_2 z=0,\qquad \delta^2\phi=0,\qquad
\langle\phi,z\rangle=2.
\]

Thus \(z\) represents a nonzero rational second-homology class, since every rational boundary pairs to zero with \(\phi\). After the first two rank equalities, \(\ker\partial_2\) has dimension \(320-111=209\); the nonzero class therefore gives \(\operatorname{rank}_{\mathbb Q}\partial_3\le208\). The prime-field lower bound gives equality. This proves all four rational ranks, hence the displayed rational Betti numbers. Independent prime-field elimination over \(\mathbb F_3\) gives the same ranks, but is not used to infer characteristic-zero equality.

**2. Equivariant Lefschetz numbers.** For each \(g=(\sigma,\tau^t)\in G\), write \(T_j(g)\) for the signed trace on the simplicial \(j\)-chain group. A simplex contributes zero unless preserved setwise; when preserved, its contribution is the orientation sign of the induced permutation. Define

\[
L(g)=\sum_{j=0}^4(-1)^jT_j(g)-1.
\]

The final \(-1\) is the reduced degree-minus-one contribution. Since only degrees two and three have reduced rational homology, the Hopf--Lefschetz trace identity gives

\[
L(g)=\chi_2(g)-\chi_3(g).
\]

All signed traces are enumerated from the 20 rook-square vertices, for all \(120\cdot2=240\) group elements; they are independently checked to depend only on the seven cycle types of \(S_5\) and the transposition bit. For the seven cycle types in the order

\[
(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5),
\]

the trace values \(L(\sigma,1)\) (no transpose) are

\[
(-12,0,0,0,0,2,3),
\]

and the values \(L(\sigma,\tau)\) are

\[
(-6,-6,-2,0,0,0,-1).
\]

**3. Uniqueness of the one-dimensional character.** As \(\dim\widetilde H_2=1\), its rational character must be one of \(\mathbf1_{S_5}\boxtimes\mathbf1\), \(\mathbf1_{S_5}\boxtimes\varepsilon\), \(\operatorname{sgn}_{S_5}\boxtimes\mathbf1\), or \(\operatorname{sgn}_{S_5}\boxtimes\varepsilon\). For each of these four candidates, form \(\chi_3=\chi_2-L\) and take all rational inner products against the fourteen irreducible characters of \(S_5\times C_2\). Three candidates would give multiplicity \(-1\) for \(\mathbf1_{S_5}\boxtimes\varepsilon\), which is impossible for a representation. The remaining candidate is \(\mathbf1_{S_5}\boxtimes\varepsilon\), and then the only nonzero degree-three irreducible multiplicities are exactly one each for

\[
S^{(4,1)}\boxtimes\mathbf1,
\quad S^{(3,2)}\boxtimes\mathbf1,
\quad S^{(2,1,1,1)}\boxtimes\varepsilon.
\]

The verifier constructs all seven \(S_5\) irreducible characters from fixed-point and two-subset counts, the exterior-square formula and sign twisting, checks their weighted orthogonality, computes the fourteen inner products as exact integers, and confirms the unique nonnegative case. This completes the representation-theoretic proof.

## Verification

Run `python3 verify.py` from a directory containing `verify.py` and `cocycle.json` (Python 3 and NumPy are required). The script constructs all simplices and integer boundaries from scratch, checks consecutive boundary compositions, performs elimination modulo \(3\) and \(101\), checks the explicit integral cycle/cocycle pairing, and enumerates all \(240\) signed automorphism traces. The predicted representation characters are checked against all fourteen classes.

The completed verifier reports `VERIFY_OK CROWN_5 F_VECTOR_20_130_320_265_44 RANKS_19_111_208_44` and `GROUP_ORDER_240 H2_TRIVIAL_TIMES_TRANSPOSE_SIGN H3_4_PLUS_5_PLUS_4`. These finite calculations certify the stated finite matrix and character identities. The mathematical reasoning connecting them to rational homology and irreducible modules is given above.

## Relationship to prior work

Björner--Welker studied the chessboard after deleting its diagonal, and Shareshian--Wachs, Section 8 and Table 8.1, record that its degree-two integral homology at size five is \(\mathbb Z\). This agrees with (and is not claimed as) the new rank calculation. Friedman--Hanlon's representation decomposition treats the *full rectangular* chessboard complexes with the larger row-column permutation symmetry. Deleting the diagonal changes both the simplicial complex and the acting group; their formula does not imply the joint \(S_5\times C_2\) decomposition given here. Relevant close database records concern ordinary full chessboards, other graph matching complexes or different graph domination/cut complexes; none was found to state the present two-degree character. The comparison is by mathematical implication, not by terminology alone.

## Limitations

The theorem concerns the fixed five-crown graph and rational representations. It does not determine the integral \(G\)-module structure, any general \(n\)-crown character, or equivariant homotopy type. The finite computation is exhaustive only for this specified 20-vertex matching complex. A previously published equivalent character table outside the searched/indexed literature remains a residual novelty risk; database nonappearance is not a proof of priority.

## References

1. John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (first posted 2004-09-03), especially Section 8, Table 8.1, Theorem 8.3. https://arxiv.org/abs/math/0409054.
2. Anders Björner and Volkmar Welker, *Complexes of Directed Graphs*, SIAM J. Discrete Math. **12** (1999), 413--424, doi:10.1137/S0895480198338724. The relevant chessboard claim is also described in Reference 1.
3. Joel Friedman and Phil Hanlon, *On the Betti Numbers of Chessboard Complexes*, J. Algebraic Combin. **8** (1998), 193--203, doi:10.1023/A:1008693929682. Its ordinary rectangular-board scope is distinct.
4. Anders Björner, László Lovász, Siniša Vrećica and Rade Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. **49** (1994), 25--39, doi:10.1112/jlms/49.1.25.
