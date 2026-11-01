# Sharp boundary law for weighted zero densities of finite-prime Dirichlet polynomials

## Finding
Fix an integer \(d\ge 2\), pairwise distinct primes \(p_1,\ldots,p_d\), positive real amplitudes \(a_1,\ldots,a_d\), a constant \(c>1/2+A\), and a real weight exponent \(\nu>0\). Write
\[
A=\sum_{j=1}^{d}a_j,\qquad K=\sum_{j=1}^{d}a_j\log p_j,\qquad \varphi(s)=c+\sum_{j=1}^{d}a_jp_j^{-s},
\]
and set \(w_\epsilon=c-A+\epsilon\) for \(\epsilon>0\). The weighted mean counting function obeys the sharp boundary asymptotic
\[
\boxed{M_{\varphi,\nu}(w_\epsilon)=C_{d,\nu,\boldsymbol a,\boldsymbol p}\,\epsilon^{\nu+(d-1)/2}(1+O(\epsilon))},
\]
where
\[
\boxed{C_{d,\nu,\boldsymbol a,\boldsymbol p}=\frac{\Gamma(\nu+1)K^{1-\nu}}{(2\pi)^{(d-1)/2}\Gamma(\nu+(d+1)/2)\sqrt{A\prod_{j=1}^da_j}}}>0.
\]
For example, for amplitudes \((1,1)\) at primes \((2,3)\) and \(\nu=1\), the leading coefficient is \(2/(3\pi)\) and the exponent is \(3/2\). For \((1,1,1)\) at \((2,3,5)\) and \(\nu=1\), the coefficient is \(\sqrt3/(12\pi)\) and the exponent is \(2\).

## Assumptions and scope
The Dirichlet polynomial is analytic on \(\operatorname{Re}s>0\) and satisfies \(\operatorname{Re}\varphi(s)>1/2\). The primes are distinct, so their logarithms are linearly independent over the rationals and the corresponding Bohr flow is equidistributed on the \(d\)-torus. Throughout, all of \(d\), the primes, the amplitudes and \(\nu>0\) are fixed while \(\epsilon\downarrow0\).

Solutions are counted with multiplicities. For \(w\ne c\), define
\[
M_{\varphi,\nu}(w)=\lim_{\sigma\downarrow0}\lim_{T\to\infty}\frac{\pi}{T}\!\sum_{\substack{\varphi(s)=w\\ \operatorname{Re}s>\sigma,\ |\operatorname{Im}s|<T}}(\operatorname{Re}s)^\nu.
\]
The iterated limits and the unweighted Jessen identity are understood in the sense of Kouroupis–Perfekt (2023), Theorem 1.1, and its Jessen–Tornehave antecedents. We prove finiteness directly from the bounded real part of every zero and the integral identity below. Only the real ray \(w_\epsilon=c-A+\epsilon\) is covered; no uniformity in \(d\) or in degenerating amplitude vectors is asserted.

## Proof
**1. Jessen reduction.** Put \(D=A-\epsilon\), \(\lambda_j=\log p_j\), \(b_j(\sigma)=a_je^{-\lambda_j\sigma}\), and \(B(\sigma)=\sum_j b_j(\sigma)\). Let \(\theta_d=0\), with \(\theta_1,\ldots,\theta_{d-1}\) independent uniform angles. The d-torus logarithmic mean of \(\varphi(s)-w_\epsilon\) exists by rational independence of prime logarithms. Integrating the common angular phase first by the elementary Jensen formula yields, for \(\sigma\ge0\),
\[
J_\epsilon(\sigma)=\mathbb E_\theta\log\max\{D,R_\sigma(\theta)\},\qquad R_\sigma(\theta)=\left|\sum_{j=1}^d b_j(\sigma)e^{i\theta_j}\right|.
\]
The source's counting identity gives \(M_{\varphi,0}(w_\epsilon,\sigma)=-J_\epsilon'(\sigma+)\). For any \(\nu>0\), its weighted integral identity and monotone limiting argument imply
\[
M_{\varphi,\nu}(w_\epsilon)=\nu\int_0^\infty \sigma^{\nu-1}M_{\varphi,0}(w_\epsilon,\sigma)\,d\sigma.
\]
The boundary term \(\sigma^\nu M_{\varphi,0}(w_\epsilon,\sigma)\) vanishes as \(\sigma\downarrow0\), since the unweighted count is bounded here.

