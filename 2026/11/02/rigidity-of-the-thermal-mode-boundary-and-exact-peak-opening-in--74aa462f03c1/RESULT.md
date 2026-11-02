# Rigidity of the thermal-mode boundary and exact peak opening in a harmonic run-and-tumble model

## Finding

For a one-dimensional harmonically trapped run-and-tumble particle with a strictly positive Brownian diffusivity, the previously derived thermal shape-transition equation has **exactly one** solution in the thermal variance for each reduced flip rate \(0<b<1\). Its critical variance \(B_*(b)\) is smooth and strictly decreasing in \(b\), from \(1\) to \(0\). There are exactly two symmetric global density modes below this variance and exactly one above it (also at criticality). At the threshold, the central maximum is quartically flat, with exact normalized fourth derivative, and the emerging mode positions obey the parameter-independent law
\[
\frac{p_{b,B_*}^{(4)}(0)}{p_{b,B_*}(0)}=-\frac{2(1-b)}{B_*^2},\qquad
m_b(B)=\sqrt{3(B_*(b)-B)}+o\!\left(\sqrt{B_*(b)-B}\right).
\]
The peak-to-center density contrast has the further exact leading behavior
\[
\frac{p_{b,B}(m_b(B))-p_{b,B}(0)}{p_{b,B}(0)}=
\frac{3(1-b)}{4 B_*(b)^2}(B_*(b)-B)^2+o\!\left((B_*(b)-B)^2\right).
\]
For \(b\ge1\), the density is strictly unimodal for every \(B>0\). The formulas for the density and for the **location equation** of its shape transition are prior results; the claim here is the rigorous global rigidity, strict parameter ordering, and exact near-transition amplitude statements.

## Assumptions and scope

Consider the stationary limit of
\[
dX_t=(-kX_t+v\eta_t)\,dt+\sqrt{2D}\,dW_t,
\]
where \(k,v,D>0\), \(W_t\) is standard Brownian motion, and the independent stationary two-state chain \(\eta_t\in\{-1,+1\}\) flips sign at rate \(\rho>0\). Write the dimensionless position and parameters as
\[
Y=\frac{kX}{v},\quad b=\frac{\rho}{k},\quad B=\frac{Dk}{v^2}.
\]
The stationary density of \(Y\) is \(p_{b,B}\). The central result concerns all real \(b>0\), \(B>0\), including the critical boundary, and the positive mode \(m_b(B)\) is defined only for \(0<b<1\) and \(B<B_*(b)\). No claim is made about a nonequilibrium free energy, finite-sample inference, or other trap geometries.

The stationary representation is
\[
p_{b,B}(x)=\frac1{Z_b\sqrt{2\pi B}}\int_{-1}^{1}
(1-u^2)^{b-1}\exp\!\left(-\frac{(x-u)^2}{2B}\right)\,du,\qquad
Z_b=\int_{-1}^{1}(1-u^2)^{b-1}\,du.
\]
This Gaussian–Beta convolution and a corresponding hypergeometric zero-curvature condition were derived in the cited physical literature and are not claimed as new.

## Proof

**1. Independent derivation of the stationary input distribution.** In the stable filter \(dU/dt=k(-U+\eta)\), write the two stationary joint densities as \(q_+(u),q_-(u)\). Their total stationary flux vanishes, giving \((1-u)q_+=(1+u)q_-\), so \(q_\pm=(1\pm u)f(u)/2\). The \(+\)-state equation gives
\[
\frac{d}{du}[(1-u^2)f(u)]=-2bu f(u),
\]
whose integrable solution is \(f(u)=Z_b^{-1}(1-u^2)^{b-1}\) for \(|u|<1\). The Brownian stochastic convolution over the infinite past is independent of \(U\) and has variance \(D/k\); dimensionless variance is \(B\). This proves the displayed density without invoking a new stationary-law hypothesis.

**2. A transverse, uniquely crossed zero-curvature condition.** For \(z=1/(2B)\) and \(j=0,1,2\), define
\[
I_j(b,z)=\int_0^1 t^{j-1/2}(1-t)^{b-1}e^{-zt}\,dt,
\qquad H(b,z)=\frac{I_1(b,z)}{I_0(b,z)},\qquad h(b,z)=2zH(b,z)-1.
\]
Direct Gaussian differentiation shows \(p_{b,B}''(0)/p_{b,B}(0)=h(b,z)/B\). In particular, the published threshold equation is equivalent to \(h(b,z)=0\), but no uniqueness follows merely from displaying that equation.

