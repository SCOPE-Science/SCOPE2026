# Critical spectral density of the differential Hilbert operator between weighted Bergman Hilbert spaces

## Finding

Fix \(-1<\alpha<0\), put \(s=(\alpha+1)/2\) and \(c=\sqrt{(\alpha+2)(\alpha+3)}\). For \(\delta>0\), consider the differential Hilbert operator
\[
T_\delta f(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt:
A_\alpha^2\longrightarrow A_{\alpha+2+\delta}^2.
\]
Write \(s_j(T_\delta)\) for its singular values, with multiplicities, and define
\[
M_s(\xi)=\frac{\pi}{\cos\bigl(\pi(s+i\xi)\bigr)},\qquad
b_s(\xi)=c^2|M_s(\xi)|^2
=\frac{c^2\pi^2}{\cos^2(\pi s)+\sinh^2(\pi\xi)}.
\]
For **every fixed threshold** \(t>0\), the number of singular values greater than \(t\) has the exact critical density
\[
\boxed{\lim_{\delta\downarrow0}\delta\,\#\{j:s_j(T_\delta)>t\}
=\frac1{2\pi}\int_{\mathbb R}\left[\log\frac{b_s(\xi)}{t^2}\right]_+d\xi.}
\]
Here \([x]_+=\max(x,0)\). In addition, for **every fixed real** \(p\ge2\),
\[
\boxed{\lim_{\delta\downarrow0}\delta\,\|T_\delta\|_{\mathcal S_p}^{p}
=\frac{2}{p}\frac{c^p}{2\pi}\int_{\mathbb R}|M_s(\xi)|^p\,d\xi.}
\]
The stronger weighted spectral-distribution statement is: for every continuous function \(F\) on a compact interval containing all spectra \(\sigma(T_\delta^*T_\delta)\) for small \(\delta\),
\[
\lim_{\delta\downarrow0}\delta\,\operatorname{Tr}\bigl[T_\delta^*T_\delta F(T_\delta^*T_\delta)\bigr]
=\frac1{2\pi}\int_{\mathbb R}\int_0^\infty e^{-u}b_s(\xi)F(e^{-u}b_s(\xi))\,du\,d\xi.
\]
At \(\alpha=-1/2\), this implies the explicit benchmarks
\[
\lim_{\delta\downarrow0}\delta\|T_\delta\|_{\mathcal S_2}^2=\frac{15\pi}{8},\qquad
\lim_{\delta\downarrow0}\delta\|T_\delta\|_{\mathcal S_4}^4=\frac{225\pi^2}{16}.
\]

## Assumptions and scope

The spaces are complex analytic weighted Bergman Hilbert spaces with normalized area measure \(dA=dx\,dy/\pi\), and
\[
\|f\|_{A_\gamma^2}^2=(\gamma+1)\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\gamma\,dA(z),\qquad \gamma>-1.
\]
Their monomials are orthogonal and
\[
w_n(\gamma)=\|z^n\|_{A_\gamma^2}^2
=\frac{\Gamma(\gamma+2)\Gamma(n+1)}{\Gamma(n+\gamma+2)}.
\]
The claim holds for all fixed \(-1<\alpha<0\), with the indicated limit \(\delta\downarrow0\); no uniformity in \(\alpha\), \(p\), or a threshold tending to zero is claimed. The source paper establishes compactness and membership in all \(\mathcal S_p\), \(p\ge1\), for each \(\delta>0\); the result here concerns their new sharp asymptotic spectral distribution as the compactness boundary is approached.

## Proof

**Step 1: coefficient kernel and uniform Hilbert--Schmidt reduction.** With the normalized monomial bases, the operator is the matrix \(B_\delta=(b_{nk}^{(\delta)})_{n,k\ge0}\) with
\[
b_{nk}^{(\delta)}=\frac{n+1}{n+k+1}
\left[\frac{\Gamma(\alpha+4+\delta)\Gamma(n+1)}{\Gamma(n+\alpha+4+\delta)}
\frac{\Gamma(k+\alpha+2)}{\Gamma(\alpha+2)\Gamma(k+1)}\right]^{1/2}.
\]
Write \(c_\delta=[\Gamma(\alpha+4+\delta)/\Gamma(\alpha+2)]^{1/2}\). On \([1,\infty)^2\), introduce the integral kernel
\[
K_\delta(x,y)=c_\delta x^{-\delta/2}\frac{(y/x)^s}{x+y}.
\]
For any fixed sufficiently small \(\delta_0>0\), standard uniform Gamma-ratio estimates show that, for \(0\le\delta\le\delta_0\),
\[
\left|b_{nk}^{(\delta)}-K_\delta(n+1,k+1)\right|
\le C_\alpha K_\delta(n+1,k+1)
\left(\frac1{n+1}+\frac1{k+1}\right).
\]
The same relative estimate holds for replacing the kernel's value at a cell corner by its value anywhere in \([n+1,n+2)\times[k+1,k+2)\), since the logarithmic partial derivatives of \(K_\delta\) are bounded respectively by \(C_\alpha/x\) and \(C_\alpha/y\). Moreover,
\[
\sum_{n,k\ge0}K_\delta(n+1,k+1)^2
\left(\frac1{n+1}+\frac1{k+1}\right)^2\le C_\alpha.
\]
To verify the last estimate directly, write \(x=n+1\), \(y=k+1\), split into \(y\ge x\) and \(y\le x\), and bound \(K_\delta\) respectively by \(C x^{-s}y^{s-1}\) and \(C x^{-s-1}y^s\). Since \(0<s<1/2\), summing the squared bounds times \((x^{-1}+y^{-1})^2\) converges. Let \(J:\ell^2(\mathbb N_0)\to L^2([1,\infty))\) send each coordinate vector to the indicator of its unit interval. Identifying \(K_\delta\) with its integral operator, the estimates give
\[
\sup_{0<\delta\le\delta_0}\|JB_\delta J^*-K_\delta\|_{\mathcal S_2}<\infty.\tag{1}
\]
This compares actual operators, including the zero action of \(JB_\delta J^*\) on the orthogonal complement of the step-function subspace.

**Step 2: logarithmic convolution model.** The unitary \(Uf(u)=e^{u/2}f(e^u)\) from \(L^2([1,\infty),dx)\) to \(L^2([0,\infty),du)\) transforms \(K_\delta\) into
\[
(A_\delta f)(u)=c_\delta e^{-\delta u/2}
\int_0^\infty h_s(v-u)f(v)\,dv,\qquad
h_s(t)=\frac{e^{st}}{2\cosh(t/2)}.
\]
Both tails of \(h_s\) decay exponentially because \(0<s<1/2\). Thus \(\|A_\delta\|\le c_\delta\|h_s\|_1\), and, for \(\delta>0\),
\[
\|A_\delta\|_{\mathcal S_2}^2
=c_\delta^2\int_0^\infty e^{-\delta u}
\int_{-u}^\infty h_s(t)^2\,dt\,du
\le\frac{C_\alpha}{\delta}.
\]
Together with (1), this gives uniform operator-norm bounds and Hilbert--Schmidt norms \(O(\delta^{-1/2})\) for both the exact and model operators.

**Step 3: all positive integer spectral moments.** Fix any integer \(q\ge1\). Put \(G_\delta=A_\delta^*A_\delta\). Expanding the trace of \(G_\delta^q\) by Tonelli gives
\[
\operatorname{Tr}(G_\delta^q)=c_\delta^{2q}
\int_{[0,\infty)^{2q}}\prod_{i=1}^q
\Bigl[e^{-\delta u_i}h_s(v_i-u_i)h_s(v_{i+1}-u_i)\Bigr]
\,d\boldsymbol u\,d\boldsymbol v,
\quad v_{q+1}=v_1.
\]
Anchor \(u_1=t\), subtract \(t\) from all other integration variables, and substitute \(t=z/\delta\). The graph of the \(2q\) convolution edges is connected. Hence its product of exponential-decay kernels is integrable in all \(2q-1\) differences, with an exponentially decaying envelope, even after multiplication by \(e^{-\delta\sum_{i=2}^q(u_i-t)}\) for sufficiently small \(\delta\). For every fixed \(z>0\), dominated convergence removes the half-line boundary because \(t=z/\delta\to\infty\). A second dominated convergence in \(z\) now yields
\[
\lim_{\delta\downarrow0}\delta\operatorname{Tr}(G_\delta^q)
=\frac{c^{2q}}q J_q,
\qquad
J_q=\frac1{2\pi}\int_{\mathbb R}|\widehat h_s(\xi)|^{2q}\,d\xi.
\tag{2}
\]
Indeed the entire-line difference integral equals the convolution trace density \(J_q\), by Plancherel. With the transform convention \(\widehat h_s(\xi)=\int_{\mathbb R}e^{-i\xi t}h_s(t)\,dt\), the beta integral yields
\[
\widehat h_s(\xi)=\frac{\pi}{\cos\bigl(\pi(s-i\xi)\bigr)},
\qquad |\widehat h_s(\xi)|=|M_s(\xi)|.
\]
We transfer (2) back to \(B_\delta\). For nonnegative trace-class operators, telescoping the difference of their powers gives
\[
\left|\operatorname{Tr}\bigl((S^*S)^q-(T^*T)^q\bigr)\right|
\le q\max(\|S\|,\|T\|)^{2q-2}
\|S-T\|_2(\|S\|_2+\|T\|_2).
\]
Using (1), its right side is \(O_q(\delta^{-1/2})\); multiplication by \(\delta\) makes it vanish. Consequently, for the original differential Hilbert operator,
\[
\lim_{\delta\downarrow0}\delta\operatorname{Tr}[(T_\delta^*T_\delta)^q]
=\frac{c^{2q}}{2\pi q}\int_{\mathbb R}|M_s(\xi)|^{2q}\,d\xi
\qquad(q=1,2,\ldots).\tag{3}
\]

**Step 4: full limiting spectral measure.** Let \(\lambda_j(\delta)=s_j(T_\delta)^2\). Define the finite positive measures
\[
\mu_\delta=\delta\sum_j\lambda_j(\delta)\,\delta_{\lambda_j(\delta)}.
\]
The operator-norm bound provides one common compact spectral interval, and the \(q=1\) case of (3) provides bounded total masses. The moment limits (3) determine, by polynomial approximation on that interval, weak convergence to the finite positive measure characterized by
\[
\int F(\lambda)\,d\mu_0(\lambda)
=\frac1{2\pi}\int_{\mathbb R}\int_0^\infty
 e^{-u}b_s(\xi)F(e^{-u}b_s(\xi))\,du\,d\xi.
\]
This is the asserted weighted spectral-distribution statement. Since \(\mu_0\) has no atom at any \(\lambda>0\), apply weak convergence to \(\mathbf1_{(t^2,\infty)}(\lambda)/\lambda\); integration in \(u\) produces the boxed counting law. For any fixed \(p\ge2\), applying it instead to \(F(\lambda)=\lambda^{p/2-1}\), continuous even at zero, gives
\[
\lim_{\delta\downarrow0}\delta\sum_j\lambda_j(\delta)^{p/2}
=\frac{c^p}{2\pi}\int|M_s(\xi)|^p d\xi
\int_0^\infty e^{-pu/2}\,du,
\]
which is the boxed Schatten asymptotic.

## Verification

The coefficient matrix is the direct exact expansion of \((1-tz)^{-2}\), using the stated monomial norms. The main nonstandard estimates are the uniform Hilbert--Schmidt comparison (1), the connected-cycle domination in Step 3, and the moment-determinacy argument in Step 4; all are proved above without using a finite experiment to infer an infinite theorem. The beta integral gives the independent check
\[
\frac1{2\pi}\int_{\mathbb R}|M_s(\xi)|^2d\xi
=\int_{\mathbb R}h_s(t)^2dt=B(1+2s,1-2s).
\]
At \(s=1/4\), one has \(|M_s(\xi)|^2=2\pi^2\operatorname{sech}(2\pi\xi)\), giving \(J_1=\pi/2\) and \(J_2=2\pi^2\), hence the two displayed exact benchmarks. A standalone numerical check reproduces these integrals and evaluates finite logarithmic-convolution discretizations as an illustrative, non-certifying consistency test.

## Relationship to prior work

Li and Zhou (arXiv:2610.05672, public October 5, 2026) prove the sharp compactness boundary, trace-class membership immediately above it, the critical operator norm, and a double-series formula for the Hilbert--Schmidt norm. Their complete primary text does not state the \(\delta\)-scaled singular-value counting law, spectral measure, or the all-real-\(p\ge2\) asymptotic constants. The present theorem resolves that quantitative boundary degeneration rather than reproving membership.

Fedele (arXiv:1903.11572; published 2020) studies singular-value densities of fixed-symbol Hankel matrices under large finite-section and regularizing Schur cutoffs. The current two-weight coefficient matrix is generally non-Hankel, and its parameter-dependent power damping creates an additional continuum of logarithmic spatial scales. Fedele's fixed-cutoff theorem does not directly yield the \(e^{-u}\)-mixture shown here; it is relevant methodological precedent. General Szegő/Wiener--Hopf trace asymptotics provide a broader conceptual analogy, not an identified statement for this operator family.

## Limitations

Only \(-1<\alpha<0\) is treated. The limiting counting law is pointwise at each fixed \(t>0\), not uniform as \(t\downarrow0\). The Schatten limit is proved only for fixed \(p\ge2\); it does not establish a corresponding sharp \(\mathcal S_1\)-norm asymptotic. It does not determine individual singular-value asymptotics at ranks scaling in a prescribed way with \(\delta\). Historical priority relative to very general operator-valued semiclassical trace theorems remains a residual risk.

## References

1. Songxiao Li and Mengmeng Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672v1, first public October 5, 2026. Full text: https://arxiv.org/html/2610.05672v1.
2. Emilio Fedele, *The spectral density of Hankel operators with piecewise continuous symbols*, arXiv:1903.11572, first public March 27, 2019; *Integral Equations and Operator Theory* 92 (2020), article 1, https://doi.org/10.1007/s00020-019-2556-9.
3. A. Böttcher, *Schatten norms of Toeplitz matrices with Fisher--Hartwig singularities*, *Electronic Journal of Linear Algebra* 15 (2006), https://doi.org/10.13001/1081-3810.1235 (related Toeplitz rather than this weighted Hilbert family).
