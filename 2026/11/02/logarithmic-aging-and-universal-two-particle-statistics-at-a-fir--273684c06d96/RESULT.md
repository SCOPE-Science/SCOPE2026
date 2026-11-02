# Logarithmic aging and universal two-particle statistics at a first-passage resetting threshold

## Finding

Consider two independent one-dimensional Brownian particles whose positions are simultaneously returned to the origin whenever either reaches the positive threshold \(L\). This process has no stationary position law [1], but it has the following sharp nonstationary limit theorem. Put \(t_0=L^2/D\), let \(A_t\) be the time since the most recent collective reset, and set \(Z_i(t)=L-X_i(t)>0\) for \(i=1,2\). Define
\[
U_t=\frac{\log(1+A_t/t_0)}{\log(1+t/t_0)}.
\]
Then as \(t\to\infty\),
\[
\left(U_t,\frac{Z_1(t)}{\sqrt{4DA_t}},\frac{Z_2(t)}{\sqrt{4DA_t}}\right)
\Longrightarrow (U,Y_1,Y_2),
\]
where \(U\) is uniform on \([0,1]\), \(Y_1,Y_2\) are independent random variables with density \(2y e^{-y^2}\) for \(y>0\), and all three variables on the right are independent. The logarithmic age limit is an instance of Erickson's established renewal theorem [2]; the joint conditioned-position conclusion is the model-specific result.

In particular, the two logarithmic distance exponents converge together:
\[
\left(
\frac{\log(1+Z_1(t)/L)}{\log(1+t/t_0)},
\frac{\log(1+Z_2(t)/L)}{\log(1+t/t_0)}
\right)\Longrightarrow (U/2,U/2).
\]
The scale-free distance ratio converges to a law independent of \(D,L\):
\[
\frac{Z_1(t)}{Z_2(t)}\Longrightarrow R,\qquad
\mathbb P(R\le r)=\frac{r^2}{1+r^2},\quad
f_R(r)=\frac{2r}{(1+r^2)^2},\quad r>0.
\]
The limiting ratio \(R\) is independent of \(U\).

There is also a complete positive joint-moment asymptotic. For **each fixed** \(a,b\ge0\) with \(a+b>0\),
\[
\mathbb E[Z_1(t)^a Z_2(t)^b]
\sim
\frac{2(4Dt)^{(a+b)/2}\Gamma(1+a/2)\Gamma(1+b/2)}{(a+b)\log(t/t_0)}.
\]
In consequence, the ordinary Pearson correlation of the two physical distances has a strictly subunit universal limit:
\[
\boxed{\lim_{t\to\infty}\operatorname{Corr}(Z_1(t),Z_2(t))=\pi/4.}
\]
Thus the logarithmic exponents synchronize exactly in the limit, although the normalized physical distances retain independent Rayleigh fluctuations conditional on age.

## Assumptions and scope

Fix arbitrary \(D,L>0\). Two particles begin at \(X_1(0)=X_2(0)=0\) and evolve independently as \(dX_i(t)=\sqrt{2D}\,dB_i(t)\) between resets, with \(B_1,B_2\) independent Brownian motions. Upon the **first** arrival of either coordinate at \(L\), both positions reset instantaneously to zero, and independent Brownian increments are used in subsequent excursions. Resetting is instantaneous and has no additional delay, drift, interactions, or external reset clock. The joint process is observed at deterministic \(t>0\). The logarithms are dimensionless through \(t_0=L^2/D\) and \(L\). At deterministic observation times, equality \(X_i(t)=L\) has zero probability. The age-scaled expressions are well-defined almost surely for \(t>0\).

## Proof

