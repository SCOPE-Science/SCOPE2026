# Complete dihedral rational homology representations of odd Möbius-ladder perfect-matching complexes

## Finding

For every **odd integer** \(n\ge3\), define the Möbius ladder \(M_{2n}\) on \(\mathbb Z/(2n)\) with rim edges \(e_i=\{i,i+1\}\), indexed modulo \(2n\), and antipodal spokes \(\{i,i+n\}\). Let \(X_n=\mathcal M_p(M_{2n})\) be the simplicial complex of all graph matchings extendible to a perfect matching. The full natural dihedral group \(G=D_{2n}\) acts on its vertices (graph edges) through
\[
r(i)=i+1,\quad s(i)=-i,\qquad r^{2n}=s^2=1,\quad srs=r^{-1}.
\]
Write \(d=\lfloor(n+1)/3\rfloor\), and let \(H=\langle a,b\rangle\le G\) with \(a=r^2\), \(b=rs\). This is an index-two dihedral subgroup of order \(2n\). If \(W_n=\widetilde H_{d-1}(\operatorname{Ind}(C_n);\mathbb Q)\), with the natural \(H\)-action on the alternating rim-edge cycle described below, then
\[
\widetilde H_i(X_n;\mathbb Q)\cong
\begin{cases}
\operatorname{Ind}_H^G W_n,&i=d,\\
0,&i\ne d.
\end{cases}
\]
The \(H\)-representation \(W_n\) is explicitly as follows:

* For \(n=6k+1\), \(k\ge1\), it is a line with \(a\mapsto 1\) and \(b\mapsto(-1)^k\).
* For \(n=6k+5\), \(k\ge0\), it is a line with \(a\mapsto 1\) and \(b\mapsto(-1)^{k+1}\).
* For \(n=6k+3\), \(k\ge0\), it is the two-dimensional standard rational representation of \(D_3\), inflated along \(H\twoheadrightarrow D_3\) sending \(a\) to a threefold rotation and \(b\) to a reflection. In this description \(W_n\) has trace \(2\) on powers \(a^j\) with \(3\mid j\), trace \(-1\) on other powers, and trace \(0\) on all reflections.

Equivalently, define integers \(p_0=1\), \(p_1=0\), and \(p_m=p_{m-1}-p_{m-2}\) for \(m\ge2\). The **complete** character \(\chi_n=\operatorname{tr}(-\mid\widetilde H_d(X_n;\mathbb Q))\) on the full group is
\[
\chi_n(r^j)=
\begin{cases}
0,&j\text{ odd},\\
2,&j\text{ even and }3\nmid n,\\
4,&3\mid n\text{ and }6\mid j,\\
-2,&3\mid n,\ j\text{ even},\ 6\nmid j,
\end{cases}
\]
\[
\chi_n(r^j s)=
\begin{cases}
0,&j\text{ even},\\
2(-1)^d\,p_{(n-1)/2},&j\text{ odd}.
\end{cases}
\]
All exponents are interpreted modulo \(2n\). Thus the homology rank is \(2\) if \(3\nmid n\), and \(4\) if \(3\mid n\).

## Assumptions and scope

The graph is simple and finite, \(n\) is **odd and at least three**, all homology is reduced simplicial homology with \(\mathbb Q\)-coefficients, and an empty simplex contributes in the usual degree-minus-one augmented chain convention. An edge collection in \(X_n\) must **extend to a perfect matching**; it is not the ordinary matching complex. Let \(P_0\) and \(P_1\) be the full simplices spanned respectively by the alternating rim perfect matchings \(\{e_0,e_2,\ldots,e_{2n-2}\}\) and \(\{e_1,e_3,\ldots,e_{2n-1}\}\). The stabilizer of each \(P_i\) is precisely \(H\); rotation \(r\) exchanges them. On the rim-edge labels, \(a(e_i)=e_{i+2}\) and \(b(e_i)=e_{-i}\). Within either alternating matching the forbidden-edge-pair graph is the \(n\)-cycle with adjacency differences \(n-1\) and \(n+1\) modulo \(2n\), equivalent to the usual \(C_n\).

## Proof

