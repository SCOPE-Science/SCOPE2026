# Bounded exponential Fock commutators: an anti-diagonal criterion and exact essential norms

## Finding

Let \(\mathcal F^2\) be the Gaussian Fock space in one complex variable, and let \(f,g,h,k\) be arbitrary finite exponential polynomials, i.e. finite linear combinations of functions \(z\mapsto e^{az}\) with complex frequencies. Define, on the common dense exponential-kernel domain,
\[
C=[T_{f+\overline{k}},T_{h+\overline{g}}].
\]
Write \(f(z)=\sum_a f_a e^{az}\), and similarly for \(g,h,k\), with missing coefficients interpreted as zero. Define the finitely supported coefficient array
\[
q_{a,b}=(1-e^{a\overline b})(f_a\overline{g_b}-h_a\overline{k_b}).
\]
After combining every occurrence of each frequency pair, the following are equivalent:

1. The densely defined commutator \(C\) has a bounded extension to \(\mathcal F^2\).
2. \(q_{a,b}=0\) for all frequency pairs satisfying \(a+b\ne0\).

When these equivalent conditions hold, the extension is a finite sum of Fock Weyl unitaries,
\[
C=\sum_a d_a W_{\overline a},\qquad
 d_a=e^{|a|^2/2}q_{a,-a},\qquad
 (W_\xi u)(z)=e^{z\overline\xi-|\xi|^2/2}u(z-\xi).
\]
Every such bounded commutator has **exact essential norm equal to its operator norm**:
\[
\boxed{\|C\|_{\mathrm{ess}}=\|C\|.}
\]
In particular, it is compact if and only if it vanishes. If at most two distinct coefficients \(d_a\) survive, its exact norm is
\[
\boxed{\|C\|=\|C\|_{\mathrm{ess}}=\sum_a|d_a|.}
\]
For two distinct nonzero parameters \(a,b\in\mathbb C\), a concrete nonzero-commutator family is
\[
U=T_{e^{az}+\overline{e^{-bz}}},\qquad
V=T_{e^{bz}+\overline{e^{-az}}},
\]
with
\[
\boxed{\|[U,V]\|=\|[U,V]\|_{\mathrm{ess}}=
2\sinh(|a|^2/2)+2\sinh(|b|^2/2).}
\]
The individual Toeplitz operators in this displayed pair are generally unbounded; their commutator on the common invariant domain nevertheless extends boundedly. The bracket denotes this extension, not a commutator of everywhere-defined bounded operators.

## Assumptions and scope

