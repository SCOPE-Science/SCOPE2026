# Sharp random-sensor threshold for a single slowing Ornstein–Uhlenbeck mode

## Finding
Consider an \(n\)-dimensional stationary Ornstein–Uhlenbeck diffusion with one small relaxation rate and \(n-1\) unit relaxation rates. With \(m_n=\lfloor n^\kappa\rfloor\) independent random unit-direction sensors for fixed \(\kappa>0\), the sharp threshold for any sensor's *population slow-mode variance contribution to exceed its fast-mode contribution* has a logarithmic dimension-dependent scale and a nondegenerate Gumbel window.

For \(m\ge2\), put \(b_m=2\log m-\log\log m-\log\pi\). Let \(W_n^*\) be the largest squared projection of the sampled directions onto the unique slow mode. Then
\[
\frac{nW_n^*-b_{m_n}}{2}\ \Longrightarrow\ G,\qquad
\Pr(G\le x)=\exp(-e^{-x}).
\]
At the window \(\epsilon_n=(b_{m_n}+2x)/n\), the number \(K_n\) of sensors for which the critical mode contributes more stationary variance than all stable modes together satisfies
\[
K_n\Longrightarrow\operatorname{Poisson}(e^{-x}),\qquad
\Pr(K_n\ge1)\longrightarrow1-\exp(-e^{-x}).
\]
Thus \(\epsilon_n\approx 2\log m_n/n\) is the *sharp, second-order-centered* sensor-budget crossover, not merely an order-of-magnitude estimate. The probability is over random sensor directions. A fixed sensor population variance is not an estimated finite-sample variance.

The exact conditional maximum variance and its autocorrelation also yield a first-order phase diagram. If \(\epsilon_n\to0\) and \(q_n=n\epsilon_n/(2\log m_n)\to q\in[0,\infty]\), then, in probability,
\[
V_n^*\to
\begin{cases}
1/2,&q=\infty,\\
(1+q^{-1})/2,&0<q<\infty,\\
+\infty,&q=0,
\end{cases}
\]
where \(V_n^*\to+\infty\) means divergence in probability. For every fixed lag \(t>0\), the autocorrelation \(R_n^*(t)\) of a maximizing direction tends to \(e^{-t}\), \((q^{-1}+e^{-t})/(q^{-1}+1)\), or \(1\), in the same order.

## Assumptions and scope
For each integer \(n\ge2\), let \(X=(X_1,\ldots,X_n)\) be the *stationary* solution of the independent-noise SDEs
\[
dX_1(t)=-\epsilon_n X_1(t)\,dt+dB_1(t),\qquad
dX_j(t)=-X_j(t)\,dt+dB_j(t)\quad(2\le j\le n),
\]
where all \(B_j\) are independent standard Brownian motions and \(0<\epsilon_n<1\). The sensor directions \(U_{n,i}\), \(1\le i\le m_n\), are independent, Haar-uniform on \(S^{n-1}\subset\mathbb R^n\), and independent of the diffusion. The recorded scalar process is \(Z_{n,i}(t)=\langle U_{n,i},X(t)\rangle\). Define its conditional stationary population variance \(V_{n,i}=\operatorname{Var}(Z_{n,i}(0)\mid U_{n,i})\) and its conditional population lag autocorrelation \(R_{n,i}(t)\). Let \(i_n^*\) be any index of maximal variance, \(V_n^*=V_{n,i_n^*}\), and \(R_n^*(t)=R_{n,i_n^*}(t)\). With probability one, there are no ties for \(n\ge2\) and \(m_n\ge2\).

