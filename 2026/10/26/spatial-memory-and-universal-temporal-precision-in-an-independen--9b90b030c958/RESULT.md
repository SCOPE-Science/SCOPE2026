# Quenched time-average noise and its exact phase spread in a reset Brownian gas

## Finding

Place independent Brownian particles at fixed reset anchors \(-x\) with positive distances \(x\in\mathcal A\), diffusivity \(D>0\) and individual Poisson reset rate \(r>0\). Initialize each displacement in its own stationary law. Let \(Q_t\) count the particles on the positive half-line, not their crossing events, and let \(\overline Q_T=T^{-1}\int_0^TQ_t\,dt\). Write \(\alpha=\sqrt{r/D}\) and assume \(m(\mathcal A)=\frac12\sum_{x\in\mathcal A}e^{-\alpha x}<\infty\). The exact configuration-dependent coefficient of the quenched variance is
\[
B(\mathcal A)=\lim_{T\to\infty}T\,\operatorname{Var}(\overline Q_T\mid\mathcal A)
=\frac1{4r}\sum_{x\in\mathcal A}\left[3e^{-\alpha x}-(\alpha x+2)e^{-2\alpha x}\right].
\]
The error in replacing \(\operatorname{Var}(\overline Q_T\mid\mathcal A)\) by \(B(\mathcal A)/T\) is nonnegative in the latter minus the former direction and is at most \(2m(\mathcal A)/(r^2T^2)\).

For a shifted lattice \(\mathcal A_u=\{(j+u)/\rho:j=0,1,\ldots\}\), \(0<u<1\), set \(\beta=\alpha/\rho\) and \(q=e^{-\beta}\). Its quenched coefficient is the strictly decreasing function
\[
B_\beta(u)=\frac1{4r}\left[\frac{3e^{-\beta u}}{1-q}
-e^{-2\beta u}\left(\frac{\beta u+2}{1-q^2}+\frac{\beta q^2}{(1-q^2)^2}\right)\right].
\]
Its phase spread is exactly \(B_\beta(0^+)-B_\beta(1^-)=1/(4r)\), independent of density and diffusivity. If the phase is uniform, the mean coefficient is \(7/(16r\beta)\), the same as for Poisson anchors at the same intensity. Thus even when the annealed temporal correction agrees, its fixed-configuration coefficients can vary with the lattice phase by a known, nonzero amount.

## Assumptions and scope

The anchor set is locally finite and deterministic for the quenched assertion. Displacements conditional on the anchors are independent stationary Markov processes with generator of free motion \(D\partial_y^2\) and resetting to zero in displacement coordinates. The anchors remain fixed throughout the observation; clocks are independent, not shared. Observables are time averages of occupation indicators. For an annealed comparison the anchor set is the negative half of a stationary simple process on the line, reflected to positive distances, and \(m(\mathcal A)\) must have finite second moment. Lattice endpoint phases in the spread are one-sided limits, not a convention about counting an anchor exactly on the boundary.

## Proof

**Local Green–Kubo kernel.** The stationary displacement law \(\pi\) has density \(\alpha e^{-\alpha|y|}/2\), obtained by observing Brownian motion at independent age exponential of rate \(r\). Set \(f_x(y)=\mathbf1_{\{y>x\}}\) and \(p_x=\pi(f_x)=e^{-\alpha x}/2\). Let \(P_s^0\) be the free Brownian semigroup. Conditioning on whether a reset occurs between zero and \(s\) gives the stationary covariance
\[
c_x(s)=e^{-rs}\operatorname{Cov}_\pi(f_x(Y),P_s^0f_x(Y)),\qquad Y\sim\pi;
\]
on the event of a reset, the conditional expectation of the final indicator is independent of \(Y\). Both functions in the remaining covariance are increasing, so \(0\le c_x(s)\le p_x e^{-rs}\).

The operator \(r\int_0^\infty e^{-rs}P_s^0\,ds\) adds an independent Laplace displacement of rate \(\alpha\). Applied to \(f_x\), it gives the function \(H_x(y)=\frac12e^{-\alpha(x-y)}\) for \(y\le x\), and \(H_x(y)=1-\frac12e^{-\alpha(y-x)}\) for \(y>x\). Integration against \(\pi\) on \((x,\infty)\) gives \(\mathbb E[f_x(Y)H_x(Y)]=3e^{-\alpha x}/8\). On the three regions \((-\infty,0)\), \((0,x)\) and \((x,\infty)\), respectively, the contributions to \(\mathbb E H_x(Y)\) are \(e^{-\alpha x}/8\), \(\alpha x e^{-\alpha x}/4\) and \(3e^{-\alpha x}/8\). Thus
\[
2\int_0^\infty c_x(s)\,ds
=\frac{2}{r}\left[\frac{3e^{-\alpha x}}8-p_x\frac{(\alpha x+2)e^{-\alpha x}}4\right]
=\frac{3e^{-\alpha x}-(\alpha x+2)e^{-2\alpha x}}{4r}.
\]

