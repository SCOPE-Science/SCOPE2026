# Sharp spectral-spacing constants for finite-dimensional endpoint maximal regularity

## Finding
Fix \(b>1\), \(r\in[1,\infty]\), and \(N\in\mathbb N\). Define the finite-dimensional diagonal evolution generator \(A_{N,b}=\operatorname{diag}(b,b^2,\ldots,b^N)\) on the real or complex sequence space \(\ell_r^N\). Its endpoint maximal-regularity map on \(L^1((0,\infty);\ell_r^N)\) is
\[
(\mathcal T_{N,b}f)_n(t)=\int_0^t b^n e^{-b^n(t-s)}f_n(s)\,ds,\qquad 1\le n\le N.
\]
Use \(1/\infty=0\). Define the absolutely convergent logarithmic-scale coefficient
\[
\kappa_r(b)=\int_1^b\left\|(b^k e^{-b^ku})_{k\in\mathbb Z}\right\|_{\ell_r(\mathbb Z)}\,du.
\]
**Theorem.** For any integer \(K\ge1\) with \(2K<N\),
\[
\boxed{\left|N^{-(1-1/r)}\|\mathcal T_{N,b}\|-\kappa_r(b)\right|\le\frac{2K}{N}+b^{-K}+e^{-b^{K+1}}.}
\]
In particular, for each fixed \(b>1\) and \(r\in[1,\infty]\),
\[
\|\mathcal T_{N,b}\|=\kappa_r(b)N^{1-1/r}+O_{b,r}\bigl(N^{-1/r}\log(N+1)\bigr).
\]
The endpoint \(r=1\) has \(\|\mathcal T_{N,b}\|=\kappa_1(b)=1\), while \(0<\kappa_r(b)<1\) for \(1<r\le\infty\). The spectral-spacing limits are
\[
\lim_{b\to\infty}\kappa_r(b)=1\quad(1\le r\le\infty),
\]
\[
\kappa_r(b)\sim\frac{\Gamma(r)^{1/r}}{r}(\log b)^{1-1/r}\quad(b\downarrow1,\;1\le r<\infty),
\qquad
\kappa_\infty(b)\sim\frac{\log b}{e}\quad(b\downarrow1).
\]
For the dyadic Hilbert-coordinate case, \(\kappa_2(2)=0.416277305367437044\ldots\), evaluated numerically from its convergent defining integral.

## Assumptions and scope
The time interval is the half-line \((0,\infty)\); integration uses ordinary Lebesgue measure. The coefficient field may be real or complex. The norm \(\|\mathcal T_{N,b}\|\) is the usual operator norm on the Bochner space \(L^1((0,\infty);\ell_r^N)\), not an \(L^p\)-in-time norm for \(p>1\). Each eigenvalue has multiplicity one, the spectrum is a geometric progression, and \(N\) tends to infinity at fixed \(b\) before any separate spacing limit. The statement does not assert a uniform error estimate as \(b\downarrow1\).

## Proof
**1. Exact finite-dimensional norm reduction.** Let \(k_n(t)=b^n e^{-b^nt}\) for \(t>0\), and zero otherwise. Minkowski's inequality and Tonelli's theorem imply
\[
\|\mathcal T_{N,b} f\|_{L^1(\ell_r^N)}\le\int_0^\infty\int_0^\infty\|(k_n(u) f_n(s))_{n=1}^N\|_{\ell_r^N}\,du\,ds.
\]
Hence the operator norm is no larger than
\[
M_{N,r,b}:=\sup_{\|v\|_{\ell_r^N}=1}\int_0^\infty\|(k_n(u)v_n)_{n=1}^N\|_{\ell_r^N}\,du.
\]
For each fixed unit vector \(v\), the inputs \(f_\varepsilon(s)=\varepsilon^{-1}\mathbf1_{(0,\varepsilon)}(s)v\) have unit Bochner \(L^1\)-norm. The convolution outputs converge as \(\varepsilon\downarrow0\) in Bochner \(L^1\) to \(u\mapsto(k_n(u)v_n)_n\), by translation continuity for finitely many integrable kernels. Thus \(\|\mathcal T_{N,b}\|=M_{N,r,b}\). For \(r<\infty\), writing \(a_n=|v_n|^r\) gives \(a_n\ge0\), \(\sum_{n=1}^N a_n=1\), and
\[
M_{N,r,b}=\sup_{\substack{a_n\ge0\\\sum a_n=1}}\int_0^\infty\Bigl(\sum_{n=1}^N a_n k_n(u)^r\Bigr)^{1/r}\,du.
\]
When \(r=\infty\), all coordinates of the maximizing vector can be taken equal to one, so \(M_{N,\infty,b}=\int_0^\infty\max_{1\le n\le N}k_n(u)\,du\). These formulas are equalities, not estimates from particular test vectors.

