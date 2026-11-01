# Exact singular spectrum and critical square-root collapse of quadratic-Gaussian Fock contractions

## Finding
On the normalized one-variable analytic Bargmann–Fock space, consider
\[
(T_{t,b}f)(z)=t\,e^{bz^2}f(tz),\qquad 0<t<1,\quad b\in\mathbb C.
\]
Put \(b_*(t)=(1-t^2)/2\). This operator, initially specified on polynomials when the images belong to the space, extends boundedly **exactly** when \(|b|\le b_*(t)\). It is compact, in fact in every Schatten class \(S_p\) for \(p>0\), exactly when \(|b|<b_*(t)\); at equality it is bounded but noncompact.

For \(|b|<b_*(t)\), define
\[
Q=(1-t^2)^2-4|b|^2>0,\quad
h=2+\frac{Q}{t^2},\quad
r=\frac{h-\sqrt{h^2-4}}2\in(0,1).
\]
The **entire nonzero singular spectrum, with multiplicities**, is simple and equals
\[
\boxed{s_n(T_{t,b})=\sqrt t\,r^{(2n+1)/4},\qquad n=0,1,2,\ldots.}
\]
Consequently, for every real \(p>0\),
\[
\boxed{\|T_{t,b}\|_{S_p}^{p}=\frac{t^{p/2}r^{p/4}}{1-r^{p/2}}.}
\]
For each fixed \(0<t<1\), let \(\delta=b_*(t)-|b|\downarrow0\). Then
\[
1-r\sim\frac{2\sqrt{1-t^2}}t\sqrt\delta,
\qquad
\boxed{\|T_{t,b}\|_{S_p}^{p}\sim
\frac{t^{p/2+1}}{p\sqrt{1-t^2}}\,\delta^{-1/2}.}
\]
Meanwhile the **ordinary nonzero eigenvalues** are \(t^{n+1}\) for \(n\ge0\), independent of \(b\). Thus the ordinary spectrum does not detect the nonnormal singular-value inflation.

## Assumptions and scope
The Hilbert space is
\[
\mathcal F^2=\left\{f\text{ entire}:\|f\|^2=\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\frac{dA(z)}\pi<\infty\right\},
\]
with orthonormal monomials \(e_n(z)=z^n/\sqrt{n!}\). The normalization factor \(t\) in \(T_{t,b}\) is part of the definition. Every claim holds for all real \(0<t<1\), all complex \(b\), and, where applicable, all real \(p>0\). For complex \(b\), a unitary rotation reduces the proof to \(b\ge0\).

This weighted contraction is a concrete quadratic-Gaussian Bargmann operator. In parameter ranges where the Toeplitz symbol has its standard dense domain, Gaussian integration identifies it with compression of \(e^{-c|z|^2+\eta z^2}\), using \(t=(1+c)^{-1}\) and \(b=\eta t^2\). No unrestricted Toeplitz-domain identification is required for the theorem.

## Proof
**1. The exact boundedness boundary.** By unitary rotation take \(b\ge0\). Write \(z=x+iy\). At \(b=b_*=(1-t^2)/2\), substituting \(w=tz\) gives the identity
\[
\|T_{t,b_*}f\|^2
=\int_{\mathbb C}|f(w)|^2e^{-|w|^2}
\exp\!\left[-\frac{2(1-t^2)}{t^2}(\operatorname{Im}w)^2\right]\frac{dA(w)}\pi
\le\|f\|^2.
\]
For \(0\le b<b_*\), the substitution \(w=tz\) produces strictly stronger decay than \(e^{-|w|^2}\) in both Cartesian directions because \((1\mp2b)/t^2>1\). Hence the same boundedness estimate holds throughout the closed permitted range; the Hilbert–Schmidt calculation below gives compactness in its interior. At the boundary take the normalized coherent vectors \(k_R(z)=\exp(Rz-R^2/2)\), with \(R\to+\infty\). They converge weakly to zero, whereas direct Gaussian integration gives
\[
\|T_{t,b_*}k_R\|^2=\frac{t^2}{\sqrt{1-4b_*^2}}>0.
\]
Hence the boundary operator is not compact. If \(b_*<b<1/2\), the same integral gives
\[
\|T_{t,b}k_R\|^2=
\frac{t^2}{\sqrt{1-4b^2}}
\exp\!\left[\left(\frac{t^2}{1-2b}-1\right)R^2\right]
\longrightarrow\infty.
\]
For \(b\ge1/2\), already \(T_{t,b}1\notin\mathcal F^2\). This proves necessity. Each fixed complex argument of \(b\) is unitarily rotated away.

