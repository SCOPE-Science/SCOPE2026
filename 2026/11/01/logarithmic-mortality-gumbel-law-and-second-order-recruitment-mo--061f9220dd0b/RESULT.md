# Logarithmic-mortality Gumbel law and second-order recruitment–mortality design

## Finding

For a family of independent, independently dying Brownian-equivalent searchers with Poisson recruitment, write \(\rho=\lambda/\mu\) for the recruitment-to-mortality ratio, \(d>0\) for the transformed-coordinate distance to the absorbing target, \(D>0\) for the transformed diffusivity, and \(t_0=d^2/D\). Fix any \(x>0\), set \(L=\log\rho\), and tune mortality and recruitment according to
\[
\mu t_0=xL,\qquad \lambda=\rho\mu.
\]
Let \(\tau_{\rho,x}\) be the first arrival of any searcher at the target, starting with one searcher at time zero. Define
\[
C_L(x)=L-\frac32\log L+\log\frac{x}{4\sqrt\pi}-\frac{x}{4}.
\]
Then, as \(\rho\to\infty\), the transformed arrival time satisfies
\[
\frac{t_0}{4\tau_{\rho,x}}-C_L(x)\ \Longrightarrow\ G,
\qquad \mathbb P(G\le z)=\exp(-e^{-z}),
\]
with convergence of every positive integer moment of the transformed variable. Moreover,
\[
\frac{\mathbb E\tau_{\rho,x}}{t_0}=
\frac{1}{4L}+
\frac{\frac32\log L-\log\frac{x}{4\sqrt\pi}+\frac{x}{4}-\gamma}{4L^2}
+o(L^{-2}),
\]
where \(\gamma\) is Euler's constant. These claims and remainders are uniform for \(x\) in any fixed compact subset of \((0,\infty)\). For any two fixed \(x,x_0>0\),
\[
\lim_{\rho\to\infty}\frac{4L^2}{t_0}
\bigl(\mathbb E\tau_{\rho,x}-\mathbb E\tau_{\rho,x_0}\bigr)
=\frac{x-x_0}{4}-\log\frac{x}{x_0}.
\]
Consequently, **among fixed positive coefficients of the logarithmic mortality scaling**, the unique asymptotic second-order minimizer is \(x=4\); the limiting mean excess relative to it is
\[
\lim_{\rho\to\infty}\frac{4L^2}{t_0}
\bigl(\mathbb E\tau_{\rho,x}-\mathbb E\tau_{\rho,4}\bigr)
=\frac{x}{4}-1-\log\frac{x}{4}\ge0,
\]
with equality exactly at \(x=4\). The result **does not** assert that the global finite-\(\rho\) optimizer exists uniquely or that its ratio to \(\log\rho\) tends to four.

## Assumptions and scope

The free motion is \(Y_t=Y_0+\sqrt{2D}\,B_t\) on the real line, with an absorbing target a distance \(d>0\) from \(Y_0\). Equivalently, this applies to the transformed-coordinate realization of one-dimensional Stratonovich heterogeneous diffusion with \(\mathcal D(X)=D_\alpha|X|^\alpha\), \(\alpha<2\), initial position \(0<X_0<X_{\mathrm{target}}\), and
\[
y(X)=\frac{2}{2-\alpha}\operatorname{sgn}(X)|X|^{(2-\alpha)/2},\quad
 d=y(X_{\mathrm{target}})-y(X_0),\quad D=D_\alpha.
\]
The transformed-coordinate realization is assumed at any singular interface; no uniqueness claim for alternative boundary realizations at the origin is made. Each searcher has an independent exponential lifetime with rate \(\mu\), independent of its Brownian path. At time zero there is one searcher; thereafter independent searchers start from \(Y_0\) according to a rate-\(\lambda\) Poisson process. The first successful target arrival defines \(\tau_{\rho,x}\). Rates are constant within each member of the asymptotic family. The ratio \(\rho\) and therefore \(\lambda\) vary as specified; this is not fixed-\(\lambda\) optimization.

## Proof

