# A sharp skewness window and a mixing penalty in two-atom clipped SGD

## Finding

Consider constant-step, whole-gradient-clipped stochastic gradient descent on a scalar quadratic with centered two-point noise. For every integer \(N\ge1\), total noise span \(S>0\), and \(0<p<1\), put \(q=1-p\), \(c=S/N\), and let fresh independent gradient errors be \(+qS\) with probability \(p\) and \(-pS\) with probability \(q\). For the curvature-normalized step \(\eta=1\),
\[
X_{n+1}=X_n-\operatorname{clip}_{c}(X_n+\Xi_{n+1}),
\qquad \operatorname{clip}_{c}(v)=\max\{-c,\min(v,c)\}.
\]
From every deterministic real start, the process almost surely enters the finite lattice \(x_j=-qS+jS/N\), \(0\le j\le N\), in finite time and never leaves. Its unique stationary law and complete nontrivial transition spectrum are
\[
\pi_j=\frac{(q/p)^j}{\sum_{\ell=0}^{N}(q/p)^\ell},
\qquad
\lambda_k=2\sqrt{pq}\cos\frac{k\pi}{N+1},\quad 1\le k\le N.
\]
The remaining eigenvalue equals \(1\). Thus the exact absolute nontrivial spectral radius is \(2\sqrt{pq}\cos(\pi/(N+1))\).

There is a sharp skewness window as \(N\to\infty\) with fixed \(S\). If \(p_N=1/2+\theta/N\), for fixed \(\theta\in\mathbb R\) and all sufficiently large \(N\), the stationary positions converge weakly to a continuously distributed \(X_\theta\) on \([-S/2,S/2]\) with density
\[
h_\theta(x)=\begin{cases}
\dfrac{2\theta}{S\sinh(2\theta)}e^{-4\theta x/S},&\theta\ne0,\\
1/S,&\theta=0,
\end{cases}
\]
and the spectral gap satisfies
\[
N^2\left(1-2\sqrt{p_N(1-p_N)}\cos\frac\pi{N+1}\right)
\longrightarrow\frac{\pi^2}{2}+2\theta^2.
\]
The limiting mean and variance are respectively
\[
\mathbb E X_\theta=S\left(\frac{1}{4\theta}-\frac{\coth(2\theta)}2\right),\quad
\operatorname{Var}(X_\theta)=S^2\left(\frac1{16\theta^2}-\frac1{4\sinh^2(2\theta)}\right)
\]
for \(\theta\ne0\), extended continuously as \(0\) and \(S^2/12\) at \(\theta=0\). If instead \(p_N-1/2\to0\) with \(N(p_N-1/2)\to+\infty\), the limiting position is \(-S/2\); the opposite sign concentrates at \(+S/2\). Fixed \(p<1/2\) concentrates at \(+pS\), and fixed \(p>1/2\) at \(-qS\), with stationary variance of order \(N^{-2}\). Therefore the skewness transition has the exact scale \(N^{-1}\).

For exactly symmetric samples, \(p=q=1/2\), the invariant distribution is uniform on the \(N+1\) sites. With \(c=S/N\) and a stationary chain, the coordinate's integrated autocorrelation time and the asymptotic variance coefficient of sample averages are exactly
\[
\tau_{\mathrm{int}}=\frac{2N^2+4N-1}{5},\qquad
\lim_{T\to\infty} T\operatorname{Var}\left(\frac1T\sum_{n=0}^{T-1}X_n\right)
=\frac{S^2(N+2)(2N^2+4N-1)}{60N}.
\]
In contrast, the single-iterate variance is \(S^2(N+2)/(12N)\), which falls from \(S^2/4\) to \(S^2/12\) as clipping becomes stronger, even as the time-average variance coefficient diverges like \(S^2N^2/30\). At \(N=1\), the samples are independent and the two coefficients coincide at \(S^2/4\).

## Assumptions and scope