**1. Exact excursion survival and marginal renewal.** For a single Brownian motion killed upon reaching \(L\), the reflection principle gives the killed transition density, for \(x<L\) and \(s>0\),
\[
G(x,s)=\frac{e^{-x^2/(4Ds)}-e^{-(2L-x)^2/(4Ds)}}{\sqrt{4\pi Ds}}.
\]
Its total surviving mass is \(S_1(s)=\operatorname{erf}(L/\sqrt{4Ds})\). The duration \(T\) of a two-particle excursion is the minimum of two independent single-particle first-passage times; hence
\[
S(s):=\mathbb P(T>s)=S_1(s)^2
=\operatorname{erf}\!\left(\frac{L}{\sqrt{4Ds}}\right)^2
\sim\frac{c}{s},\qquad c=\frac{L^2}{\pi D}.
\]
The interarrival distribution has a smooth, strictly positive, nonarithmetic density and infinite mean. Its truncated mean \(m(s)=\int_0^s S(u)\,du\) satisfies \(m(s)\sim c\log(s/t_0)\). By Theorem 6 of Erickson [2], the renewal age satisfies \(m(A_t)/m(t)\Longrightarrow U\), with \(U\sim\mathrm{Unif}[0,1]\). Since \(m(s)\) grows logarithmically and \(A_t\to\infty\) in probability, this implies \(U_t\Longrightarrow U\). This age theorem is used here as prior work, not asserted to be new.

**2. Conditional law at a fixed age.** Let \(u(ds)=\sum_{n\ge0}\mathbb P(T_1+\cdots+T_n\in ds)\) denote the renewal measure, including its atom at zero. For any bounded measurable observable \(H\) of the current age and positions, the renewal decomposition is
\[
\mathbb EH(A_t,X_1(t),X_2(t))
=\int_{[0,t]}u(dv)\int_{x_1,x_2<L}
G(x_1,t-v)G(x_2,t-v)H(t-v,x_1,x_2)\,dx_1dx_2.
\]
In particular, conditional on \(A_t=s\), the current coordinates are independent with individual density \(G(x,s)/S_1(s)\); the possible atom at \(A_t=t\) obeys the same conditional law.

Write \(Y_i^{(s)}=(L-X_i)/\sqrt{4Ds}\) and \(\epsilon=L/\sqrt{4Ds}\). The **exact** conditional density of each \(Y_i^{(s)}\), on \(y>0\), is
\[
q_{\epsilon}(y)=
\frac{e^{-(y-\epsilon)^2}-e^{-(y+\epsilon)^2}}
{\sqrt\pi\,\operatorname{erf}(\epsilon)}.
\]
As \(s\to\infty\) (thus \(\epsilon\downarrow0\)), this converges in \(L^1(0,\infty)\) to \(q_0(y)=2ye^{-y^2}\). Pointwise convergence follows by the first-order odd difference; convergence in total variation follows from the normalization of the nonnegative densities and Scheffé's lemma. Since \(A_t\to\infty\) in probability, the conditional product law of \((Y_1^{(A_t)},Y_2^{(A_t)})\) converges in total variation to \(q_0\otimes q_0\) independently of any bounded function of \(A_t\). Combined with the age limit, this gives the stated three-coordinate joint limit, including independence.

**3. Ratio and logarithmic exponents.** For independent \(Y_1,Y_2\) with density \(q_0\), the density of \(R=Y_1/Y_2\) is
\[
\int_0^\infty yq_0(ry)q_0(y)\,dy
=4r\int_0^\infty y^3e^{-(1+r^2)y^2}\,dy
=\frac{2r}{(1+r^2)^2}.
\]
Integration gives the stated distribution function. The continuous mapping theorem and positivity of \(Y_2\) give the ratio limit. The fixed threshold and Rayleigh fluctuation yield
\[
\log(1+Z_i/L)=\tfrac12\log(1+A_t/t_0)+O_{\mathbb P}(1)
\]
by tightness of the conditional Rayleigh factors and their reciprocals, together with \(A_t\to\infty\) in probability. Dividing by \(\log(1+t/t_0)\) gives both exponents \(U/2\).

