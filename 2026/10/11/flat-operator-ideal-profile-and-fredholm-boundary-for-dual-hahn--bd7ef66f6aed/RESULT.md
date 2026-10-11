# Flat operator-ideal profile and Fredholm boundary for dual-Hahn convolution

## Finding

Let \(\mathbb N_0=\{0,1,2,\ldots\}\), and let \(\sigma_\infty\) be the complex Banach space
\[
\sigma_\infty=\left\{x:\ \|x\|_{\sigma_\infty}:=\sup_{m\ge0}\frac{1}{m+1}\left|\sum_{j=0}^{m}x_j\right|<\infty\right\}.
\]
For every \(a=(a_k)_{k\ge0}\in\ell_1(\mathbb N_0)\), define \((T_ax)_m=\sum_{k=0}^ma_kx_{m-k}\) and \(f_a(z)=\sum_{k\ge0}a_kz^k\). Write \(A=\sum_{k\ge0}|a_k|\).

**Theorem (flat ideal profile and Fredholm boundary).** For each integer \(n\ge1\),
\[
a_n(T_a)=b_n(T_a)=c_n(T_a)=A,
\qquad
\operatorname{dist}(T_a,\mathcal K(\sigma_\infty))=
\operatorname{dist}(T_a,\mathcal {SS}(\sigma_\infty))=A.
\]
Here \(a_n\) is the infimum of \(\|T_a-F\|\) over operators of rank less than \(n\); \(b_n\) is the supremum, over \(n\)-dimensional subspaces \(E\), of \(\inf_{x\in E,\|x\|=1}\|T_ax\|\); and \(c_n\) is the infimum of \(\|T_a|_M\|\) over closed subspaces of codimension less than \(n\). The ideals \(\mathcal K\) and \(\mathcal{SS}\) are respectively the compact and strictly singular bounded operators. For \(a\ne0\) and every \(\varepsilon>0\), there is a closed subspace \(E\subset\sigma_\infty\) isometric to \(\ell_\infty\) on which \(\|T_ax\|\ge(A-\varepsilon)\|x\|\).

With \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\mathbb T=\partial\mathbb D\), the *Fredholm* essential spectrum and index are
\[
\sigma_{\mathrm{ess},F}(T_a)=f_a(\mathbb T),\qquad
\operatorname{ind}(T_a-\lambda I)=-\sum_{\substack{z\in\mathbb D\\ f_a(z)=\lambda}}\operatorname{ord}_{z}(f_a-\lambda)
\quad(\lambda\notin f_a(\mathbb T)).
\]
The sum is finite; it is zero when there are no interior zeros. These statements include scalar convolution operators (also \(a=0\)). The known ordinary spectrum is \(f_a(\overline{\mathbb D})\). Thus already for the shift symbol \(f_a(z)=z\), the ordinary spectrum is a closed disk while the Fredholm essential spectrum is only its boundary circle.

## Assumptions and scope

Sequences and operators are complex, with indices starting at zero. The coefficient condition \(a\in\ell_1\) is necessary and sufficient for bounded convolution on this space in the cited primary literature. The stated essential spectrum uses the *Fredholm* definition: \(\lambda\) belongs to it exactly when \(T_a-\lambda I\) fails to have closed range and finite-dimensional kernel and cokernel. No equality with other conventions for essential spectra is implied. The index is \(\dim\ker(T_a-\lambda I)-\operatorname{codim}\operatorname{ran}(T_a-\lambda I)\). No finite-support assumption on \(a\) is imposed.

## Proof

**1. Isometric coordinates and compact shift defect.** Set \((Ux)_m=(m+1)^{-1}\sum_{j=0}^m x_j\). This defines a surjective linear isometry \(U:\sigma_\infty\to\ell_\infty(\mathbb N_0)\), since its explicit inverse is \(x_m=(m+1)y_m-my_{m-1}\), with \(y_{-1}=0\). Let \(R\) denote the right shift on \(\sigma_\infty\), \((Rx)_0=0\) and \((Rx)_m=x_{m-1}\) for \(m\ge1\). Then \(W=URU^{-1}\) obeys
\[
(Wy)_0=0,\quad (Wy)_m=\frac{m}{m+1}y_{m-1}\ (m\ge1),\quad
(W^ky)_m=\mathbf1_{m\ge k}\frac{m-k+1}{m+1}y_{m-k}.
\]
In particular \(\|W\|\le1\). Denote by \(S\) the unweighted right shift on \(\ell_\infty\). The operator \(W-S\) is compact: its nonzero coordinate weights have magnitudes \((m+1)^{-1}\to0\), and truncation to finitely many output coordinates gives finite-rank approximants converging in operator norm. Since \(T_a=\sum_{k\ge0}a_kR^k\) in operator norm, conjugating yields \(UT_aU^{-1}=f_a(W)\), and
\[
f_a(W)-f_a(S)=\sum_{k\ge0}a_k(W^k-S^k)\in\mathcal K(\ell_\infty).
\]
Each difference of powers is compact, and the absolutely convergent sum is compact because the compact ideal is norm closed. The power series also gives \(\|T_a\|\le A\).