**1. Exact survival identity (prior formula).** In units of \(t_0\), the free single-searcher hitting-time density is
\[
f(s)=\frac{e^{-1/(4s)}}{2\sqrt\pi\,s^{3/2}},\qquad s>0.
\]
Put \(m=\mu t_0=xL\), \(F_m(s)=\int_0^s e^{-mu}f(u)\,du\), and
\(J_m(s)=\int_0^s(s-u)e^{-mu}f(u)\,du=\int_0^s F_m(u)\,du\). The independence and Poisson probability-generating functional give the already established identity
\[
\mathbb P(\tau_{\rho,x}>t_0s)
=(1-F_m(s))\exp[-\rho mJ_m(s)]. \tag{1}
\]
Since \(J_m'=F_m\) and \(J_m(s)\to\infty\) as \(s\to\infty\), integration by parts also gives the exact mean identity
\[
\frac{\mathbb E\tau_{\rho,x}}{t_0}
=\int_0^\infty e^{-\rho mJ_m(s)}\,ds-\frac1{\rho m}. \tag{2}
\]
Neither (1) nor (2) is asserted to be new.

**2. A moving-endpoint estimate.** Set \(w=1/(4s)\), and substitute \(u=1/[4(w+v)]\) into the two integrals. Direct Jacobian calculation yields the exact formulas
\[
F_m(s)=\frac{e^{-w}}{\sqrt\pi}
\int_0^\infty \frac{e^{-v-m/[4(w+v)]}}{\sqrt{w+v}}\,dv,\tag{3}
\]
\[
J_m(s)=\frac{e^{-w}}{4\sqrt\pi\,w}
\int_0^\infty \frac{v e^{-v-m/[4(w+v)]}}{(w+v)^{3/2}}\,dv.\tag{4}
\]
For \(w=L+O(\log L)\) and \(m=xL\), with \(x\) in a compact positive interval, dominated expansion in \(v\) against \(e^{-v}(1+v)\) implies, uniformly,
\[
F_m(s)=\frac{e^{-w-m/(4w)}}{\sqrt{\pi w}}\left(1+O(L^{-1})\right),\qquad
J_m(s)=\frac{e^{-w-m/(4w)}}{4\sqrt\pi\,w^{5/2}}\left(1+O(L^{-1})\right).\tag{5}
\]
For example, on \(v\le\sqrt L\) the Taylor remainder of the exponent is bounded by a constant times \((v+v^2)/L\); on \(v>\sqrt L\), the integrands are bounded by the exponentially integrable weight \(e^{-v}\) times a polynomial. These bounds justify the stated relative error.

**3. Gumbel limit.** Substitute \(w=C_L(x)+z\), where \(z\) is fixed, into (5). The centering has been chosen so that
\[
\rho mJ_m\bigl(1/[4(C_L(x)+z)]\bigr)\longrightarrow e^{-z},
\quad F_m\bigl(1/[4(C_L(x)+z)]\bigr)\longrightarrow0.\tag{6}
\]
The event \(t_0/(4\tau_{\rho,x})-C_L(x)\le z\) is exactly \(\tau_{\rho,x}\ge t_0/[4(C_L(x)+z)]\), up to zero-probability equality. Equation (1) and (6) prove the asserted Gumbel CDF.

**4. Tail controls and moments.** Write \(G_L=t_0/(4\tau_{\rho,x})-C_L(x)\). For \(u\ge0\), equations (3)–(4), \(1-e^{-v}\le v\), and \(w=C_L+u\) yield \(\mathbb P(G_L>u)\le K e^{-u}\) for all sufficiently large \(L\), uniformly on compact positive \(x\)-intervals. For \(0\le u\le C_L-L/2\), restrict the integral (4) to \(1\le v\le2\) with \(w=C_L-u\ge L/2\); the integrand is uniformly bounded below after extracting its exponential factors. It follows that \(\mathbb P(G_L<-u)\le\exp[-k e^u]\). For the remaining negative tail, at \(s_*=1/(2L)\), equation (4) gives \(\rho mJ_m(s_*)\ge\exp(cL)\) for some \(c>0\). Hence \(\mathbb P(\tau_{\rho,x}>t_0s_*)\le\exp[-\exp(cL)]\). For \(s\ge s_*\), \(J_m(s)\ge J_m(s_*)+(s-s_*)F_m(s_*)\), so
\[
\int_{s_*}^\infty\mathbb P(\tau_{\rho,x}>t_0s)\,ds
\le\frac{\exp[-\rho mJ_m(s_*)]}{\rho mF_m(s_*)},\tag{7}
\]
which is super-exponentially small in \(L\). These bounds give uniform integrability of all fixed positive integer powers of \(G_L\) and, in particular, \(\mathbb E G_L\to\gamma\). They also permit expanding the mean on \(s<s_*\), where \(C_L+G_L\ge L/2\). Taylor expansion of \(1/(C_L+G_L)\), moment bounds, and (7) give
\[
\frac{\mathbb E\tau_{\rho,x}}{t_0}
=\frac1{4C_L(x)}-\frac{\gamma+o(1)}{4C_L(x)^2}+O(L^{-3}).\tag{8}
\]
Expanding \(C_L(x)\) proves the mean formula. All estimates are locally uniform in \(x>0\).

**5. Second-order design.** Subtract the two mean expansions at fixed \(x,x_0>0\); all common \(L^{-1}\), \(\log L/L^2\), and Euler-constant terms cancel, leaving the displayed difference. The derivative of \(x/4-\log x\) is \(1/4-1/x\), its second derivative is \(1/x^2>0\), and it has its unique minimum at \(x=4\). This proves precisely the restricted asymptotic design statement.

## Verification

The accompanying `verify.py` evaluates (3)–(4), checks them against direct time-domain integration, checks the survival identity against an independent complementary-error-function expression for \(F_m\), checks the expected movement of the centered Gumbel CDF as \(L\) grows, and evaluates finite-\(L\) mean arrival times and the relative excess. It tests selected parameter instances only; steps 1–5 above establish the asymptotic claims. Run `python verify.py` with Python, NumPy and SciPy. The reported check count is printed by the script when it passes.

## Relationship to prior work

Gutiérrez et al. [1], Sec. 4 and Appendix B, give the heterogeneous-diffusion transform, the exact recruitment-and-mortality survival formula, and numerical mean-time optimization at fixed recruitment-to-mortality ratio. Linn and Kumar [2] derive the wider dynamic-redundancy-and-mortality framework and study fixed-ratio high- and low-turnover regimes. Mercado-Vásquez and Boyer [3] derive the corresponding synthesis–degradation first-passage formulas, including the same exact mean identity and an optimal long-time exponential decay scale. Tung and Lawley [4] rigorously study the Gumbel regime for *fast immigration with a fixed single-particle hitting-time law*. Grebenkov, Metzler and Oshanin [5] study finite-population, time-distributed entry. The present result instead takes a *joint* limit in which the mortality-dependent single-searcher law changes with the growing recruitment ratio, identifies its moving centering including the mortality penalty, and establishes the second-order optimization in a specified logarithmic-rate class. Prior general formulas are foundational, not claimed as new; the joint scaling theorem is the evaluated addition.

## Limitations

The optimizer \(x=4\) applies only to the class \(\mu t_0=x\log(\lambda/\mu)\) with a fixed positive coefficient. No global finite-ratio optimizer, uniformity as \(x\to0\) or \(x\to\infty\), or finite-ratio threshold is proved. This is an asymptotic theorem and its \(o(L^{-2})\) remainder is not a numerical error guarantee at moderate ratios. The model assumes independent Poisson recruitment, independent exponential removal, and Brownian-equivalent unbounded motion with one target; interactions, finite populations, spatially varying mortality, and alternative diffusion interface realizations are not covered. The publication-priority assessment is best-knowledge and should not be mistaken for independent verification.

## References

1. E. D. Gutiérrez, A. López, R. K. Singh, S. Fumeron, M. Henkel and T. Sandev, *Heterogeneous diffusion with recruitment and mortality*, arXiv:2610.08022, first submitted 2026-10-06, https://arxiv.org/abs/2610.08022 .
2. S. Linn and A. Kumar, *Dynamic redundancy and mortality in stochastic search*, arXiv:2601.07096, 2026, https://arxiv.org/abs/2601.07096 .
3. I. Mercado-Vásquez and D. Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting*, arXiv:2602.11095, 2026, https://arxiv.org/abs/2602.11095 .
4. H.-R. Tung and S. D. Lawley, *First passage times with fast immigration*, arXiv:2502.10915, 2025, https://arxiv.org/abs/2502.10915 .
5. D. S. Grebenkov et al., *Fastest first-passage time statistics for time-dependent particle injection*, arXiv:2503.19105, 2025, https://arxiv.org/abs/2503.19105 .
