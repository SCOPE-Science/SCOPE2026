# Power-compact Kraus families restore row–column spectral symmetry

## Finding

Let \(H\) be any complex Hilbert space and let \((X_j)_{j\in J}\subset B(H)\) be a nonempty finite or countable family satisfying \(\sum_{j\in J}\|X_j\|^2<\infty\). Define
\[
\Phi(A)=\sum_j X_j A X_j^*,\qquad \Psi(A)=\sum_j X_j^* A X_j.
\]
For a word \(w=(j_1,\ldots,j_m)\), put \(X_w=X_{j_1}\cdots X_{j_m}\), and let \(\mathfrak I\) denote any one of \(B(H)\), \(K(H)\), or \(S_p(H)\) for \(1\le p<\infty\), equipped with its usual norm. For each integer \(m\ge1\), the following are equivalent:

1. Every word product \(X_w\) of length \(m\) is compact on \(H\).
2. The map \(\Phi^m:\mathfrak I\to\mathfrak I\) is a compact Banach-space operator for at least one (hence every) choice of \(\mathfrak I\).
3. The map \(\Psi^m:\mathfrak I\to\mathfrak I\) is a compact Banach-space operator for at least one (hence every) choice of \(\mathfrak I\).

Whenever these conditions hold, the nonzero spectral eigenvalues, **with their Riesz algebraic multiplicities**, of \(\Phi^m\) and \(\Psi^m\) are identical, independently of whether the maps are considered on \(B(H)\), \(K(H)\), or \(S_p(H)\). In particular, for the row/column word-growth quantities
\[
\rho_{\rm row}(X)=\lim_{n\to\infty}\Big\|\sum_{|w|=n}X_wX_w^*\Big\|^{1/(2n)},\qquad
\rho_{\rm col}(X)=\lim_{n\to\infty}\Big\|\sum_{|w|=n}X_w^*X_w\Big\|^{1/(2n)},
\]
there is exact equality \(\rho_{\rm row}(X)=\rho_{\rm col}(X)\). Both limits exist. The theorem allows every \(X_j\) to be noncompact if the family becomes compact after a fixed word length. For \(m=1\) it gives spectral-multiset equality across every Schatten ideal for compact Kraus families.

## Assumptions and scope

All operators are bounded and complex-linear. The sum-of-squared-norms assumption is imposed when \(J\) is infinite; it guarantees convergence in operator norm of both Kraus series on each indicated ideal and, for any fixed \(n\), of the sums over all length-\(n\) words. The word products are ordered as written. \(S_p(H)\) is the Schatten ideal for \(1\le p<\infty\); there is no quasi-Banach assertion for \(p<1\). Spectral multiplicity means the rank of the Riesz projection for an isolated nonzero spectral point, not geometric multiplicity. Zero is excluded from the multiset assertion and need not have finite multiplicity.

## Proof

**1. A compactness test for Kraus maps.** Consider any finite or countable family \((Y_j)\) with \(\sum\|Y_j\|^2<\infty\), and the completely positive operator \(T_Y(A)=\sum_jY_jAY_j^*\). Claim: \(T_Y:\mathfrak I\to\mathfrak I\) is compact, for any one (equivalently every) indicated ideal, **if and only if each \(Y_j\) is compact**.

If every \(Y_j\) is compact, truncate the absolutely convergent sum to finitely many terms and approximate each remaining \(Y_j\) by a finite-rank \(F_j\). Taking a common finite-rank orthogonal projection \(P\) covering the initial and final spaces of the \(F_j\), the map \(T_F(A)=\sum_jF_jAF_j^*\) takes values in \(PB(H)P\), so is finite rank on every \(\mathfrak I\). The estimate
\[
\|YAY^*-FAF^*\|_{\mathfrak I}
\le(\|Y\|+\|F\|)\|Y-F\|\,\|A\|_{\mathfrak I}
\]
works on \(B(H)\), \(K(H)\), and each \(S_p(H)\). Together with \(\|YAY^*\|_{\mathfrak I}\le\|Y\|^2\|A\|_{\mathfrak I}\), it proves convergence of finite-rank maps to \(T_Y\) in the corresponding Banach operator norm.