The Hilbert space is
\[
\mathcal F^2=\left\{u\text{ entire}:\frac1\pi\int_{\mathbb C}|u(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
The Toeplitz operator \(T_\phi=P M_\phi\) uses the orthogonal Gaussian Fock projection, initially on the dense linear span \(\mathcal D\) of the exponential kernels \(K_w(z)=e^{z\overline w}\). All finite sums of exponential Toeplitz symbols preserve \(\mathcal D\), and so do their finite products and commutators. Thus all statements about bounded extension have their usual unique meaning.

The coefficient indices \(a,b\) range over a finite union of the supports of the four exponential polynomials; repeated equal frequencies must be combined before defining \(q_{a,b}\). No assumption of real frequencies, disjoint supports, nonzero symbols, or absence of cancellations is made. In the two-frequency exact-norm clause the distinctness of the surviving frequencies is required; coinciding frequencies must first be combined. Zero coefficients and the zero commutator are included.

## Proof

**1. Dense-domain reduction.** The Gaussian reproducing formula implies
\[
(T_{\overline{e^{bz}}}u)(z)=u(z+\overline b),\qquad
(T_{e^{az}}u)(z)=e^{az}u(z)
\]
on \(\mathcal D\). Consequently, on the same domain,
\[
[T_{e^{az}},T_{\overline{e^{bz}}}]u(z)
=(1-e^{a\overline b})e^{az}u(z+\overline b).
\]
Analytic–analytic and coanalytic–coanalytic Toeplitz operators commute on \(\mathcal D\). Bilinearity and frequency collection yield
\[
(Cu)(z)=\sum_{a,b}q_{a,b}e^{az}u(z+\overline b).
\tag{1}
\]
The equation is an identity of actual entire functions on \(\mathcal D\), not merely a formal matrix expansion.

**2. Detecting all unbounded frequencies.** For \(w\in\mathbb C\), let
\(k_w(z)=e^{z\overline w-|w|^2/2}\) be the normalized kernel. Direct evaluation of (1) gives
\[
\langle Ck_w,k_w\rangle
=P(w):=\sum_{a,b}q_{a,b}e^{aw+\overline b\,\overline w}.
\tag{2}
\]
If \(C\) extends boundedly, \(|P(w)|\le\|C\|\) for every \(w\).

Here is the needed finite-exponential lemma, including possible coincident real growth rates. For a finite sum of distinct characters
\[
P(w)=\sum_jc_j e^{a_jw+\overline{b_j}\overline w},
\]
with pairs \((a_j,b_j)\) distinct and coefficients nonzero, boundedness on \(\mathbb C\) forces \(a_j+b_j=0\) for each term. To prove it, put \(s_j=a_j+b_j\). If some \(s_j\ne0\), choose a nonzero exposed vertex of the convex hull of the finite set of \(s_j\), and a generic direction \(\theta\) for which the exposed maximal growth
\(m=\max_j\operatorname{Re}(s_je^{i\theta})\) is strictly positive. By avoiding finitely many additional directions, terms having the same \(s_j\) have distinct oscillation rates along \(w=te^{i\theta}\). After division by \(e^{mt}\), all slower terms vanish exponentially, while the leading terms form a nonzero finite trigonometric polynomial in \(t\). The mean-square average of this polynomial on long intervals is the sum of the squares of its nonzero coefficients. Thus its absolute value has positive limsup; \(P(te^{i\theta})\) is unbounded. This contradiction proves the lemma. The converse is immediate: if \(b_j=-a_j\), each exponential has modulus one. Applying the lemma to (2) proves that boundedness forces \(q_{a,b}=0\) when \(a+b\ne0\).

**3. Weyl representation and sufficiency.** The operators \(W_\xi\) defined above are unitary, as follows directly by changing variables in the Gaussian norm. When \(b=-a\),
\[
e^{az}u(z-\overline a)=e^{|a|^2/2}W_{\overline a}u(z).
\]
Hence (1), with only anti-diagonal pairs, becomes the asserted finite Weyl sum. It extends boundedly with norm at most \(\sum_a|d_a|\), proving the converse implication.

**4. Essential norm and compactness.** For every fixed vector \(v\in\mathcal F^2\), and any sequence \(\xi_j\in\mathbb C\) with \(|\xi_j|\to\infty\), one has \(W_{\xi_j}v\rightharpoonup0\). It suffices to verify this on coherent kernels, where the Gaussian kernel-overlap formula decays as their centers separate, then use density and unitarity. Weyl commutation gives, for each fixed displacement \(\eta\),
\[
W_\xi^*W_\eta W_\xi=\chi_\eta(\xi)W_\eta,
\qquad |\chi_\eta(\xi)|=1.
\]
For \(C=\sum_a d_aW_{\overline a}\), pass to a subsequence along which the finitely many phases converge. Then
\(W_{\xi_j}^*CW_{\xi_j}\to B\) in operator norm, where \(B\) is another finite Weyl sum, and \(\|B\|=\|C\|\), since all conjugates have norm \(\|C\|\).

For any compact \(K\) and unit vector \(v\), compactness plus weak convergence gives \(KW_{\xi_j}v\to0\). Therefore
\[
\|C+K\|\ge\lim_j\|(C+K)W_{\xi_j}v\|
=\lim_j\|W_{\xi_j}^*CW_{\xi_j}v\|=\|Bv\|.
\]
Taking the supremum over \(v\) proves \(\|C+K\|\ge\|C\|\) for every compact \(K\), and the reverse bound follows by taking \(K=0\). Thus the essential-norm equality holds. An operator is compact exactly when its essential norm vanishes, giving the stated compactness dichotomy.

**5. Sharp two-frequency norm.** If two displacements \(\xi\ne\eta\) occur, factor out the first Weyl unitary. Up to a scalar phase, the remaining operator is \(cI+dW_{\eta-\xi}\). The spectrum of any nonzero-displacement Weyl unitary is the entire unit circle: its spectrum is a nonempty subset of that circle, and conjugation by Weyl unitaries rotates it by every unimodular factor. For this normal operator, the spectral theorem gives
\[
\|cI+dW_{\eta-\xi}\|=\sup_{|\zeta|=1}|c+d\zeta|=|c|+|d|.
\]
The one-frequency and zero-frequency cases are immediate. This proves the sharp formula.

Finally, in the two-parameter example the only surviving coefficients have pairs \((a,-a)\) and \((b,-b)\), with opposite signs. Each coefficient has modulus
\[
(1-e^{-|a|^2})e^{|a|^2/2}=2\sinh(|a|^2/2),
\]
and similarly for \(b\). The two-frequency theorem supplies the displayed exact norm and essential norm.

## Verification

The proof above verifies the infinite-dimensional assertions independently of finite experiments. The companion `checker.py`, run with Python's standard library, independently expands both Toeplitz orders on exponential test functions, compares all four finite exponential sums with (1), checks the Weyl normalization in (3), and checks the sharp example's hyperbolic-sine coefficients. It reports 1775 passing finite diagnostic assertions. The finite diagnostics are not used to infer the finite-exponential lemma, essential-norm equality, or spectral-circle theorem; those are established analytically in Steps 2, 4, and 5.

To reproduce the finite diagnostics, run `python checker.py`. Reproduction requires no data download or external package.

## Relationship to prior work

Qin, Liu and Huang (2026) corrected the characterization of *vanishing* commutators with harmonic Fock Toeplitz symbols of exponential type. Their coefficient cancellation mechanism motivates considering finite exponential frequencies, but their Theorems 4.1–4.2 do not give boundedness or essential norms of **nonzero** commutators. The present theorem identifies exactly which nonzero commutators have bounded extensions and how they sit relative to compact operators.

Cho, Park and Zhu (2012), Main Theorem and Lemma 1, characterize when a *single product* \(T_fT_{\overline g}\) is bounded and identify opposite linear exponentials with Weyl unitaries. That case underlies the Weyl representation here, but it does not account for cancellations between four exponential-polynomial symbols nor determine the essential norm of an arbitrary finite Weyl sum. Earlier Bauer–Choe–Koo (2015) addresses commutation/Berezin fixed points; access to its entire 44-page text was unavailable for a definitive negative priority comparison.

## Limitations

This theorem is for finite **pure** exponential sums in one variable, not polynomial-times-exponential symbols or arbitrary exponential-type entire functions. It proves the complete boundedness/compactness classification and essential-norm identity for any finite number of frequencies, but evaluates the common operator/essential norm explicitly as a coefficient \(\ell^1\) sum only when at most two distinct anti-diagonal frequencies survive. For three or more frequencies the norm of the finite Weyl sum remains a separate spectral problem. Existing general Weyl-operator or almost-periodic operator theory could contain equivalent operator-algebraic statements, and the complete 2015 commutator paper was not inspected; publication priority remains subject to verification.

## References

1. J. Qin, Y. Liu and S. Huang, *Commuting Toeplitz operators with harmonic symbols on the Fock space*, arXiv:2610.22136v1, first posted 15 October 2026. https://arxiv.org/html/2610.22136v1
2. H. R. Cho, J.-D. Park and K. Zhu, *Products of Toeplitz operators on the Fock space*, arXiv:1212.0045v1, first posted 30 November 2012. https://arxiv.org/html/1212.0045v1
3. W. Bauer, B. R. Choe and H. Koo, *Commuting Toeplitz operators with pluriharmonic symbols on the Fock space*, J. Funct. Anal. 268 (2015), 3017–3060. https://doi.org/10.1016/j.jfa.2015.03.003
4. S. Wu and D. Zheng, *Toeplitz operators on the Fock space via the Fourier transform*, arXiv:2103.03458, 2021. https://arxiv.org/abs/2103.03458