Integrating the derivative of \(t^{1/2}(1-t)^b e^{-zt}\) over \((0,1)\), with vanishing boundary terms, yields
\[
\frac12-\left(b+\frac12\right)H-z\frac{I_1-I_2}{I_0}=0.
\]
Using \(\partial_z H=H^2-I_2/I_0\), at **every** possible zero \(h(b,z)=0\) (where \(H=1/(2z)\)) we obtain the exact crossing derivative
\[
\left.\partial_z h(b,z)\right|_{h=0}=\frac{1-b}{z}.
\]
For \(0<b<1\), \(h(b,z)\to-1\) as \(z\downarrow0\), whereas elementary Laplace asymptotics at \(t=0\) give
\[
h(b,z)=\frac{1-b}{z}+O(z^{-2})>0\qquad(z\to\infty).
\]
Existence follows by continuity. Every zero crosses from negative to positive, so there cannot be two zeros: two upward crossings would force an intervening non-upward crossing. This proves a unique critical \(z_*(b)\), and \(B_*(b)=1/(2z_*(b))\). The positive transverse derivative gives smoothness by the implicit function theorem.

For each fixed \(z>0\), differentiation of the tilted \(t\)-expectation with respect to \(b\) gives
\[
\partial_b H(b,z)=\operatorname{Cov}_{b,z}\big(t,\log(1-t)\big)<0,
\]
because the first function strictly increases while the second strictly decreases under a nondegenerate density. Thus \(\partial_b h<0\). Comparing the unique upward crossings shows that \(z_*(b)\) increases strictly with \(b\) and \(B_*(b)\) decreases strictly. As \(b\downarrow0\) the tilted \(t\)-distribution tends to a unit atom, and \(h\to2z-1\), giving \(B_*(b)\to1\). As \(b\uparrow1\), the corresponding uniform prior has strictly negative central curvature at every finite \(z\); hence \(z_*(b)\to\infty\), i.e. \(B_*(b)\to0\).

**3. Global mode count.** For \(0<b<1\), the unsmoothed integrable Beta profile has one interior minimum and singular peaks at the two support edges. Approximate it in \(L^1\) by a symmetric, compactly supported, continuous piecewise smooth profile that increases on a short interval at the left edge, decreases to a positive central minimum, increases to the right edge, then decreases to zero at the right support edge. The derivative of each approximant has precisely the four sign blocks \(+,-,+,-\). The Gaussian kernel is variation diminishing: its convolution with a signed, compactly supported integrable function with at most \(s\) sign changes has at most \(s\) sign changes. For completeness, after multiplying the convolution by its positive Gaussian factor, this is the classical generalized Descartes theorem for \(\int e^{xy/B}g(y)\,dy\); an elementary proof inducts on sign changes, multiplying by \(e^{-xy_0/B}\) and differentiating to remove a sign boundary at \(y_0\), then applying Rolle's theorem. Therefore each approximated density derivative has at most three sign changes. Gaussian smoothing makes the derivatives converge uniformly to \(p_{b,B}'\), so the limit also has at most three sign changes.

The derivative is odd; it is strictly negative for \(x>1\) and positive for \(x<-1\). When \(h<0\), it is negative immediately to the right of zero, and no positive derivative region on \(x>0\) is possible without at least five total sign changes. Thus the center is the unique global mode. When \(h>0\), the derivative is positive immediately right of zero, so it must change to negative at precisely one positive location; by symmetry there are exactly two global maxima and a central minimum. At \(h=0\), the fourth-derivative calculation below shows that the derivative is negative immediately right of zero; the same global argument applies. For \(b=1\) the input prior is uniform; for \(b>1\) it is strictly decreasing on \((0,1)\). Convolution with a Gaussian is then strictly decreasing on the positive half-line, as follows directly from pairing the signs of the input derivative. This handles every parameter, including the endpoints.

