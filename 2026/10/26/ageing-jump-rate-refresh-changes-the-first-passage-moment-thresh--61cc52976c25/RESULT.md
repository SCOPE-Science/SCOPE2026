# Ageing jump-rate refresh changes the first-passage moment threshold, with a logarithmic boundary

## Finding

For a simple symmetric continuous-time random walk on the positive integers with an absorbing origin, independently redrawing a heavy-tailed jump rate after *ageing*, deterministic refresh intervals produces a different first-passage exponent from the fixed-refresh model. Let the length of refresh interval \(j\) be
\[
\ell_j=\tau j^\beta[\log(ej)]^\delta,
\qquad \tau>0,\quad\beta\ge0,\quad\delta\in\mathbb R,
\]
and take an independent rate \(\lambda_j>0\) on each interval with
\[
\mathbb E[e^{-s\lambda_j}]=\frac1{1+s^\alpha},\qquad s\ge0,\quad0<\alpha\le1.
\]
Starting from any fixed positive integer \(x\), write \(T\) for the first time the position reaches zero. Define
\[
\gamma=\frac{1+\alpha\beta}{2\alpha(1+\beta)},\qquad
\eta=\delta\left(\gamma-\frac12\right).
\]
Then
\[
\boxed{\Pr(T>t)\sim C\,t^{-\gamma}(\log t)^\eta}
\]
where the *explicit* positive constant is
\[
C=\frac{x\sqrt2\,\Gamma(1/(2\alpha))}{\alpha\pi}\;
\tau^{\gamma-1/2}(1+\alpha\beta)^{1/(2\alpha)}
(1+\beta)^{-\gamma-\eta}.
\]
For every \(q>0\),
\[
\boxed{\mathbb E[T^q]<\infty
\iff(q<\gamma)\ \text{or}\ (q=\gamma\ \text{and}\ \eta<-1).}
\]
In particular, the mean is finite precisely when \(\alpha<1/(\beta+2)\), or at equality when \(\delta<-2\). For fixed refresh intervals (\(\beta=\delta=0\)), the critical exponent reduces to \(\alpha=1/2\), but polynomially ageing intervals move it to \(\alpha=1/(\beta+2)\); at the critical power, the logarithmic refresh correction resolves a second threshold.

## Assumptions and scope

The random walk starts at the deterministic integer \(x\ge1\). Conditional on the complete rate path, the jumps occur according to an inhomogeneous Poisson process of instantaneous rate \(\lambda_j\) on interval \([t_{j-1},t_j)\), with \(t_0=0\) and \(t_j=\sum_{i=1}^j\ell_i\); each jump has an independent fair sign. The walk is killed on first reaching zero. Rates are independent across intervals and independent of jump directions. The rate distribution is the positive Mittag–Leffler-rate law specified *by its Laplace transform*, which is sufficient for the theorem. For \(\alpha=1\) it is exponential with mean one; for \(\alpha<1\) it has infinite mean. Each rate is finite and positive almost surely, and \(t_j\to\infty\) for all stated parameters.

The result concerns a time-inhomogeneous refresh schedule, not an iid sequence of interarrival waiting times, and does not assert the same exponent for arbitrary dependent rates or arbitrary stochastic refresh times. The source model with fixed refresh duration is the subfamily \(\beta=\delta=0\).

## Proof

**1. Operational-time reduction.** Put \(\Lambda_t=\int_0^t\lambda(s)\,ds\). Conditioned on rates, the counting process of jumps is Poisson with cumulative intensity \(\Lambda_t\), independent of jump signs. Thus the survival probability has the exact representation
\[
\Pr(T>t)=\mathbb E[f_x(\Lambda_t)],
\]
where \(f_x(u)\) is the survival probability up to operational time \(u\) for the unit-rate, continuous-time simple symmetric random walk on the positive integers, absorbing at zero.

The method of images applied to its heat kernel gives, for every \(u\ge0\),
\[
f_x(u)=e^{-u}\sum_{k=1-x}^{x} I_{|k|}(u),
\]
where \(I_k\) is the modified Bessel function of the first kind. To verify the identity, subtract the free-lattice heat kernels \(e^{-u}I_{y-x}(u)-e^{-u}I_{y+x}(u)\) at each \(y\ge1\) and sum; the series telescopes to the indicated \(2x\) terms. The standard fixed-order Bessel asymptotic yields
\[
f_x(u)\sim x\sqrt{\frac{2}{\pi}}\,u^{-1/2},\qquad u\to\infty.
\]
Also, since \(I_{|k|}(u)\le I_0(u)\), there is \(A_x<\infty\) with
\[
0\le f_x(u)\le A_x(1+u)^{-1/2}\quad\text{for every }u\ge0.
\]

