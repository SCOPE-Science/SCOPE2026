# Inward-pointing propulsion in a three-dimensional trapped run-and-tumble particle

## Finding

For the stationary athermal three-dimensional run-and-tumble oscillator with isotropically renewed propulsion direction, the **joint** position–heading law has an exact last-run disintegration, and the probability that propulsion points *toward* the trap center has two sharp, nonzero asymptotic coefficients. With normalized position \(X\), current unit heading \(N\), and dimensionless tumble rate \(\alpha>0\), put

\[
Q(\alpha)=\mathbb P(X\cdot N<0).
\]

Let \(p_\alpha\) be the stationary density of one normalized position coordinate (the even density described in the references). Then, for every \(\alpha>0\),

\[
\boxed{Q(\alpha)=\int_0^1p_\alpha(u)\bigl[1-(1+u)^{-\alpha}\bigr]\,du,\quad 0<Q(\alpha)<\tfrac12.}
\]

The two asymptotic laws are

\[
\boxed{\lim_{\alpha\downarrow0}\frac{Q(\alpha)}{\alpha}=\log2-\frac12,\qquad
\lim_{\alpha\to\infty}\sqrt\alpha\bigl(\tfrac12-Q(\alpha)\bigr)=\sqrt{\frac3{2\pi}}.}
\]

At \(\alpha=1\), the exact one-dimensional integral in the first display evaluates numerically to \(Q(1)=0.115696771276\ldots\). This is a numerical evaluation of an exact integral, not a claimed elementary constant.

## Assumptions and scope

Take \(\mu,v_0,\gamma>0\). In \(\mathbb R^3\), the motion is \(\dot{\mathbf r}=-\mu\mathbf r+v_0N_t\). The unit heading \(N_t\in S^2\) is held fixed between events of a rate-\(\gamma\) Poisson process and replaced at each event by an independent Haar-uniform direction. Tumbling is instantaneous; there is no translational Brownian forcing. Set \(X=\mu\mathbf r/v_0\) and \(\alpha=\gamma/\mu\). The unique stationary solution has \(\lvert X\rvert<1\) almost surely. The event \(X\cdot N<0\) describes inward **active propulsion**, not necessarily inward total velocity (which also contains the trap drift).

Write \(h_\alpha(\lvert x\rvert)\) for the stationary density of the full position vector with respect to three-dimensional volume, and \(\sigma\) for normalized surface measure on \(S^2\). The exact conditional position density given a fixed current heading \(n\) is, for almost every \(x\),

\[
\boxed{g_\alpha(x\mid n)=\alpha\int_0^1 a^{\alpha-4}
 h_\alpha\!\left(\left\lvert\frac{x-(1-a)n}{a}\right\rvert\right)
\mathbf1_{\{\lvert x-(1-a)n\rvert<a\}}\,da.}
\]

Consequently the joint law is \(g_\alpha(x\mid n)\,d^3x\,\sigma(dn)\). The marginal density \(h_\alpha\) and its coordinate projection \(p_\alpha\) are established in the published literature; this statement does not claim them as new.

## Proof

**Step 1: exact current-heading disintegration.** In the stationary two-sided Poisson process, the time \(B\) since the last heading renewal is exponential with rate \(\gamma\), independent of the current heading \(N\) and the position \(Y_\alpha\) immediately preceding that renewal. By stationarity and the independence of renewals, \(Y_\alpha\) has the unconditional stationary position law and is independent of \((B,N)\). Linear trap evolution during the last run gives

\[
X=(1-A)N+AY_\alpha,\qquad A=e^{-\mu B}\sim\operatorname{Beta}(\alpha,1),
\]

with the three quantities independent. Conditional scaling of \(Y_\alpha\) proves the displayed formula for \(g_\alpha\), including its Jacobian \(a^{-3}\).

**Step 2: the inward probability.** Since \(Y_\alpha\) is isotropic, the projection \(U=N\cdot Y_\alpha\) is independent of \(N\), has even density \(p_\alpha\) on \((-1,1)\), and is independent of \(A\). The sign event is

