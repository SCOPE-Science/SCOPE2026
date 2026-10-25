# A half-integer inverse-moment staircase for a Gaussian RMSprop variance accumulator

## Finding

The stationary second-moment accumulator associated with independent standard Gaussian gradient innovations is
\[
V_\beta=(1-\beta)\sum_{j=0}^{\infty}\beta^j Z_j^2,
\qquad 0<\beta<1,
\]
where the \(Z_j\) are independent \(N(0,1)\) variables. The infinite series is almost surely finite and strictly positive. For every \(p>0\), its inverse moment \(M_p(\beta)=\mathbb E[V_\beta^{-p}]\) is finite. Its exact small-memory asymptotics are as follows.

If \(k\ge0\) is an integer and \(k/2<p<(k+1)/2\), set
\[
E_k(p)=kp-\frac{k(k+1)}4,\qquad
C_{k,p}=\frac{2^{-p}\Gamma(p-k/2)\Gamma((k+1)/2-p)}{\sqrt\pi\,\Gamma(p)}.
\]
Then
\[
\boxed{\lim_{\beta\downarrow0}\beta^{E_k(p)}M_p(\beta)=C_{k,p}.}
\]
At each critical half-integer \(p=k/2\), \(k\ge1\), the power law acquires precisely one logarithm:
\[
\boxed{\lim_{\beta\downarrow0}
\frac{\beta^{k(k-1)/4}M_{k/2}(\beta)}{\log(1/\beta)}
=\frac{2^{-k/2}}{\Gamma(k/2)}.}
\]
Both coefficients are positive and finite; thus all exponents and logarithmic factors are sharp. At \(\beta=0\), \(V_0=Z_0^2\), and \(\mathbb E[V_0^{-p}]<\infty\) holds exactly for \(0<p<1/2\).

There is a complementary *finite-startup barrier*. With zero accumulator initialization and bias correction, the \(n\)-sample denominator is
\[
V_{\beta,n}=\frac{1-\beta}{1-\beta^n}
\sum_{j=0}^{n-1}\beta^j Z_j^2.
\]
For any \(0<\beta<1\), any integer \(n\ge1\), and any \(p>0\),
\[
\boxed{\mathbb E[V_{\beta,n}^{-p}]<\infty\quad\Longleftrightarrow\quad n>2p.}
\]
Thus every fixed positive memory parameter yields inverse moments of all orders *in stationarity*, while a finite startup requires strictly more than \(2p\) independent observations. The stationary inverse moments nevertheless have an exact, increasingly singular dependence on the memory parameter as \(\beta\downarrow0\).

## Assumptions and scope

Every Gaussian variable in the statement is real, centered, has variance one, and is independent of the others. All arithmetic and probability identities are exact. The autoregressive accumulator is
\[
W_0=0,\qquad W_n=\beta W_{n-1}+(1-\beta)Z_n^2,
\]
with \(0<\beta<1\); its bias-corrected version is \(W_n/(1-\beta^n)\). The law of \(W_n\) is that of the stated \(n\)-term sum, and the invariant law of this Markov recursion is that of \(V_\beta\). The powers \(p\) in the theorem are all real \(p>0\), not only integer moments.

This is an autonomous noise-only model of the adaptive denominator, with independent Gaussian innovations. It does not identify the law of a gradient accumulator whose innovations depend on a simultaneously updated optimization variable, and it does not assert any convergence rate of that variable.

## Proof

**Existence, uniqueness, and finite-sample integrability.** Monotone convergence gives
\(\mathbb E\sum_{j\ge0}\beta^jZ_j^2=(1-\beta)^{-1}\), so the series converges almost surely. It is positive almost surely because \(Z_0\ne0\) almost surely. The recursion contracts the distance of any two accumulator trajectories driven by the same innovations by the exact factor \(\beta^n\); the above sum gives an invariant law, and this contraction gives uniqueness.

For any finite \(n\), the defining positive quadratic form is bounded above and below by positive multiples of \(\sum_{j<n}Z_j^2\). The Gaussian density on \(\mathbb R^n\) is bounded above globally and bounded below on a ball about zero. Polar integration therefore shows that its reciprocal \(p\)-moment is finite exactly when \(\int_0^1r^{n-1-2p}\,dr\) is finite, namely \(n>2p\). For any fixed \(p>0\), choose an integer \(n>2p\); the infinite sum dominates its first \(n\) terms, so its reciprocal moment is finite. At \(\beta=0\), the same one-dimensional test gives the stated boundary.

**Exact Laplace representation.** Let \(S_\beta=\sum_{j\ge0}\beta^jZ_j^2\). Independence, the Gaussian square transform, and the Euler--Gamma integral yield
\[
\begin{aligned}
\mathbb E[e^{-tS_\beta}]&=\prod_{j=0}^\infty(1+2t\beta^j)^{-1/2},\\
I_p(\beta):=\mathbb E[S_\beta^{-p}]&=\frac1{\Gamma(p)}
\int_0^\infty t^{p-1}\prod_{j=0}^\infty(1+2t\beta^j)^{-1/2}\,dt.
\end{aligned}
\]
Tonelli justifies the integral and product limits; preceding integrability gives their finiteness. Finally \(M_p(\beta)=(1-\beta)^{-p}I_p(\beta)\), and the prefactor tends to one.

