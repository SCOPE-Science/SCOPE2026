# Spontaneous transport-design symmetry breaking in a two-bath harmonic dimer

## Finding

Consider two unit-mass classical harmonic oscillators, each attached to a distinct white-noise Langevin bath, with mutual spring stiffness \(k>0\). A fixed total on-site pinning stiffness \(P>0\) and fixed total damping \(\Gamma>0\) can be distributed between the two oscillators. Write \(a,b\geq0\), \(a+b=P\), for the on-site stiffnesses and \(\gamma_1,\gamma_2>0\), \(\gamma_1+\gamma_2=\Gamma\), for the damping coefficients. Assume unequal fixed bath temperatures \(T_L>T_R\), in units where the Boltzmann constant is one.

**Theorem (complete joint allocation phase diagram).** The unique heat-current-maximizing allocation is symmetric, \(a=b=P/2\) and \(\gamma_1=\gamma_2=\Gamma/2\), if and only if \(\Gamma^2\leq8k\). If \(\Gamma^2>8k\), the maximizing configurations are exactly two mirror images, with more pinning stiffness assigned to the more strongly damped oscillator. Their precise forms are as follows.

Let
\[
 r_0=\sqrt{1-\frac{8k}{\Gamma^2}},\qquad
 P_c=\frac{\Gamma^2 r_0}{4},\qquad
 \delta=a-b,\quad \eta=\frac{\gamma_2-\gamma_1}{\Gamma}.
\]

If \(P\geq P_c\), the two maximizers are exactly
\[
 (\delta,\eta)=\left(-\frac{\Gamma^2r_0}{4},r_0\right)
 \quad\text{and}\quad
 (\delta,\eta)=\left(\frac{\Gamma^2r_0}{4},-r_0\right).
\]
If \(0<P<P_c\), the two maximizers are exactly
\[
 (\delta,\eta)=(-P,r_*)\quad\text{and}\quad(P,-r_*),
\]
where \(r_*\in(4P/\Gamma^2,1)\) is the unique solution of
\[
 \frac{8k^2r_*}{(1-r_*^2)^2}=\frac{\Gamma^2P}{2}.
\]
Thus for small pinning budgets the optimizer concentrates all pinning in one oscillator, whereas above \(P_c\) it retains positive pinning at both sites. At \(P=P_c\), the interior and boundary descriptions agree. At the damping threshold, symmetry is unbroken, and for any fixed \(P>0\) the damping imbalance emerges continuously with square-root order parameter \(r_0\).

For example, at \(k=1\), \(\Gamma=4\), \(P=3\), and \(T_L-T_R=1\), one optimizer has
\[
 (a,b)=\left(\frac{3-2\sqrt2}{2},\frac{3+2\sqrt2}{2}\right),\qquad
 (\gamma_1,\gamma_2)=(2-\sqrt2,2+\sqrt2).
\]
Its heat current is exactly \(1/10\), versus \(1/11\) for the equal allocation. Swapping both site allocations gives the other maximizer.

## Assumptions and scope

Oscillator displacements are \(x_1,x_2\) and velocities \(v_1,v_2\). The model is the Itô system
\[
 \begin{aligned}
 dx_1&=v_1\,dt, &dx_2&=v_2\,dt,\\
 dv_1&=[-(a+k)x_1+kx_2-\gamma_1v_1]dt+\sqrt{2\gamma_1T_L}\,dW_1,\\
 dv_2&=[kx_1-(b+k)x_2-\gamma_2v_2]dt+\sqrt{2\gamma_2T_R}\,dW_2,
 \end{aligned}
\]
with independent standard Brownian motions. Temperatures and budget totals are held fixed while allocations vary. The masses and mutual spring strength are fixed; no temperature-dependent friction, nonlinear reservoirs, quantum corrections, or non-Markovian bath dynamics are assumed. Zero *on-site* pinning at one end is allowed, but the total \(P\) is positive and both damping rates remain strictly positive.

## Proof