The population objective is \(f(x)=x^2/2\), and the stochastic gradient is the unbiased oracle \(x+\Xi\). Sampling is independent across iterations. The learning rate is the reciprocal of the quadratic curvature (normalized to one). The clipping threshold is commensurate with the two-noise-atom span, exactly \(c=S/N\). All claims about global absorption concern any fixed finite deterministic initial position; the resulting unique invariant measure applies to any initial distribution as well. The time-average variance identity assumes stationary initialization and takes \(T\to\infty\) at fixed \(N\), before any \(N\to\infty\) limit. Spectral gap means \(1\) minus the largest nonunit eigenvalue; here it also equals \(1\) minus the nontrivial absolute spectral radius.

## Proof

**1. A finite lattice emerges from an unconstrained real recursion.** The closed interval \(I=[-qS,pS]\) is invariant. For \(x>pS\), both possible clipped gradients are positive and the next iterate moves toward \(I\), by \(c\) or by a final partial displacement landing at its upper endpoint. The analogous fact holds for \(x<-qS\). Hence the process enters \(I\) after finitely many steps irrespective of future choices. Introduce \(z=x+qS\in[0,S]\). Its two noise-conditioned update maps are exactly
\[
z\mapsto\max\{z-c,0\}\quad(\Xi=+qS),\qquad
z\mapsto\min\{z+c,S\}\quad(\Xi=-pS).
\]
Every run of \(N\) consecutive plus noises sends every \(z\in[0,S]\) to zero. Disjoint blocks of length \(N\) are independent; each is such a run with probability \(p^N>0\). Thus the first complete plus block appears almost surely, with a geometric block-count tail. Thereafter the state remains on \(\{jc:0\le j\le N\}\). This proves finite-time lattice absorption, not merely approximate attraction to lattice points.

**2. Exact invariant law and spectrum.** On the lattice, indices move one site left with probability \(p\), one site right with probability \(q\), and hold at the appropriate endpoint when a proposed move exits. Detailed balance on every adjacent pair requires \(\pi_jq=\pi_{j+1}p\), giving the stated truncated geometric law. Because \(p,q>0\), the finite chain is irreducible and has positive self-loops, hence is aperiodic; its stationary law is unique and it converges in total variation. Absorption implies these properties for the original real-valued process after its random entrance time, and excludes any further invariant distribution. Conjugating by the square root of the stationary weights produces a symmetric tridiagonal matrix with off-diagonal entries \(\sqrt{pq}\), boundary diagonal entries \(p,q\), and zero interior diagonal. Its characteristic polynomial is
\[
(\lambda-1)(\sqrt{pq})^N U_N\!\left(\frac{\lambda}{2\sqrt{pq}}\right),
\]
where \(U_N\) is the degree-\(N\) Chebyshev polynomial of the second kind. This identity follows by the tridiagonal determinant recurrence and the two endpoint conditions; its \(N\) nonunit roots yield the claimed spectrum.

**3. Sharp skewness scaling.** The stationary weights depend on \(p\) only through \(r=q/p\). At \(p_N=1/2+\theta/N\),
\[
N\log r_N\to-4\theta,\qquad
x_j/S=-q_N+j/N\to-1/2+j/N.
\]
The stationary expectations are therefore weighted Riemann sums converging to integrals with weight \(e^{-4\theta t}\) on \([-1/2,1/2]\). Normalizing and differentiating the resulting partition function \(\sinh(2\theta)/(2\theta)\) yields the mean and variance formulas. If \(N|p_N-1/2|\to\infty\) while \(p_N\to1/2\), the endpoint mass outside every fixed neighborhood tends to zero by the geometric weight ratio; the endpoint is chosen by the sign. For fixed unequal probabilities the same geometric tail estimate gives endpoint concentration with fluctuations of size \(O(S/N)\). Finally,
\[
2\sqrt{p_Nq_N}=\sqrt{1-4\theta^2/N^2},
\]
combined with the cosine expansion proves the spectral critical law and shows that \(N^{-1}\) is the exact cross-over scale.

