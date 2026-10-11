# Fractional-phase law for the centered numerical-range inradius of contracting dilations

## Finding
Fix a real number \(0<a<1\). For the unweighted composition operator \(C_{\lambda z}\) on the weighted Dirichlet Hilbert space \(\mathcal D_s\), where \(0<s<1\) and \(\lambda=a e^{i\theta}\), let
\[
\rho_a(\theta)=\sup\{r\ge0:\{w\in\mathbb C:|w|\le r\}\subseteq W(C_{\lambda z};\mathcal D_s)\}.
\]
For \(0\le t<1\), set
\[
H_a(t)=\max_{j\ge1}a^j(j-t),\qquad F_a(t)=a^{-t}H_a(t),\qquad t_\theta=\{\pi/\theta\}.
\]
Here braces denote the fractional part. As \(\theta\downarrow0\), **uniformly in the fractional part** \(t_\theta\),
\[
\boxed{\rho_a(\theta)=\theta a^{\pi/\theta}\bigl(F_a(t_\theta)+O_a(\theta^2+a^{\pi/\theta})\bigr).}
\]
The maximum defining \(H_a(t)\) occurs at
\[
\boxed{j_a(t)=\max\{1,\lceil t+a/(1-a)\rceil\},}
\]
with a possible tie between \(j_a(t)\) and \(j_a(t)+1\) when \(t+a/(1-a)\) is a positive integer. The positive continuous function \(F_a\) extends to a **nonconstant continuous one-periodic function**. Hence the normalized centered inradius generally has different subsequential limits:
\[
\frac{\rho_a(\theta)}{\theta a^{\pi/\theta}}-F_a(t_\theta)\longrightarrow0,
\qquad
\lim_{\theta\downarrow0}\theta\log\rho_a(\theta)=\pi\log a.
\]
For instance, for \(a=1/2\), the two phase limits at \(t=0\) and \(t=1/2\) are respectively \(1/2\) and \(3\sqrt2/8\). For all sufficiently small \(\theta>0\), the numerical range is a **closed finite polygon** containing the origin in its interior. The formula and the numerical range are independent of \(s\).

## Assumptions and scope
The space \(\mathcal D_s\), \(0<s<1\), consists of holomorphic power series with the monomials
\[
e_n(z)=\left(\frac{\Gamma(n+s)}{\Gamma(n+1)\Gamma(s)}\right)^{1/2}z^n,\quad n\ge0,
\]
forming an orthonormal basis. The composition symbol is \(\varphi(z)=a e^{i\theta}z\), with fixed \(0<a<1\) and \(\theta>0\) tending to zero. The disk defining \(\rho_a(\theta)\) is centered at zero and is **closed**. No claim of uniformity as \(a\to0\) or \(a\to1\) is made.

## Proof
**1. Diagonal numerical range.** Directly \(C_{\lambda z}e_n=\lambda^n e_n\). For every unit vector \(f=\sum_{n\ge0}c_ne_n\),
\[
\langle C_{\lambda z}f,f\rangle=\sum_{n\ge0}|c_n|^2\lambda^n.
\]
Conversely every probability vector \((p_n)_{n\ge0}\) occurs by taking \(c_n=\sqrt{p_n}\). Thus the numerical range consists exactly of all such convex barycenters. Its closure is the compact convex hull of \(\{0\}\cup\{\lambda^n:n\ge0\}\).

**2. Sharp downward support.** Write \(k=\lfloor\pi/\theta\rfloor\) and \(t=\pi/\theta-k\in[0,1)\). For \(n\le k\), the imaginary part of \(\lambda^n\) is nonnegative. For \(n=k+j\), \(j\ge1\),
\[
-\operatorname{Im}\lambda^{k+j}=a^{k+j}\sin((j-t)\theta).
\]
Consequently the greatest downward support depth is
\[
M_a(\theta)=\max_{n\ge0}(-\operatorname{Im}\lambda^n)_+
=a^k\max_{j\ge1}a^j\sin((j-t)\theta)>0.
\]
The elementary inequality \(|\sin x-x|\le |x|^3/6\), combined with \(\sup_{j\ge1}a^j j^3<\infty\), gives, uniformly for \(t\in[0,1)\),
\[
\left|\frac{M_a(\theta)}{\theta a^k}-H_a(t)\right|
\le\frac{\theta^2}{6}\sup_{j\ge1}a^j j^3=O_a(\theta^2).
\]
Also \(H_a(t)\ge a^2(2-t)\ge a^2>0\), and \(H_a(t)\le\sum_{j\ge1}ja^j=a/(1-a)^2\). The downward supporting line implies \(\rho_a(\theta)\le M_a(\theta)\).