**2. Exact support.** Since \(B(0)=A>D\) and \(B\) decreases strictly to zero, there is a unique \(\sigma_\epsilon>0\) such that \(B(\sigma_\epsilon)=D\). For \(\sigma\ge\sigma_\epsilon\), the triangle inequality gives \(R_\sigma(\theta)\le D\); hence \(J_\epsilon=\log D\) and \(M_{\varphi,0}=0\). Taylor's theorem gives
\[
\sigma_\epsilon=\frac\epsilon K+O(\epsilon^2),\qquad
\delta_\sigma:=B(\sigma)-D=K(\sigma_\epsilon-\sigma)(1+O(\epsilon))
\]
uniformly for \(0\le\sigma\le\sigma_\epsilon\).

**3. Uniform phase-cap asymptotic.** The function \(R_\sigma\) has a unique global maximizer on the relative angle torus at \(\theta=0\), since every \(b_j(\sigma)>0\); its maximum is \(B(\sigma)\). The real analytic function \(F_\sigma(\theta)=B(\sigma)-R_\sigma(\theta)\) is even under \(\theta\mapsto-\theta\), and therefore
\[
F_\sigma(\theta)=\frac12\theta^\mathsf{T}H_\sigma\theta+O(|\theta|^4),\quad
H_\sigma=\operatorname{diag}(b_1,\ldots,b_{d-1})-\frac{(b_ib_j)_{i,j<d}}{B(\sigma)}.
\]
The matrix is positive definite because the omitted amplitude \(b_d>0\). The matrix determinant lemma gives exactly
\[
\det H_\sigma=\frac{\prod_{j=1}^d b_j(\sigma)}{B(\sigma)}.
\]
The ellipsoid volume formula, the even-order remainder and the compact positive parameter range \(0\le\sigma\le\sigma_\epsilon=O(\epsilon)\) yield the *uniform* small-cap estimate, with \(h=(d-1)/2\),
\[
\mathbb P\{R_\sigma>D\}=\frac{\sqrt{B(\sigma)/\prod_jb_j(\sigma)}}{(2\pi)^h\Gamma(h+1)}\delta_\sigma^h\bigl(1+O(\delta_\sigma)\bigr).
\]
Indeed, the set is \(F_\sigma(\theta)<\delta_\sigma\); rescale \(\theta=\sqrt{\delta_\sigma}\,u\) and compare the volume of the quadratic ellipsoid to its analytic-even perturbation. The factor \((2\pi)^{d-1}\) in the denominator is the normalized torus measure. This step is uniform in \(\sigma\) because the amplitude vector varies in a compact subset of the positive orthant.

**4. Derivative of the logarithmic mean.** For \(0\le\sigma<\sigma_\epsilon\), the level surface \(R_\sigma=D\) has angular measure zero (it is nonconstant real analytic). Differentiation under the integral gives
\[
-J_\epsilon'(\sigma)=\mathbb E\left[\mathbf1_{\{R_\sigma>D\}}\frac{-\partial_\sigma R_\sigma}{R_\sigma}\right].
\]
On the cap, \(|\theta|^2=O(\delta_\sigma)\). Because derivatives are even in \(\theta\), with \(K_\sigma=\sum_j\lambda_jb_j(\sigma)\), one has
\[
-\partial_\sigma R_\sigma=K_\sigma+O(\delta_\sigma),\qquad R_\sigma=B(\sigma)+O(\delta_\sigma).
\]
Consequently
\[
M_{\varphi,0}(w_\epsilon,\sigma)=\frac{K}{A}\frac{\sqrt{A/\prod_j a_j}}{(2\pi)^h\Gamma(h+1)}\delta_\sigma^h(1+O(\epsilon)),
\]
uniformly on \(0\le\sigma<\sigma_\epsilon\), and both sides vanish at the endpoint.