**1. A stationary state exists uniquely.** The stiffness matrix
\[
 K=\begin{pmatrix}a+k&-k\\-k&b+k\end{pmatrix}
\]
is positive definite because its determinant is \(ab+kP>0\). For the deterministic drift, the positive quadratic mechanical energy has derivative \(-\gamma_1v_1^2-\gamma_2v_2^2\). The only drift-invariant trajectory with both velocities identically zero is the origin, by positive definiteness of \(K\). The linear drift is therefore Hurwitz; the Gaussian Ornstein–Uhlenbeck system has a unique stationary covariance.

**2. The exact heat current.** At stationarity define
\[
 q=\langle x_1v_2\rangle=-\langle x_2v_1\rangle,
 \qquad w=\langle v_1v_2\rangle.
\]
Stationarity of the four position-position moments gives \(\langle x_iv_i\rangle=0\) and the displayed antisymmetry. Stationarity of the velocity cross moment gives
\[
 (\gamma_1+\gamma_2)w=(b-a)q.
\]
Stationarity of \(\langle x_1v_2\rangle\), \(\langle x_2v_1\rangle\), and \(\langle x_iv_i\rangle\) implies
\[
 k\big(\langle v_1^2\rangle-\langle v_2^2\rangle\big)
 =\big[(a+k)\gamma_2+(b+k)\gamma_1\big]q+(b-a)w.
\]
The kinetic variances, from Itô's identity, are
\[
 \langle v_1^2\rangle=T_L-\frac{kq}{\gamma_1},\qquad
 \langle v_2^2\rangle=T_R+\frac{kq}{\gamma_2}.
\]
Eliminating \(w\) and the variances yields the heat current \(J=kq=\gamma_1(T_L-\langle v_1^2\rangle)\):
\[
 \boxed{\displaystyle
 J=\frac{k^2\Gamma(T_L-T_R)}{
 (a-b)^2+\Gamma(a\gamma_2+b\gamma_1+k\Gamma)
 +k^2\Gamma^2/(\gamma_1\gamma_2)}.}
\]
This is an equal-mass specialization of previously known exact harmonic-dimer conductance formulas; its use as an optimization objective, not its derivation, is the claimed contribution.

**3. Exact reduction to an allocation problem.** Set \(\delta=a-b\in[-P,P]\) and \(\eta=(\gamma_2-\gamma_1)/\Gamma\in(-1,1)\). Then \(a=(P+\delta)/2\), \(b=(P-\delta)/2\), \(\gamma_1=\Gamma(1-\eta)/2\), and \(\gamma_2=\Gamma(1+\eta)/2\). Maximizing \(J\) is equivalent to minimizing
\[
 F(\delta,\eta)=\delta^2+\frac{\Gamma^2}{2}\delta\eta+\frac{4k^2}{1-\eta^2},
\]
because the omitted denominator term is the fixed positive quantity \(\Gamma^2(P/2+k)\). The objective is invariant under simultaneous sign reversal of \((\delta,\eta)\). For each fixed \(\eta\geq0\), strict convexity in \(\delta\) gives the unique minimizer
\[
 \delta_*(\eta)=-\min\left\{\frac{\Gamma^2\eta}{4},P\right\}.
\]

**4. Complete global minimization.** For \(0\leq\eta\leq4P/\Gamma^2\), wherever that interval lies in \([0,1)\), the reduced objective is
\[
 F_{\mathrm{int}}(\eta)=-\frac{\Gamma^4\eta^2}{16}+\frac{4k^2}{1-\eta^2},
 \quad F'_{\mathrm{int}}(\eta)=\eta\left[-\frac{\Gamma^4}{8}+\frac{8k^2}{(1-\eta^2)^2}\right].
\]
The bracket is strictly increasing on \((0,1)\). If \(\Gamma^2\leq8k\), it is nonnegative and is strictly positive for every \(\eta>0\), proving the unique symmetric minimizer. If \(\Gamma^2>8k\), it changes sign exactly once, at \(r_0\), from negative to positive.

