# Transposition-dominated automorphisms of random binary perfect evolution algebras

## Finding
Fix an integer \(n\ge 2\). Draw \(M\) uniformly from \(\mathrm{GL}_n(\mathbb F_2)\), and define the evolution algebra \(E_M\) by \(e_i e_j=0\) for distinct basis vectors and \(e_i^2=\sum_{j=1}^n M_{ij}e_j\). Then
\[
\Pr\bigl(\operatorname{Aut}_{\mathbb F_2}(E_M)\ne\{1\}\bigr)
=\binom n2\frac{2^{1-2n}}{(1-2^{1-n})(1-2^{-n})}
+O\bigl(n^4 2^{-4n}\bigr).
\]
In particular the probability is asymptotic to \(n(n-1)2^{-2n}\). Moreover, given that \(E_M\) has a nontrivial automorphism, with probability tending to one its *entire* automorphism group consists of the identity and a single transposition of the natural basis. The result concerns the distribution of the full algebra automorphism group, not merely its diagonal subgroup.

## Assumptions and scope
The field is exactly \(\mathbb F_2\); the dimension is any integer \(n\ge2\). The random model is uniform among invertible labelled structure matrices, with no quotient by algebra isomorphism. All automorphisms are \(\mathbb F_2\)-linear. The big-\(O\) constant is absolute and the asymptotic is for \(n\to\infty\). Write \(G_n=|\mathrm{GL}_n(\mathbb F_2)|=2^{n^2}\prod_{j=1}^n(1-2^{-j})\) and \(G_0=1\).

## Proof
**1. Complete automorphism reduction.** If \(\phi\) is an automorphism and its matrix has columns \(a_i\), then for distinct \(i,j\),
\(0=\phi(e_i e_j)=\phi(e_i)\phi(e_j)=\sum_k (a_i)_k(a_j)_k e_k^2\). Since \(M\) is invertible, the elements \(e_k^2\) form a basis, so the supports of distinct columns are disjoint. Invertibility makes all \(n\) supports nonempty; their disjoint union lies in an \(n\)-element set, and therefore each support is a singleton. Since the sole nonzero scalar of \(\mathbb F_2\) is \(1\), \(\phi\) is exactly a permutation of the natural basis. Comparing squares shows that the associated permutation \(\sigma\) acts as an algebra automorphism precisely when \(M_{\sigma(i),\sigma(j)}=M_{ij}\) for all \(i,j\), equivalently its permutation matrix commutes with \(M\).

**2. Exact probability for one transposition.** Fix \(\tau=(1\,2)\). In characteristic two, \(N=P_\tau-I\) has rank one and satisfies \(N^2=0\). In a suitable basis \(u,w,z_1,\ldots,z_{n-2}\), \(Nw=u\) and \(Nu=Nz_i=0\). Directly solving \(XN=NX\) gives exactly the matrices
\[
X=\begin{pmatrix}a&b&\alpha\\0&a&0\\0&\beta&D\end{pmatrix},
\]
where \(a,b\in\mathbb F_2\), \(\alpha\in\mathbb F_2^{1\times(n-2)}\), \(\beta\in\mathbb F_2^{(n-2)\times1}\), and \(D\in M_{n-2}(\mathbb F_2)\). Such a matrix is invertible exactly when \(a=1\) and \(D\in\mathrm{GL}_{n-2}(\mathbb F_2)\). Hence the number of commuting invertible matrices equals \(2^{2n-3}G_{n-2}\) and
\[
p_n=\frac{2^{2n-3}G_{n-2}}{G_n}
=\frac{2^{1-2n}}{(1-2^{1-n})(1-2^{-n})}.
\]
This exact identity also holds for \(n=2\), with empty \(D\).