**2. Stable operational-clock limit.** Given \(t\in[t_n,t_{n+1})\), put \(r_t=t-t_n\), and define
\[
B_t=\sum_{j=1}^{n}\ell_j^\alpha+r_t^\alpha,\qquad b_t=B_t^{1/\alpha}.
\]
Independence and the rate Laplace transform give the exact identity
\[
\mathbb E[e^{-s\Lambda_t/b_t}]
=\left[\prod_{j=1}^{n}\left(1+s^\alpha\frac{\ell_j^\alpha}{B_t}\right)^{-1}\right]
\left(1+s^\alpha\frac{r_t^\alpha}{B_t}\right)^{-1}.
\]
Write the normalized nonnegative weights as \(w_{j,t}\), including the partial interval. Their sum is one. The polynomial–logarithmic schedule implies
\[
\max_j w_{j,t}\longrightarrow0.
\]
Indeed, for the last half of the completed intervals \(\ell_j\) is comparable to \(\tau n^\beta(\log n)^\delta\), whereas \(B_t\asymp\tau^\alpha n^{1+\alpha\beta}(\log n)^{\alpha\delta}\). The earlier intervals cannot exceed the resulting sum by a positive fraction. Since \(\sum_jw_{j,t}^2\le\max_jw_{j,t}\), taking logarithms in the preceding transform shows
\[
\mathbb E[e^{-s\Lambda_t/b_t}]\longrightarrow e^{-s^\alpha}\quad(s\ge0).
\]
Consequently \(\Lambda_t/b_t\Rightarrow Z_\alpha\), where \(Z_\alpha\) is the positive \(\alpha\)-stable variable characterized by \(\mathbb E[e^{-sZ_\alpha}]=e^{-s^\alpha}\). At \(\alpha=1\), this variable equals one almost surely.

**3. Negative-moment uniform integrability.** Weak convergence alone is insufficient to pass the unbounded function \(v^{-1/2}\) through expectation. Fix any \(q>1/2\). For all large \(n\), at least \(n/2\) completed intervals satisfy
\[
\frac{\ell_j^\alpha}{B_t}\ge\frac{c}{n}
\]
with a constant \(c>0\) independent of \(t\). Therefore, writing \(V_t=\Lambda_t/b_t\),
\[
\mathbb E[e^{-sV_t}]\le(1+cs^\alpha/n)^{-n/2}.
\]
The Mellin identity for negative moments and the beta integral yield, for sufficiently large \(n\),
\[
\begin{aligned}
\mathbb E[V_t^{-q}]
&=\frac1{\Gamma(q)}\int_0^\infty s^{q-1}\mathbb E[e^{-sV_t}]\,ds\\
&\le\frac{(n/c)^{q/\alpha}}{\alpha\Gamma(q)}
\mathrm B\left(\frac q\alpha,\frac n2-\frac q\alpha\right)=O(1).
\end{aligned}
\]
The last bound follows from the gamma ratio as \(n\to\infty\). This proves uniform integrability of \(V_t^{-1/2}\) and handles the small-operational-time contribution. In particular, the Bessel bound from Step 1 and convergence in distribution imply
\[
\sqrt{b_t}\,\Pr(T>t)
\longrightarrow x\sqrt{\frac2\pi}\,\mathbb E[Z_\alpha^{-1/2}].
\]
Using the Mellin–Laplace formula again,
\[
\mathbb E[Z_\alpha^{-1/2}]
=\frac{\Gamma(1/(2\alpha))}{\alpha\Gamma(1/2)}
=\frac{\Gamma(1/(2\alpha))}{\alpha\sqrt\pi}.
\]
Thus
\[
\Pr(T>t)\sim\frac{x\sqrt2\,\Gamma(1/(2\alpha))}{\alpha\pi}\,B_t^{-1/(2\alpha)}.
\]
This is a proven positive constant, not a Monte Carlo extrapolation.

**4. Clock conversion and logarithmic boundary.** Standard sum–integral comparison for \(\beta\ge0\) and arbitrary real \(\delta\) gives
\[
t_n\sim\frac{\tau}{1+\beta}n^{1+\beta}(\log n)^\delta,
\qquad
B_{t_n}\sim\frac{\tau^\alpha}{1+\alpha\beta}
 n^{1+\alpha\beta}(\log n)^{\alpha\delta}.
\]
The incomplete current interval contributes only a vanishing relative fraction to both asymptotics, uniformly between adjacent refresh times. Since \(\log n\sim(\log t)/(1+\beta)\), the operational-clock result becomes
\[
\Pr(T>t)\sim
\frac{x\sqrt2\,\Gamma(1/(2\alpha))}{\alpha\pi}
\tau^{\gamma-1/2}(1+\alpha\beta)^{1/(2\alpha)}
(1+\beta)^{-\gamma-\eta}
 t^{-\gamma}(\log t)^\eta,
\]
with \(\gamma\) and \(\eta\) as claimed.