Beyond the clipping point \(\eta_b=4P/\Gamma^2<1\), when this region exists, the reduced objective is
\[
 F_{\mathrm{bdry}}(\eta)=P^2-\frac{\Gamma^2P}{2}\eta+\frac{4k^2}{1-\eta^2},
 \quad F'_{\mathrm{bdry}}(\eta)=-\frac{\Gamma^2P}{2}+\frac{8k^2\eta}{(1-\eta^2)^2}.
\]
This derivative is strictly increasing on \((0,1)\), tends to infinity at one, and agrees with \(F'_{\mathrm{int}}\) at \(\eta_b\). Therefore if \(r_0\leq\eta_b\), the unique nonnegative minimizing imbalance is \(r_0\), while if \(r_0>\eta_b\), it is the unique zero \(r_*\in(\eta_b,1)\) of \(F'_{\mathrm{bdry}}\). These inequalities are equivalent to \(P\geq P_c\) and \(P<P_c\), respectively. Sign symmetry then gives exactly the stated one or two global optimizers. Since \(F\to\infty\) as \(|\eta|\to1\), no nonattained optimizer at zero damping is missing.

## Verification

The standalone program `thermal_dimer_check.py` reproduces an exact rational stationary covariance calculation, independently solves 600 numerical four-dimensional Lyapunov equations, and compares the closed optimizer with 180 independent bounded scalar optimizations. It also checks the exact-parameter witness above. Run `python thermal_dimer_check.py` with NumPy, SciPy, and SymPy installed. No numerical test is used as a substitute for the all-parameter proof.

## Relationship to prior work

Saito and Dhar's 2010 preprint gives a general classical harmonic-network heat-transfer framework and Green-function formulas. Simón and collaborators' 2019 ion-crystal work uses graded local trap frequencies and stochastic baths. Their 2020 harmonic-dimer preprint (published 2021) gives exact heat currents for arbitrary local trap strengths, damping rates, and masses; the equal-mass current formula here is already covered by that source's Eq. (22) and is **not** claimed as novel. Its main optimization is of *thermal rectification under bath interchange*, whereas the present statement maximizes the magnitude of a single temperature-biased heat current under *two simultaneous fixed-sum stiffness and friction budgets*. In particular, the universal symmetry-breaking threshold \(\Gamma^2=8k\), its mirror-optimum classification, and the pinning saturation threshold \(P_c\) are not stated in that primary work. Both results concern the same physical model, so historical priority of the allocation theorem remains a residual risk.

## Limitations

The result concerns two **unit-mass**, linearly coupled classical oscillators with Markovian, independent Gaussian thermal baths and fixed temperature difference. It does not claim a general optimizer for unequal masses, arbitrary networks, quantum reservoirs, or temperature-dependent damping. The optimal states on the boundary set one local *pinning* stiffness to zero; imposing strictly positive local pinning would yield a supremum, rather than an attained maximum, in that regime. The theorem's originality is restricted to the two-budget optimizer classification, **not** the known steady-state current expression. Independent validation has not been performed; uninspected literature may contain the same classification.

## References

1. K. Saito and A. Dhar, *Generating Function Formula of Heat Transfer in Harmonic Networks*, arXiv:1012.0622 (first public version December 3, 2010); Phys. Rev. E 83, 041121 (2011). https://arxiv.org/abs/1012.0622
2. M. A. Simón, S. Martínez-Garaot, M. Pons and J. G. Muga, *Asymmetric Heat Transport in Ion Crystals*, arXiv:1905.11854 (first public version May 28, 2019); Phys. Rev. E 100, 032109 (2019). https://arxiv.org/abs/1905.11854
3. M. A. Simón, A. Alaña, M. Pons, A. Ruiz-García and J. G. Muga, *Heat rectification with a minimal model of two harmonic oscillators*, arXiv:2010.10432 (first public version October 20, 2020); Phys. Rev. E 103, 012134 (2021). https://arxiv.org/abs/2010.10432
4. N. Freitas and J. P. Paz, *New analytic solution for the heat flow through a general harmonic network*, arXiv:1409.2904 (submitted September 9, 2014). A revision was withdrawn for errors in specified formulas; this work is cited for historical scope only, not used as a proof premise. https://arxiv.org/abs/1409.2904
