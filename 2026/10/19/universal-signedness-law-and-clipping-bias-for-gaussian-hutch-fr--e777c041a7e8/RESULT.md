# Signed limit and clipping bias at high effective rank for Gaussian Hutch#

## Finding
For a nonzero real matrix \(A\) and a positive integer \(r\), let \(\Omega\) and \(\Psi\) be independent standard Gaussian sketch matrices with \(r\) columns and respectively as many rows as \(A\) has columns and rows. Define
\[
F(A)=\|A\|_F^2,\qquad
H_r(A)=\frac{\|A\Omega\|_F^2+\|\Psi^{\mathsf T} A\|_F^2}{r}
-\frac{\|\Psi^{\mathsf T} A\Omega\|_F^2}{r^2},\qquad H_r^+(A)=\max(0,H_r(A)).
\]
Suppose \(A_j\) are nonzero deterministic real matrices of arbitrary, possibly changing dimensions, and
\[
R_j=\frac{F(A_j)^2}{\operatorname{tr}((A_j^{\mathsf T}A_j)^2)}\longrightarrow\infty .
\]
Then for every fixed \(r\),
\[
\frac{H_r(A_j)}{F(A_j)}\xrightarrow{\mathrm{law}}2-\frac{\chi^2_{r^2}}{r^2} .
\]
In particular, writing \(q_r=\Pr(\chi^2_{r^2}>2r^2)\), one has
\[
\begin{aligned}
\lim_j\Pr(H_r(A_j)<0)&=q_r>0,\\
\lim_j\frac{\mathbb E H_r^+(A_j)-F(A_j)}{F(A_j)}
&=\Pr(\chi^2_{r^2+2}>2r^2)-2q_r>0 .
\end{aligned}
\]
For example, at \(r=1\) the sign probability is \(0.157299207050\ldots\) and the relative clipping bias is \(0.257808290370\ldots\). For the resulting limiting sign probabilities, as \(r\to\infty\),
\[
q_r\sim\frac{1}{\sqrt{\pi}\, r}\exp\!\left[-\frac{1-\log 2}{2}r^2\right].
\]

## Assumptions and scope
All sketches are real and have independent standard normal entries, with independent sketches on the two sides. The estimator is the unweighted nonadaptive Hutch# estimator of the **squared** Frobenius norm. The dimension and spectrum of \(A_j\) can vary subject to \(R_j\to\infty\). The effective-rank limit takes \(j\to\infty\) at fixed \(r\); the large-\(r\) expansion is only for the resulting limits and asserts no joint asymptotic. The theorem is not about other sketches or about weighted Hutch#.

## Proof
**Limit in law.** By orthogonal invariance, for each \(j\) write \(\sigma_i\) for the nonzero singular values and let \(X_i,Y_i\) be independent \(N(0,I_r)\) vectors for each singular direction, all independent across directions. Put \(F_j=\sum_i\sigma_i^2\) and \(S_j=\sum_i\sigma_i^4\). In these coordinates the two positive terms of \(H_r/F_j\) are \(\sum_i\sigma_i^2\|X_i\|^2/(rF_j)\) and the same expression with \(Y_i\); each has mean one and variance \(2S_j/(rF_j^2)\). The negative term to subtract is the squared norm divided by \(r^2\) of
\[
W_j=\sum_i\frac{\sigma_i}{\sqrt{F_j}}\operatorname{vec}(Y_i X_i^{\mathsf T}).
\]
The summands are centered, independent across \(i\), with total covariance \(I_{r^2}\). For fixed \(r\), their fourth norm moments sum to \(\mathbb E[\|Y_1\|^4\|X_1\|^4]S_j/F_j^2\to0\). The Lyapunov central limit theorem applied to every fixed linear projection and the Cramér–Wold theorem give \(W_j\Rightarrow N(0,I_{r^2})\). Slutsky’s theorem and continuous mapping give the claimed law; it has no atom at zero.

**Clipping.** For the centered Wishart matrices \(M=\Omega\Omega^{\mathsf T}/r-I\) and \(L=\Psi\Psi^{\mathsf T}/r-I\), expansion gives \(H_r(A)-F(A)=-\operatorname{tr}(LA M A^{\mathsf T})\). Conditional on \(M\), this has mean zero and variance \(2\|A M A^{\mathsf T}\|_F^2/r\). In the right singular-vector basis, the diagonal entries of \(M\) have variance \(2/r\) and the off-diagonal entries have variance \(1/r\). Thus
\[
\mathbb E H_r=F(A),\qquad
\operatorname{Var}(H_r/F(A))=\frac{2}{r^2}\left(1+\frac{\operatorname{tr}((A^{\mathsf T}A)^2)}{F(A)^2}\right)\le \frac{4}{r^2}.
\]
The bound ensures uniform integrability of \((-H_r/F(A_j))_+\), so the relative clipping bias tends to \(\mathbb E[(Z/r^2-2)_+]\) for \(Z\sim\chi^2_{r^2}\). For chi-square densities \(f_k\), \(x f_k(x)=k f_{k+2}(x)\). Integrating above \(2r^2\) gives the claimed difference, strictly positive since \(Z\) has positive mass above \(2r^2\).

**Large sketch tail of the limiting law.** Put \(k=r^2\) and \(I(u)=(u-1-\log u)/2\). Stirling’s formula gives the density of \(Z/k\) as \(C_k u^{-1}e^{-kI(u)}\), where \(C_k\sim\sqrt{k/(4\pi)}\). In the integral over \(u\ge2\) put \(u=2+t/k\). Since \(I'\) is increasing and \(I'(2)=1/4\), the integrand after removing \(e^{-k I(2)}\) is dominated by \(e^{-t/4}/2\) and converges to it. The integral is therefore asymptotic to \((2/k)e^{-k I(2)}\) before multiplication by \(C_k\). This gives the stated prefactor and exponent.

## Relationship to other results
Chen, Halikias, Musco and Persson, *Hutch#: Optimal non-adaptive Frobenius norm estimation*, [arXiv:2609.28472](https://arxiv.org/abs/2609.28472), introduce the estimator and give unbiasedness and the exact variance (Theorem 1.1). Those moments do not determine the limiting law or the clipping bias. The substantive finding here is the fixed-sketch signed and clipped behavior across arbitrary high-effective-rank spectra; the large-sketch tail of that limiting law is a chi-square consequence.

For contrast only, the rank-one case has a different sign tail. *Sharp sign-safety and negative-tail law for weighted Hutch# Frobenius estimation*, [Resultary record a93f4801fdb5](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-sign-safety-and-negative-tail-law-for-weighted-hutch-frobe--a93f4801fdb5), gives a fixed-weight rank-one integral and asymptotic; at weight \(\alpha=1\) it gives the unweighted rate \(e^{-r(1-\log 2)}/\sqrt{6\pi r}\). That result is not a separate originality claim here, and it does not cover the high-effective-rank theorem. This comparison asserts mathematical overlap, not historical priority.

## Reproducibility and limitations
The accompanying `verify.py` requires NumPy and SciPy. It checks the centered identity and chi-square constants and illustrates the limit with finite Gaussian simulations on a nonconstant-spectrum family. Its rank-one checks pertain to the comparative regime only. These computations are not the proof of any infinite-limit assertion. No finite-rank error bound, joint limit, or conclusion about replacing Gaussian sketches is claimed.