**4. Exact quartic coefficient and peak separation.** At the critical point, \(H=B_*\). The integration-by-parts identity above then gives the additional exact moment relation
\[
\frac{I_2}{I_0}=(2b+1)B_*^2.
\]
Differentiating the Gaussian four times and using the two moment identities yields
\[
\frac{p_{b,B_*}^{(4)}(0)}{p_{b,B_*}(0)}=
\frac{(I_2/I_0)-6B_*H+3B_*^2}{B_*^4}
=-\frac{2(1-b)}{B_*^2}<0.
\]
The crossing derivative also gives
\[
\left.\partial_B\left(\frac{p_{b,B}''(0)}{p_{b,B}(0)}\right)\right|_{B=B_*}
=-\frac{1-b}{B_*^2}.
\]
Analyticity in \(x\) and \(B>0\), plus even symmetry, therefore gives, with \(\delta=B_*-B\),
\[
\frac{p_{b,B}'(x)}{x\,p_{b,B}(0)}=
\frac{1-b}{B_*^2}\left(\delta-\frac{x^2}{3}\right)
+o(\delta+x^2),
\qquad \delta\downarrow0,
\]
uniformly as \(x\to0\). The analytic implicit-function theorem applied to the equation in \(x^2\) proves \(m_b(B)^2=3\delta+o(\delta)\). The global mode count above ensures that this local nonzero root is the unique positive **global** mode. Fourth-order Taylor expansion also yields the stated \(3(1-b)/(4B_*^2)\) peak-height coefficient.

## Verification

The companion standard-library program `verify_pitchfork.py` performs independent midpoint quadrature after the endpoint-regularizing substitution \(t=1-(1-u^2)^{1/b}\). It calculates the tilted-moment critical root by bisection, checks the exact critical moments, checks the ordering of five critical widths, and locates the two modal peaks directly from the Gaussian-mixture derivative at several subcritical widths. Execution with Python 3 completed 41 assertions successfully. Representative values are \(B_*(0.25)\approx0.53856358\), \(B_*(0.50)\approx0.31646434\), and \(B_*(0.75)\approx0.18327382\). Finite numerical checks corroborate, but do not establish, the universal theorem.

## Relationship to prior work

The Gaussian–Beta convolution and the model were derived by Frydel (2022). Sabhapandit and Majumdar (2024, Sec. 4.1.1 and Eq. (96)) already provide the exact central-curvature condition, the one-versus-two-peak phase diagram, and numerical boundary points. Guéneau, Majumdar and Schehr (2026, Sec. V.1.1) revisit the same finite-temperature boundary for the one-dimensional RTP and derive further turning-surface scaling. **None of those previously displayed threshold equations is being presented as a new threshold equation here.** The new evaluated statement is the strict single-crossing proof for every \(b\), the monotone ordering of the boundary, the globally exhaustive mode count, and the exact critical quartic and peak-opening amplitudes. The amplitude's square-root exponent is familiar from pitchfork bifurcations and the coefficient \(\sqrt3\) is consistent with generic Gaussian heat-flow normal forms; it is not claimed to define a novel universality class. The total-positivity argument invokes a standard Gaussian variation-diminishing property.

## Limitations

The theorem concerns fixed-rate, symmetric two-state switching, a harmonic trap and additive independent Brownian noise. It does not establish analogous classifications for asymmetric switching, nonharmonic confinement, colored thermal forcing, or coupled particles. The formula is local near the critical line, not a quantitative error bound away from it. Algebraic and numerical consequences of published exact convolution formulas may also be obtainable by other standard methods. An independent mathematical review and definitive literature-priority assessment have not been conducted.

## References

1. D. Frydel, *Positing the problem of stationary distributions of active particles as third-order differential equation*, arXiv:2207.08695 (first posted 2022-07-18), https://arxiv.org/abs/2207.08695.
2. S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480 (first posted 2024-04-03), https://arxiv.org/abs/2404.02480; Sec. 4.1.1, Eq. (96).
3. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first posted 2026-02-09), https://arxiv.org/abs/2602.08436; Sec. V.1.1.
4. *Applications of total positivity theory to 1D prescribed curvature problems*, Journal of Mathematical Analysis and Applications (2015), https://doi.org/10.1016/j.jmaa.2015.03.002 (variation-diminishing theorem for totally positive kernels).
