# The first unavoidable triple-cluster sector of the open EAST dark manifold

## Finding

For every integer \(n\geq7\), consider \(n\) qubits on an open chain and the facilitated collective lowering operator
\[
F_n=\sum_{j=2}^{n} n_{j-1}\sigma^-_j,
\qquad n_j=|1\rangle_j\langle1|.
\]
Let \(\mathcal H_{n,4}\) be the four-excitation subspace, let
\(\mathcal D_{n,4}=\ker(F_n|_{\mathcal H_{n,4}})\), and let
\(\mathcal D_{n,4}^{(<3)}\) be the subspace of \(\mathcal D_{n,4}\) whose computational-basis support avoids three consecutive occupied sites. Then
\[
\boxed{\dim \mathcal D_{n,4}=\binom n4-\binom n3+5},
\]
\[
\boxed{\dim \mathcal D_{n,4}^{(<3)}=
\binom{n-3}{4}+3\binom{n-3}{3}-\binom{n-2}{3}+1},
\]
and, consequently,
\[
\boxed{\dim\bigl(\mathcal D_{n,4}/\mathcal D_{n,4}^{(<3)}\bigr)
=\binom{n-5}{2}}.
\]
Thus exactly \(\binom{n-5}{2}\) independent dark-state directions, modulo all dark vectors having no triple motif, necessarily require amplitudes on at least one word containing `111`. This sector first appears at seven sites (dimension one), then grows quadratically in chain length. The quotient counts linearly independent directions, not canonical localized basis vectors.

## Assumptions and scope

Each site has basis \(|0\rangle,|1\rangle\); all coefficients of the local terms in \(F_n\) are one, and the boundary is **open**. The excitation-number-four sector is the span of all binary words of length \(n\) with exactly four ones. The string `111` means three adjacent occupied sites in the computational basis. The no-triple condition applies to **every word with nonzero amplitude**, not merely to an expected block-count observable. The assertions refer to the kernel of the specified collective jump, equivalently to the zero eigenspace of its positive operator \(F_n^\dagger F_n\). They do not classify the periodic model, other excitation sectors, or the stationary state of an arbitrary Lindbladian.

## Proof

**1. Block decomposition by the leftmost excitation.** Since the removal rule cannot erase the leftmost occupied site, the four-excitation domain and its image split as direct sums indexed by that site's position. If the frozen leftmost excitation is followed by \(m\) sites, the remaining three excitations are acted on by the *seeded* operator
\[
B_m=\sigma^-_1+\sum_{j=2}^m n_{j-1}\sigma^-_j,
\]
where the virtual site immediately to its left is occupied. Write \(B_{m,k}\) for its map from the \(k\)-excitation space to the \((k-1)\)-excitation space. Then
\[
\operatorname{rank}(F_n|_{\mathcal H_{n,4}})
=\sum_{m=3}^{n-1}\operatorname{rank} B_{m,3}.
\]

**2. Seeded rank lemma.** Direct integer matrices, indexed by ascending binary mask, establish
\[
\det B_{3,2}=-1,\qquad
\det B_{5,3}=-1,
\]
and \(B_{4,3}\) has rank four: in the ascending row ordering, rows 1–4 (one-based) form a four-by-four minor of determinant one. Also \(B_{3,3}\) has rank one. These small, exact matrices are recreated by the accompanying standalone verifier.

For general \(m\), separate input and output by whether the final site is occupied. In the appropriate block order,
\[
B_{m+1,k}=\begin{pmatrix}
B_{m,k}&P_{m,k-1}\\
0&B_{m,k-1}
\end{pmatrix},
\]
where \(P_{m,k-1}\) is the diagonal projector onto words occupying the final old site. If both displayed diagonal maps are surjective, the block map is surjective: choose a preimage of the lower target, then adjust the upper target using the first block. The map \(B_{m,1}\) is surjective onto the vacuum for every \(m\ge1\), since its first-site lowering term is present. Starting from \(B_{3,2}\), induction therefore makes \(B_{m,2}\) surjective for all \(m\ge3\). Starting from \(B_{5,3}\), another induction makes \(B_{m,3}\) surjective for every \(m\ge5\). Hence
\[
\operatorname{rank}B_{m,3}=
\begin{cases}
1,&m=3,\\
4,&m=4,\\
\binom m2,&m\ge5.
\end{cases}
\]
By the hockey-stick binomial identity and the three missing contributions of sizes \(1,2,2\) relative to \(\sum_{m=0}^{n-1}\binom m2=\binom n3\),
\[
\operatorname{rank}(F_n|_{\mathcal H_{n,4}})=\binom n3-5
\qquad(n\ge6).
\]
Rank-nullity proves the first displayed dimension formula.