**2. Uniform block lower estimate.** First suppose \(A>0\). Fix \(\varepsilon>0\) and an integer \(N\ge0\) such that \(\tau_N:=\sum_{k>N}|a_k|<\varepsilon\), with at least one \(a_k\ne0\) among the first \(N+1\) coefficients. Put \(\omega_k=\overline{a_k}/|a_k|\) when \(a_k\ne0\), and \(\omega_k=1\) otherwise. Choose increasing integers \(m_j\) such that the finite blocks \(B_j=\{m_j-N,\ldots,m_j\}\) are pairwise disjoint, \(m_1\ge N\), and \(N A/(m_1+1)<\varepsilon\). For every \(c=(c_j)\in\ell_\infty\), define \(y_c\in\ell_\infty\) by
\[
(y_c)_{m_j-k}=c_j\omega_k\quad(0\le k\le N),\qquad
(y_c)_i=0\quad\text{outside the blocks}.
\]
This is a linear isometry from \(\ell_\infty\) onto the closed block subspace \(E_\varepsilon\). At output coordinate \(m_j\), the contributions from its own block and indices \(0\le k\le N\) add with the phase of \(c_j\), and their total modulus is at least \((A-\tau_N-\varepsilon)|c_j|\). All possible contributions from earlier blocks have convolution indices \(k>N\), whose total modulus is at most \(\tau_N\|c\|_\infty\). Later blocks cannot affect output coordinate \(m_j\). Consequently
\[
\|f_a(W)y_c\|_\infty
\ge (A-\tau_N-\varepsilon)\sup_j|c_j|-\tau_N\|c\|_\infty
\ge(A-3\varepsilon)\|c\|_\infty.
\]
Because \(\varepsilon\) was arbitrary, \(\|T_a\|=A\), and the same construction gives the asserted isometric \(\ell_\infty\) lower-bound subspaces (replacing \(3\varepsilon\) by the desired tolerance).

**3. Flat approximation, Bernstein, Gelfand and ideal distances.** For every finite \(n\), the subspace of \(E_\varepsilon\) consisting of vectors supported on its first \(n\) blocks has dimension \(n\) and carries the same lower bound. Thus \(b_n(T_a)\ge A-3\varepsilon\), so \(b_n(T_a)=A\). If \(F\) has rank below \(n\), its restriction to this \(n\)-dimensional subspace has a nonzero kernel vector; hence \(\|T_a-F\|\ge A-3\varepsilon\) and \(a_n(T_a)=A\). If \(M\) has codimension below \(n\), it intersects the same \(n\)-dimensional subspace nontrivially, yielding \(\|T_a|_M\|\ge A-3\varepsilon\) and \(c_n(T_a)=A\). Upper bounds in every case follow from \(\|T_a\|=A\).

Let \(J\) be strictly singular. Such an operator cannot be bounded below on the infinite-dimensional space \(U^{-1}E_\varepsilon\). For every \(\delta>0\) it therefore has a unit vector there on which \(\|Jx\|<\delta\); hence \(\|T_a-J\|\ge A-3\varepsilon-\delta\). It follows that \(\operatorname{dist}(T_a,\mathcal {SS})=A\). Since every compact operator is strictly singular, \(\operatorname{dist}(T_a,\mathcal K)=A\) too. If \(a=0\), all assertions in Steps 2 and 3 hold trivially with \(A=0\).

**4. Fredholm shift model away from the unit circle.** Let \(L:\ell_\infty\to\ell_\infty\) be the left shift, \((Ly)_m=y_{m+1}\); then \(LS=I\) and \(SL=I-P_0\), where \(P_0\) is the rank-one projection onto the first coordinate. If \(|\alpha|<1\), then \(I-\alpha L\) is invertible and
\[
S-\alpha I=S(I-\alpha L)-\alpha P_0.
\]
Consequently \(S-\alpha I\) is Fredholm of index \(-1\), by finite-rank invariance from the right shift \(S\), whose range has codimension one and kernel zero. If \(|\alpha|>1\), a Neumann series makes \(S-\alpha I\) invertible.

Fix \(\lambda\notin f_a(\mathbb T)\). The analytic Wiener function \(f_a-\lambda\) is nonzero on the unit circle. It has finitely many zeros \(\alpha_1,\ldots,\alpha_q\) in \(\mathbb D\), counted with multiplicity; the absence of zeros near the compact boundary and isolation of analytic zeros ensure finiteness. Dividing successively by \(z-\alpha_j\) remains inside the analytic Wiener algebra, since the quotient of \(f(z)-f(\alpha)\) by \(z-\alpha\) has absolutely summable coefficients bounded in absolute sum by \(\sum_{k\ge1}|a_k|/(1-|\alpha|)\). Thus
\[
f_a(z)-\lambda=\prod_{j=1}^q(z-\alpha_j)g(z),
\]
where \(g\) belongs to the analytic Wiener algebra and is nonvanishing on the closed disk. The analytic Wiener inverse lemma implies \(1/g\) also belongs to this algebra, so \(g(S)\) is invertible. Therefore \(f_a(S)-\lambda I\) is Fredholm with index \(-q\). The compact equivalence from Step 1 carries this Fredholm property and index to \(T_a-\lambda I\).