**1. Equivariant decomposition and vanishing central piece.** Call two distinct edges incompatible if they share a graph vertex, or if they are both rim edges \(e_i,e_j\) with \(j-i\equiv n-1\) or \(n+1\pmod{2n}\). Let \(U_n\) be the independence complex of this incompatibility graph. This definition is manifestly invariant under \(G\). The matching-extension analysis for odd Möbius ladders in Agarwal–Basak [1, Theorem 21 and Lemmas 16–20] gives, as an **equality of simplicial subcomplexes**,
\[
X_n=U_n\cup P_0\cup P_1,\qquad U_n\simeq *,\qquad U_n\cap P_i\cong\operatorname{Ind}(C_n).
\]
For clarity, the source proof uses a graph-folding reduction on the incompatibility graph. Opposite rim-edge vertices have identical open neighborhoods; folding these yields a triangular-path graph with one additional vertex. Deleting that vertex and its closed neighborhood produces the two graphs denoted \(H_n\) and \(H_{n-2}\) in [1]. Their independence complexes are contractible for odd indices: a further neighborhood fold reduces \(H_m\) to the disjoint union of \(H_{m-2}\) with a three-vertex path, and \(H_1\) has an isolated vertex. The deletion/link decomposition therefore makes \(U_n\) contractible for every odd \(n\). This is an **ordinary**, not an equivariant, contractibility statement, which is sufficient for the following rational homology calculation. Direct recursive perfect-matching enumeration independently checks the exact union, the two cycle intersections, and the reduced mod-two acyclicity of \(U_n\) for \(n=3,5,7\) (verification below); finite checks are not substituted for the general argument.

**2. The induced module.** Relative simplicial chains satisfy a canonical \(G\)-equivariant isomorphism
\[
C_*(X_n,U_n;\mathbb Q)
\cong C_*(P_0,U_n\cap P_0;\mathbb Q)
\oplus C_*(P_1,U_n\cap P_1;\mathbb Q).
\]
The two alternating rim simplices have disjoint nonempty faces, and the group permutes these two relative-chain summands transitively. Hence their direct sum is the module induced from the stabilizer \(H\). Since each \(P_i\) is contractible, the relative long exact sequence gives
\[
H_j(P_i,U_n\cap P_i;\mathbb Q)
\cong\widetilde H_{j-1}(\operatorname{Ind}(C_n);\mathbb Q)
\]
for \(j\ge1\), naturally under \(H\). Since \(U_n\) is contractible, the inclusion of the pair yields \(\widetilde H_j(X_n;\mathbb Q)\cong H_j(X_n,U_n;\mathbb Q)\) for \(j\ge1\). The zero-degree case also vanishes because \(X_n\) is connected (it contains a connected nonempty contractible \(U_n\), and each \(P_i\) meets \(U_n\) along a nonempty cycle independence complex). These maps are natural, not just dimension isomorphisms. The standard homology theorem for cycle independence complexes [1, Proposition 8] says that for \(n=3q\) the nonzero reduced homology is \(\mathbb Q^2\) in degree \(q-1\), for \(n=3q+1\) it is \(\mathbb Q\) in degree \(q-1\), and for \(n=3q+2\) it is \(\mathbb Q\) in degree \(q\). For all odd \(n\ge3\), this degree equals \(d-1\); all other reduced degrees vanish. Thus the induced-module statement and degree concentration follow.

**3. Rotations of the cycle module.** Work first in \(W_n\). Rotation \(a^j\) acts by an \(n\)-cycle rotation. Put \(g=\gcd(n,j)\). Every invariant independent vertex set is a union of rotation orbits. For odd \(n\), these orbits have odd cardinality, and the orbit quotient has the adjacency relation of \(C_g\). The case \(g=1\) has a loop, so only the empty set is allowed. With \(I(C_g;z)=\sum_{S\text{ independent}}z^{|S|}\), using the loop convention \(I(C_1;-1)=1\), the signed reduced Lefschetz number of \(a^j\) on \(\operatorname{Ind}(C_n)\) is
\[
\widetilde L(a^j)=-I(C_g;-1)=-2\cos(g\pi/3).
\]
Indeed a fixed simplex made of \(t\) odd-sized orbits contributes \((-1)^{t-1}\) after combining the chain-degree and simplex-orientation signs. The cycle identity follows by splitting according to an independent set at one vertex or by the usual two-state transfer recurrence; at the possible odd residues \(g\equiv1,3,5\pmod6\), the value is respectively \(1,-2,1\), with the loop convention for length one. Since reduced homology is concentrated in degree \(d-1\), the trace on \(W_n\) is \((-1)^{d-1}\widetilde L(a^j)\). If \(3\nmid n\), this is \(1\) for every \(j\). If \(3\mid n\), the dimension is two and the trace is \(2\) when \(3\mid j\) and \(-1\) otherwise.

