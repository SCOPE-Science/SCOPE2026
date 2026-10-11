# Rational cyclic homology representations of three-cut complexes of cycle powers

## Finding
For integers \(p\geq2\) and \(n\geq6p-3\), let \(C_n^p\) be the graph on \(\mathbb Z/n\mathbb Z\) in which two distinct vertices are adjacent precisely when their cyclic distance is at most \(p\). Let \(K=\Delta_3(C_n^p)\) be the **ordinary** three-cut complex, whose facets are complements of disconnected induced three-vertex subgraphs. Let \(\rho(i)=i+1\), \(G=\langle\rho\rangle\cong C_n\), and let \(\mathcal H=\widetilde H_{n-4}(K;\mathbb Q)\). Write \(\epsilon\) for the one-dimensional orientation-sign character \(\epsilon(\rho^s)=(-1)^{n-\gcd(n,s)}\), and \(\mathbb Q[G]\) for the rational regular representation.

The graded reduced rational homology of \(K\) is concentrated in degree \(n-4\), and its complete \(G\)-representation is:

\[
\mathcal H\cong
\begin{cases}
\mathbb Q\oplus \mathbb Q[G]^{\oplus (n-4p-1)/2},&n\text{ odd},\\[3pt]
\epsilon\oplus\mathbb Q[G]^{\oplus(n/2-2p-1)}\oplus
\bigl(\epsilon\otimes\operatorname{Ind}_{\langle\rho^{n/2}\rangle}^{G}\eta\bigr),&n\text{ even},
\end{cases}
\]
where \(\eta\) is the nontrivial one-dimensional rational character of the two-element subgroup \(\langle\rho^{n/2}\rangle\). The exponents are nonnegative integers in the given range. Equivalently, with \(\beta=1+n(n-4p-1)/2\), the full character is
\[
\operatorname{tr}(\rho^s\mid\mathcal H)=
\begin{cases}
\beta,&s\equiv0\pmod n,\\
(-1)^{n-\gcd(n,s)}(1-n/2),&n\text{ even and }s\equiv n/2\pmod n,\\
(-1)^{n-\gcd(n,s)},&\text{all other }s\not\equiv0\pmod n.
\end{cases}
\]

## Assumptions and scope
The graph is the \(p\)-th power of the **simple undirected cycle**, \(p\) and \(n\) are integers within the stated range, and coefficients are rational. The complex is the ordinary cut complex: a removed triple is required to induce a **disconnected** graph, not necessarily an independent set. Group actions on chains use the canonical orientation of vertices in increasing order. The published nonequivariant shellability and sphere-count theorem for precisely this range is used as an input [1, Theorem 1.4]. No assertion is made at parameters outside that theorem's range.

## Proof
**1. Dual complex and degree concentration.** Define the combinatorial Alexander dual \(L=K^\vee\), with faces \(S\subseteq\mathbb Z/n\mathbb Z\) for which \((\mathbb Z/n\mathbb Z)\setminus S\) is not a face of \(K\). By the facet definition, this is exactly the family in which **every** three-vertex subset of \(S\) induces a connected subgraph of \(C_n^p\). Equivalently, each \(x\in S\) has at most one nonneighbor *within* \(S\). Indeed, a disconnected three-vertex graph has an isolated vertex, and conversely any vertex having two nonneighbors produces such a disconnected triple. In particular, every singleton and pair is a face of \(L\); hence \(L\) is connected.

By [1, Theorem 1.4], \(K\simeq\bigvee^{\beta}S^{n-4}\), with
\[
\beta=\binom{n-2p}{2}-(2p^2+p-1)=1+\frac{n(n-4p-1)}2.
\]
Combinatorial Alexander duality gives \(\widetilde H^j(L;\mathbb Q)=0\) for \(j\ne1\) and \(\dim H^1(L;\mathbb Q)=\beta\). Its equivariant chain-level version, obtained by identifying complementary oriented simplices in the ambient \((n-1)\)-simplex, contributes the orientation-sign character; therefore
\[
\mathcal H\cong\epsilon\otimes H^1(L;\mathbb Q)
\]
as rational \(G\)-modules. The orientation factor on \(\rho^s\) is the sign of the permutation of all \(n\) vertices, namely \((-1)^{n-\gcd(n,s)}\). This is a statement about representations, not merely abstract vector spaces.

**2. Rotations of order at least three fix no nonempty dual simplex.** Fix \(\rho^s\) with order \(m=n/d\ge3\), where \(d=\gcd(n,s)\). Any nonempty invariant face \(S\) must contain a complete orbit; that orbit is \(\{x+jd:0\le j<m\}\) (the generator may traverse it in another order). If \(m\ne4\), choose \(j=\lceil m/3\rceil<m/2\). The two distinct orbit vertices \(x+jd\) and \(x-jd\) are at cyclic distance \(jd\ge n/3>p\) from \(x\), violating the face condition in step 1. The inequality follows from \(n\ge6p-3\) and \(p\ge2\). When \(m=4\), choose \(j=1\); the two distances are \(n/4>p\), because \(6p-3>4p\) for \(p\ge2\). Thus no nonempty simplex is fixed setwise by any rotation of order at least three. The ordinary simplicial Lefschetz number is consequently zero.

