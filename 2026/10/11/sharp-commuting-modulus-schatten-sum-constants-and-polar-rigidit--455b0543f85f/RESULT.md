# Sharp commuting-modulus Schatten sum constants and polar rigidity

## Finding
Let \(m\ge2\), \(n\ge1\), and let \(A_1,\ldots,A_m\in M_n(\mathbb C)\). Write \(P_k=|A_k|=(A_k^*A_k)^{1/2}\), assume that all \(P_k\) commute pairwise, and define \(S=\sum_{k=1}^mP_k\), \(T=\sum_{k=1}^mA_k\). For \(1\le p\le\infty\), use the Schatten norm, with \(\|\cdot\|_{S_\infty}\) the spectral norm. Then

\[
\|T\|_{S_p}\le K_{m,p}\|S\|_{S_p},\qquad
K_{m,p}=\begin{cases}1&1\le p\le2,\\ m^{1/2-1/p}&2\le p\le\infty.\end{cases}
\]

For each fixed \(m\) and \(p\) the constant is best possible uniformly over matrix dimensions. For \(1\le p<2\) and \(S\ne0\), equality occurs **exactly** when the matrices have a common left polar partial isometry: there is \(V\) such that \(V^*V=\operatorname{supp}S\) and \(A_k=VP_k\) for every \(k\). For \(p=2\), equality requires and is implied by alignment of the nonzero column vectors \(A_ke_j\) for each joint eigenvector \(e_j\); alignment directions may vary and need not be orthogonal for different indices.

## Assumptions and scope
The integers \(m\ge2\) and \(n\ge1\) are arbitrary; matrices are complex and finite-dimensional. The positive semidefinite moduli commute, not necessarily the original matrices or their polar factors. Here \(\operatorname{supp}S\) is the orthogonal projection onto the range of \(S\); in the zero case all the matrices vanish and the bound is trivial. The endpoint exponent is defined by \(1/\infty=0\). Only this commuting-modulus class is covered; no conclusion is drawn for arbitrary matrix families.

## Proof
**Simultaneous spectral coordinates.** The commuting positive operators have a common orthonormal eigenbasis \(e_1,\ldots,e_n\). Write \(P_ke_j=p_{kj}e_j\), \(p_{kj}\ge0\), and \(s_j=\sum_kp_{kj}\). Extend each polar partial isometry to a unitary \(U_k\), so that \(A_k=U_kP_k\). Put \(v_j=Te_j=\sum_kp_{kj}U_ke_j\). The triangle inequality gives \(\|v_j\|_2\le s_j\) for every \(j\).

**The concave range.** Let \(G=T^*T\). In the chosen basis \(G_{jj}=\|v_j\|_2^2\). For \(1\le p\le2\), Schur--Horn majorization and concavity of \(t\mapsto t^{p/2}\) imply
\[
\|T\|_{S_p}^{p}=\operatorname{Tr}G^{p/2}
\le\sum_{j=1}^nG_{jj}^{p/2}
=\sum_{j=1}^n\|v_j\|_2^p
\le\sum_{j=1}^ns_j^p=\|S\|_{S_p}^{p}.
\]
For \(1\le p<2\), strict concavity forces equality in the first inequality exactly when \(G\) is diagonal in the common eigenbasis, equivalently when the nonzero \(v_j\) are pairwise orthogonal. Equality in the second inequality forces \(\|v_j\|_2=s_j\) for every \(j\); the equality criterion in the Euclidean triangle inequality says that, whenever \(p_{kj}>0\), the vectors \(U_ke_j\) all equal a common unit vector \(w_j\). Hence \(v_j=s_jw_j\) and orthogonality of distinct nonzero columns gives orthonormal \(w_j\) for \(s_j>0\). Define \(Ve_j=w_j\) when \(s_j>0\) and \(Ve_j=0\) otherwise. This \(V\) is a partial isometry with \(V^*V=\operatorname{supp}S\), and \(A_ke_j=p_{kj}w_j=VP_ke_j\) for every index. Conversely a common \(V\) yields \(T=VS\), which has exactly the same nonzero singular values as \(S\). For \(p=2\), the first inequality is an identity, and only the columnwise Euclidean alignment condition remains.

