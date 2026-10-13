# Unique optimal density and cube-root strong-recovery saturation in the tandem exclusion process

## Finding

For the two-stage tandem exclusion process of Ngo Phuoc Nguyen Ngoc, Lam Thi Nhung, and Huynh Anh Thi, the thermodynamic stationary current has **exactly one** globally maximizing density for every pair of positive transition rates. Its optimizer is the unique positive zero of an explicit sign-regular quintic. In the strong-recovery limit, the maximizer approaches full occupancy on a sharp cube-root scale, while the maximum current approaches the head-move rate on the *same* cube-root scale. A distinct order-\(q^{-1}\) inverse-recovery-rate boundary layer explains why the pointwise current limit is nonuniform near full occupancy.

Precisely, let \(\alpha>0\), \(\beta>0\), and \(q=\beta/\alpha\). For any \(q>0\), define
\[
\begin{aligned}
P_q(s)={}&q^2(q+1)s^5+4q^2s^4-2(q^2+1)s^3\\
&-2(q^2+4q+3)s^2-(5q+9)s-4.
\end{aligned}
\]
There is exactly one \(s_q>0\) with \(P_q(s_q)=0\). The unique optimal density and optimal current are
\[
\rho_*(q)=\frac{s_q(1+qs_q)}{1+2s_q+qs_q^2},\qquad
J_{\max}(q)=\alpha\frac{qs_q^2(s_q+2+qs_q)}{(1+s_q)(1+qs_q)(1+2s_q+qs_q^2)}.
\]
For every \(q>0\), the maximization is over the entire physical interval \(0\leq\rho\leq1\), with endpoint currents defined by continuity. In particular, \(\rho_*(1)=2/3\) and \(J_{\max}(1)=8\alpha/27\).

The two singular rate limits have exact constants:
\[
\begin{aligned}
\lim_{q\downarrow0}\rho_*(q)&=1/\sqrt2,&
\lim_{q\downarrow0}\frac{J_{\max}(q)}{\alpha}&=3-2\sqrt2,\\
\lim_{q\to\infty}q^{1/3}(1-\rho_*(q))&=2^{-2/3},&
\lim_{q\to\infty}q^{1/3}\left(1-\frac{J_{\max}(q)}{\alpha}\right)&=3\cdot2^{-2/3}.
\end{aligned}
\]
In addition, for every fixed \(\xi\geq0\), if \(\rho_q\in(0,1)\) and \(q(1-\rho_q)\to\xi\), then
\[
\lim_{q\to\infty}\frac{J(\rho_q;q)}{\alpha}
=\frac{\sqrt{1+4\xi}-1}{\sqrt{1+4\xi}+1}.
\]
The right side equals zero at \(\xi=0\). Thus the boundary-layer width is order \(q^{-1}\), different from the maximizing density's order \(q^{-1/3}\).

## Assumptions and scope

On a periodic one-dimensional lattice, the local moves are \(110\to101\) at rate \(\alpha\) and \(101\to011\) at rate \(\beta\). The claimed optimization concerns the stationary *thermodynamic-limit* current in the active sector at particle density \(\rho\in(0,1)\), using the exact flux derived in the cited 2026 paper. The first-public source date is 2026-06-01 (arXiv:2606.01568v1). All density limits are taken after the thermodynamic stationary-current formula has been established; no finite-ring mixing or interchange of thermodynamic and rate limits is asserted.

The starting published formula is
\[
\frac{J(\rho;q)}{\alpha}
=\frac{q\rho s(s+2+qs)}{(1+s)(1+qs)^2},\qquad
q(1-\rho)s^2+(1-2\rho)s-\rho=0,\quad s>0.
\]
The parameter \(\alpha\) fixes the current scale; the dimensionless optimization depends only on \(q\).

## Proof

**1. Positive parametrization.** Solving the quadratic relation for the density gives
\[
\rho=R_q(s)=\frac{s(1+qs)}{1+2s+qs^2},\qquad
\frac{dR_q}{ds}=\frac{1+2qs+qs^2}{(1+2s+qs^2)^2}>0.
\]
As \(s\) increases from zero to infinity, \(R_q(s)\) increases continuously from zero to one. Substitution in the published current yields
\[
j_q(s)=\frac{J(R_q(s);q)}{\alpha}
=\frac{qs^2(s+2+qs)}{(1+s)(1+qs)(1+2s+qs^2)}.
\]
This is positive for \(s>0\) and tends to zero at both ends. No branch of the original positive quadratic root is discarded.

**2. Exactly one maximum at every rate ratio.** Direct differentiation, without approximations, gives
\[
\frac{d j_q}{ds}=-\frac{qsP_q(s)}{(1+s)^2(1+qs)^2(1+2s+qs^2)^2}.
\]
For each fixed \(q>0\), the coefficient signs of \(P_q\), ordered from degree five down to its constant term, are \((+,+,-,-,-,-)\). Descartes' rule of signs therefore allows *at most* one positive zero, counting multiplicity. Because \(P_q(0)=-4<0\) and its leading coefficient is positive, a positive zero exists; it is unique. The derivative is positive before that zero and negative afterward. Together with the endpoint values and the monotonicity of \(R_q\), this proves the unique *global* density maximum. At \(q=1\), the factorization \(P_1(s)=2(s-2)(s+1)^4\) gives the stated benchmark.

