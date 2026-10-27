# A universal two-age caustic in the far tails of shear-driven resetting diffusion

## Finding

In planar shear diffusion with Poisson resetting of both coordinates, parabolically distant stationary displacements have two competing optimal elapsed times since the last reset. Their dominance exchanges at one explicit, nonanalytic critical spatial ray. At the critical ray, the posterior reset age has a nondegenerate two-atom limit, with universal weights. The leading rare-event law is unaffected by any fixed longitudinal translational diffusivity.

For fixed \(\delta\geq0\), take independent standard Brownian motions and the process between common resets to the origin at rate one,
\[
dY_t=\sqrt2\,dB_t^{(2)},\qquad dX_t=Y_t\,dt+\sqrt{2\delta}\,dB_t^{(1)}.
\]
Let \(p_\delta\) be its unique stationary joint density. For each fixed \(c>0\), define \(F_c(s)=s+s^{-1}-3cs^{-2}+3c^2s^{-3}\), \(J(c)=\min_{s>0}F_c(s)\), and \(M(c)=\{s>0:F_c(s)=J(c)\}\). As \(L\to\infty\),
\[
p_\delta(cL^2,L)\sim\sqrt{\frac{3}{2\pi}}L^{-3/2}e^{-LJ(c)}\sum_{s\in M(c)}\frac{1}{s^2\sqrt{F_c''(s)}}.
\]
All global minimizers are nondegenerate. There is exactly one critical ray parameter \(c_*=\sqrt3/24\). For \(0<c<c_*\), the sole minimizer is the old-age branch \(s_o(c)=(1+\sqrt{1-12c})/2\); for \(c>c_*\), it is the young-age branch \(s_y(c)=(\sqrt{1+12c}-1)/2\). At equality both minimize, with \(u=(\sqrt3-1)/4\), \(v=(\sqrt3+1)/4\), and \(J(c_*)=\sqrt3\). The rate has a genuine downward corner:
\[
J'_-(c_*)=-12+4\sqrt3,\qquad J'_+(c_*)=-12-4\sqrt3.
\]
Conditioning on the exact stationary position \((X,Y)=(c_*L^2,L)\) in the regular density sense, the elapsed reset age \(T\) obeys
\[
\frac{T}{L}\Longrightarrow \frac{\sqrt{2+\sqrt3}}{1+\sqrt{2+\sqrt3}}\,\delta_u+\frac1{1+\sqrt{2+\sqrt3}}\,\delta_v.
\]
For any fixed \(c\ne c_*\), the posterior converges instead to the single point mass at the unique minimizing age. The asymptotic formulas and age weights do not depend on \(\delta\).

## Assumptions and scope

The planar diffusion starts from the origin after every reset. Both coordinates reset simultaneously at the jump times of an independent rate-one Poisson process, and each Brownian motion is independent of that clock and of the other Brownian motion. The parameter \(\delta\) is finite and fixed as \(L\to\infty\); \(c>0\) is fixed, not varied with \(L\). The displayed density and conditioning are for the stationary distribution and its regular conditional reset age. The case \(\delta=0\) is included: the joint Gaussian free propagator is nondegenerate at every positive age because transverse Brownian motion is integrated by the shear.

The model with physical parameters \(dY=\sqrt{2D}\,dB^{(2)}\), \(dX=\gamma Y\,dt+\sqrt{2D}\,dB^{(1)}\), reset rate \(r\), \(D,r>0\), and \(\gamma\ne0\), maps to the stated normalization by time \(rt\), transverse position \(Y\sqrt{r/D}\), and longitudinal position \(Xr^{3/2}/(\gamma\sqrt D)\). Thus \(\delta=(r/\gamma)^2\), and the critical scaled parabola corresponds for positive transverse displacement to \(X=(\gamma\sqrt3/(24\sqrt{rD}))Y^2\). This is an *asymptotic ray* statement, not a claim about a finite-position singularity of the smooth density.

## Proof

**Renewal representation.** At stationarity the time \(T\) since the last simultaneous reset is exponential with rate one. Conditional on \(T=t>0\), the free particle is a centered Gaussian with covariance (ordered as \((X,Y)\))
\[
\Sigma_{t,\delta}=\begin{pmatrix}2\delta t+\frac23t^3&t^2\\t^2&2t\end{pmatrix},\quad \det\Sigma_{t,\delta}=4\delta t^2+\frac13t^4>0.
\]
The exact density is \(p_\delta(x,y)=\int_0^\infty e^{-t}(2\pi\sqrt{\det\Sigma_{t,\delta}})^{-1}\exp[-\tfrac12(x,y)\Sigma_{t,\delta}^{-1}(x,y)^{\mathsf T}]\,dt\). This representation also defines the regular posterior density of the reset age by dividing its integrand by \(p_\delta(x,y)\).

**Uniform Laplace reduction.** Substituting \(t=Ls\), \((x,y)=(cL^2,L)\), direct matrix inversion gives, on every compact subinterval of \(s\in(0,\infty)\),
\[
t+\frac12(x,y)\Sigma_{t,\delta}^{-1}(x,y)^{\mathsf T}
=LF_c(s)+O(L^{-1}),\qquad
\frac{L}{2\pi\sqrt{\det\Sigma_{Ls,\delta}}}=\frac{\sqrt3}{2\pi Ls^2}(1+O(L^{-2})).
\]
The error bounds hold uniformly with derivatives in the compact interval for each fixed \(c,\delta\). To localize globally, note that every Gaussian joint exponent is at least its \(Y\)-marginal exponent \(L^2/(4t)\); also \((\det\Sigma_{t,\delta})^{-1/2}\leq\sqrt3/t^2\). The integral on \(0<t\leq\epsilon L\) is therefore at most a constant times \(L^{-2}e^{-L/(4\epsilon)}\), and the integral on \(t\geq RL\) is bounded by a constant times \(L^{-1}e^{-RL}\). Taking \(\epsilon\) sufficiently small and \(R\) sufficiently large compared with the finite minimum \(J(c)\) leaves exactly the interior global minima. The ordinary one-dimensional Laplace theorem now yields the prefactor and the exponential rate. Applying the same argument to bounded continuous tests of \(T/L\) proves posterior concentration and, at a tie, the stated prefactor-derived mixture weights.

