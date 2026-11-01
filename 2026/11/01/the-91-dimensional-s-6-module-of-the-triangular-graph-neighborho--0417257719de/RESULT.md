# The 91-dimensional \(S_6\)-module of the triangular-graph neighborhood complex
## Finding
Let \(T_6=L(K_6)\), the triangular graph on unordered pairs from six labels, and let \(X=\mathcal N(T_6)\) be its open Lovász neighborhood complex. Then \(\widetilde H_i(X;\mathbb Q)=0\) for \(i\ne3\), and, as rational \(S_6\)-modules,
\[
\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong {}&S^{(4,2)}\oplus S^{(3,3)}\oplus 2S^{(3,2,1)}\\
&\oplus S^{(3,1,1,1)}\oplus 2S^{(2,2,2)}\oplus S^{(2,2,1,1)}\\
&\oplus 3S^{(2,1,1,1,1)}\oplus S^{(1,1,1,1,1,1)}.
\end{aligned}
\]
Here \(S^\lambda\) is the irreducible rational Specht representation associated to the partition \(\lambda\vdash6\). The dimensions sum to \(9+5+2(16)+10+2(5)+9+3(5)+1=91\).

The multiplicity of the trivial representation is zero, while that of the sign representation is one. Consequently
\[
\widetilde H_*(|X|/S_6;\mathbb Q)=0,\qquad
\widetilde H_i(|X|/A_6;\mathbb Q)\cong
\begin{cases}\mathbb Q,&i=3,\\0,&i\ne3.\end{cases}
\]
Moreover \(X=\Delta_7(T_6)\), the ordinary seven-cut complex of the same graph.

## Assumptions and scope
The vertices of \(T_6\) are the 15 two-element subsets of \(\{1,2,3,4,5,6\}\). Two distinct vertices are adjacent precisely when their two-element subsets intersect. The neighborhood complex \(X\) contains a set \(F\) of these 15 vertices if and only if there is a vertex outside \(F\) adjacent to all of \(F\). Its maximal simplices are the 15 eight-element open neighborhoods \(N_{T_6}(e)\), one for each edge \(e\) of \(K_6\). The symmetric group \(S_6\) acts by permuting the six underlying labels. All coefficient calculations and representation decompositions are over \(\mathbb Q\).

## Proof
**Exact rational chain ranks.** Enumerate every nonempty subset of each eight-element neighborhood and deduplicate. The resulting face vector in dimensions zero through seven is
\[(15,105,420,945,840,420,120,15).\]
Order the simplices by increasing vertex indices, and use the standard integral alternating boundary. Exact rational sparse column elimination yields ranks for \(\partial_1,\ldots,\partial_7\) of
\[(14,91,329,525,315,105,15).\]
The identities \(\partial_i\partial_{i+1}=0\) are checked on every generator. The formula \(\dim H_i=\dim C_i-\operatorname{rank}\partial_i-\operatorname{rank}\partial_{i+1}\), with reduced degree zero, gives \(\widetilde\beta_3=91\) and all other reduced rational Betti numbers zero. Every rational pivot and boundary coefficient is computed exactly (no floating-point tolerance).

**Character on all conjugacy classes.** For a permutation \(g\in S_6\), the action on each oriented simplex has sign \(\operatorname{sgn}(g|_F)\) when \(gF=F\), and gives no trace otherwise. Let \(f_i(g)\) be the signed trace on the simplicial chain group in degree \(i\). As the only unreduced homology groups are the trivial \(H_0\) and the degree-three group, the Hopf trace formula gives
\[\chi(g)=1-\sum_{i=0}^{7}(-1)^i f_i(g).\]
The following table records the complete character, indexed by cycle type of \(g\); every value is obtained by enumerating the fixed oriented faces, including their parity signs.

| Cycle type | \(\chi(g)\) |
|---|---:|
| \((6)\) | 1 |
| \((5,1)\) | 1 |
| \((4,2)\) | −3 |
| \((4,1,1)\) | −3 |
| \((3,3)\) | 1 |
| \((3,2,1)\) | −1 |
| \((3,1,1,1)\) | 1 |
| \((2,2,2)\) | 7 |
| \((2,2,1,1)\) | 7 |
| \((2,1,1,1,1)\) | −13 |
| \((1,1,1,1,1,1)\) | 91 |

