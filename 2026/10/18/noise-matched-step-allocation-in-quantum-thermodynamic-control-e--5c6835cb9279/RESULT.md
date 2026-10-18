# Noise-matched step allocation in quantum thermodynamic control: exact joint optimum and integer-step limit

## Finding

For an oriented scalar control interval \([a,b]\), the leading quadratic dissipation functional for a noisy, step-equilibrated protocol need not be minimized by constant thermodynamic-metric speed. When the noise-increment variance at control value \(u\) is \(\phi(u)>0\), the **joint** optimum over the positive real step count and the time parameterization is instead characterized by the local matching law
\[
\dot x(t)=N\sqrt{\phi(x(t))}.
\]
The resulting sharp value and optimal step count are
\[
\boxed{\min_{N>0,x}\mathcal E[N,x]=\int_a^b g(u)\sqrt{\phi(u)}\,du,\qquad
N_*=\int_a^b\frac{du}{\sqrt{\phi(u)}}.}
\]
In the Gaussian white-control-noise case \(\phi\equiv s^2\), the unique optimal interpolating control is the *uniform parameter ramp* \(x(t)=a+(b-a)t\), even if the thermodynamic metric \(g\) changes sharply. The optimal real count \(N_*=(b-a)/s\) is independent of that metric. A constant-thermodynamic-speed ramp, optimized over its own count, incurs a strict excess when \(g\) is nonconstant:
\[
\mathcal E_{\mathrm{geo}}=s\sqrt{\left(\int_a^b\sqrt{g(u)}\,du\right)
\left(\int_a^b g(u)^{3/2}\,du\right)}
> s\int_a^b g(u)\,du=\mathcal E_*.
\]
For a commuting thermal qubit with \(H(u)=u\sigma_z/2\) and inverse temperature \(\beta>0\),
\[
g(u)=\frac\beta4\operatorname{sech}^2\!\left(\frac{\beta u}{2}\right),\qquad
\mathcal E_* =\frac{s}{2}\left[\tanh\left(\frac{\beta b}{2}\right)-\tanh\left(\frac{\beta a}{2}\right)\right].
\]
On symmetric intervals \([-h,h]\), the ratio \(\mathcal E_{\mathrm{geo}}/\mathcal E_*\) approaches \(\pi/(2\sqrt2)=1.1107207345\ldots\) as \(\beta h\to\infty\): the metric-speed allocation has a limiting **11.07% higher leading quadratic cost**. The limit concerns the response functional and is not a claim of uniform physical validity of a weak-noise expansion in that extreme regime.

There is a corresponding theorem for the actual **integer** number of steps in the quadratic discrete model. For each \(s>0\), minimize
\[
E_s(N,x_0,\ldots,x_N)=\frac12\sum_{i=0}^{N-1}g(x_i)\big[(x_{i+1}-x_i)^2+s^2\big]
\]
over all integers \(N\ge1\) and monotone grids \(a=x_0\le\cdots\le x_N=b\). If \(g\) is positive and continuously differentiable, a global minimizer exists for every \(s>0\), and as \(s\downarrow0\),
\[
\boxed{\inf E_s=s\int_a^b g(u)\,du+O(s^2).}
\]
For **every** choice of global minimizing grids,
\[
\boxed{\sum_{i=0}^{N-1}(x_{i+1}-x_i-s)^2=O(s^2),\qquad
Ns=(b-a)+O(s^{1/2}).}
\]
Thus the uniform-control-increment law is asymptotically compelled by the exact finite-step quadratic objective, without assuming a preferred interpolation or a fixed number of steps.

## Assumptions and scope

Let \(a<b\). For the continuous theorem, assume \(g\in C([a,b])\) is strictly positive and \(\phi\in C([a,b])\) is strictly positive. Admissible controls \(x:[0,1]\to[a,b]\) are absolutely continuous and nondecreasing, with \(x(0)=a\), \(x(1)=b\). For real \(N>0\), define
\[
\mathcal E[N,x]=\frac12\int_0^1g(x(t))\left(\frac{\dot x(t)^2}{N}+N\phi(x(t))\right)dt.
\]
Controls with infinite integral cost are admitted but cannot be minimizers. The real \(N\) is the continuum relaxation of a large integer quench count; it is **not** a physical fractional number of quenches. For the integer-grid theorem, also assume \(g\in C^1([a,b])\), and use the discrete quadratic cost shown above. Constants in the integer-grid \(O(\cdot)\) estimates may depend on \(a,b,g\), not on \(s\) or the chosen global optimizer.