**Conditional variance and remainder.** Conditional on \(\mathcal A\), the counts are square integrable because the second moment is at most \(m^2+m\), and their lag covariance is \(C_{\mathcal A}(s)=\sum_x c_x(s)\). Truncation to finite subsets followed by convergence in conditional \(L^2\) gives this identity for the full count. The covariance bound gives \(0\le C_{\mathcal A}(s)\le m e^{-rs}\). Conditional stationarity and integration on the observation square give
\[
\operatorname{Var}(\overline Q_T\mid\mathcal A)=\frac2T\int_0^\infty(1-s/T)_+ C_{\mathcal A}(s)\,ds.
\]
The coefficient \(B=2\int_0^\infty C_{\mathcal A}(s)\,ds\) follows by substitution and summation. Since \(0\le1-(1-s/T)_+\le s/T\), the difference from \(B/T\) is bounded by \(2mT^{-2}\int_0^\infty s e^{-rs}ds=2m/(r^2T^2)\).

**Phase profile.** Substitute \(\alpha x=\beta(j+u)\) into the sum for \(B\). The geometric sums with ratios \(q,q^2\) and the first geometric moment with ratio \(q^2\) give the displayed \(B_\beta(u)\). With \(v=\alpha x\), the derivative of the summand before multiplication by \(1/(4r)\) is
\[
\frac{d}{dv}\left[3e^{-v}-(v+2)e^{-2v}\right]=e^{-2v}(2v+3-3e^v)<0\quad(v>0).
\]
Each term decreases strictly with phase; convergence is uniform for \(u\in[0,1]\), so the limits exist. The endpoint configurations differ by precisely the limiting \(j=0\) summand with \(v=0\); the remaining terms cancel after shifting the index. Consequently the spread is \((3-2)/(4r)\). Uniform phase yields the mean by combining the adjacent unit intervals in the sum, or by Campbell's identity at intensity \(\rho\):
\[
\mathbb E B_\beta(U)=\frac1{4r\beta}\int_0^\infty[3e^{-v}-(v+2)e^{-2v}]\,dv=\frac{7}{16r\beta}.
\]

## Annealed comparison

For any stationary anchor ensemble in the stated scope, the law of total variance adds \(\operatorname{Var}(m(\mathcal A))\) to the average conditional variance. Campbell's first-moment identity gives \(\mathbb E B=7\rho/(16r\alpha)\), independently of correlations, and the averaged error bound is \(\rho/(\alpha r^2T^2)\). This universal annealed coefficient is included for context, not as a distinct contribution over the fixed-rate spatially integrated covariance calculation in [1]. The spatial plateau for Poisson anchors is \(\rho/(8\alpha)\) by the Poisson integral variance. For the shifted lattice, \(m(U)=e^{-\beta U}/[2(1-e^{-\beta})]\), giving the plateau \(\coth(\beta/2)/(8\beta)-1/(4\beta^2)\) by integration in the uniform phase. It tends to \(1/48\) as \(\beta\downarrow0\). The quenched coefficient and phase spread describe fluctuations conditional on geometry, not this static plateau.

## Relationship to prior work and limitations

[1] *Rate-disorder transition in stationary Brownian reset current fluctuations*, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-rate-disorder-transition-in-stationary-brownian-reset-current-fl--211aa471cfd1/RESULT.md, Proof §§1–4. Its two-time covariance representation contains the same single-anchor integrand. It evaluates the spatially integrated kernel, then integrates in time for the integrable disorder regime. The fixed-rate spatial mean coefficient agrees algebraically. This provides no phase-resolved formula from the spatial average alone; the local Laplace evaluation above supplies that information.

[2] C. Di Bello et al., *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696. The defined half-line count agrees with their one-time current observable for a step initial condition; the present calculation concerns time-average variance at stationary displacement.

[3] F. den Hollander et al., *Large deviations for occupation and waiting times of Brownian motion with resetting*, arXiv:1801.09909. The general renewal transform applies broadly to additive functionals; their explicitly treated positive occupation time has the threshold at the reset point. The phase profile uses nonzero thresholds determining the individual anchor contributions.

The formulas are restricted to independent resetting and stationary initial displacements. The uniform-phase mean does not describe every fixed phase. No interchange of a dense-anchor limit and the time-average asymptotic is asserted. The exact local and lattice results are analytic; finite checks only corroborate the algebra.
