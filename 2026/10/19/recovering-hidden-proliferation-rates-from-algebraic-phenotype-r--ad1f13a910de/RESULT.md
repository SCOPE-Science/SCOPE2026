# Recovering hidden proliferation rates from algebraic phenotype relaxation

## Finding
For a finite irreducible phenotype-switching population with uniform competition and a flat carrying-capacity brake, the eventual phenotype mix is independent of proliferation rates, as known from previous convergence theory. Nevertheless, its **leading algebraic departure from equilibrium**, combined with the scalar population relaxation, uniquely determines every positive proliferation rate.

Precisely, put \(U(t)=\sum_{i=1}^{n}u_i(t)\), \(y(t)=u(t)/U(t)\), and \(z(t)=1-U(t)\). For a fixed \(p>1\) define \(\bar r=\sum_i r_i\pi_i\), where \(\pi\) is the stationary switching distribution. There is a uniquely determined zero-sum vector \(L\) such that
\[
QL=-\operatorname{diag}(\pi)(r-\bar r\mathbf1),\qquad \mathbf1^{\mathsf T}L=0.
\]
For every strictly positive initial vector with \(U(0)<1\),
\[
\lim_{t\to\infty}\frac{z(t)^{1-p}}{t}=(p-1)\bar r,\qquad
\lim_{t\to\infty}\frac{y(t)-\pi}{z(t)^p}=L.
\]
In particular, the entire proliferation vector is identified by these long-time data:
\[
\boxed{\quad r_i=\bar r-\frac{(QL)_i}{\pi_i},\quad i=1,\ldots,n.\quad}
\]
If the saturation exponent was not known beforehand, it is identified as well by \(\lim_{t\to\infty}\log z(t)/\log t=-1/(p-1)\). These formulas reconstruct rates from a vanishing signal, not from the equilibrium phenotype distribution alone.

## Assumptions and scope
Let \(n\ge2\). Let \(Q\in\mathbb R^{n\times n}\) be an irreducible continuous-time Markov generator written in **column** convention: \(Q_{ij}\ge0\) for \(i\ne j\), and \(\mathbf1^{\mathsf T}Q=0\). Let the proliferation rates \(r_i>0\) be fixed and let \(p>1\) be any real number. Consider the population equation
\[
\dot u=Qu+(1-\mathbf1^{\mathsf T}u)^p\operatorname{diag}(r)u,
\qquad u_i(0)>0,\quad 0<\sum_i u_i(0)<1.
\]
Only the invariant region \(0<U<1\) is considered. Irreducibility ensures a unique strictly positive probability column \(\pi\), with \(Q\pi=0\) and \(\sum_i\pi_i=1\); it need not satisfy detailed balance. The vector \(L\) above is uniquely solvable because its right side sums to zero and \(Q\) is invertible on the zero-sum subspace. The theorem concerns exact ideal continuous-time asymptotics, not noisy finite-time parameter inference.

## Proof
1. **Positive invariance and saturation.** The vector field is locally Lipschitz on \(0<U<1\). The positive orthant is forward invariant by the Metzler switching matrix and nonnegative proliferation. With \(a(t)=r^{\mathsf T}y(t)\in[r_{\min},r_{\max}]\), total mass obeys
\[
\dot U=U(1-U)^p a(t)>0.
\]
It cannot reach \(U=1\) in finite time because \(\dot U\le r_{\max}(1-U)^p\). Thus the solution stays positive and bounded for all time. If its increasing limit were smaller than one, then \(\dot U\ge U(0)r_{\min}(1-U)^p\) would be bounded away from zero, a contradiction. Hence \(U\to1\) and \(z\to0\).

2. **Stationary phenotype composition.** Differentiating \(y=u/U\) gives
\[
\dot y=Qy+z^pH(y),\quad H(y)=\operatorname{diag}(r)y-(r^{\mathsf T}y)y,\quad \mathbf1^{\mathsf T}H(y)=0.
\]
Write \(w=y-\pi\). Since the semigroup \(e^{Qt}\) contracts exponentially on the zero-sum subspace, there exist finite \(C,\gamma>0\) such that
\[
\|w(t)\|\le Ce^{-\gamma t}\|w(0)\|+C\int_0^t e^{-\gamma(t-s)}z(s)^p\,\|H(y(s))\|\,ds.
\]
The probability vector \(y(s)\) remains in the compact simplex, so \(H\) is bounded. Because \(z(s)^p\to0\), split the convolution at \(t/2\) to see its two pieces vanish. Therefore \(y(t)\to\pi\) and \(a(t)\to\bar r>0\).

3. **Algebraic saturation clock.** The identity
\[
\frac{d}{dt}z^{1-p}=(p-1)(1-z)\,a(t)
\]
shows, by averaging a function converging to \(\bar r\), that \(z(t)^{1-p}/t\to(p-1)\bar r\). Thus for \(\beta=p/(p-1)>1\),
\[
 z(t)^p\sim [(p-1)\bar r\,t]^{-\beta}.
\]
In particular, \(z(t-v)^p/z(t)^p\to1\) for every fixed \(v\ge0\), and \(z(t-v)^p/z(t)^p\) is uniformly bounded for \(0\le v\le t/2\) and large \(t\). These conclusions follow directly from the displayed positive asymptotic equivalent.