Conversely, if some \(Y_{j_0}\) is noncompact, the Hilbert-space characterization of compact operators provides an orthonormal sequence \((e_n)\) and \(\varepsilon>0\) with \(\|Y_{j_0}e_n\|\ge\varepsilon\). The rank-one projections \(P_n=|e_n\rangle\langle e_n|\) have unit norm in all indicated spaces. Positivity gives
\[
T_Y(P_n)=\sum_j|Y_je_n\rangle\langle Y_je_n|\ge |Y_{j_0}e_n\rangle\langle Y_{j_0}e_n|,
\quad \|T_Y(P_n)\|\ge\varepsilon^2.
\]
For any \(u,v\in H\), \(\langle T_Y(P_n)u,v\rangle\to0\): each \(Y_je_n\) is weakly null, and the infinite tail is uniformly bounded by \(\|u\|\|v\|\sum_{j>J_0}\|Y_j\|^2\). Thus the outputs converge weakly as Hilbert-space operators to zero, but cannot have a norm-convergent subsequence in any \(\mathfrak I\), because ideal-norm convergence implies operator-norm convergence. This contradicts compactness and proves the claim. The analogous test applies to \(\sum_jY_j^*A Y_j\) because compactness of \(Y_j\) and \(Y_j^*\) is equivalent.

**2. Word compactness is power compactness.** Expanding a power of the Kraus maps gives
\[
\Phi^m(A)=\sum_{|w|=m}X_w A X_w^*,\qquad
\Psi^m(A)=\sum_{|w|=m}X_w^* A X_w.
\]
Reversing the finite words in the second identity gives exactly the same set of products, so the order notation is consistent. Moreover
\(\sum_{|w|=m}\|X_w\|^2\le(\sum_j\|X_j\|^2)^m\). Applying Step 1 to the word family proves the three-way equivalence, for every \(m\ge1\) and every allowed ideal.

**3. Nonzero spectra of compact Kraus maps are ideal-independent.** Under the compactness condition, work with the word Kraus family \(Y_w=X_w\), all compact. Step 1 gives norm approximations of \(T_Y=\Phi^m\) and \(\widetilde T_Y=\Psi^m\) by a common sequence of finite-rank-Kraus maps \(T_{F,k}\), \(\widetilde T_{F,k}\), using the same finitely many coefficients \(F_j\) supported on one common finite-dimensional projection \(P_k\). These approximations converge in operator norm **on every** \(\mathfrak I\). Each approximant has range in \(P_kB(H)P_k\). At a nonzero eigenvalue, its entire generalized eigenspace is contained in this finite-dimensional range, so its nonzero spectrum and Riesz multiplicities on \(B(H)\), \(K(H)\), and \(S_p(H)\) agree with its restriction to \(P_kB(H)P_k\).

On this finite-dimensional Hilbert–Schmidt matrix space the two maps are Hilbert-space adjoints, so their eigenvalues are complex conjugate with algebraic multiplicity. Each map also preserves adjoints of its matrix argument, so an antilinear adjoint involution pairs its eigenvalues \(\lambda\) and \(\overline\lambda\), preserving generalized-eigenspace dimensions. Consequently the two approximants have **identical** nonzero eigenvalue multisets.

For each nonzero isolated eigenvalue of a compact Banach-space operator, a small resolvent circle defines a finite-rank Riesz projection. Operator-norm convergence of the finite-rank approximants gives convergence of these projections and eventual equality of ranks. Conversely, a sequence of eigenvalues of the approximants that stays away from zero can only accumulate at spectral points of the limit. Therefore the nonzero eigenvalue multisets, including multiplicities, coincide for \(T_Y\) and \(\widetilde T_Y\) across all ideals. This completes the spectral assertion.

**4. Row–column equality.** Complete positivity yields \(\|\Phi^n\|_{B(B(H))}=\|\Phi^n(I)\|\) and \(\|\Psi^n\|_{B(B(H))}=\|\Psi^n(I)\|\). Expanding their values at \(I\) produces precisely the row and column word sums in the statement (reversing words when needed). The Gelfand formula therefore gives
\[
\rho_{\rm row}(X)^2=r_{B(H)}(\Phi),\qquad
\rho_{\rm col}(X)^2=r_{B(H)}(\Psi).
\]
Step 3 applies to \(\Phi^m,\Psi^m\). Their spectral radii are equal, so \(r(\Phi)^m=r(\Psi)^m\), and hence the desired row–column equality follows. This also covers spectral radius zero.