**Exact irreducible decomposition.** For every partition \(\lambda\vdash6\), the multiplicity is the character inner product \(\langle\chi,\chi^\lambda\rangle=\sum_{\mu\vdash6}\chi(\mu)\chi^\lambda(\mu)/z_\mu\), where \(z_\mu=\prod_{j\ge1}j^{m_j}m_j!\) and \(m_j\) counts length-\(j\) cycles. The verifier obtains all irreducible characters via the Jacobi–Trudi alternating permutation-module formula, verifies their complete mutual orthogonality, and reconstructs the original 11 character values. The resulting multiplicities are exactly those stated above. Since a finite-group quotient has rational homology identified with the invariant rational homology after equivariant barycentric subdivision, the trivial and sign multiplicities give the two quotient conclusions: restriction to \(A_6\) identifies the sign and trivial characters, leaving one invariant line.

**Cut-complex identification.** A seven-element vertex subset of \(T_6\) is an edge set of \(K_6\) with seven edges. For its induced subgraph in \(T_6\) to be disconnected, those edges must split into two nonempty families with disjoint underlying endpoint sets. On six endpoints, the maximum edge count in such a split is \(\binom42+\binom22=7\), achieved precisely by the complete graph on four endpoints together with the complementary pair edge. Thus its complement in the 15 edges of \(K_6\) is exactly one eight-element open neighborhood in \(T_6\). These are precisely the 15 facets of \(\mathcal N(T_6)\), proving \(\Delta_7(T_6)=X\). The verifier separately enumerates all seven-element subsets and checks this facet identity.

## Verification
Run the included standalone `verify.py` with Python 3 and no third-party dependencies. It enumerates all simplices, reconstructs the rational chain maps using `fractions.Fraction`, verifies boundary-squared-zero, computes each conjugacy-class signed Lefschetz trace, checks the Jacobi–Trudi irreducible character orthogonality and multiplicity decomposition, reconstructs every trace from the resulting irreducibles, and independently enumerates the seven-cut facets. The saved `verification_output.txt` records an exact successful run and complete numerical outputs. Each calculation is finite and exhaustive within the specified complex.

## Relationship to prior work
Lovász introduced neighborhood complexes in studying graph chromatic numbers. Matsushita's 2012 preprint develops their fundamental groups but does not present the six-label triangular-graph symmetry character. Prior published computational work on triangular neighborhoods establishes the 91-dimensional **mod-two** degree-three homology at six labels, with the first two-degree mod-two example occurring at seven labels; the dimension and concentration alone do not determine the \(S_6\)-action. A separate published character calculation for the **five-label** triangular graph's four-cut complex determines an 11-dimensional \(S_5\)-module, not the six-label representation. Bayer and collaborators treat topology and equivariant homology of cut complexes for several other graph families; their published general results do not give this specific six-label character. Fröberg's 2026 neighborhood-ring calculations concern other named graph families and do not imply this representation. The exact 91-dimensional decomposition, its sign multiplicity and the resulting alternating-group quotient difference are the contributions asserted here.

## Limitations
Only reduced rational homology and its natural finite-group representation are determined. No assertion is made about integral torsion, an integral representation lattice, simple-homotopy type, higher label counts or quotient fundamental groups. The published mod-two Betti number and the five-label character are acknowledged prior results, not new claims. Absence of a discovered equivalent formula is not proof of global publication priority; independent mathematical verification remains outstanding.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first posted 2012-10-10; *J. Math. Sci. Univ. Tokyo* 24 (2017), 321–353.
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26; *SIAM J. Discrete Math.* 38 (2024), 1630–1675.
3. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, *J. Algebraic Combin.* 63 (2026), article 56, DOI 10.1007/s10801-026-01530-x.
4. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, publicly available research result dated 2026-10-11, `2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec`.
5. *Eleven three-spheres and the symmetric-group character of a four-cut complex*, publicly available research result dated 2026-10-11, `2026/10/11/SCOPE-eleven-three-spheres-and-the-symmetric-group-character-of-a-four--9dc76d8fa65e`.