Finally, the tail integration identity \(\mathbb E[T^q]=q\int_0^\infty t^{q-1}\Pr(T>t)\,dt\) for \(q>0\) gives the moment criterion by the integral test for powers and logarithms. When \(q=1\), solving \(\gamma>1\) yields \(\alpha<1/(\beta+2)\); at equality \(\gamma=1\) and \(\eta=\delta/2\), so integrability holds exactly for \(\delta<-2\). This proves both the power-law and logarithmic boundaries.

## Verification

The included standalone `verify_ageing_rates.py` performs five exact rational-parameter phase checks, including the two sides of the logarithmic mean boundary, and four finite-stage integrations of the exact nonnegative spectral survival representation at starting site one. The numerical integrations use only Python's standard library and composite Simpson quadrature; they compare the finite-stage answer with the independently derived stable normalization, with deviations under \(1\%\) in the chosen examples. The executed output was:

```text
alpha=2/5 beta=0 delta=0 n=200 survival=0.0013658415675 normalization=565685.425 ratio_to_stable_limit=1.00707451
alpha=2/5 beta=1 delta=0 n=200 survival=0.000146563378025 normalization=49187498.1 ratio_to_stable_limit=1.00768923
alpha=1/3 beta=1 delta=-3 n=300 survival=0.00028786689189 normalization=17506095.7 ratio_to_stable_limit=1.00636390
alpha=1/3 beta=1 delta=-2 n=300 survival=0.000120071351244 normalization=100640214 ratio_to_stable_limit=1.00645382
CHECK_OK exact_parameter_cases=5 spectral_quadratures=4
```

The spectral formula checked numerically for \(x=1\) is
\[
\Pr(T>t_n)=\frac1\pi\int_0^\pi(1+\cos\theta)
\left[\prod_{j=1}^{n}\frac{1}{1+[\ell_j(1-\cos\theta)]^\alpha}\right]d\theta,
\]
Numerics are sanity checks of the displayed formulas and play no role in the infinite-time proof.

## Relationship to prior work

Levit and Reuveni (arXiv:2609.26925, first posted September 22, 2026) establish the fixed-refresh Mittag–Leffler-rate first-passage tail \(t^{-1/(2\alpha)}\) and its finite-mean transition at \(\alpha=1/2\). Their supplementary derivation and Appendix A use a *constant* relaxation time, and the discussion of general jump-rate dynamics expresses survival through the Laplace transform of its integrated rate. The present result uses that general operational-time framework but changes the driving model: deterministic polynomial–logarithmic intervals have no uniformly bounded relaxation time. Weighted triangular-array stable convergence, control of negative moments, and clock inversion give a new exponent, sharp moment boundary, and logarithmic endpoint rule, none of which is stated by the fixed-refresh analysis.

Arutkin and Reuveni (arXiv:2302.07041, first posted February 14, 2023) establish the broader doubly stochastic continuous-time random-walk framework and its operational-time representation. Their worked resampling example again uses constant-length intervals, and the first-exit calculation is for a finite interval. Their general transform identity supplies a starting point but does not provide this nonstationary half-line asymptotic or its critical logarithmic moment test.

## Limitations

The assumptions include iid rates with exactly the Laplace transform \((1+s^\alpha)^{-1}\), fair nearest-neighbour steps, and deterministic power–logarithmic interval lengths. No claim is made for correlated rate redraws, arbitrary renewal schedules, or random-walk jump distributions lacking the simple half-line Bessel survival asymptotic. The result is derived in a literature with general subordination and regular-variation machinery; an equivalent theorem formulated in that broader language remains a priority risk despite the focused source comparisons. Independent external validation has not been performed.

## References

- Bara Levit and Shlomi Reuveni, “First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean,” arXiv:2609.26925 (first posted 2026-09-22). https://arxiv.org/abs/2609.26925
- Maxence Arutkin and Shlomi Reuveni, “Doubly stochastic continuous time random walk,” arXiv:2302.07041 (first posted 2023-02-14); *Physical Review Research* 6, L012033 (2024). https://arxiv.org/abs/2302.07041
- NIST Digital Library of Mathematical Functions, modified Bessel-function fixed-order large-argument asymptotics, §10.40. https://dlmf.nist.gov/10.40