**All stationary-age extrema.** A direct derivative factorization gives
\[
F_c'(s)=1-\frac{(s-3c)^2}{s^4}.
\]
The young local minimum is \(s_y(c)=(\sqrt{1+12c}-1)/2\). For \(0<c<1/12\), the old local minimum and intervening local maximum are respectively \(s_o(c)=(1+\sqrt{1-12c})/2\) and \((1-\sqrt{1-12c})/2\). For \(c\geq1/12\), there is no competing old local minimum. Each global minimum has \(F_c''>0\), including at the eventual crossing.

**Uniqueness and exact location of the crossover.** Write \(u=s_y(c)\), \(v=s_o(c)\). Their stationarity equations give \(3c=u+u^2=v-v^2\); their values are \(F_c(u)=(4u-1+u^{-1})/3\) and \(F_c(v)=(4v+1+v^{-1})/3\). Setting both values equal produces \((v-u)(1/(uv)-4)=2\). Combining with \(v-u=u^2+v^2\), and using \(v>u>0\), forces \(v-u=1/2\) and \(u+v=\sqrt3/2\). Consequently \(u=(\sqrt3-1)/4\), \(v=(\sqrt3+1)/4\), and \(c=\sqrt3/24\), the only possible crossing. As \(c\downarrow0\) the young-branch cost diverges while the old cost tends to two; near \(c=1/12\) the young branch is globally lower, giving the claimed ordering on each side. The envelope theorem gives the two one-sided derivatives at the crossing.

**Exact posterior weights.** At the crossing,
\[
F_{c_*}''(u)=\frac{2(1+2u)}{u^2},\qquad
F_{c_*}''(v)=\frac{2(2v-1)}{v^2}.
\]
The saddle weights are proportional to \(s^{-2}/\sqrt{F_{c_*}''(s)}\); hence their young-to-old ratio equals \(\sqrt{2+\sqrt3}\), giving the asserted two-point law. Fixed longitudinal diffusivity affects neither leading saddle weights nor the rate because its covariance contribution is lower order on the scale \(t\asymp L\).

**Independent path-action interpretation.** Without longitudinal thermal diffusion, the transverse Brownian path that ends at \(Y(s)=1\) and produces integrated displacement \(\int_0^sY(t)dt=c\) minimizes \(\tfrac14\int_0^s\dot Y(t)^2dt\) and is quadratic. Its minimum action is \(s^{-1}-3cs^{-2}+3c^2s^{-3}\); adding the resetting-age cost \(s\) reproduces \(F_c\). Thus the two minimizers represent genuinely different typical elapsed reset ages and optimal sheared trajectories.

## Verification

Run `python checks/checker.py` with Python 3, NumPy, SymPy, and SciPy. The included checker verifies symbolic factorization, roots, exact critical costs and jump slopes, stationary covariance and determinant, the independently derived constrained path action, branch inequalities on a finite numerical grid, and exact-density quadratures for several scale and thermal-diffusivity values. On successful execution it ends with `EXACT_ALL_TESTS_PASSED`. The mathematical proof above, not the finite grid or quadrature, establishes the global uniqueness, asymptotic limits, and posterior mixture.

## Relationship to prior work

Abdoli, Olsen, and Löwen [1] introduced the shear-Brownian Poisson-reset model studied here and gave the exact free Gaussian propagator, reset-age stationary mixture, moments, and spatial distributions. Those source results underlie the first step of our proof; none of the inspected sections or appendices gives the two-minimum far-tail stationary variational law, its exact \(\sqrt3/24\) caustic, or the critical posterior two-age weights. General restarting and renewal results [2,3] justify regenerative mixtures, but do not directly supply the saddle competition or threshold. Related large-deviation literature [4] treats Markov-path or time-integrated observables rather than this explicit stationary space-conditioned reset-age law. These comparisons do not prove worldwide priority, and other asymptotic-geometry treatments could overlap.

## Limitations

The result concerns only \(L\to\infty\) at a fixed ray parameter \(c>0\) and fixed finite \(\delta\geq0\). The one-sided corner refers to the limiting spatial rate \(J\), not a finite-position singularity or thermodynamic transition. No uniform critical-window expansion for \(c-c_*\) shrinking with \(L\), physical finite-sample inference, nonlinear shear, finite-time start, or simultaneous high-diffusivity limit is proved. Uninspected equivalent stationary large-deviation formulations remain a literature priority risk.

## References

[1] I. Abdoli, K. Stølevik Olsen, and H. Löwen, *Shear-Driven Diffusion with Stochastic Resetting*, arXiv:2410.10333v1 (public 2024-10-14), https://arxiv.org/html/2410.10333v1 . The full HTML body and displayed appendices were inspected.

[2] M. R. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A 53 (2020), arXiv:1910.07993, https://arxiv.org/abs/1910.07993 .

[3] S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18 (2016), https://doi.org/10.1088/1367-2630/18/3/033006 .

[4] C. Monthus, *Large deviations for Markov processes with stochastic resetting*, arXiv:2009.12287, https://arxiv.org/abs/2009.12287 .