This is a theorem about the **quadratic stochastic linear-response approximation** of McKeever, Miller and Nazir, arXiv:2605.04681v1, equations (4) and (7). In their independent Gaussian-control-error model, \(s^2\) equals the variance of successive noise increments, \(2\sigma_\eta^2\), not the individual control-error variance. We retain the source's physical hypotheses of weak errors and approximately complete re-equilibration between quenches. Replacing a finite sum by the displayed continuous functional is a leading-order approximation; the integer-grid result treats the quadratic sum itself exactly, not the untruncated mean dissipated work.

## Proof

**1. Global continuous lower bound, attainment, and uniqueness.** At almost every \(t\), positivity of \(N\), \(g\), and \(\phi\) and nonnegativity of \(\dot x\) yield
\[
\frac12\left(\frac{\dot x^2}{N}+N\phi(x)\right)
-\dot x\sqrt{\phi(x)}
=\frac{(\dot x-N\sqrt{\phi(x)})^2}{2N}\ge0.
\]
Multiply by \(g(x)\), integrate, and apply the substitution formula for absolutely continuous monotone maps:
\[
\mathcal E[N,x]=\int_a^b g(u)\sqrt{\phi(u)}\,du
+\frac1{2N}\int_0^1g(x(t))\big(\dot x(t)-N\sqrt{\phi(x(t))}\big)^2dt.
\]
Equality requires \(\dot x=N\sqrt{\phi(x)}\) almost everywhere. Define \(F(y)=\int_a^y du/\sqrt{\phi(u)}\). This is strictly increasing, continuously differentiable, and \(F(a)=0\). Equality implies \(\frac d{dt}F(x(t))=N\) almost everywhere, so \(F(x(t))=Nt\) and \(N=F(b)\). Conversely, \(x_*(t)=F^{-1}(tF(b))\) attains equality, proving existence, the formulas and uniqueness up to equality almost everywhere (indeed everywhere for continuous representatives).

**2. Uniform noise and metric-speed comparison.** If \(\phi=s^2\), then \(F(y)=(y-a)/s\); hence \(N_*=(b-a)/s\) and \(x_*(t)=a+(b-a)t\). Let \(L_g=\int_a^b\sqrt{g(u)}\,du\). A constant-thermodynamic-speed control obeys \(\sqrt{g(x)}\dot x=L_g\) and has
\[
\int_0^1g(x)\dot x^2dt=L_g^2,\qquad
\int_0^1g(x)dt=\frac1{L_g}\int_a^b g(u)^{3/2}du.
\]
Optimizing \(\frac12[L_g^2/N+Ns^2(\int g^{3/2})/L_g]\) over real \(N>0\) gives the stated \(\mathcal E_{\mathrm{geo}}\). Cauchy-Schwarz for \(g^{1/4}\) and \(g^{3/4}\) proves
\[
\left(\int_a^b g\right)^2\le\left(\int_a^b\sqrt g\right)
\left(\int_a^b g^{3/2}\right),
\]
with equality precisely when \(g\) is constant on the interval (continuity and strict positivity). Thus the superiority of the noise-matched schedule is strict for every nonconstant metric.

**3. Thermal qubit and the limiting ratio.** For \(H(u)=u\sigma_z/2\), direct differentiation of the Gibbs free energy gives the Kubo metric \(g(u)=\beta\operatorname{Var}_{\pi_u}(\sigma_z/2)=\beta\operatorname{sech}^2(\beta u/2)/4\). Integrating yields the stated hyperbolic-tangent formula. Under the change of variable \(z=\beta u/2\), dominated convergence on \([-\beta h/2,\beta h/2]\) and the elementary integrals
\[
\int_{-\infty}^{\infty}\operatorname{sech}z\,dz=\pi,
\qquad \int_{-\infty}^{\infty}\operatorname{sech}^3z\,dz=\frac\pi2,
\qquad \int_{-\infty}^{\infty}\operatorname{sech}^2z\,dz=2
\]
show that \(\int\sqrt g\to\pi/\sqrt\beta\), \(\int g^{3/2}\to\pi\sqrt\beta/8\), and \(\int g\to1\). Their ratio tends to \(\pi/(2\sqrt2)\). All integrations are over the expanding symmetric interval, and no interchange with a physical response-limit remainder is asserted.