**2. Logarithmic partition and finite error.** Partition \((0,\infty)\) into \((b^{-j},b^{1-j}]\), \(j\in\mathbb Z\), and put \(u=b^{-j}w\), \(1\le w\le b\). Let \(v_k(w)=b^k e^{-b^kw}\). For \(1\le r<\infty\), the exact norm reduces to
\[
\sup_{\sum a_n=1}\sum_{j\in\mathbb Z}\int_1^b\Bigl(\sum_{n=1}^N a_n v_{n-j}(w)^r\Bigr)^{1/r}\,dw.
\]
Fix \(K\ge1\) with \(2K<N\). Write
\[
\eta_K=\int_1^b\sum_{|k|>K}v_k(w)\,dw.
\]
The negative-index tail is bounded by a geometric series, and the positive-index tail telescopes exactly; thus
\[
0\le\eta_K\le b^{-K}+e^{-b^{K+1}}.
\]
Define the truncated coefficient \(\kappa_{r,K}(b)=\int_1^b\|(v_k(w))_{|k|\le K}\|_{\ell_r}\,dw\). The triangle inequality gives \(0\le\kappa_r(b)-\kappa_{r,K}(b)\le\eta_K\) for all \(r\), including \(r=\infty\).

For the lower bound at finite \(r\), choose \(a_n=1/N\). Each scale \(j=K+1,\ldots,N-K\) contains all indices \(|n-j|\le K\); therefore
\[
M_{N,r,b}\ge (N-2K)N^{-1/r}\kappa_{r,K}(b).
\]
For the upper bound, split the sum into \(|n-j|\le K\) and its complement using Minkowski. The complement is at most \(\eta_K\sum_n a_n^{1/r}\le\eta_K N^{1-1/r}\). The retained scales lie among exactly \(N+2K\) possible integers \(j\), and Hölder in \(j\) gives
\[
M_{N,r,b}\le(N+2K)^{1-1/r}\kappa_{r,K}(b)+N^{1-1/r}\eta_K.
\]
For \(r=\infty\), the same lower and upper arguments use pointwise maxima in place of \(\ell_r\)-norms and yield the corresponding bounds with the factor \(N\) replacing \(N^{1-1/r}\). Finally \(\kappa_r(b)\le1\), since \(\ell_r\)-norm is bounded by the \(\ell_1\)-norm and
\[
\int_1^b\sum_{k\in\mathbb Z} b^k e^{-b^kw}\,dw
=\sum_{k\in\mathbb Z}(e^{-b^k}-e^{-b^{k+1}})=1.
\]
After division by \(N^{1-1/r}\), both preceding bounds give exactly the displayed error \(2K/N+\eta_K\). Choosing \(K=\lceil\log_b N\rceil\) for sufficiently large \(N\) proves the rate. The equality \(M_{N,1,b}=1\) follows immediately by Tonelli, while strict \(\kappa_r(b)<1\) for \(r>1\) follows pointwise from the fact that at least two kernel coordinates are positive.