**4. Positive moments and correlation.** For each fixed \(p\ge0\), the conditional density above and Gaussian domination imply
\[
\mathbb E[Z_i^p\mid A_t=s]
=(4Ds)^{p/2}\bigl[\Gamma(1+p/2)+o(1)\bigr],\qquad s\to\infty,
\]
with the convention \(\Gamma(1)=1\); the error is uniform on \(s\ge s_0\) as \(s_0\to\infty\). Since the conditional coordinates are independent, their joint conditional moment is the product. The exact renewal-age identity is
\[
\mathbb E[A_t^v]=\int_{[0,t]}(t-w)^vS(t-w)\,u(dw).
\]
For every fixed \(v>0\), the index-one infinite-mean strong renewal theorem [2, Theorem 1] gives
\[
\boxed{\mathbb E[A_t^v]\sim\frac{t^v}{v\log(t/t_0)}.}
\]
For clarity, one can prove this implication without assuming a density for \(u\). On ages \(s\le(1-\delta)t\), divide time into fixed-length renewal bins: uniformly for renewal epochs \(w\in[\delta t,t]\), \(u([w,w+h])\sim h/(c\log(t/t_0))\); Riemann upper and lower sums and \(S(s)\sim c/s\) give \((1-\delta)^vt^v/(v\log t)\) to leading order. The remaining ages \(s>(1-\delta)t\) contribute at most \(t^vS((1-\delta)t)u([0,\delta t])\). Erickson's renewal-function asymptotic \(u([0,x])\sim x/(c\log x)\) bounds that remainder by \((\delta/(1-\delta)+o(1))t^v/\log t\); now send \(\delta\downarrow0\). Small ages contribute only lower order for \(v>0\). Combining the conditional moments with \(v=(a+b)/2>0\) proves the joint-moment formula.

In particular, \(\mathbb E Z_i^2\sim4Dt/\log(t/t_0)\), \(\mathbb E[Z_1Z_2]\sim\pi Dt/\log(t/t_0)\), whereas \((\mathbb E Z_i)^2=O(t/\log^2t)\). Centering therefore does not alter the leading second moments, giving the Pearson limit \(\pi/4\).

## Verification

The accompanying standard-library script `verify.py` checks, by independent finite numerical quadrature and exact identities: the Brownian hitting-time tail and its density derivative, normalization and Rayleigh limit of the conditioned position kernel, Rayleigh moments, the ratio law and its cumulative distribution, the moment-coefficient correlation identity, and logarithmic truncated-mean growth. Execute `python verify.py` from the extracted folder. These finite checks are consistency tests; the infinite-time laws and universal quantifiers follow from the proof and the explicitly cited renewal theorems, not from these computations.

## Relationship to prior work

Biroli, Majumdar and Schehr [1] derive the exact killed propagator and renewal representation for the first-passage resetting gas and prove that a stationary joint distribution exists only for more than two particles. Their paper does not derive the two-particle nonstationary logarithmic-position joint law, the universal distance-ratio distribution or the Pearson limit above. The logarithmically normalized *renewal age alone* is already the content of Erickson's 1970 Theorem 6 [2], which this work explicitly uses and credits. De Mauro, Biroli, Majumdar and Schehr [3] derive stationary correlations for exogenously sampled resetting intervals of finite mean; their Pareto discussion restricts the tail exponent to the finite-mean regime, so it does not establish the joint critical two-particle theorem for first-hit-triggered resetting. The novelty asserted here is limited to the **combined spatial aging, universal ratio, and moment/correlation laws in the specifically first-passage-coupled critical system**, not to the renewal-age theorem or the killed Brownian kernel.

## Limitations

The theorem treats exactly two particles in one dimension, independent zero-drift Brownian motion between excursions, a common upper absorbing threshold, and instantaneous all-particle resetting. The position limit is nonstationary; it is not a stationary joint density. The Pearson limit \(\pi/4\) is strictly below perfect linear correlation even though the logarithmic exponents agree asymptotically. Positive-moment asymptotics are asserted for fixed nonnegative exponents with positive total exponent, not for negative moments or growing exponents. The uniform limit of the age is an established renewal theorem, not a new claim. The result does not cover unequal diffusivities, imperfect thresholds, stochastic resetting delays, higher dimensions, or arbitrary heavy-tailed renewal laws. No independent scientific validation or exhaustive literature-priority certification has been performed.

## References

[1] M. Biroli, S. N. Majumdar, and G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440 (first arXiv timestamp 2025-11-29), especially the model, reflection kernel and renewal equations (1)–(12). https://arxiv.org/pdf/2512.00440

[2] K. B. Erickson, *Strong renewal theorems with infinite mean*, Transactions of the American Mathematical Society **151** (1970), 263–291; Theorems 1, 5 and 6. https://doi.org/10.1090/S0002-9947-1970-0268976-9

[3] G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, published Phys. Rev. E **113** (2026), 014120. https://arxiv.org/pdf/2509.06658