**The convex range.** For \(s_j>0\) put \(w_{kj}=p_{kj}/s_j\), and for \(s_j=0\) put \(w_{kj}=0\). Define diagonal positive contractions \(W_ke_j=w_{kj}e_j\), and \(V_0=\sum_kU_kW_k\), so that \(T=V_0S\). On the space of diagonal matrices, consider the linear map \(\mathscr L(D)=V_0D\). Since \(\|V_0e_j\|_2\le\sum_kw_{kj}\le1\),
\[
\|\mathscr L(D)\|_{S_2}^2=\sum_j|D_{jj}|^2\|V_0e_j\|_2^2\le\|D\|_{S_2}^2.
\]
For any vector \(x\), by Cauchy--Schwarz and the fact that \(\sum_kw_{kj}^2\le1\) for each \(j\),
\[
\|V_0x\|_2\le\sum_k\|W_kx\|_2
\le\sqrt m\left(\sum_k\|W_kx\|_2^2\right)^{1/2}
\le\sqrt m\|x\|_2.
\]
Thus \(\|\mathscr L(D)\|_{S_\infty}\le\sqrt m\|D\|_{S_\infty}\). Complex interpolation of the compatible couples \((\ell_2^n,\ell_\infty^n)\) and \((S_2^n,S_\infty^n)\) gives, for \(2\le p\le\infty\),
\[
\|\mathscr L(D)\|_{S_p}\le m^{(1-2/p)/2}\|D\|_{S_p}
=m^{1/2-1/p}\|D\|_{S_p}.
\]
Apply this to the diagonal operator \(D=S\). The endpoint \(p=\infty\) is already included in the spectral bound.

**Sharpness.** For \(1\le p\le2\) choose nonzero positive commuting \(A_k=P_k\); then \(T=S\) and the ratio equals one. For \(2\le p\le\infty\) choose \(n=m\) and \(A_k=e_1e_k^*\). Then \(P_k=e_ke_k^*\) are pairwise orthogonal projections, \(S=I_m\), and \(T\) has precisely one nonzero singular value \(\sqrt m\). Consequently \(\|T\|_{S_p}/\|S\|_{S_p}=\sqrt m/m^{1/p}\), exactly the stated constant for all \(p\ge2\).

## Verification
Every inequality above is independent of any numerical experiment. A separate deterministic numerical script checks hundreds of random families with jointly diagonal moduli and verifies the extremal singular values, including exponents on both sides of two. Such finite tests detect implementation and algebraic mistakes but do not prove the universal assertion. Reproduce with a Python environment containing NumPy by running `python verify_commuting_moduli.py`.

## Relationship to prior work
Tang and Zhang, arXiv:2510.16846, formulate the unrestricted matrix-modulus sum inequality and determine its sharp Hilbert--Schmidt coefficient \(\sqrt{(1+\sqrt m)/2}\), strictly larger than one when \(m>1\). Zeng, Liu, and Ratnavelu, arXiv:2608.15558, examine a counterexample below the Hilbert exponent and sharp rank-one bounds above it; their inspected theorem statements treat unrestricted families or rank-one families, not pairwise commuting moduli. Zhang, arXiv:2603.01046, treats norms of symmetric variants of operator moduli rather than the present commutative-modulus restriction. This theorem is a restricted, sharp phase diagram with an accompanying polar-factor equality classification, not a claim to settle the unrestricted problem.

## Limitations
The theorem addresses only finite-dimensional complex matrices and commuting positive moduli. No claim is made about noncommuting moduli, non-Schatten symmetrically normed ideals, or equality classifications for \(p>2\). The dimension-free best constant can require dimension at least \(m\) for the exhibited sharpness witness. The comparison with the original 2025 preprint uses its available abstract and theorem synopsis; its full primary PDF was not available for material inspection, leaving residual risk of an equivalent observation there or in older matrix-inequality literature. The numerical verifier is not a replacement for the analytic proof, and no independent external validation is claimed.

## References
1. Q. Tang and S. Zhang, *Generalizing Lee's conjecture on the sum of absolute values of matrices*, arXiv:2510.16846 (first public October 19, 2025).
2. Z. Zeng, H. Liu and K. Ratnavelu, *A Counterexample to the Tang--Zhang Schatten Norm Conjecture and Sharp Positive Results*, arXiv:2608.15558; open text at https://www.preprints.org/manuscript/202608.1067 (2026).
3. T. Zhang, *Operator symmetric moduli and sharp triangle inequalities*, arXiv:2603.01046 (2026).
4. Classical tools: Schur--Horn majorization, strict Jensen concavity, and complex interpolation of Schatten ideals.