**5. Beta integration.** Substitute this expression into the weighted identity. The rescaling \(\sigma=(\epsilon/K)u\), and \(\delta_\sigma=\epsilon(1-u)(1+O(\epsilon))\) in an integrated, uniform relative sense (more precisely use \(u=\sigma/\sigma_\epsilon\) and the previous uniform difference formula), gives
\[
\begin{aligned}
M_{\varphi,\nu}(w_\epsilon)
&=\nu\,\frac{K}{A}\frac{\sqrt{A/\prod_j a_j}}{(2\pi)^h\Gamma(h+1)}\left(\frac\epsilon K\right)^\nu\epsilon^h
\int_0^1 u^{\nu-1}(1-u)^h\,du\,(1+O(\epsilon))\\
&=\frac{\Gamma(\nu+1)K^{1-\nu}}{(2\pi)^h\Gamma(\nu+h+1)\sqrt{A\prod_ja_j}}\epsilon^{\nu+h}(1+O(\epsilon)).
\end{aligned}
\]
The Beta identity holds for every fixed \(\nu>0\) and \(h>0\). Positivity of the leading coefficient proves strict positivity for sufficiently small \(\epsilon>0\); the representation proves finiteness. This proves the assertion.

## Verification
The included standalone program `verification/check.py` uses exact rational arithmetic for the phase-Hessian determinant and deterministic torus midpoint quadratures of the *exact Jensen mean*, not simulation of zeros. The calculated ratios to the proposed leading constants converge to \(1\) for two and three prime frequencies. Numerical finite quadrature is corroboration, not the proof of the uniform small-cap lemma or the infinite-height zero count.

## Relationship to prior work
Kouroupis and Perfekt (2023) establish the general weighted counting function and its relation to the derivative of the Jessen mean, including the integral identity used here. Brevig and Perfekt (2020) establish the unweighted mean-counting framework. The present result specializes to a natural family but computes a dimension-dependent *exact* boundary exponent and coefficient which those source theorems do not state. Ronkin/Mahler-measure geometry for affine polynomials, discussed by Lundqvist (2015) and Bao–He–Zahabi (2022), supplies a related geometric framework; the final asymptotic requires the phase-cap determinant and weighted beta integration. A general undetected Ronkin boundary theorem could conceivably imply these formulas; priority is therefore provisional pending independent historical review.

## Limitations
The statement requires fixed positive amplitudes, distinct prime frequencies, a real target approaching the *negative extreme point* of the symbol's range, and a fixed \(\nu>0\). It gives no estimates uniform under coalescing amplitudes, unbounded prime counts or simultaneous parameter limits. It does not characterize arbitrary complex target approaches, nor does it imply compactness or boundedness criteria for composition operators. The correctness and novelty assessments are a self-review analysis, not independent certification.

## References
1. A. Kouroupis and K.-M. Perfekt, “Composition operators on weighted Hilbert spaces of Dirichlet series,” *J. London Math. Soc.* 108 (2023), 837–868, first published May 24, 2023, DOI 10.1112/jlms.12771.
2. O. F. Brevig and K.-M. Perfekt, “A mean counting function for Dirichlet series and compact composition operators,” preprint first posted May 11, 2020, arXiv:2005.05094.
3. J. Lundqvist, “An explicit calculation of the Ronkin function,” *Ann. Fac. Sci. Toulouse* 24 (2015), 227–250, DOI 10.5802/afst.1447.
4. J. Bao, Y.-H. He and A. Zahabi, “Mahler Measure for a Quiver Symphony,” *Commun. Math. Phys.* 394 (2022), 573–624, arXiv:2108.13903.