**5. Failure of Fredholmness on the boundary image.** Let \(\lambda=f_a(\zeta)\) for some \(\zeta\in\mathbb T\). Choose pairwise disjoint finite intervals escaping to infinity and on the \(j\)-th interval place \(v^{(j)}_m=\zeta^{-m}h_j(m)\), where \(h_j\) is a nonnegative discrete triangular tent of maximum one, zero outside its interval and with adjacent-value differences at most \(1/j\). Then \(\|v^{(j)}\|_\infty=1\) and \(\|(S-\zeta I)v^{(j)}\|_\infty\le1/j\). Polynomial approximation of \(f_a\) in the analytic Wiener norm implies \(\|(f_a(S)-\lambda I)v^{(j)}\|_\infty\to0\): for each fixed power the shift defect telescopes, and the \(\ell_1\) coefficient tail is uniformly negligible. The vectors \(v^{(j)}\) are weakly null. Indeed, for any continuous linear functional \(\varphi\) on \(\ell_\infty\), the disjoint support property implies \(\sum_{j=1}^J|\varphi(v^{(j)})|\le\|\varphi\|\) for each \(J\), by aligning phases of the disjoint blocks; thus \(\varphi(v^{(j)})\to0\). If \(f_a(S)-\lambda I\) were Fredholm, Atkinson's theorem would provide bounded \(B\) and compact \(K\) with \(B(f_a(S)-\lambda I)=I-K\); applying this identity to \(v^{(j)}\) contradicts their unit norms because \(Kv^{(j)}\to0\). Hence \(\lambda\) belongs to the Fredholm essential spectrum. Step 1 and compact invariance yield \(\sigma_{\mathrm{ess},F}(T_a)=f_a(\mathbb T)\), completing the proof.

## Verification

The conjugacy and telescoping formulas in Step 1 are exact coordinate identities. The block proof controls the infinite \(\ell_1\) tail uniformly in all bounded block coefficients; it is not based on finite computation or on a limiting matrix experiment. The analytic Wiener division estimate and standard inverse theorem justify the factorization even for nonpolynomial symbols. For an elementary finite support sanity check, with \(a_0=1\), \(a_1=-1/2\), \(a_2=i/5\) and output index \(m=1000\), the phase-aligned test yields modulus \(1.6991008991008991\), compared with coefficient mass \(1.7\). This numerical illustration is not used to establish an infinite-dimensional conclusion.

## Relationship to prior work

Saha and Patra (arXiv:2610.02919v1, §§2–4) define the same \(\sigma_\infty\), give the convolution representation, cite the pre-existing exact norm \(\|T_a\|=\|a\|_1\), and determine the ordinary and fine spectra. Those are **prior inputs**, not the present novelty. The theorem above distinguishes the Fredholm boundary from the usually larger ordinary spectral image and proves a complete flat approximation/Bernstein/Gelfand and strictly-singular-distance profile. The earlier Saha–Patra work on weighted Hahn spaces (arXiv:2606.22912) discusses boundedness and compactness, but its complete text was not available for definitive implication comparison. Curbera–Ricker's study of convolution on dual Cesàro spaces \(d_p\) concerns different Banach sequence norms and does not state this profile on \(\sigma_\infty\). Standard Wiener–Hopf index theory supplies the familiar analytic factorization mechanism; its applicability here rests on the explicitly proved compactly weighted shift model. No assertion of priority beyond the inspected literature is made.

## Limitations

The result concerns only one-sided convolution with absolutely summable complex coefficients on the unweighted dual-Hahn space \(\sigma_\infty\). It does not classify all multipliers on general weighted Hahn spaces, arbitrary Toeplitz matrices, other essential-spectrum conventions, or non-absolutely-summable symbols. The norm and ordinary-spectrum formulas are previously known. The accessible abstract of arXiv:2606.22912 does not suffice to exclude all indirect coverage from its inaccessible full text; this remains a literature risk. No independent external audit has been performed.

## References

1. S. Saha and A. Patra, *Spectral Properties of Convolution Operators on Non-Separable Sequence Spaces*, arXiv:2610.02919v1 (first public 2026-10-02), especially §§2–4.
2. S. Saha and A. Patra, *Convolution Operators on Weighted Hahn Spaces*, arXiv:2606.22912v1 (first public 2026-06-22); complete full-text comparison unavailable.
3. G. P. Curbera and W. J. Ricker, *Convolution in Dual Cesàro Sequence Spaces*, arXiv:2302.08745v1 (2023), especially §§1, 2 and 6.
4. Standard analytic Wiener inverse theorem and Fredholm/Atkinson theory; for Wiener–Hopf context, M. C. Câmara, *Toeplitz operators and Wiener–Hopf factorisation: an introduction*, arXiv:1710.11572 (2017).