**4. Exact symmetric averaging cost.** At \(p=q=1/2\), write \(y_j=j-N/2\). The centered observable is \(f_j=cy_j\), and the explicit centered Poisson solution is
\[
g_j=c\left[\left(\frac{N^2}{4}+\frac N2+\frac13\right)y_j-\frac{y_j^3}{3}\right],\qquad
(I-P)g=f.
\]
The identity holds also at the reflecting endpoints, which is necessary for the exact coefficient. For the uniform measure, the exact sums are
\[
\mathbb E_\pi[y^2]=\frac{N(N+2)}{12},\qquad
\mathbb E_\pi[y^4]=\frac{N(N+2)(3N^2+6N-4)}{240}.
\]
Reversibility and the absence of a nonconstant eigenvalue of modulus one give the Green–Kubo identity
\[
\lim_{T\to\infty}T\operatorname{Var}(T^{-1}\sum_{n<T}X_n)
=2\langle f,g\rangle_\pi-\langle f,f\rangle_\pi.
\]
Substitution gives the stated rational coefficient. Dividing by the stationary variance gives the integrated autocorrelation time. This uses an infinite covariance sum justified by the finite-chain spectrum; it is not inferred from a finite simulation.

## Verification

Run `python verify.py` with Python 3 and no third-party dependencies. The script checks the two clipped maps, exact invariant probabilities, geometric reset from external starts, the characteristic-polynomial roots, the exact endpoint-inclusive Poisson equation, uniform-coordinate moment identities, the averaging coefficients, and numerical critical-window convergence. Its exact-rational and numerical assertions passed in the packaged test run. Numerical limits are supporting checks; the results for all positive integers \(N\), all \(p\in(0,1)\), and all real \(\theta\) rest on the above proofs.

## Relationship to prior work

Koloskova, Hendrikx and Stich (2023) define the clipped-gradient update and prove stochastic clipping-bias and convergence bounds. Their main estimates do not classify fixed-step invariant distributions, exact transition spectra, or the sharp \(N^{-1}\) noise-skewness window. Chen, Wu and Hong (2020) treat geometric clipping bias; Mai and Johansson (2021) treat clipping stability and convergence. Suvorikova et al. (2026) give a related two-atom asymmetric-noise example for a **decreasing** step sequence and identify a shifted mean-field root, as well as broader averaging risk comparisons, but not the fixed-step lattice absorption, the stationary transition spectrum, or the present critical law. Classical reflected birth–death-chain theory already contains the geometric stationary weights and Chebyshev spectral analysis **for an abstract walk**; these constituent facts are not independently claimed as new. The mathematical contribution is the exact reduction from the unprojected, nonlinear clipped optimizer for every real start and the resulting critical skewness–mixing classification and quantitative averaging tradeoff. Earlier published signSGD/Ehrenfest-chain examples involve a different noise distribution and a different birth–death kernel.

## Limitations

This is an exact, intentionally specialized benchmark, not a universal clipping guarantee. The reciprocal-curvature learning rate and commensurability \(c=S/N\) matter; noncommensurate clipping thresholds can yield different invariant supports. The two-point distribution has bounded noise; no heavy-tail conclusions follow. The spectral gap characterizes stationary reversible relaxation, not a dimension-free worst-initial-state total-variation mixing time, and no inference is drawn about changing \(N\) during a single optimization run. The order of stationary sample-average and fine-clipping limits matters. Existing general Markov-chain results may encompass individual components of the theorem under another formulation; the publication-priority assessment of their precise combination is not independently certified.

## References

- A. Koloskova, H. Hendrikx, and S. U. Stich, *Revisiting Gradient Clipping: Stochastic Bias and Tight Convergence Guarantees*, arXiv:2305.01588, first posted 2023-05-02. https://arxiv.org/abs/2305.01588
- X. Chen, B. Wu, and Y. Hong, *Understanding Gradient Clipping in Private SGD: A Geometric Perspective*, arXiv:2006.15429. https://arxiv.org/abs/2006.15429
- V. Mai and M. Johansson, *Stability and Convergence of Stochastic Gradient Clipping: Beyond Lipschitz Continuity and Smoothness*, arXiv:2102.06489. https://arxiv.org/abs/2102.06489
- A. Suvorikova et al., *Clipped or Unclipped? Finite-Sample Trade-offs for Averaged SGD under Heavy-Tailed Noise*, arXiv:2609.32962, first posted 2026-09-26, especially Proposition D.5 and Appendix E. https://arxiv.org/abs/2609.32962
- Classical finite birth–death chain reversibility, Chebyshev tridiagonal spectra, and Poisson-equation variance identities are used as standard mathematical tools.
