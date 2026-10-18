# Dimension-free leverage control of E-optimal two-row Krylov sketch distortion

## Finding
For two-row restrictions of a real orthonormal two-column Krylov basis, the global minimum-singular-value objective can differ from the minimum subspace-distortion objective. A previously established worst-case separation grows with ambient dimension. Here the sharper question is whether **row leverage imbalance**, rather than ambient dimension, controls this difference: the answer is a dimension-free inequality, with exact agreement at equal leverage and a quantitatively small discrepancy for nearly uniform leverage.

**Theorem.** Let \(n\ge2\) and \(Q\in\mathbb R^{n\times2}\) satisfy \(Q^{\mathsf T}Q=I_2\), with every row nonzero. Write \(\ell_i=\|e_i^{\mathsf T}Q\|_2^2\) and \(\rho=\max_i\ell_i/\min_i\ell_i\). Among all distinct two-row selections \(S\) for which \(SQ\) is invertible, let \(S_E\) maximize \(\sigma_{\min}(SQ)\), and let \(S_D\) minimize \(\kappa_2(SQ)\). Then every such pair of optimizers satisfies

\[
\kappa_2(S_EQ)^2\le\rho\bigl(\kappa_2(S_DQ)^2+1\bigr)-1,
\qquad
\frac{\kappa_2(S_EQ)}{\kappa_2(S_DQ)}\le\sqrt{2\rho-1}.
\]

In particular, at equal leverage \(\rho=1\), the E-optimal and distortion-optimal sets of selections are identical.

The square-root dependence on leverage imbalance is unavoidable in order. A concrete family, of the same general kind as earlier dimension-dependent separation constructions, also realizes a genuine two-dimensional Krylov subspace of a real symmetric nonsingular matrix. For every integer \(n\ge5\), define the columns \(u_n,v_n\) of \(Q_n\in\mathbb R^{n\times2}\) by

\[
 u_n=\frac{\sqrt n\,e_1+e_3}{\sqrt{n+1}},\qquad
 v_n=\frac{2e_2+\sum_{j=4}^{n}e_j}{\sqrt{n+1}}.
\]

Then \(Q_n^{\mathsf T}Q_n=I_2\), its leverage ratio is \(\rho=n\), and the **unique** E-optimal two-row selection is \(\{1,2\}\), with \(\kappa_2(S_EQ_n)=\sqrt n/2\). A distortion-optimal selection takes \(\{3,j\}\) with any \(4\le j\le n\), and has \(\kappa_2(S_DQ_n)=1\). Thus

\[
\frac{\kappa_2(S_EQ_n)}{\min_S\kappa_2(SQ_n)}=\frac{\sqrt\rho}{2}
\longrightarrow\infty.
\]

## Assumptions and scope
The row-selection matrix \(S\) consists of two distinct rows of an identity matrix; no row scaling, repeated index, or oversampling is allowed. Condition numbers are spectral singular-value ratios, computed only for nonsingular selected submatrices. All entries are real and operations are exact. Each row leverage is strictly positive, ensuring \(\rho<\infty\). Since \(Q\) has rank two, at least one admissible pair exists. The bound holds for any choices among tied optimizers.

The constructed symmetric matrix in the last part is

\[
A_n=u_nv_n^{\mathsf T}+v_nu_n^{\mathsf T}+
2(I_n-u_nu_n^{\mathsf T}-v_nv_n^{\mathsf T}).
\]

It is symmetric and invertible, with eigenvalues \(1,-1\) on \(\operatorname{span}\{u_n,v_n\}\) and eigenvalue \(2\) on its orthogonal complement. With initial vector \(b_n=u_n\), the two-step Arnoldi/Lanczos basis is exactly \(Q_n\), because \(A_nu_n=v_n\) and \(u_n^{\mathsf T}v_n=0\).

## Proof
**Universal leverage bound.** For a full-rank selected matrix \(T=SQ\), put \(m(T)=\sigma_{\min}(T)^2\), \(h(T)=\sigma_{\max}(T)^2\), and \(F(T)=\|T\|_F^2\). For two columns, exactly \(F(T)=m(T)+h(T)\) and hence \(\kappa_2(T)^2=F(T)/m(T)-1\). The E-optimality of \(S_E\) gives \(m(S_EQ)\ge m(S_DQ)\). For any two rows, \(2\min_i\ell_i\le F(SQ)\le2\max_i\ell_i\), so \(F(S_EQ)\le\rho F(S_DQ)\). Therefore

\[
\begin{aligned}
\kappa_2(S_EQ)^2
&=\frac{F(S_EQ)}{m(S_EQ)}-1
\\&\le\rho\frac{F(S_DQ)}{m(S_DQ)}-1
=\rho\bigl(\kappa_2(S_DQ)^2+1\bigr)-1.
\end{aligned}
\]

As \(\kappa_2(S_DQ)\ge1\), division by its square gives

\[
\left(\frac{\kappa_2(S_EQ)}{\kappa_2(S_DQ)}\right)^2
\le\rho+\frac{\rho-1}{\kappa_2(S_DQ)^2}\le2\rho-1.
\]