**3. Uniform bound for other permutations.** Let \(\sigma\) have \(f\) fixed points and support \(m=n-f\ge3\). Let its nontrivial cycle lengths be \(\ell_1,\ldots,\ell_t\), so that \(t\le m/2\). The dimension \(d(\sigma)\) of the \(\mathbb F_2\)-vector space of matrices commuting with \(P_\sigma\) equals the number of orbits of \(\sigma\) on ordered pairs of basis indices:
\[
d(\sigma)=f^2+2ft+\sum_{a,b=1}^{t}\gcd(\ell_a,\ell_b)
\le f^2+2ft+tm
\le n^2-m\left(n-\frac m2\right).
\]
The orbit expression follows by regarding the matrix entries as functions on ordered pairs; a pair of cycles of lengths \(r,s\) has \(\gcd(r,s)\) simultaneous-shift orbits. For a three-cycle the exact dimension is \(n^2-4n+6\); for a permutation supported on four points, the largest dimension is \(n^2-4n+8\), attained by a product of two disjoint transpositions. Put \(c_*=\prod_{j=1}^\infty(1-2^{-j})>0\). Since \(G_n\ge c_*2^{n^2}\),
\[
\Pr(P_\sigma M=MP_\sigma)\le c_*^{-1}2^{d(\sigma)-n^2}.
\]
There are at most \(n^m\) permutations with support \(m\). Thus the total probability of an automorphism with support three is \(O(n^3 2^{-4n})\), and that with support four is \(O(n^4 2^{-4n})\). The sum for \(5\le m\le n/2\) is \(O(n^5 2^{-5n})\): successive upper bounds have ratio at most \(n2^{-n/2+1/2}<1/2\) for all sufficiently large \(n\). For \(m>n/2\), the entire contribution is at most \(c_*^{-1}n^{n+1}2^{-n^2/4}\), which is exponentially smaller than \(n^5 2^{-5n}\). Consequently
\[
\Pr(\text{some automorphism moves at least three vertices})
=O(n^4 2^{-4n}).
\]

**4. Intersections of transposition events.** Let \(A_\tau\) denote the event that transposition \(\tau\) commutes with \(M\). If two distinct transpositions commute with \(M\), so does their product, which is either a three-cycle or a product of two disjoint transpositions. The corresponding centralizer dimension bounds from step 3 imply \(\Pr(A_\tau\cap A_\eta)=O(2^{-4n})\) uniformly over distinct transpositions \(\tau,\eta\). As there are \(O(n^4)\) such ordered pairs, the first two Bonferroni inequalities give
\[
\Pr\Bigl(\bigcup_{\tau\text{ transposition}} A_\tau\Bigr)
=\binom n2 p_n+O(n^4 2^{-4n}).
\]
Step 3 adds only \(O(n^4 2^{-4n})\) for all other nonidentity permutations. This proves the asserted probability and its equivalent. Finally, if a stabilizer contains a nonidentity element but none moving three or more vertices, it contains exactly one transposition: two distinct ones would give a product moving at least three. Hence the remaining event has automorphism group \(C_2\). Its complement among nontrivial stabilizers is \(O(n^4 2^{-4n})\), while the nontrivial probability has size \(\Theta(n^2 2^{-2n})\), proving the conditional statement.

## Verification
Run `python3 verify_binary_evolution_symmetry.py`. It exhaustively enumerates all invertible binary matrices in dimensions \(2,3,4\), independently checks every basis permutation, and compares fixed-transposition counts against \(2^{2n-3}G_{n-2}\). For \(n=2\), it finds \(6\) matrices, \(2\) with nontrivial automorphisms and \(2\) with a single transposition stabilizer. For \(n=3\), the respective numbers are \(168,24,21\); for \(n=4\), they are \(20160,1344,1008\). The checker prints `VERIFY_OK` if all assertions pass. The infinite-dimensional estimates follow from the proof, not these tests.

## Relationship to prior work
Wei and Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (arXiv:2310.12368, 2023), give the full monomial action on invertible evolution-algebra structure matrices, a general Burnside orbit-counting formula, and explicit isomorphism-class numbers in dimensions two through four. In the binary case, their group action reduces to simultaneous permutations of rows and columns. The present theorem evaluates a different statistic: the probability of a nontrivial stabilizer in a uniform labelled invertible matrix, the sharp leading contribution, and the typical isomorphism type of its stabilizer. The general Burnside orbit identity gives an average stabilizer size but does not by itself establish this probability or the uniqueness of a transposition. Rodiño Montoya, Viana Bedoya, and Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs* (arXiv:2505.15604, 2025), analyze graph-induced symmetries in designated undirected-graph algebra families, rather than a random uniform invertible binary-matrix ensemble. Those structural contributions are used as background and are not claimed as new.

## Limitations
The binary-field property \(\mathbb F_2^\times=\{1\}\) is essential. The theorem does not assert the same asymptotic for other fields or for an unlabeled-uniform isomorphism-class distribution. The novelty comparison cannot rule out unindexed or implicitly equivalent probability estimates. The review is same-model only, not an independent audit.

## References
1. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (initial public version 2023-10-18), https://arxiv.org/abs/2310.12368, sections 1–2 and 4–6.
2. M. L. Rodiño Montoya, N. A. Viana Bedoya, and C. Henao, *Group actions and automorphisms of evolution algebras associated to finite graphs*, arXiv:2505.15604 (initial public version 2025-05-21), https://arxiv.org/abs/2505.15604, introduction and sections 1–3.
3. A. Elduque and A. Labra, *Evolution algebras and graphs*, J. Algebra Appl. 14 (2015), 1550103, as cited and used in references 1–2.