**2. Hilbert–Schmidt trace and the positive Gaussian kernel.** For \(0\le b<b_*\), summing \(\sum_n|e_n(tz)|^2=e^{t^2|z|^2}\) before Gaussian integration gives
\[
\operatorname{tr}(T^*T)=\|T\|_{S_2}^2
=t^2\int_{\mathbb C}\exp\left(-(1-t^2)|z|^2+2b\operatorname{Re}z^2\right)\frac{dA(z)}\pi
=\frac{t^2}{\sqrt Q}.
\]
Put \(D=1-4b^2>0\), \(A=bt^2/D\), and \(B=t^2/D\). The reproducing kernel of \(H=T^*T\), with antiholomorphic second variable, is
\[
H(z,\bar w)=\frac{t^2}{\sqrt D}\exp\!\left[A(z^2+\bar w^2)+Bz\bar w\right].
\]
For reference, the underlying complex Gaussian identity is
\[
\int_{\mathbb C}e^{-|w|^2+\alpha w^2+\gamma\bar w^2+vw+u\bar w}\frac{dA(w)}\pi
=\frac{\exp((\alpha u^2+\gamma v^2+uv)/(1-4\alpha\gamma))}{\sqrt{1-4\alpha\gamma}},
\]
when the real quadratic form is integrable; its use below is legitimate because \(0\le A<1/4\) and \(0\le s<1\).

**3. Exact spectral diagonalization without a completeness assumption.** The smaller positive root \(s\in[0,1)\) of
\[
s=2A+\frac{sB^2}{1-2As}
\]
is well defined; for \(A>0\), the corresponding quadratic is \(2As^2-(1+4A^2-B^2)s+2A=0\). Its value at zero is positive, while at one it is negative because \(1-2A>B>0\) for \(b<b_*\); hence its smaller root is strictly between zero and one. When \(A=0\), take \(s=0\). Set
\[
r=\frac{B}{1-2As},\qquad
\zeta=\frac{A}{(1-2As)(1-r^2)},\qquad
f_v(z)=e^{sz^2/2+vz-\zeta v^2}.
\]
The quadratic equation implies \(r+r^{-1}=t^2+D/t^2=2+Q/t^2\), selecting the root \(0<r<1\) given in the theorem. The Gaussian identity yields the **exact intertwining**
\[
Hf_v=t\sqrt r\,f_{rv}.
\]
For every integer \(n\ge0\), differentiating \(n\) times in \(v\) at zero produces a nonzero function \(f_n\in\mathcal F^2\) (a degree-\(n\) polynomial times \(e^{sz^2/2}\)) satisfying
\[
Hf_n=t\,r^{n+1/2}f_n.
\]
These eigenvalues are pairwise distinct and the functions consequently orthogonal. No basis-completeness assertion is needed: using \((1-r)^2/r=Q/t^2\), their sum is
\[
\sum_{n\ge0}t\,r^{n+1/2}
=\frac{t\sqrt r}{1-r}=\frac{t^2}{\sqrt Q}=\operatorname{tr}H.
\]
Since \(H\) is positive and trace class, no further positive eigenvalues exist. Since \(T\) is injective, \(\ker H=0\). Taking square roots gives the complete singular values and summing their \(p\)-th powers gives the Schatten formula.

**4. Critical scaling and ordinary eigenvalues.** From the defining reciprocal equation,
\[
\frac{(1-r)^2}{r}=\frac{Q}{t^2},\qquad
Q=4(1-t^2)\delta-4\delta^2.
\]
Thus \(1-r\sim 2\sqrt{1-t^2}\sqrt\delta/t\), and \(1-r^{p/2}\sim(p/2)(1-r)\), yielding the displayed square-root blowup. Separately the explicit eigenvectors
\[
g_n(z)=z^n\exp\!\left(\frac{bz^2}{1-t^2}\right)\in\mathcal F^2
\]
satisfy \(Tg_n=t^{n+1}g_n\) in the compact range. Conversely, comparison of the first nonzero Taylor coefficient of any eigenvector forces its eigenvalue to equal one of \(t^{n+1}\). Compactness then excludes other nonzero spectral values.

## Verification
A standalone script `CHECK.py` reconstructs finite Taylor matrices in the orthonormal monomial basis using
\[
\langle Te_n,e_{n+2j}\rangle
=t^{n+1}\frac{b^j}{j!}\sqrt{\frac{(n+2j)!}{n!}},\qquad j\ge0,
\]
and checks their top singular values against the exact geometric law, including complex phases. It checks the Hilbert–Schmidt trace identity, finite sums of the Schatten geometric series and near-boundary scaling. The packaged checker produced **125 successful finite assertions**. The analytical proof, not finite truncations, establishes completeness and critical asymptotics.