Write \(W_{n,i}=|U_{n,i,1}|^2\), \(W_n^*=\max_i W_{n,i}\), and \(K_n=\#\{i:W_{n,i}/\epsilon_n>1-W_{n,i}\}\). The strict inequality defines a *variance-component dominance criterion*; it is not a statement about the statistical power of finite-length data.

## Proof
**1. Exact finite-dimensional reduction.** Independent stationary OU coordinates satisfy \(\operatorname{Var}(X_1)=1/(2\epsilon_n)\), \(\operatorname{Var}(X_j)=1/2\) for \(j\ge2\), and respective lag covariances \(e^{-\epsilon_n t}/(2\epsilon_n)\) and \(e^{-t}/2\) for \(t\ge0\). Orthogonality of the observation vector gives
\[
V_{n,i}=\tfrac12[1+(\epsilon_n^{-1}-1)W_{n,i}],\qquad
R_{n,i}(t)=\frac{(W_{n,i}/\epsilon_n)e^{-\epsilon_n t}+(1-W_{n,i})e^{-t}}{W_{n,i}/\epsilon_n+1-W_{n,i}}.
\]
Since \(\epsilon_n<1\), maximization of variance is equivalent to maximization of \(W_{n,i}\). For a uniform spherical direction, \(W_{n,i}\) has the classical \(\operatorname{Beta}(1/2,(n-1)/2)\) law. If \(I_w\) is its regularized incomplete beta cdf, the *exact*, finite-\(n\), finite-\(m\) identities are
\[
\Pr(W_n^*\le w)=I_w(\tfrac12,\tfrac{n-1}{2})^{m_n},\qquad
\Pr(K_n=0)=I_{\epsilon_n/(1+\epsilon_n)}(\tfrac12,\tfrac{n-1}{2})^{m_n}.
\]
The second formula holds because slow variance exceeds fast variance if and only if \(W>\epsilon_n/(1+\epsilon_n)\).

**2. Uniform sphere-to-Gaussian comparison.** Realize the independent directions as \(U_{n,i}=G_{n,i}/\|G_{n,i}\|\), where all entries of the vectors \(G_{n,i}\) are independent standard normal variables. Put \(A_n=\max_{i\le m_n}G_{n,i,1}^2\), and \(D_{n,i}=\|G_{n,i}\|^2/n\). A union bound and standard exponential \(\chi^2_n\) concentration yield
\[
\max_{i\le m_n}|D_{n,i}-1|=O_{\Pr}\!\left(\sqrt{\frac{\log n}{n}}\right),
\]
for every fixed \(\kappa>0\). A Gaussian tail union bound yields \(A_n=O_{\Pr}(\log n)\). On the event where all \(D_{n,i}\) stay bounded away from zero,
\[
\left|nW_n^*-A_n\right|\le A_n\max_i|D_{n,i}^{-1}-1|
=O_{\Pr}\!\left(\frac{(\log n)^{3/2}}{\sqrt n}\right)=o_{\Pr}(1).
\]
In particular, the tiny fluctuations of the Gaussian denominators cannot change the order-one centering in the limiting extreme-value law.

**3. Extreme-value centering.** For \(Z\sim N(0,1)\), the elementary Mills-ratio expansion is
\[
\Pr(Z^2>y)=\sqrt{\frac2{\pi y}}e^{-y/2}\bigl(1+O(y^{-1})\bigr)\quad(y\to\infty).
\]
With \(m=m_n\to\infty\) and \(b_m=2\log m-\log\log m-\log\pi\), direct substitution gives, for each fixed real \(x\),
\[
m\Pr(Z^2>b_m+2x)\longrightarrow e^{-x}.
\]
Independence of the \(G_{n,i,1}\) therefore gives
\[
\Pr\bigl(A_n\le b_{m_n}+2x\bigr)\longrightarrow\exp(-e^{-x}),
\]
and the \(o_{\Pr}(1)\) comparison transfers this limit to \(nW_n^*\). It also implies \(nW_n^*/(2\log m_n)\to1\) in probability.

**4. Exact sharp window and Poisson law.** Fix \(x\in\mathbb R\) and choose \(\epsilon_n=(b_{m_n}+2x)/n\), which belongs to \((0,1)\) for all sufficiently large \(n\). The threshold becomes
\[
\frac{n\epsilon_n}{1+\epsilon_n}=b_{m_n}+2x+o(1),
\]
because \((\log m_n)^2/n\to0\). Thus for one sensor the exceedance probability \(p_n\) satisfies \(m_np_n\to e^{-x}\). Since different directions are independent, \(K_n\sim\operatorname{Binomial}(m_n,p_n)\), and the binomial-to-Poisson limit proves \(K_n\Rightarrow\operatorname{Poisson}(e^{-x})\). The stated nonzero-detection probability is its complement at zero.

**5. Population-moment phase diagram.** The convergence \(nW_n^*/(2\log m_n)\to1\) and the definition of \(q_n\) imply \(W_n^*/\epsilon_n\to q^{-1}\) for finite positive \(q\), \(W_n^*/\epsilon_n\to0\) for \(q=\infty\), and divergence in probability for \(q=0\). Also \(W_n^*\to0\) in probability, while \(e^{-\epsilon_n t}\to1\) for fixed \(t\) because \(\epsilon_n\to0\). Insert these into the exact formulas of Step 1. Boundary cases follow directly, with the natural conventions \(q^{-1}=0\) when \(q=\infty\) and \(q^{-1}=+\infty\) when \(q=0\).

## Verification
The standalone file `check_sensor_extremes.py` checks the exact beta maximum CDF in dimensions two and three, the exact slow/fast variance decomposition and autocorrelation algebra, and numerical proximity of the finite-sample beta threshold and classical \(\chi^2\) extremes to their Gumbel limits. Run with `python check_sensor_extremes.py` after installing SciPy. On the packaged source it reports 208 passing finite diagnostics. These computations are *not* proofs of the infinite statements; Steps 2–5 are their analytical proofs.

## Relationship to prior work
Ditlevsen and Ditlevsen (2026), Section 2 and its variance and autocorrelation equations, already determine how projection angle and stable-mode noise mask a slow direction in a fixed-dimensional example. Morr, Boers and Ashwin (2023/2024) analyze multivariate noise interference and fixed linear observables. Lohmann and Gottwald (2025) design observables to reveal critical slowing through the Fokker–Planck operator. These results motivate the question but do not supply the independent-random-sensor maximum, the \(\log m/n\) dominance scale, the second-order centering or the Poisson/Gumbel window. The spherical beta law and Gaussian maxima are classical and are not claimed as separate discoveries. The contribution is their exact integration into a dimensional sensor-budget law for the slow-mode population variance and autocorrelation of this explicit model.

## Limitations
The proof covers isotropic independent-coordinate noise, one slow mode, identical unit decay rates on all orthogonal modes, real Haar-random linear directions, independent directions, and polynomially many sensors. It does not establish a corresponding theorem under shared/correlated forcing, anisotropic stable covariance, exponentially many sensors, nonlinear bifurcation trajectories, finite sample-length measurement uncertainty, or noisy sensor selection. Detecting a contribution that dominates another is not equivalent to statistically detecting an impending tipping event. An earlier equivalent use of the Gaussian extreme-value theorem in sensor placement may exist; mathematical originality is subject to independent literature validation.

## References
1. S. Ditlevsen and P. Ditlevsen, “Early Warning Signals Can Vanish or Amplify: Dimensionality in Complex Systems,” arXiv:2609.01164v1, first posted 2026-09-01, especially Section 2 and equations (3)–(4). https://arxiv.org/html/2609.01164v1
2. J. Lohmann and G. A. Gottwald, “Choosing observables that capture critical slowing down before tipping points: A Fokker-Planck operator approach,” arXiv:2506.11735, first posted 2025-06-13. https://arxiv.org/html/2506.11735v2
3. A. Morr, N. Boers and P. Ashwin, “Internal noise interference in anticipation of tipping points of generic multi-dimensional dynamical systems,” arXiv:2311.18597, first posted 2023-11-30. https://ar5iv.labs.arxiv.org/html/2311.18597
4. A. Gasull, M. Jolis and F. Utzet, “On the norming constants for normal maxima,” arXiv:1308.5541, 2013. https://arxiv.org/abs/1308.5541