4. **The nonzero rate fingerprint.** The variation-of-constants formula on the zero-sum subspace is
\[
 w(t)=e^{Qt}w(0)+\int_0^t e^{Qv}z(t-v)^pH(y(t-v))\,dv.
\]
After dividing by \(z(t)^p\), the homogeneous term vanishes exponentially relative to its polynomial denominator. The contribution from \(v\ge t/2\) is likewise bounded by a constant times \(e^{-\gamma t/2}/z(t)^p\), and tends to zero. For \(0\le v\le t/2\), the preceding bounded-ratio fact and \(H(y(t-v))\to H(\pi)=h:=\operatorname{diag}(\pi)(r-\bar r\mathbf1)\) permit dominated convergence against \(Ce^{-\gamma v}\). The limit is
\[
\lim_{t\to\infty}w(t)/z(t)^p=\int_0^{\infty}e^{Qv}h\,dv=:L.
\]
The integral converges on the zero-sum subspace, satisfies \(QL=-h\), and sums to zero. Uniqueness follows from the one-dimensional nullspace of \(Q\). This proves the stated sharp limit even when \(h=0\).

5. **Inverse uniqueness.** The mass clock identifies \(\bar r\); the phenotype limit identifies \(L\). Rearranging \(QL=-\operatorname{diag}(\pi)(r-\bar r\mathbf1)\) yields \(r_i=\bar r-(QL)_i/\pi_i\). Since every \(\pi_i>0\), this is the unique compatible proliferation vector. Finally, \(z(t)\sim[(p-1)\bar r t]^{-1/(p-1)}\) gives the asserted log-slope and identifies \(p\) independently.

## Verification
For \(Q=\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\), \(r=(3,1)^{\mathsf T}\), and \(p=2\), the formulas give \(\pi=(1/2,1/2)^{\mathsf T}\), \(\bar r=2\), and \(L=(1/4,-1/4)^{\mathsf T}\). Consequently \(t^2(y_1(t)-1/2)\to1/16\). Recovering \(r\) from \(QL\) gives exactly \((3,1)^{\mathsf T}\).

The included `checker.py` evaluates the Poisson-type linear equations and integrates the transformed dynamical system for both \(p=2\) and \(p=3\), and for a nonsymmetric three-phenotype switching matrix. Execute `python checker.py` with Python 3, NumPy, and SciPy; it prints the theoretical and observed limiting fingerprints and ends in `PASS`. Numerical tests support the implementation but do not prove the infinite-time limits; the preceding analytic proof does.

## Relationship to prior work
Fassoni, *Fitness is asymptotically irrelevant under uniform competition in phenotype-structured populations* (arXiv:2609.32585v1, first public 2026-09-26), proves convergence of phenotype distributions to the switching stationary law and gives an explicit decay estimate for the fitness imprint. Its Theorem C addresses general Markov semigroups, but gives convergence/bounds rather than the sharp nonzero rescaled coefficient and its inverse recovery. Fassoni, *Stochastic gradient descent on the epigenetic landscape* (arXiv:2609.37703v1, 2026-09-29), treats the same general finite-state uniformly competitive system, including convergence and exponential switching-memory bounds (Theorem 1 and Appendix A). Its hypotheses allow many growth brakes; the present theorem instead isolates the **flat** brake and establishes its exact algebraic asymptotic and the inverse determination of the entire static fitness vector. These earlier equilibrium statements and general switching semigroup estimates are not claimed as new here. The zero-sum resolvent/Poisson equation is also a standard Markov-chain tool; the claim is its sharp scaling and injective fitness interpretation in this nonlinear demographic model.

## Limitations
The theorem requires fixed positive fitness, an irreducible time-independent finite switching generator, initial total biomass strictly below capacity, and a power-law saturation brake with exponent exceeding one. It gives no stability guarantee for reconstructing parameters from noisy, discrete, or realistically finite observation times. The normalized equilibrium alone never identifies fitness; the result requires access to the small asymptotic correction plus the mass relaxation. No claim is made for continuous phenotype spaces, nonuniform competition, or time-dependent fitness. Although two directly relevant primary preprints were inspected in HTML, there remains the ordinary possibility of an unindexed equivalent asymptotic calculation.

## References
- A. C. Fassoni, *Fitness is asymptotically irrelevant under uniform competition in phenotype-structured populations*, arXiv:2609.32585v1 (public 2026-09-26), https://arxiv.org/html/2609.32585v1.
- A. C. Fassoni, *Stochastic gradient descent on the epigenetic landscape: a unified framework for cellular plasticity, tumor heterogeneity, and the asymptotic irrelevance of fitness*, arXiv:2609.37703v1 (public 2026-09-29), https://arxiv.org/html/2609.37703v1.