**Noncritical \(p\).** Fix \(k/2<p<(k+1)/2\) and substitute \(t=\beta^{-k}u\). Multiplying by \(\beta^{E_k(p)}\) gives an integrand whose pointwise limit is
\[
\frac{2^{-k/2}}{\Gamma(p)}
\,u^{p-k/2-1}(1+2u)^{-1/2}.
\]
Indeed the factors with \(j<k\) contribute \((2u)^{-k/2}\beta^{k(k+1)/4}\), the factor at \(j=k\) remains \((1+2u)^{-1/2}\), and the factors with \(j>k\) tend jointly to one: their sum of logarithms is at most \(u\beta/(1-\beta)\). The same expression bounds the normalized integrand from above for every \(0<\beta<1\), since \(1+x\ge x\) for the first \(k\) factors and all later factors are at most one. It is integrable at zero exactly when \(p>k/2\), and at infinity exactly when \(p<(k+1)/2\). Dominated convergence applies, and \(v=2u\) gives
\[
\frac{2^{-k/2}}{\Gamma(p)}\int_0^\infty
u^{p-k/2-1}(1+2u)^{-1/2}\,du
=\frac{2^{-p}}{\Gamma(p)}B\left(p-\frac k2,\frac{k+1}2-p\right)=C_{k,p}.
\]
**Critical \(p\).** Let \(p=k/2\) with integer \(k\ge1\), set \(L=\log(1/\beta)\), and substitute \(t=e^{sL}\) into the Laplace integral. Dividing the normalized integral by \(L\) produces
\[
\frac1{\Gamma(k/2)}\int_{\mathbb R}F_{\beta,k}(s)\,ds,
\quad
F_{\beta,k}(s)=e^{(ks/2-k(k-1)/4)L}
\prod_{j=0}^\infty(1+2e^{(s-j)L})^{-1/2}.
\]
For every fixed \(s\) strictly between \(k-1\) and \(k\), exactly \(k\) factors are asymptotically large, and \(F_{\beta,k}(s)\to2^{-k/2}\). For every fixed \(s\) outside the closed interval, the normalized expression tends to zero, because its exponent is strictly below the plateau exponent.

This pointwise limit admits an explicit integrable majorant whenever \(L\ge1\). For \(s<k-1\), bounding the first \(k-1\) reciprocal square-root factors by their large-argument powers gives
\(F_{\beta,k}(s)\le2^{-(k-1)/2}e^{(s-k+1)/2}\). For \(k-1\le s\le k\), the first \(k\) factors give \(F_{\beta,k}(s)\le2^{-k/2}\). For \(s>k\), the first \(k+1\) factors give \(F_{\beta,k}(s)\le2^{-(k+1)/2}e^{-(s-k)/2}\). These three functions have an integrable union. Dominated convergence therefore gives the plateau integral \(2^{-k/2}\cdot(k-(k-1))\), proving the logarithmic coefficient. The boundary points have measure zero.

Together these arguments cover every \(p>0\) and every boundary, with no extrapolation from finitely many computations.

## Verification

The accompanying `verify.py` uses only the Python standard library. It reconstructs the Gaussian Laplace-transform functional equation, numerically integrates the positive Mellin integral on logarithmic coordinates, checks the predicted noncritical scaling at two small memory parameters, and checks the logarithmic coefficients at four critical orders through independent two-scale slopes. The finite-sample integrability cutoff is established analytically by polar integration. Execute `python3 verify.py` from the extracted package directory. Its numerical assertions test the formulas but do not prove the universal limits; those follow from the dominated-convergence arguments above.

## Relationship to prior work

Dereich and Jentzen, *Convergence rates for the RMSprop optimizer with full control of the hyperparameters* (arXiv:2608.30382v1, first posted 2026-08-31), formulate the bias-corrected geometric second-moment recursion in equations (3)--(4). Their Theorem 1.1 controls an optimization error under restrictions including \(\beta\ge1/2\); their Section 4 obtains conditional inverse-moment bounds after a startup threshold under a general Laplace nondegeneracy assumption. Those results do not state an exact stationary Gaussian inverse-moment asymptotic as \(\beta\downarrow0\), or the sequence of half-integer logarithmic transitions here.

Liu et al., *On the Variance of the Adaptive Learning Rate and Beyond* (arXiv:1908.03265), examine early-stage fluctuations and use a scaled inverse-chi-square approximation in Section 3.2. An approximation by an effective degree of freedom is not the law of the geometrically weighted infinite Gaussian sum and does not imply the stated sharp exponents and coefficients. Zhang, Zhou and Zou, *Convergence Guarantees for RMSProp and Adam in Generalized-smooth Non-convex Optimization with Affine Noise Variance* (arXiv:2404.01436), prove optimization complexity estimates under stochastic-gradient assumptions, not this exact Gaussian stationary denominator classification. General Gaussian quadratic-form and Laplace-transform identities are used as standard tools, not claimed as new.

## Limitations

The conclusions apply to independent real Gaussian innovations, a scalar squared-gradient accumulator, and exact arithmetic. Correlations, non-Gaussian small-ball exponents, positive denominator floors, parameter-dependent gradient distributions, and coupled optimizer trajectories can change the conclusions. The analysis identifies singular denominator moments; it does not claim that RMSprop itself diverges or that large inverse moments must cause poor optimization. The literature comparison cannot establish historical priority against every older treatment of geometrically weighted quadratic forms. No independent mathematical audit has been performed.

## References

1. S. Dereich and A. Jentzen, *Convergence rates for the RMSprop optimizer with full control of the hyperparameters*, arXiv:2608.30382v1 (2026), https://arxiv.org/abs/2608.30382.
2. L. Liu, H. Jiang, P. He, W. Chen, X. Liu, J. Gao, and J. Han, *On the Variance of the Adaptive Learning Rate and Beyond*, arXiv:1908.03265, ICLR 2020, https://arxiv.org/abs/1908.03265.
3. Q. Zhang, Y. Zhou, and S. Zou, *Convergence Guarantees for RMSProp and Adam in Generalized-smooth Non-convex Optimization with Affine Noise Variance*, arXiv:2404.01436, Transactions on Machine Learning Research (2025), https://arxiv.org/abs/2404.01436.