**3. No-triple word partition.** A four-one word with no `111` has either zero, one or two disjoint adjacent `11` pairs. The numbers of such words are, respectively,
\[
\binom{n-3}{4},\qquad
3\binom{n-3}{3},\qquad
\binom{n-3}{2},
\]
by the standard count \(\binom{3}{r-1}\binom{n-3}{r}\) of four-one words with exactly \(r\) occupied runs. Zero-pair words are annihilated by \(F_n\). Every one-pair word produces exactly one three-one word with **zero** adjacent pairs. Such output words are independent-set triples. Every independent-set triple has a one-pair parent except the unique terminal alternating pattern \(0^{n-5}10101\). Therefore this block of the restricted jump has rank \(\binom{n-2}{3}-1\).

Every two-pair word produces two three-one words, each retaining exactly one adjacent pair. Their outputs are disjointly supported as the input two-pair word varies: in such an output the isolated excitation determines the unique possible newly inserted adjacent partner. Thus the two-pair columns are linearly independent and contribute rank \(\binom{n-3}{2}\). The zero- and one-pair output subspaces have disjoint computational support, so ranks add. The rank of the jump restricted to no-triple input is consequently
\[
\binom{n-2}{3}-1+\binom{n-3}{2}.
\]
Subtracting this from the number of no-triple input words gives the second displayed dimension formula.

**4. Exact quotient.** Since the no-triple dark space is a linear subspace of the full dark space, subtracting the two dimensions and simplifying binomial coefficients gives \(\binom{n-5}{2}\), proving the last formula. All calculations are exact over \(\mathbb C\); no generic-parameter assumption or asymptotic limit is used.

## Verification

Run `python3 verify.py` in the same directory as this document. The script uses only Python's standard library. It reconstructs the exact integer base matrices and checks their determinants \(-1,+1,-1\), then computes the full and no-triple four-excitation jump matrices for \(7\le n\le12\) and verifies both ranks using two distinct large prime moduli. The resulting quotient dimensions are \(1,3,6,10,15,21\). The determinant identities and the analytic induction/counting arguments, not finite numerical enumeration, establish the theorem for all \(n\ge7\).

## Relationship to prior work

Winter, Kumlin, Pohl and Nunnenkamp introduce the same open EAST lowering operator in Supplemental Eq. (66), its amplitude cancellation rule in Eq. (72), explicit dimer and triple packets in Eqs. (78)–(97), and a general dark-packet spanning construction in Eq. (98). Those constructions and the existence of triple-containing dark states are **prior results**. The contribution here is the exact dimension of the first excitation sector supporting the triple packet, the rank of its no-triple restriction, and the quotient dimension counting unavoidable triple-support directions for every chain length. The packet spanning statement is not asserted to be new, nor is a new dynamical or entanglement witness claimed.

The unconstrained Tavis–Cummings collective lowering operator studied by Ozhigov has a different set of allowed transitions and Catalan-type dark-state counts. The coherent quantum East Hamiltonian studied by Pancotti and coauthors is not the collective jump \(F_n\). Neither statement supplies this fixed-excitation, support-filtered quotient as stated.

## Limitations

Open rather than periodic boundary conditions are essential. The formula counts abstract vector-space dimensions; it does not construct a uniquely preferred basis, establish dynamical reachability from a selected initial state, or quantify stationary-state entanglement or preparation speed. The 2026 source develops a general spanning hierarchy; the relationship of the closed dimension formulas to every possible unindexed specialization of that hierarchy remains a literature-indexing risk. Independent review has not been performed.

## References

1. L. Winter, J. Kumlin, T. Pohl, and A. Nunnenkamp, *Extensive mixed-state entanglement in kinetically constrained superradiance*, arXiv:2605.16131v1 (first public 2026-05-15), particularly Supplemental Section III, Eqs. (66)–(101).
2. N. Pancotti, G. Giudice, J. I. Cirac, J. P. Garrahan, and M. C. Bañuls, *Quantum East Model: Localization, Nonthermal Eigenstates, and Slow Dynamics*, Physical Review X **10**, 021051 (2020), DOI:10.1103/PhysRevX.10.021051.
3. Y. I. Ozhigov, *Space of dark states in Tavis-Cummings model*, arXiv:1606.08483 (2016).
