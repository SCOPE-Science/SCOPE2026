# The logarithmic spectral filter for smooth radial Fock Toeplitz operators

## Finding
For every complex dimension \(d\ge1\), smooth real \(2\pi\)-periodic function \(\varphi\), and real \(b>\|\varphi\|_\infty\), put
\[
a(z)=\frac{b+\varphi(\log\log(e+|z|^2))}{(1+|z|^2)^d},\qquad
G_\varphi(v)=\int_0^\infty e^{-s}\varphi(v-s)\,ds.
\]
Let \(T_a\) be the Toeplitz operator on standard Gaussian Fock space over \(\mathbb C^d\), and write its singular values in nonincreasing order \(s_1(T_a)\ge s_2(T_a)\ge\cdots\). Then
\[
\boxed{\frac{\sum_{j=1}^N s_j(T_a)}{\log N}=\frac{b+G_\varphi(\log\log N-\log d)}{d!}+o(1)}\quad(N\to\infty).
\]
The exact cluster interval is
\[
\left[\frac{b+\min G_\varphi}{d!},\frac{b+\max G_\varphi}{d!}\right].
\]
Every number in the interval occurs as a Dixmier trace of \(T_a\). In particular, \(T_a\) is Dixmier measurable exactly when \(\varphi\) is constant. When \(\varphi(v)=\sin v\),
\[
G_\varphi(v)=\frac{\sin v-\cos v}{2},\qquad
\operatorname{Tr}_\omega(T_a)\in\left[\frac{b-1/\sqrt2}{d!},\frac{b+1/\sqrt2}{d!}\right],
\]
and each value in this interval is realized by a dilation-invariant generalized limit. The Fourier modes of the symbol profile are multiplied by \((1+ik)^{-1}\) in the spectral-mean profile.

## Assumptions and scope
The normalized Gaussian Fock space is
\[
\mathcal F_d=\left\{F\text{ entire on }\mathbb C^d:\ \|F\|^2=\pi^{-d}\int_{\mathbb C^d}|F(z)|^2e^{-|z|^2}\,dV(z)<\infty\right\}.
\]
Here \(d\) is any positive integer, \(\varphi\in C^\infty(\mathbb R/2\pi\mathbb Z;\mathbb R)\), and \(b>\|\varphi\|_\infty\) is fixed. The Toeplitz operator is \(T_aF=P(aF)\), where \(P\) is orthogonal Fock projection. The symbol is bounded and strictly positive, vanishes at infinity, and is eventually strictly decreasing as a function of \(|z|\). For each multi-index \(\alpha\), \(D^\alpha a(z)=O((1+|z|)^{-2d-|\alpha|})\); thus it belongs to the Shubin class \(\mathrm{GLS}^{-2d}\). If \(\varphi\) is nonconstant, the coefficient \(|z|^{2d}a(z)\) has no limit at infinity, so the symbol does not belong to the polyhomogeneous class \(\mathcal A_{-2d}\) covered by the older measurability theorem. The operator is positive, compact, belongs to weak trace class, and is not trace class.

## Proof
**Step 1: exact spectral diagonalization.** The normalized monomials \(e_\alpha(z)=z^\alpha/\sqrt{\alpha!}\) form an orthonormal basis. Radial symmetry makes \(T_a\) diagonal, with common eigenvalue in total degree \(k\)
\[
\lambda_k=\frac1{\Gamma(k+d)}\int_0^\infty
\frac{b+\varphi(\log\log(e+t))}{(1+t)^d}\,t^{k+d-1}e^{-t}\,dt,
\qquad m_k=\binom{k+d-1}{d-1}.
\]
Its multiplicity is \(m_k\), and \(\lambda_k>0\). Let \(S_k\) have the Gamma law with shape \(k+d\) and unit scale. Then \(\lambda_k=\mathbb E a_0(S_k)\), where \(a_0(t)=a(z)\) for \(|z|^2=t\).