**3. The unique order-two rotation.** For even \(n\), write \(h=\rho^{n/2}\). Every nonempty invariant face is a union of antipodal pairs. Any one antipodal pair is an edge in \(L\). If \(S\) contained two such pairs, fix \(x\) in the first and \(y\) in the second. The vertex \(x+n/2\) is a nonneighbor of \(x\). At least one of \(y\) and \(y+n/2\) is also a nonneighbor of \(x\): if both were adjacent, their mutual cyclic distance \(n/2\) would be at most \(2p\), contradicting \(n\ge6p-3\), which implies \(n/2>2p\) for even \(n\) and \(p\ge2\). Hence the only nonempty invariant simplices are the \(n/2\) antipodal edges. Each is reversed under \(h\); its contribution to the alternating chain trace is \((-1)^1(-1)=+1\), so the ordinary Lefschetz number is exactly \(n/2\).

**4. Characters and reconstruction.** Since \(L\) is connected and its rational cohomology is only in degrees zero and one, the Lefschetz equality reads \(\Lambda(g;L)=1-\operatorname{tr}(g\mid H^1(L;\mathbb Q))\). Steps 2 and 3 give trace \(1\) for every nonidentity rotation other than \(h\), trace \(1-n/2\) for \(h\), and the known dimension \(\beta\) at the identity. Tensoring by \(\epsilon\) proves the displayed character.

For odd \(n\), the characters of \(\mathbb Q\) and \(\mathbb Q[G]\) are respectively constant one and supported at the identity with value \(n\). Since \(\beta-1=n(n-4p-1)/2\), they give the first decomposition. For even \(n\), the character of \(\operatorname{Ind}_{\langle h\rangle}^G\eta\) equals \(n/2\) at the identity, \(-n/2\) at \(h\), and zero elsewhere. Its sum with \(\mathbb Q\oplus\mathbb Q[G]^{\oplus(n/2-2p-1)}\) has exactly the computed dual-cohomology character. Tensoring with \(\epsilon\) gives the second decomposition; twisting the regular representation does not change its isomorphism class. Maschke semisimplicity and character injectivity for rational representations of finite cyclic groups conclude the proof.

## Verification
Execute `python3 verify.py` with Python 3's standard library from a directory containing this file and `verify.py`. Its independent finite routines construct the Alexander dual directly by connected triples, enumerate rotation-fixed oriented simplices, compute exact binary boundary ranks, and separately construct ordinary cut complexes from disconnected triples. The deterministic run returned `VERIFY_OK dual_faces=6426 dual_rotations=186 mod2_betti=12 direct_cut_actions=42`. Additional algebraic character checks cover \(2\le p\le6\) and \(6p-3\le n<6p+15\). These computations check finite instances and representation arithmetic; the all-parameter result is furnished by the preceding proof.

## Relationship to prior work
Chauhan and Shukla [1, Theorem 1.4] proved shellability and the exact nonequivariant sphere multiplicity for the same graphs and parameter range. Their construction does not supply the rotation character. The squared-cycle special case of Chauhan, Shukla and Vinayak [2] likewise supplies nonequivariant topology. Bayer and collaborators [3, Theorem 7.15] and [4, Theorem 6.6] determined cyclic and dihedral homology representations of ordinary cut complexes of **unpowered** cycles, and [3, Proposition 7.29] treats different exceptional squared-cycle cut parameters. Those statements neither compute nor imply the claimed character for \(p\ge2\), \(k=3\), \(n\ge6p-3\). The total cut complex, which requires independent removed triples, is a different complex.

## Limitations
The result classifies rational representations for the cyclic rotation subgroup only. It does not determine a dihedral reflection character, integral module structure, an equivariant wedge-of-spheres homotopy type, or cases below the proved shellability threshold. Exhaustive checks are finite and not a replacement for the all-parameter argument. An equivalent unindexed computation cannot be excluded by literature searches alone.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1 (first publicly submitted 2026-03-24), Theorem 1.4 and Section 3.2.1. https://arxiv.org/abs/2603.23155
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979v1 (2024). https://arxiv.org/abs/2406.01979
3. M. Bayer, M. Denker, M. Jelić Milutinović, M. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, especially Theorem 7.15 and Proposition 7.29. https://arxiv.org/abs/2304.13675
4. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, especially Section 6.2 and Theorem 6.6. https://arxiv.org/abs/2407.08158