## Relationship to prior work
Coburn, Hitrik and Sjöstrand (2018, 2023) develop boundedness/compactness of quadratic-exponential Bargmann Toeplitz operators and rapid decay of singular values under strict positivity. Xiong (2023) treats inhomogeneous quadratic symbols. Seyoum and Mengestie (2021), Theorem 3.1, determine ordinary spectra of compact Fock weighted composition operators. Dong and Zhu (2025), Theorem A, give exact geometric singular values for canonical Gaussian kernels with coupled holomorphic/antiholomorphic quadratic coefficients; that family has an antiholomorphic quadratic term whenever its holomorphic quadratic term is nonzero, unlike the kernel \(t e^{bz^2+tz\overline w}\) here. Their theorem therefore does not directly specialize by matching coefficients to the present operator, although a hidden unitary/metaplectic reduction is a remaining priority risk. Sang and Zhao (2026) include this weighted composition kernel within a five-parameter Gaussian family, prove compactness and Schatten-class membership and compute Hilbert–Schmidt norms, but do not give the full nonzero singular-value sequence or its sharp critical constant. Benahmadi and Ghanmi (2020) give singular values for a different Itô–Hermite integral transform from planar Gaussian space to bidisk Bergman space; Mengestie and Takele (2023) establish a Schatten-membership criterion on faster-than-Gaussian Fock-type spaces, whose hypotheses exclude the classical Gaussian weight here. These supply the natural operator class, boundedness context and qualitative trace-class behavior; the present **exact singular ratio for this quadratic family**, all-\(p\) Schatten formula and explicit critical blowup quantify information not stated in those inspected treatments. The Gaussian diagonalization uses classical Mehler-type ideas, and older equivalent formulations remain possible; no blanket novelty or independence certification is claimed.

## Limitations
The theorem concerns the one-variable normalized Gaussian Fock Hilbert space and scalar contractions with \(0<t<1\); it does not assert analogous formulas for general anisotropic multivariable Gaussian operators, inhomogeneous symbols, non-Gaussian weights or arbitrary Toeplitz domains. The endpoint is only asserted bounded and noncompact. No rate of convergence for finite matrix singular values is claimed. Bibliographic comparison cannot eliminate all historical-priority risk, especially possible reparameterizations of Gaussian/Mehler spectral decompositions. The review is not independent verification.

## References
- L. Coburn, M. Hitrik and J. Sjöstrand, *Positivity, complex FIOs, and Toeplitz operators* (first posted 2018-07-02), arXiv:1807.00922, https://arxiv.org/abs/1807.00922; Proposition 3.3 and Section 4.
- L. Coburn, M. Hitrik and J. Sjöstrand, *Characterizing boundedness of metaplectic Toeplitz operators* (first posted 2023-03-02), arXiv:2303.01558, https://arxiv.org/abs/2303.01558; Theorems 1.1–1.2 and Section 3.
- H. Xiong, *Boundedness of metaplectic Toeplitz operators and Weyl symbols* (first posted 2023-05-06), arXiv:2305.03948, https://arxiv.org/abs/2305.03948.
- X. Dong and K. Zhu, *Canonical integral operators on the Fock space II* (first posted 2025-09-20), arXiv:2509.16672, https://arxiv.org/abs/2509.16672; Theorem A and Section 4.
- Y. Sang and L. Zhao, *Gaussian Integral Operator between Fock Spaces* (first posted 2026-10-20), arXiv:2610.28279, https://arxiv.org/abs/2610.28279; Theorems 1.1–1.2 and Section 5.
- A. Benahmadi and A. Ghanmi, *Dual of 2D fractional Fourier transform associated to Itô–Hermite polynomials* (first posted 2020-05-18), arXiv:2005.08490, https://arxiv.org/abs/2005.08490; Theorem 1.2 and Section 4.
- T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces* (published online 2023-02-23), Bull. Malays. Math. Sci. Soc. **46**, article 80, https://doi.org/10.1007/s40840-023-01476-4; Theorem 3.2.
- W. Seyoum and T. Mengestie, *Spectrums and Uniform Mean Ergodicity of Weighted Composition Operators on Fock Spaces* (published online 2021-10-07), Bull. Malays. Math. Sci. Soc. **45** (2022), 455–481, https://doi.org/10.1007/s40840-021-01203-x; Theorem 3.1.