**Step 2: quantitative Gamma localization.** For all sufficiently large \(t\), \(|a_0'(t)|\le C_dt^{-d-1}\). The standard Gamma Chernoff estimate implies \(\mathbb P(S_k\notin[k/2,3k/2])\le C e^{-ck}\) for fixed \(d\), and \(\mathbb E|S_k-k|=O(\sqrt k)\). Split the expectation on this central event and its complement to obtain
\[
\lambda_k=a_0(k)+O(k^{-d-1/2})
=\frac{b+\varphi(\log\log k)}{k^d}+O(k^{-d-1/2}).
\]
The logarithmic-logarithmic shift from \(e+k\) to \(k\), and the denominator shift, contribute only \(O(k^{-d-1})\).

**Step 3: eventual spectral ordering.** For sufficiently large \(t\), direct differentiation gives
\[
a_0'(t)=(1+t)^{-d-1}\left[-d(b+\varphi(v))+
\frac{1+t}{(e+t)\log(e+t)}\varphi'(v)\right],\quad v=\log\log(e+t).
\]
Because \(b-\|\varphi\|_\infty>0\), this derivative is strictly negative and is bounded above by \(-c t^{-d-1}\). Coupling \(S_{k+1}=S_k+E\) with an independent unit exponential \(E\), the event \(S_k\in[k/2,3k/2]\), \(0<E\le1\) contributes at most \(-c'k^{-d-1}\) to \(\lambda_{k+1}-\lambda_k\). All contributions with \(S_k\) beyond the eventual-decrease threshold are nonpositive, and the contribution with \(S_k\) below that threshold is exponentially small. Hence \(\lambda_{k+1}<\lambda_k\) for all sufficiently large \(k\). The finite initial eigenvalues are strictly positive, so for large \(K\) the first \(B_K=\sum_{k=0}^{K}m_k=\binom{K+d}{d}\) decreasingly ordered singular values are exactly all the degree-at-most-\(K\) eigenvalues, with multiplicities.

**Step 4: logarithmic spectral asymptotics.** The multiplicity formula and the Gamma error yield an absolutely summable remainder:
\[
m_k\lambda_k=\frac{b+\varphi(\log\log k)}{(d-1)!\,k}+O(k^{-3/2}).
\]
A sum-integral comparison, using the integrability of the derivative of \(x\mapsto\varphi(\log\log x)/x\) for \(x\ge2\), gives
\[
\sum_{j=1}^{B_K}s_j(T_a)=\frac{1}{(d-1)!}
\left[b\log K+\int_1^K\frac{\varphi(\log\log x)}{x}\,dx\right]+O(1).
\]
The integral is *exactly* \(\log K\,G_\varphi(\log\log K)\): set \(u=\log x\), then \(w=\log u\). Also \(\log B_K=d\log K-\log(d!)+o(1)\), hence \(\log\log K=\log\log B_K-\log d+o(1)\). Since \(m_{K+1}\lambda_{K+1}=O(1/K)\), the result extends from \(B_K\) to arbitrary integer \(N\), giving the displayed boxed formula.

**Step 5: exact Dixmier trace range and measurability.** Positivity and \(b>\|\varphi\|_\infty\) give \(s_j(T_a)\asymp j^{-1}\), so \(T_a\) lies in the Dixmier ideal. Its continuous logarithmic average \(Q(t)=(\log(1+t))^{-1}\sum_{1\le j\le\lfloor t\rfloor}s_j(T_a)\) has the same asymptotics. Every dilation-invariant generalized limit applied to \(Q\) lies between its liminf and limsup. Conversely, for a desired phase \(\theta\), put \(x_m=\exp(2\pi m+\theta+\log d)\) and \(L_m=\sqrt{x_m}\). The functional
\[
\omega_\theta(f)=\lim_{m\to\mathcal U}\frac1{L_m}
\int_{x_m}^{x_m+L_m}f(e^y)\,dy
\]
on bounded measurable functions, with any free ultrafilter \(\mathcal U\), is a positive normalized generalized limit invariant under every fixed dilation of its argument: a dilation translates the \(y\)-interval by a bounded amount, while \(L_m\to\infty\). Since \(L_m/x_m\to0\), the logarithmic-mean formula is uniform over these intervals and implies
\[
\omega_\theta(Q)=\frac{b+G_\varphi(\theta)}{d!}.
\]
All values in the claimed interval occur because \(G_\varphi\) is continuous and periodic. Moreover \(G_\varphi'+G_\varphi=\varphi\), so \(G_\varphi\) is constant exactly when \(\varphi\) is constant. The sine and Fourier-mode formulas follow by elementary integration.

## Verification
The proof uses exact radial Gamma moments and standard Gamma concentration, not numerical extrapolation. Direct numerical quadrature against the Gamma densities for complex dimensions \(d=1,2,3\) and degrees \(k=5,30,90\) showed convergence of \(\lambda_k/a_0(k)\) toward one, consistent with the proved localization estimate. Specifically, for \(d=1\) the ratios were approximately \(0.9633,0.9980,0.9998\); for \(d=2\), \(0.7884,0.9649,0.9887\); and for \(d=3\), \(0.5570,0.9037,0.9671\). The source formula, moment integral, and each limiting step are fully specified above so the argument is independently reproducible without software.

## Relationship to prior work
Bommier-Hato, Engliš and Youssfi's *Dixmier trace and the Fock space* proves measurability and a trace formula for Fock Toeplitz symbols in the polyhomogeneous class \(\mathcal A_{-2d}\) (Theorem 7) and explicitly discusses the distinction between that class and the broader Shubin class in Section 7.5. The present theorem gives a precise complementary boundary: all symbols considered here lie in \(\mathrm{GLS}^{-2d}\), yet every nonconstant periodic profile yields nonmeasurability, with its full trace-value interval determined by an exponential-convolution filter. Xu and Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces* (2026), studies singular-value asymptotics and includes a radial counterexample to an unqualified Weyl coefficient; failure of a Weyl coefficient alone does not determine whether logarithmic spectral means converge or their cluster range. Only its public abstract was accessible for comparison, so possible additional implicit coverage is not excluded.

## Limitations
The claim is confined to smooth radial symbols of the displayed log-log periodic family on the Gaussian Fock space in finite complex dimension. It does not classify all Shubin symbols, all weighted Fock spaces, or arbitrary slowly oscillating profiles. The exact logarithmic profile and Dixmier nonmeasurability are proved; no assertion is made about other singular traces or about optimal constants for unrelated Toeplitz families. The 2026 motivating manuscript could not be inspected in full; this is an originality residual risk, not proof of noncoverage. No independent audit has been performed.

## References
1. C. Xu and J. Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970v1, publicly posted 2026-09-15, https://arxiv.org/abs/2609.16970.
2. H. Bommier-Hato, M. Engliš and E.-H. Youssfi, *Dixmier trace and the Fock space*, author-posted full text https://users.math.cas.cz/~englis/79.pdf, Theorem 7 and Sections 7.4--7.5.
3. Standard Gamma moment identity and Chernoff exponential-tail bounds, as used explicitly in the proof.