**4. Reflections of the cycle module.** The reflection \(b=rs\) fixes one rim edge \(e_0\) of \(P_0\) and swaps the remaining cycle vertices in pairs. Exactly one paired orbit consists of adjacent cycle vertices and is inadmissible; the other paired orbits together with the fixed vertex have the incompatibility graph of the path \(P_m\), \(m=(n-1)/2\). An invariant simplex made of \(t\) reflection-orbits again contributes \((-1)^{t-1}\) to the reduced Lefschetz sum, irrespective of orbit sizes. Thus
\[
\widetilde L(b)=-I(P_m;-1)=-p_m,\qquad
\operatorname{tr}(b\mid W_n)=(-1)^d p_m,
\]
where \(p_0=1,p_1=0,p_m=p_{m-1}-p_{m-2}\). The sequence is six-periodic: \(1,0,-1,-1,0,1\). Consequently the reflection trace is \((-1)^k\) for \(n=6k+1\), \((-1)^{k+1}\) for \(n=6k+5\), and zero for \(n=6k+3\). All reflections in odd-order \(H\) are conjugate. Together with the rotational traces, this identifies the two one-dimensional cases and the two-dimensional \(D_3\)-inflated case. Over \(\mathbb Q\), equality of finite-group characters determines the isomorphism class of a representation.

**5. Passage to the whole dihedral group.** The subgroup \(H\) is normal of index two in \(G\). Odd powers of \(r\), and reflections \(r^j s\) with even \(j\), lie outside \(H\), so the character of \(\operatorname{Ind}_H^G W_n\) is zero on them. For even powers \(r^{2j}\), both cosets contribute the trace of \(a^j\). For reflections \(r^{2j+1}s\), both cosets contribute the common reflection trace of \(W_n\). This yields the two displayed complete character formulas. No claim about integral lattice decomposition is needed.

## Verification

Run the standalone Python 3 standard-library program `verify_dihedral.py`. It enumerates all perfect matchings of \(M_{2n}\) recursively, generates the *full* down-closed complex, verifies the equivariant decomposition on each tested graph, and computes the signed augmented simplicial trace for every tested group element without using the proof's relative-chain construction. Direct traces were checked for every element at \(n=3,5,7,9\) and for eleven selected elements at \(n=11\), totaling **107** traces and **204,100** generated simplicial faces. Exact bitset boundary ranks over \(\mathbb F_2\) verify the concentration and ranks of homology and the acyclicity of the central subcomplex for \(n=3,5,7\). The program prints `VERIFY_OK` on successful completion. The infinite-width result rests on the proof above, not on the finite computations.

## Relationship to prior work

Agarwal and Basak [1] determine the *nonequivariant* homotopy types of these Möbius-ladder perfect-matching complexes and supply the decomposition and contractibility lemmas. Their complete 2026 preprint does not give the action of the full dihedral group on homology; knowing only the sphere multiplicities cannot determine the character. Živaljević [2, Section 8] studies \(\mathbb Z_2\)-equivariant homotopy types for the ordinary independence complexes of paths and cycles, furnishing a related analysis of the cycle *building block* rather than the perfect-matching complex of a Möbius ladder. A restricted computation of the central half-turn's homology action does not determine the rotation or reflection traces or the induced \(D_{2n}\)-module: it is strictly weaker than the present full-character statement. This is a statement-level comparison and not a claim that literature searches prove absolute novelty.

## Limitations

The theorem is for odd \(n\ge3\), the specified natural dihedral subgroup, and rational homology. It does not identify integral \(\mathbb Z[G]\)-lattices, an equivariant wedge-of-spheres decomposition, or the even-width dihedral representation. The proof uses published combinatorial decomposition and ordinary contractibility results, plus a new equivariant relative-chain argument; the independent finite tests verify examples but do not certify the all-parameter statements. Equivalent unindexed work may exist.

## References

1. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, v1 publicly posted 2026-08-31; v2 publicly posted 2026-09-14. Full text: https://arxiv.org/html/2608.30601v2 ; original: https://arxiv.org/html/2608.30601v1 .
2. Rade T. Živaljević, *WI-posets, graph complexes and Z_2-equivalences*, arXiv:math/0405419 (2004), especially Section 8. Full text: https://arxiv.org/html/math/0405419v1 .