**4. Existence and asymptotics for integer counts.** Put \(d_i=x_{i+1}-x_i\ge0\), \(\ell=b-a\), \(m=\min g>0\), \(M=\max g\), and \(L=\sup|g'|<\infty\). For each fixed \(N\), the grid simplex is compact and \(E_s\) continuous. Moreover \(E_s\ge (m/2)Ns^2\), so a globally minimizing count must lie below a finite bound determined by the cost of any admissible trial grid. Global minima therefore exist for each \(s>0\).

For the trial grid \(N_s=\lceil\ell/s\rceil\), \(d_i=\ell/N_s=s+O(s^2)\); the Lipschitz left-Riemann-sum estimate gives
\[
E_s(N_s,\mathrm{uniform\ grid})=sG+O(s^2),\qquad G=\int_a^b g(u)du.
\]
In detail, use \(\sum_i g(x_i)d_i=G+O(\sum_i d_i^2)=G+O(s)\) and \(E_s=s\sum_i g(x_i)d_i+\frac12\sum_i g(x_i)(d_i-s)^2\); for the uniform trial, the latter square sum is \(O(s^3)\).

For an arbitrary globally minimizing grid, the trial bound gives \(E_s=O(s)\). Positivity therefore forces \(\sum_i d_i^2\le2E_s/m=O(s)\) and \(N\le 2E_s/(ms^2)=O(s^{-1})\). The exact identity
\[
E_s=s\sum_i g(x_i)d_i+\frac12\sum_i g(x_i)(d_i-s)^2
\]
and the Lipschitz quadrature inequality
\[
\sum_i g(x_i)d_i\ge G-\frac L2\sum_i d_i^2
\]
then imply
\[
E_s\ge sG-O(s^2)+\frac m2\sum_i(d_i-s)^2.
\]
Comparison with the trial upper bound proves \(\sum_i(d_i-s)^2=O(s^2)\) and \(\inf E_s=sG+O(s^2)\). Finally, \(\sum_i d_i=\ell\), so by Cauchy-Schwarz
\[
|\ell-Ns|=\left|\sum_i(d_i-s)\right|
\le\sqrt{N\sum_i(d_i-s)^2}=O(s^{1/2}).
\]
The argument is uniform over every minimizing grid; it does not depend on a chosen sequence of minimizers. This closes the proof.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. Run `python3 checker.py` from the directory containing that file. It performs 236 numerical assertions, including (i) comparison of Gibbs-metric curvature with the exact binary relative-entropy expansion, (ii) nonconstant positive noise functions and the matching map, (iii) the strict thermodynamic-speed gap and its limiting coefficient, (iv) exact finite-grid identities and quadrature bounds for randomized monotone grids, and (v) constructive integer-grid asymptotics. These tests are **finite supporting checks**; all quantifiers and asymptotic statements above follow from the analytical proof, not from sampling.

## Relationship to prior work

McKeever, Miller and Nazir (2026), arXiv:2605.04681v1, derive the stochastic quadratic quench cost and a finite optimal step number using a prescribed geodesic/thermodynamic-length schedule (their equations (4), (7), (9)–(11)). These forward equations, the underlying Kubo metric, and the existence of finite duration under noise are **prior work**. The result here optimizes the schedule and the count **simultaneously**, proves the strict metric-speed disadvantage on nonconstant one-dimensional metrics, gives the qubit coefficient, and carries the matching principle to the discrete integer-grid quadratic objective. It does not claim to have introduced thermodynamic length, stochastic costs, or AM–GM itself.

Large, Chetrite and Sivak (2018), arXiv:1802.02670, analyze thermodynamic costs of stochastic control in classical microscopic systems, including uniform-friction settings. Large and Sivak (2018), arXiv:1812.08216, examine deterministic discrete step placement. General one-dimensional variational principles can suggest the matching identity, so implicit coverage by broader optimization theory is a residual originality risk; no claim of exhaustive uniqueness is made.

## Limitations

The statements apply to a single oriented scalar control and positive scalar metric and noise variance. They do not solve multi-parameter anisotropic quantum optimal-control problems. The continuously optimized \(N_*\) is a real relaxation; physical protocols use integer counts. The integer-step theorem is an asymptotic result as \(s\downarrow0\), not an assertion of exact equal increments for every fixed \(s\). Neither theorem controls third- and higher-order terms omitted from the microscopic mean-work response law; thus the \(O(s^2)\) quadratic-model remainder must not be conflated with an error estimate for full quantum dissipation. The large-\(\beta h\) 11.07% coefficient is an exact formal comparison of two quadratic costs, not a uniform validity statement for cold, strongly driven devices. Experimental control constraints, correlated/non-Markovian noise, finite thermalization, and measurement errors are outside scope.

## References

1. Theodore McKeever, Harry J. D. Miller and Ahsan Nazir, *Finite steps optimise dissipation in stochastically controlled quantum systems*, arXiv:2605.04681v1 (first posted 2026-05-06). https://arxiv.org/html/2605.04681v1
2. Steven J. Large, Raphael Chetrite and David A. Sivak, *Stochastic control in microscopic nonequilibrium systems*, arXiv:1802.02670v2. https://arxiv.org/abs/1802.02670
3. Steven J. Large and David A. Sivak, *Optimal discrete control: minimizing dissipation in discretely driven nonequilibrium systems*, arXiv:1812.08216v2. https://arxiv.org/abs/1812.08216