**3. Matching disk from three eigenvalues.** Let \(j_*\ge1\) maximize the sine expression above and set \(v=\lambda^{k+j_*}\), so \(\operatorname{Im}v=-M_a(\theta)\). For small \(\theta\), the competitor \(j=2\) gives \(M_a(\theta)\ge(2/\pi)\theta a^{k+2}\). Since \(M_a(\theta)\le\theta a^{k+j_*}(j_*-t)\), one has \(j_*a^{j_*}\ge(2/\pi)a^2\). Exponential decay of \(ja^j\) therefore bounds \(j_*\le J_a\), independent of \(\theta\) and \(t\).

Set \(p=\lfloor\pi/(2\theta)\rfloor\), \(u=\lambda^p\), and \(A=1\). For sufficiently small \(\theta\), the arguments of \(u\) and \(v\) lie respectively in \([\pi/2-\theta,\pi/2]\) and \((\pi,\pi+(J_a+1)\theta)\). The triangle \(T=\operatorname{conv}\{A,u,v\}\subseteq W(C_{\lambda z})\) contains the origin strictly. Indeed, each oriented edge has the origin on its left: the positive signed cross products of \((u-A,-A)\), \((v-u,-u)\), and \((A-v,-v)\) follow from the indicated angle ranges and the positive and negative imaginary parts of \(u\) and \(v\).

The distances from zero to the supporting lines through its three sides satisfy
\[
\begin{split}
 d(A,u)&=\frac{\operatorname{Im}u}{|1-u|}\ge\frac{a^p}{4},\\
 d(u,v)&=\frac{|u|\,|v|\sin(\arg v-\arg u)}{|u-v|}\ge\frac{|v|}{4}\ge\frac{a^{k+J_a}}4,\\
 d(v,A)&=\frac{M_a(\theta)}{|1-v|}\ge\frac{M_a(\theta)}{1+a^k}.
\end{split}
\]
For the middle bound use \(\sin(\arg v-\arg u)\ge1/2\) and \(|v|\le|u|\) when \(\theta\) is sufficiently small. Since \(M_a(\theta)=O_a(\theta a^k)\), the first two displayed distances eventually exceed \(M_a(\theta)\): indeed \(a^p/(\theta a^k)\to\infty\) and \(a^{J_a}/\theta\to\infty\). A closed centered disk of radius \(M_a(\theta)/(1+a^k)\) therefore lies in \(T\), proving
\[
\boxed{\frac{M_a(\theta)}{1+a^k}\le\rho_a(\theta)\le M_a(\theta)}
\]
for sufficiently small \(\theta\). These are uniform in \(t\) for each fixed \(a\).

**4. Fractional-phase factor, exact maximizing index, and polygonality.** The last bound and step 2 give
\[
\rho_a(\theta)=\theta a^k\bigl(H_a(t)+O_a(\theta^2+a^k)\bigr)
=\theta a^{\pi/\theta}\bigl(F_a(t)+O_a(\theta^2+a^{\pi/\theta})\bigr).
\]
In the second equality, \(a^{-t}\) lies in \([1,a^{-1}]\). For \(j\ge1\), successive terms of \(H_a\) satisfy
\[
a^{j+1}(j+1-t)-a^j(j-t)
=a^j\bigl(a-(1-a)(j-t)\bigr).
\]
Thus the terms increase until \(j\) passes \(t+a/(1-a)\), and then decrease, giving the index and tie rule. Each \(H_a\) is uniformly the maximum of functions decaying geometrically in \(j\), hence continuous, and \(H_a(1)=aH_a(0)\). This gives continuity at the periodic seam of \(F_a\). On every open interval where its maximizing integer is fixed, \(F_a(t)=a^{j-t}(j-t)\), an analytic nonconstant function. Finally, each prescribed phase \(t\in[0,1)\) occurs along \(\theta_N=\pi/(N+t)\), proving the distinct subsequential limits. Taking logarithms establishes the logarithmic decay law.