**3. Slow-recovery endpoint.** Put \(q=t\) and \(s=u/t\) with \(u>0\). As \(t\downarrow0\),
\[
t^3P_t(u/t)\longrightarrow u^3(u^2-2).
\]
For any fixed \(0<u_-<\sqrt2<u_+\), the polynomial has opposite signs at \(u_-/t\) and \(u_+/t\) for all sufficiently small \(t>0\). By uniqueness, \(ts_t\to\sqrt2\). Direct substitution yields
\[
R_t(u/t)\to\frac{1+u}{2+u},\qquad
j_t(u/t)\to\frac{u}{(1+u)(2+u)}.
\]
At \(u=\sqrt2\), these simplify to \(1/\sqrt2\) and \(3-2\sqrt2\), respectively.

**4. Strong-recovery optimum.** Put \(t=q^{-1/3}\) and \(s=tu\). For every fixed \(u>0\),
\[
t^4P_{t^{-3}}(tu)\longrightarrow u^2(u^3-2).
\]
As in step 3, the unique zero is trapped between arbitrarily close positive brackets around \(2^{1/3}\), proving \(q^{1/3}s_q\to2^{1/3}\). Uniformly on any compact \(u\)-interval bounded away from zero,
\[
\frac{1-R_{t^{-3}}(tu)}{t}\to\frac1{u^2},\qquad
\frac{1-j_{t^{-3}}(tu)}{t}\to u+\frac1{u^2}.
\]
The convergence follows from rational expressions after clearing powers of \(t\), so it applies to \(u=s_q/t\), whose limit is strictly positive and finite. Substitution of \(u=2^{1/3}\) gives the two constants in the theorem. This is a global optimum, not merely a trial-density lower bound, by step 2.

**5. Separate full-occupancy boundary layer.** Let \(\rho_q\in(0,1)\) satisfy \(q(1-\rho_q)\to\xi\ge0\), and let \(s=s(\rho_q,q)\) be the positive quadratic root. For \(\xi>0\), the defining quadratic tends to \(\xi s^2-s-1=0\), whose positive root is \(s_\xi=(1+\sqrt{1+4\xi})/(2\xi)\). The flux tends to \(1/(1+s_\xi)\), giving the claimed formula. If \(\xi=0\), the exact parametrization gives \(q(1-\rho_q)=q(1+s)/(1+2s+qs^2)\to0\), together with \(\rho_q\to1\). Were \(s\) bounded along any subsequence, the first expression could not vanish; hence \(s\to\infty\). The exact expression for \(j_q(s)\) then tends to zero because \(q\to\infty\) and \(s\to\infty\). This proves the endpoint continuously and completes the proof.

## Verification

The standalone `verify.py` requires Python and SymPy (see `requirements.txt`). Run `python verify.py` in the same directory. It checks the elimination of density, the exact derivative identity, the explicit polynomial, its benchmark factorization, both singular root-scaling polynomials, the leading strong-recovery expansions, and the finite positive boundary-layer limit. It also performs numerical bisection and comparison checks over a range of rate ratios; expected terminal message: `VERIFY_OK`.

The symbolic checks substantiate the critical identities. The all-parameter Descartes argument and asymptotic root localization are analytical; finite numerical examples alone would not certify them.

## Relationship to prior work

Ngo Phuoc Nguyen Ngoc, Lam Thi Nhung, and Huynh Anh Thi (2026), *Tandem Exclusion Process*, established the model, the active-sector Gibbs measure, and the full stationary-current formula used here. In particular, their equations (10)–(12) supply the input function, their equation (13) gives the special \(q=1\) flux, and equation (14) gives the pointwise strong-recovery limit at each fixed \(\rho<1\). The present result is the **global** calculus and singular-optimization analysis of that already known function, not a new stationary-measure theorem. The prior pointwise limit alone does not provide the location, uniqueness, or sharp rate of approach of the global maximum, and it misses the separate full-occupancy boundary layer.

Gabel and Redner (2011) studied a different cooperative exclusion rule: a particle's hopping rate depends on occupancy immediately behind it. Their exact current and hydrodynamic shocks concern a different generator; they do not specify the two-stage \(110\to101\to011\) process or the above optimal-current quintic. General optimization and singular-perturbation principles are standard and are not themselves claimed as new.

## Limitations

This theorem is a mathematical consequence of a previously published *exact stationary-current formula*. It does not independently prove that formula, classify finite-ring invariant measures, prove spectral gaps, or analyze fluctuations. It addresses positive finite \(\alpha\) and \(\beta\) and limits through such values, not a claim that the zero-rate generators have the same stationary sector. The recovery boundary-layer limit is a thermodynamic stationary observable, not a simultaneous microscopic large-time limit. Equivalent analytical optimization in unindexed literature remains a priority risk.

## References

1. Ngo Phuoc Nguyen Ngoc, Lam Thi Nhung, and Huynh Anh Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1, first public posting 2026-06-01, https://arxiv.org/abs/2606.01568. Author-shared full-text rendition: https://www.researchgate.net/publication/405684325_Tandem_Exclusion_Process.
2. A. Gabel and S. Redner, *Cooperativity-driven singularities in asymmetric exclusion*, Journal of Statistical Mechanics (2011) P06008, doi:10.1088/1742-5468/2011/06/P06008, full text: https://sites.santafe.edu/~redner/pubs/pdf/cooperative.pdf.