**5. Sharpness and a noncompact, nonquasinilpotent instance.** Compactness of each generator is not necessary: on \(H=(\ell_2\oplus\ell_2)\oplus\mathbb C^2\), let \(N(u,v)=(v,0)\), \(A=\operatorname{diag}(2,1)\), and \(B=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\). Put \(X_1=N\oplus A\), \(X_2=0\oplus B\). The operator \(X_1\) is noncompact, but every word of length two is supported on \(\mathbb C^2\), because \(N^2=0\). The row/column radii coincide by the theorem and are nonzero (\(X_1\) has eigenvalue \(2\)); the family is noncommuting since \(AB\ne BA\).

The word-compact hypothesis cannot simply be deleted: on \(\ell_2(\mathbb N_0)\), for any integer \(d\ge2\), the isometries \(V_j e_k=e_{dk+j-1}\) for \(1\le j\le d\) have orthogonal ranges whose projections sum to \(I\). Their row word-sum equals \(I\) at every length, while the column word-sum equals \(d^n I\) at length \(n\). Thus \(\rho_{\rm row}(V)=1\), whereas \(\rho_{\rm col}(V)=\sqrt d\).

## Verification

Run `python verify.py` (requires NumPy and SymPy). Its deterministic exact integer-matrix checks compare characteristic polynomials and Hilbert–Schmidt adjoints of finite Kraus maps. Further numerical and finite-corner checks verify related identities and the noncompact boundary construction. These finite computations do **not** certify the infinite-dimensional compactness or Riesz-projection arguments; those are proved above.

## Relationship to prior work

Scherer, Shalit, and Shamovich established row–column spectral-radius equality for finite matrix tuples and explicitly exhibited failure for unrestricted infinite-dimensional tuples. Their Section 5, Example 5.2 and Remark 5.3, connects the finite equality to Kraus-map spectral radii; it does not give the word-compact, all-ideal spectral-multiset theorem proved here. Tornes' subsequent work emphasizes the distinction between agreement on matrix tuples and agreement on operator tuples, without identifying the power-compact recovery class. Earlier work of Fong–Sourour on compact elementary operators already characterizes compactness of elementary maps; compactness of such maps is not claimed as a new idea in isolation. The proposed contribution is the **joint** criterion using compact word products together with exact row–column recovery and the nonzero Riesz spectral-multiset transfer simultaneously across the operator and Schatten ideals.

## Limitations

No assertion is made about equality for arbitrary noncompact tuples, and the explicit isometry family shows this would be false. The theorem assumes a finite or norm-square-summable countable Kraus family and does not cover all merely strongly convergent Kraus decompositions. It does not assert that \(\Phi\) and \(\Psi\) have matching individual nonzero spectra if only a higher power is compact: the established spectral-multiset assertion is specifically for that compact **power**. Possible equivalent formulations in classical elementary-operator or completely positive spectral theory remain a publication-priority risk. Independent validation has not been performed.

## References

1. M. Scherer, O. M. Shalit, and E. Shamovich, *On the spectral radius of operator tuples*, arXiv:2605.09354v1 (10 May 2026), Section 5, Example 5.2 and Remark 5.3. https://arxiv.org/html/2605.09354v1
2. M. Tornes, *On the Shalit–Shamovich Spectral Radius*, arXiv:2610.00816v1 (30 September 2026), Example 1.2. https://arxiv.org/html/2610.00816v1
3. C. K. Fong and A. R. Sourour, *On the Operator Identity \(\sum A_kXB_k\equiv0\)*, Canadian Journal of Mathematics **31** (1979), 845–857, Theorem 2. https://doi.org/10.4153/CJM-1979-080-x
4. G. Andreolas and M. Anoussis, *Compact Multiplication Operators on Nest Algebras*, Journal of Operator Theory **77** (2017), 171–189, introduction. https://doi.org/10.7900/jot.2016mar10.2090