**3. Spectral-spacing limits.** The upper bound \(\kappa_r(b)\le1\) was just established. For \(1\le w\le\sqrt b\), retain the \(k=0\) kernel, and for \(\sqrt b\le w\le b\), retain \(k=-1\). Therefore
\[
\kappa_r(b)\ge\int_1^{\sqrt b}e^{-w}\,dw+\int_{\sqrt b}^{b}b^{-1}e^{-w/b}\,dw
=e^{-b^{-1/2}}-e^{-b^{1/2}}\longrightarrow1
\]
as \(b\to\infty\). For the opposite limit write \(h=\log b\), \(w=e^s\), \(0\le s\le h\). If \(1\le r<\infty\), then
\[
\kappa_r(b)=\int_0^h\left(\sum_{k\in\mathbb Z}G_r(s+kh)\right)^{1/r}\,ds,
\quad G_r(x)=e^{rx-r e^x}.
\]
The function \(G_r\) is continuous and integrable, and its shifted Riemann sums converge uniformly in \(0\le s\le h\) as \(h\downarrow0\):
\[
h\sum_{k\in\mathbb Z}G_r(s+kh)\longrightarrow\int_{\mathbb R}G_r(x)\,dx=\frac{\Gamma(r)}{r^r}.
\]
This proves the stated finite-\(r\) asymptotic. At \(r=\infty\) replace the sum by \(\sup_{k\in\mathbb Z}G_\infty(s+kh)\), with \(G_\infty(x)=e^{x-e^x}\); it converges uniformly to its unique maximum \(e^{-1}\), proving \(\kappa_\infty(b)\sim h/e\). All limiting operations are justified by positivity and the exponential or faster decay of these kernels.

## Verification
The proof above independently supplies the exact norm reduction, a nonasymptotic two-sided error for every permissible \(N,K,b,r\), and justified spacing limits. The optional standalone script `check_constant.py` evaluates the coefficient by an explicit finite sum and composite Simpson quadrature; it illustrates convergence but is not an infinite-dimensional proof or a certified numerical bound. A high-precision evaluation of the dyadic case gives \(\kappa_2(2)\approx0.416277305367437044\); the analytical claim does not depend on decimal accuracy. See `VERIFICATION.md` for checked assumptions and limits.

## Relationship to prior work
Lorist, van Neerven, Veraar and Weis (arXiv:2608.20266v2), Proposition 3.4, use the same dyadic kernels to prove qualitative failure of maximal \(L^p\)-regularity on \(\ell_1(\ell_r)\), with a large outer sequence index and coarse lower bounds. Their result neither states the exact finite-rank endpoint \(L^1(\ell_r^N)\) operator norm nor its leading log-periodic coefficient for general geometric ratio \(b\). Blunck (2001) characterizes discrete maximal regularity primarily on UMD spaces for exponents strictly greater than one and does not address this endpoint cutoff constant. Standard positivity, Minkowski and Hölder estimates are classical ingredients and are not individually claimed as novel.

## Limitations
The theorem applies to geometric positive spectra and time exponent exactly one. It does not determine the analogous coefficients for arbitrary eigenvalue sequences, stochastic maximal regularity, or the full mixed-norm \(\ell_1(\ell_r)\) operator. The error is explicit for fixed \(b>1\), but there is no asserted uniform \(b\downarrow1\), \(N\to\infty\) joint limit. The leading coefficient is a defined convergent integral, not a claimed elementary closed form. The literature comparison remains subject to possible unindexed equivalent formulations.

## References
1. E. Lorist, J. van Neerven, M. Veraar and L. Weis, *Necessary conditions for deterministic and stochastic maximal regularity*, arXiv:2608.20266v1 (first public 20 August 2026), v2, Proposition 3.4 and Corollary 3.5; https://borowiecki.dev/pdf/2608.20266.
2. S. Blunck, *Maximal regularity of discrete and continuous time evolution equations*, Studia Mathematica 146 (2001), 157–176, DOI 10.4064/sm146-2-3; https://www.impan.pl/shop/en/publication/transaction/download/product/90837.