The triangle contains a positive closed disk about zero. Choose \(N\) so large that \(a^n\) is smaller than that disk radius for all \(n\ge N\), and also larger than all indices of the triangle vertices. Then every tail eigenvalue is in the triangle. Consequently the whole numerical range equals \(\operatorname{conv}\{1,\lambda,\ldots,\lambda^{N-1}\}\), which is a closed finite polygon. All steps depend only on the diagonal eigenvalues, not on the weight \(s\).

## Verification
Run `python3 verify_spiral.py` with the Python standard library. The script checks the discrete maximizer rule, periodic-seam identity, explicit distinct phase values, positive triangle orientation, matching analytic bounds, and several finite-angle numerical consistency cases. It prints `SPIRAL_INRADIUS_PHASE_ASYMPTOTIC_CHECKS_OK` on success. **The infinite-dimensional result and uniform asymptotic are proved above**, not inferred from finite tests.

## Relationship to prior work
Barik, Sen and Paul (2026, arXiv:2602.09481v1) introduce numerical-range questions on these weighted Dirichlet spaces. Their Theorem 1.2 excludes the complex-dilation case in its general interior-point statement; their disc-radius results impose conditions on a nonconstant or origin-vanishing multiplier and do not evaluate the centered inradius of these unweighted contractions. Sen, Halder, Birbonshi and Paul (2025 preprint; 2026 journal) give disk inclusions on weighted Bergman spaces requiring a multiplier zero and qualitative results for dilations; these are not the sharp small-phase law.

Fatehi and Negahdari (2019) study zero-inclusion for Fock-space compositions, while Fatehi (2019) and Matache (2001) address numerical ranges of composition operators, including dilation/monomial geometries. Any known convex-hull description of a diagonal dilation is accepted as antecedent; the additional claim here is the evaluated **uniform exponentially small optimal centered radius with its nonconstant fractional-phase prefactor**. Full texts of two older plausible comparisons were not obtainable; their possible stronger coverage is a bibliographic limitation.

## Limitations
The result is confined to unweighted complex dilations with fixed modulus strictly between zero and one and sufficiently small nonzero argument. It does not determine exact finite-angle polygon combinatorics, nor uniform estimates at the endpoints of the modulus interval, nor optimal disks with variable centers. The technical prefactor may have previous unindexed coverage; available comparisons do not establish publication novelty conclusively. Independent mathematical and bibliographic validation has not been performed.

## References
1. S. Barik, A. Sen, and K. Paul, *Numerical range and Berezin range of weighted composition operators on weighted Dirichlet spaces*, arXiv:2602.09481v1, posted 2026-02-10. https://arxiv.org/abs/2602.09481
2. A. Sen, S. Halder, R. Birbonshi, and K. Paul, *Numerical range of Toeplitz and composition operators on weighted Bergman spaces*, arXiv:2502.02833v1, posted 2025-02-05; later Canadian Mathematical Bulletin (2026). https://arxiv.org/abs/2502.02833
3. S. Halder, M. Mukherjee, and R. Birbonshi, *A note on weighted composition operators on Dirichlet space*, arXiv:2601.00646, 2026. https://arxiv.org/abs/2601.00646
4. M. Fatehi and A. Negahdari, *Numerical range of weighted composition operators which contain zero*, arXiv:1901.07736, 2019. https://arxiv.org/abs/1901.07736
5. M. Fatehi, *Numerical ranges of weighted composition operators*, Journal of Mathematical Analysis and Applications 477 (2019), DOI:10.1016/j.jmaa.2019.04.072.
6. V. Matache, *Numerical Ranges of Composition Operators*, Linear Algebra and its Applications (2001), DOI:10.1016/S0024-3795(01)00262-2.