At \(\rho=1\), all two-row submatrices have the same squared Frobenius norm. On this fixed-trace class, \(\kappa_2(T)^2=F(T)/m(T)-1\) strictly decreases as \(m(T)\) increases; hence the E-optimal and distortion-optimal selections coincide, including ties.

**Exact family.** The supports of \(u_n\) and \(v_n\) are disjoint, and each has squared norm one, so the columns of \(Q_n\) are orthonormal. Its squared row norms are \(n/(n+1)\) at index \(1\), \(4/(n+1)\) at index \(2\), and \(1/(n+1)\) elsewhere; because \(n\ge5\), \(\rho=n\). A full-rank two-row selection necessarily contains one index from \(\{1,3\}\) and one from \(\{2,4,\dots,n\}\). The four possible absolute diagonal pairs, after multiplication by \(\sqrt{n+1}\), are

\[
(\sqrt n,2),\quad(\sqrt n,1),\quad(1,2),\quad(1,1).
\]

Their minimum singular values, in the same units, are respectively \(2,1,1,1\); thus \(\{1,2\}\) uniquely maximizes the minimum singular value. Their condition numbers are respectively \(\sqrt n/2,\sqrt n,2,1\), so the minimum possible distortion is one, attained exactly at the last type. The displayed gap follows; it demonstrates the sharp exponent in the leverage-sensitive estimate, without claiming discovery of the earlier dimension-dependent separation. Finally, direct multiplication yields \(A_nu_n=v_n\), \(A_nv_n=u_n\); the remaining spectral assertions follow from the orthogonal decomposition. Therefore this is a two-vector symmetric Krylov construction, not merely an abstract frame.

## Verification
The standalone program `reproduce.py` independently constructs the exact rational-radical family using symbolic arithmetic and checks its frame identities, exhaustive two-row choices for dimensions \(5\le n\le15\), and its symmetric Krylov realization. It also tests the leverage bound on 1,320 independently generated real orthonormal frames. The recorded execution returned `PASS 231 symbolic family and Krylov checks; 1320 random-frame bound checks`. Symbolic verification in finitely many dimensions and randomized testing corroborate, but do not replace, the analytic argument for all eligible dimensions.

## Relationship to prior work
Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (first publicly posted April 8, 2026), studies coordinate sketches and relates the distortion of a whitened Krylov basis to the condition number of its sampled restriction. The paper explicitly uses maximizing the minimum singular value as a useful design surrogate and reports conditioning differences among practical heuristics. A previously published mathematical finding entitled *A sharp-order E-versus-K row-selection gap for two-dimensional orthonormal frames* (record identifier c6e6e137-5749-46ec-a56f-965b079a30f5) already proves that global E-optimal row restriction can have a distortion gap of order \(\sqrt n\), even on a Krylov-realizable frame. That dimension-based gap is **prior work**, not claimed here. The distinct new assertion is the leverage-sensitive dimension-free inequality and exact equivalence at uniform leverage; the previous dimension-only result does not imply either statement and is compatible with the present improvement when \(\rho\) remains bounded as dimension grows.

Drmač and Gugercin (2016), arXiv:1505.00370, develop QR-based DEIM point selection and bounds involving an inverse smallest singular value. Those bounds measure interpolation stability, a legitimate objective distinct from the condition number of the sampled subspace. The sensor-selection work of Uciński and Patan (2022) expressly compares E-efficiency and condition-number optimization, so possible coverage of a related general inequality remains a bibliographic risk; its full paper was not available for material comparison here. None of these distinctions implies that an E-optimal choice is poor for its own stated inverse-norm objective.

## Limitations
The leverage-dependent theorem concerns only unweighted selection of exactly two rows from a real orthonormal two-column basis, and the induced spectral distortion, not actual convergence of a Krylov linear solver. The upper constant \(\sqrt{2\rho-1}\) is not claimed sharp; only the exponent \(1/2\) in leverage imbalance is proved sharp in order. No analogous classification is asserted for higher-dimensional subspaces, more selected rows, row-rescaled sketches, noise, or finite-precision arithmetic. A previously published general E-efficiency-versus-conditioning comparison could subsume some of the quantitative analysis, and material comparison to the inaccessible 2022 source remains outstanding. The previously established dimension-dependent gap is explicitly acknowledged and is not a new contribution here.

## References
1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1, first posted April 8, 2026. https://arxiv.org/abs/2604.07158
2. Z. Drmač and S. Gugercin, *A new selection operator for the discrete empirical interpolation method—improved a priori error bound and extensions*, SIAM Journal on Scientific Computing 38 (2016), A631–A648. arXiv:1505.00370; DOI:10.1137/15M1019271. https://arxiv.org/abs/1505.00370
3. *A sharp-order E-versus-K row-selection gap for two-dimensional orthonormal frames*, previously published mathematical research record, identifier c6e6e137-5749-46ec-a56f-965b079a30f5 (2026); cited for the dimension-dependent comparison, not the leverage-controlled result.
4. D. Uciński and M. Patan, *Sensor Selection for Minimizing the Condition Number with Guaranteed E-Efficiency*, 61st IEEE Conference on Decision and Control (2022). DOI:10.1109/CDC51059.2022.9992335.