\[
(1-A)+AU<0\ \Longleftrightarrow\ U<0\ \text{and}\ A>\frac1{1-U}.
\]

Thus, conditional on \(U=-u\) with \(0<u<1\), its probability is \(1-(1+u)^{-\alpha}\). Integrating establishes the exact expression and strict bounds because \(p_\alpha\) gives positive mass to every interior subinterval.

**Step 3: rare tumbling.** The known stationary stick-breaking identity may also be read directly from Step 1 after projection:

\[
U_\alpha\ \overset d=\ (1-A)V+AU_\alpha',
\]

where \(V\) is uniform on \([-1,1]\) and independent of \(A,U_\alpha'\). As \(\alpha\downarrow0\), \(A\to0\) in probability, so \(U_\alpha\Rightarrow V\). Uniformly for \(0\le u\le1\),

\[
0\le\frac{1-(1+u)^{-\alpha}}{\alpha}\le\log(1+u),
\]

and the middle expression converges uniformly to \(\log(1+u)\) as \(\alpha\downarrow0\). Weak convergence therefore yields

\[
\lim_{\alpha\downarrow0}\frac{Q(\alpha)}\alpha
=\frac12\int_0^1\log(1+u)\,du=\log2-\frac12.
\]

**Step 4: a local limit theorem for the fast-tumbling regime.** The established Dirichlet-process representation of the projected stationary position permits the following self-contained local argument. Let \(G_\alpha\) be a gamma random measure on \([-1,1]\), with intensity \((\alpha/2)\,du\) with unit scale. Put \(T=\int dG_\alpha\), \(S=\int u\,dG_\alpha\). Then \(T\sim\mathrm{Gamma}(\alpha,1)\), the normalized gamma measure is independent of \(T\), and \(U_\alpha\overset d=S/T\). The characteristic function of \(Z_\alpha=(S/\sqrt\alpha,(T-\alpha)/\sqrt\alpha)\) equals

\[
\mathbb E e^{i(tZ_{\alpha,1}+sZ_{\alpha,2})}
=e^{-is\sqrt\alpha}\exp\!\left\{-\frac\alpha2\int_{-1}^1\log\left(1-\frac{i(s+tu)}{\sqrt\alpha}\right)du\right\}.
\]

It tends to \(\exp(-t^2/6-s^2/2)\). This convergence holds in integrable Fourier norm for sufficiently large \(\alpha\). Indeed set \(R^2=t^2+s^2\) and average over uniform \(u\in[-1,1]\). Then \(\mathbb E_u(s+tu)^2=s^2+t^2/3\ge R^2/3\), while \(\sup_u(s+tu)^2\le2R^2\). Thus on at least a fraction \(1/11\) of the \(u\)-interval, \((s+tu)^2\ge R^2/6\). Taking the real part of the logarithm bounds the absolute characteristic function by

\[
\bigl(1+R^2/(6\alpha)\bigr)^{-\alpha/22}.
\]

For all \(\alpha\ge100\), this is dominated by the integrable two-dimensional majorant \((1+R^2/600)^{-100/22}\), since \(\alpha\log(1+c/\alpha)\) increases in \(\alpha\). Fourier inversion and dominated convergence therefore give uniform convergence of the joint densities of \(Z_\alpha\) to the product normal density with variances \(1/3\) and \(1\).

Conditioning on \(T=\alpha\) and using independence of \(U_\alpha=S/T\) and \(T\) shows that the density \(f_\alpha\) of \(\sqrt\alpha U_\alpha\) satisfies

\[
f_\alpha(w)=\frac{f_{Z_\alpha}(w,0)}{f_{(T-\alpha)/\sqrt\alpha}(0)}
\longrightarrow\sqrt{\frac3{2\pi}}e^{-3w^2/2}
\]

locally uniformly in \(w\), since the gamma denominator tends to \(1/\sqrt{2\pi}\). In particular \(p_\alpha(w/\sqrt\alpha)/\sqrt\alpha\to\sqrt{3/(2\pi)}e^{-3w^2/2}\) locally uniformly.

**Step 5: extracting the boundary-layer constant.** Evenness gives

\[
\tfrac12-Q(\alpha)=\int_0^1p_\alpha(u)(1+u)^{-\alpha}\,du.
\]

Fix \(\delta>0\). On \(0\le u\le\delta/\sqrt\alpha\), set \(z=\alpha u\). Local uniform convergence gives a bound \(p_\alpha(z/\alpha)/\sqrt\alpha\le C_\delta\), while the remaining factor is at most \(e^{-z/2}\) for all sufficiently large \(\alpha\). Dominated convergence shows that the corresponding contribution after multiplying by \(\sqrt\alpha\) tends to \(\sqrt{3/(2\pi)}\). On \(u\ge\delta/\sqrt\alpha\), the remaining contribution, after the same multiplication, is at most \(\sqrt\alpha\exp(-c\delta\sqrt\alpha)/2\) for a fixed \(c>0\), and tends to zero. This proves the second sharp limit.

**Step 6: the explicit unit-rate example.** From the known Dirichlet-mean density at \(\alpha=1\) with uniform projected heading,

\[
p_1(u)=\frac e\pi\cos\frac{\pi u}2\,
\exp\!\left[-\frac{(1+u)\log(1+u)+(1-u)\log(1-u)}2\right],\quad |u|<1.
\]

Thus \(Q(1)=\int_0^1p_1(u)u/(1+u)\,du\), which has the stated numerical value.

## Verification

`verify.py` contains a standalone standard-library numerical diagnostic. It checks the exact \(\alpha=1\) density normalization, its variance \(1/6\), the inward probability quadrature, and direct independent simulations of the last-run construction at three rates against its conditional-probability identity and known stationary coordinate variance \(1/[3(1+\alpha)]\). The reproducible finite checks passed. The infinite-parameter and asymptotic claims depend on Steps 1–5, not on simulation or numerical integration.

## Relationship to prior work

Frydel (2023) derives moments and position marginals of the three-dimensional trapped run-and-tumble oscillator. Guéneau, Majumdar and Schehr (2026) obtain the exact all-coordinate **position** density and the Dirichlet-process representation; their discussion identifies joint position–active-velocity statistics as a further calculation (Section III.3). These foundational results are used explicitly. Sun, Ye and Podgornik (2024 preprint, 2025 journal) instead analyze a model with nonzero tumble residence time; their all-dimensional moment methodology does not establish this instantaneous-tumble heading-sign law. Sun, Ye and Chen (2026) treat a one-dimensional orientation-conditioned joint law, not the three-dimensional isotropic one. The additional mathematical contribution here is the inward-heading observable, its all-rate exact integral and its sharp slow/fast coefficients—not a new derivation of the previously published position distribution.

## Limitations

The result does not prove monotonicity of \(Q(\alpha)\), finite-sample inference accuracy, or extensions to non-Poisson renewals, non-isotropic headings, thermal translational diffusion, interactions, or inertia. It does not claim a new general Dirichlet-process identity. The publication-priority comparison is based on the identifiable literature examined; an independently located equivalent observation would supersede the novelty assessment. Numerical diagnostics are not substitutes for the analytic proof.

## References

- Derek Frydel, *Run-and-tumble oscillator: moment analysis of stationary distributions*, arXiv:2309.12537 (first public version 2023-09-21), https://arxiv.org/abs/2309.12537.
- Mathis Guéneau, Satya N. Majumdar, Grégory Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (2026), https://arxiv.org/abs/2602.08436.
- Aoran Sun, Fangfu Ye, Rudolf Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (first public version 2024-09-01), https://arxiv.org/abs/2409.00578.
- Aoran Sun, Fangfu Ye, Jeff Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961 (2026), https://arxiv.org/abs/2610.24961.
- Cifarelli and Regazzini, *Distribution functions of means of a Dirichlet process*, Annals of Statistics 18 (1990), 429–442, as cited for the established Dirichlet-mean representation in arXiv:2602.08436.
