# Two sharp spacing-edge thresholds in the two-particle active Dyson model

## Finding

For the stationary two-particle, zero-temperature **model II** of the harmonically confined active Dyson system, the interparticle spacing has two different algebraic edge exponents. These give a sharp three-regime classification in the orientation-flip rate, including a regime in which the density diverges at the *minimum* possible spacing but vanishes at the *maximum* possible spacing.

Let
\[
R=\sqrt{v^2+2\mu g},\qquad
z_-=\frac{R-v}{\mu},\qquad z_+=\frac{R+v}{\mu},
\]
\[
\beta_- = \frac{\gamma(R-v)}{\mu R},\qquad
\beta_+ = \frac{\gamma(R+v)}{\mu R}.
\]
The stationary spacing density \(p\) has support exactly \([z_-,z_+]\). There are strictly positive finite constants \(C_-,C_+\), depending on the model parameters, such that as \(\varepsilon\downarrow0\),
\[
\Pr\{Z<z_-+\varepsilon\}=C_-\varepsilon^{\beta_-}(1+O(\varepsilon)),
\qquad
\Pr\{Z>z_+-\varepsilon\}=C_+\varepsilon^{\beta_+}(1+O(\varepsilon)),
\]
and
\[
p(z_-+\varepsilon)=\beta_- C_-\varepsilon^{\beta_--1}(1+O(\varepsilon)),\qquad
p(z_+-\varepsilon)=\beta_+ C_+\varepsilon^{\beta_+-1}(1+O(\varepsilon)).
\]
The two sharp thresholds are
\[
\gamma_+=\frac{\mu R}{R+v},\qquad
\gamma_-=\frac{\mu R}{R-v},\qquad
0<\gamma_+<\mu<\gamma_-.
\]
For \(0<\gamma<\gamma_+\), the density diverges at both edges. For \(\gamma_+<\gamma<\gamma_-\), it diverges at the lower edge but vanishes at the upper edge. For \(\gamma>\gamma_-\), it vanishes at both edges. At equality with either threshold the density approaches a strictly positive finite constant at that edge. The exact geometry identities
\[
\frac{1}{\gamma_+}+\frac{1}{\gamma_-}=\frac{2}{\mu},\qquad
\gamma_- -\gamma_+=\frac{vR}{g}
\]
show that the two transitions cannot coincide at positive propulsion speed and finite repulsion.

There is also a state-resolved boundary hierarchy. Write \(p_+,p_0,p_-\) for the stationary spacing densities with relative propulsion \(+2v,0,-2v\), respectively. With
\[
k_+=\frac{2\mu R}{R+v},\qquad k_-=\frac{2\mu R}{R-v},
\]
the conditional population ratios obey
\[
\frac{p_0(z_+-\varepsilon)}{p_+(z_+-\varepsilon)}
=\frac{k_+}{2v}\varepsilon+O(\varepsilon^2),\qquad
\frac{p_-(z_+-\varepsilon)}{p_+(z_+-\varepsilon)}=O(\varepsilon^2),
\]
\[
\frac{p_0(z_-+\varepsilon)}{p_-(z_-+\varepsilon)}
=\frac{k_-}{2v}\varepsilon+O(\varepsilon^2),\qquad
\frac{p_+(z_-+\varepsilon)}{p_-(z_-+\varepsilon)}=O(\varepsilon^2).
\]
These are asymptotics for the actual stationary distributions; no approximation in the switching rate, interaction strength, or trap stiffness is imposed.

## Assumptions and scope

Take \(\mu,g,v,\gamma>0\), two labeled particles \(X_1>X_2\), and independent signs \(\sigma_i\in\{-1,+1\}\), each flipping at constant rate \(\gamma\). The deterministic motion between flips is
\[
\dot X_1=-\mu X_1+\frac{g}{X_1-X_2}+v\sigma_1,
\qquad
\dot X_2=-\mu X_2+\frac{g}{X_2-X_1}+v\sigma_2.
\]
This is the two-particle specialization of the all-to-all interacting version of the active Dyson dynamics, in the component with preserved ordering. There is no thermal Brownian noise. Define the spacing \(Z=X_1-X_2>0\) and relative-propulsion state \(S=(\sigma_1-\sigma_2)/2\in\{-1,0,+1\}\). Then
\[
\dot Z=f_S(Z),\qquad f_s(z)=-\mu z+\frac{2g}{z}+2vs.
\]
The Markov state \(S\) jumps from each extreme state to the zero state at rate \(2\gamma\), and from zero to each extreme state at rate \(\gamma\). The two microscopic zero-propulsion states have been combined into a single mode; its stationary mass is \(1/2\). The endpoints \(z_-,z_+\) are the positive zeros of \(f_{-1}\) and \(f_{+1}\), respectively.

## Proof

**1. Stationary law, support, and densities.** Each drift is strictly decreasing for \(z>0\), with \(f_s'(z)=-\mu-2g/z^2\le-\mu\), and points inward relative to the interval \([z_-,z_+]\). Two solutions driven by the same sign process contract at least exponentially at rate \(\mu\). Pullback contraction with the stationary irreducible three-state chain therefore yields a unique invariant joint law on the compact attracting interval. Arbitrarily long uninterrupted excursions in either extreme state, each of strictly positive probability, bring the spacing arbitrarily close to its corresponding endpoint. Switching times also give positive mass to every intervening open subinterval. Thus the spacing support is precisely \([z_-,z_+]\).

Each conditional stationary law is absolutely continuous in the interior: conditional on the last switch into a fixed mode, the continuously distributed holding time is pushed forward by a strictly monotone scalar flow except at its fixed point. There is no atom at a mode's fixed point, because the other modes have different fixed points and cannot supply a stationary atom there; any such atom would lose mass at rate \(2\gamma\). Consequently let \(p_s(z)\) denote the conditional stationary density, aggregated over the two microscopic zero states, and put \(p=\sum_sp_s\). The densities solve the stationary transport equations in the distributional sense and are smooth locally away from zeros of mode drifts.

**2. Stationary flux equations.** In the interior,
\[
(f_+p_+)'=-2\gamma p_+ +\gamma p_0,
\]
\[
(f_0p_0)'=2\gamma(p_++p_-)-2\gamma p_0,
\]
\[
(f_-p_-)'=-2\gamma p_-+\gamma p_0.
\]
All three mode fluxes tend to zero at each exterior endpoint: stationarity and absence of mass outside the compact support exclude incoming flux from exterior states, while the drift of the endpoint-attracting mode vanishes there and its integrable density excludes a nonzero limiting flux. The sum of the other mode fluxes is zero; both have the same strictly inward sign at that endpoint, so both vanish individually. This establishes the boundary conditions without assuming bounded endpoint densities.

**3. Exact upper-edge tail.** Set \(b=z_+\), \(x=b-\varepsilon\), and
\[
F_s(\varepsilon)=\int_{b-\varepsilon}^{b}p_s(y)\,dy.
\]
Integrating the flux equations from \(x\) to \(b\), and using the zero boundary fluxes, gives
\[
f_+(x)p_+(x)=2\gamma F_+ -\gamma F_0,
\]
\[
|f_0(x)|p_0(x)=2\gamma(F_+ +F_- -F_0),
\]
\[
|f_-(x)|p_-(x)=\gamma F_0-2\gamma F_-.
\]
As \(\varepsilon\downarrow0\), the three velocities have limits
\[
f_+(x)=k_+\varepsilon+O(\varepsilon^2),\quad
f_0(x)=-2v+O(\varepsilon),\quad f_-(x)=-4v+O(\varepsilon).
\]
Nonnegativity of the middle and last displayed fluxes implies \(F_0\le F_++F_-\) and \(2F_-\le F_0\), hence \(F_-\le F_+\). Thus \(p_0(x)\le C F_+(\varepsilon)\) and \(p_-(x)\le C F_0(\varepsilon)\), uniformly for sufficiently small \(\varepsilon\). Integration and monotonicity of \(F_+\) yield
\[
F_0(\varepsilon)=O(\varepsilon F_+(\varepsilon)),\qquad
F_-(\varepsilon)=O(\varepsilon^2F_+(\varepsilon)).
\]
Because \(F_+'(\varepsilon)=p_+(b-\varepsilon)\), the first flux relation becomes
\[
\frac{F_+'(\varepsilon)}{F_+(\varepsilon)}
=\frac{2\gamma+O(\varepsilon)}{k_+\varepsilon+O(\varepsilon^2)}
=\frac{\beta_+}{\varepsilon}+O(1).
\]
The mass \(F_+(\varepsilon)\) is strictly positive for every \(\varepsilon>0\) by the long-dwell event. Integrating the last differential relation proves
\[
F_+(\varepsilon)=C_+\varepsilon^{\beta_+}(1+O(\varepsilon)),\qquad 0<C_+<\infty.
\]
The other mode tails are lower order, establishing the upper-edge total-tail law and density asymptotic. Furthermore the middle flux relation gives \(p_0\sim(\gamma/v)F_+\), whereas \(p_+\sim(\beta_+/\varepsilon)F_+\), proving the first upper-edge conditional ratio. The last flux equation and \(F_0=O(\varepsilon F_+)\) imply \(p_-=O(\varepsilon F_+)\), proving the second.

**4. Lower edge.** Repeat the same argument at \(a=z_-\), now integrating from \(a\) to \(a+\varepsilon\) and interchanging the extreme states. Here \(f_-(a+\varepsilon)=-k_-\varepsilon+O(\varepsilon^2)\), \(f_0(a)=2v\), and \(f_+(a)=4v\). It gives \(F_-(\varepsilon)=C_-\varepsilon^{\beta_-}(1+O(\varepsilon))\), with \(C_->0\), and the lower-edge density and state ratios.

**5. Sharp parameter regimes.** The density diverges, remains finite positive, or vanishes at a given endpoint precisely when its positive exponent \(\beta\) is less than, equal to, or greater than one. From the explicit local drift derivatives,
\[
\beta_+=2\gamma/k_+ = \frac{\gamma(R+v)}{\mu R},\qquad
\beta_-=2\gamma/k_- = \frac{\gamma(R-v)}{\mu R}.
\]
Since \(R>v>0\), the two transition rates are strictly ordered. Their reciprocal sum and difference follow algebraically using \(R^2-v^2=2\mu g\). This proves every assertion.

## Verification

For the exact rational example \(\mu=v=\gamma=1\), \(g=4\), we have
\[
R=3,\quad [z_-,z_+]=[2,4],\quad
\gamma_+=3/4,\quad\gamma_-=3/2,\quad
(\beta_-,\beta_+)=(2/3,4/3).
\]
Thus the lower spacing density diverges as a negative one-third power and the upper density vanishes as a positive one-third power. The supplied standalone script `verify.py` checks all algebraic identities symbolically and solves a separate conservative upwind finite-volume approximation of the stationary three-mode generator. With 4000 cells, the fitted integrated lower and upper edge powers are approximately \(0.68818\) and \(1.32923\), compared with exact values \(2/3\) and \(4/3\). The finite-volume computation is a diagnostic; the statements for all positive parameters follow from the preceding proof, not from the discretization.

## Relationship to prior work

Touzo, Le Doussal and Schehr introduced the active Dyson models, obtained the finite-particle fixed-point structure, and studied singularities of the stationary **one-particle positional density**, including a related exponent based on the full-state escape rate. They did not give the two **spacing-marginal** exponents or the paired sharp transition rates proved here. Their 2023 follow-up focuses on weak-noise position covariance and its large-particle limit.

Le Doussal, Majumdar and Schehr (2021) developed general stationary forward equations for two interacting run-and-tumble particles and explicitly illustrated the repulsive force proportional to \(1/y-y\) in a flow diagram, thereby already identifying the relevant confinement mechanism and possible separate ordering sectors. Their text solves a harmonic attractive example and formulates the general equation without the complete spacing-edge exponent and sharp-rate classification for the repulsive active Dyson interaction. The present proof builds on this mathematical setup rather than claiming the three-state reduction or forward equations as new.

Dhar, Kundu, Majumdar, Sabhapandit and Schehr (2019) describe edge shape transitions for a single two-state run-and-tumble particle in confining potentials; their two-state and single-particle classifications do not provide the unequal pair-spacing exponents of this three-mode repulsive model.

## Limitations

This classification concerns exactly two noncrossing particles, all-to-all logarithmic repulsion, independent symmetric flipping, strictly positive parameters, and zero thermal diffusivity. It does not determine the full normalized spacing density in elementary functions, amplitudes \(C_\pm\) in closed form, joint position fluctuations, or the many-body spacing limit. The threshold values are exact **density-edge** transitions, not thermodynamic phase transitions. Earlier general stationary differential equations make this specialization natural, and an unlocated broader theorem could cover the stated edge asymptotics; publication priority remains subject to independent specialist checking.

## References

1. L. Touzo, P. Le Doussal, G. Schehr, *Interacting, running and tumbling: the active Dyson Brownian motion*, arXiv:2302.02937, first posted 2023-02-06. https://arxiv.org/abs/2302.02937
2. P. Le Doussal, S. N. Majumdar, G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, arXiv:2105.11838, first posted 2021-05-25. https://arxiv.org/html/2105.11838v1
3. L. Touzo, P. Le Doussal, G. Schehr, *Fluctuations in the active Dyson Brownian motion and the overdamped Calogero-Moser model*, arXiv:2307.14306, first posted 2023-07-26. https://arxiv.org/abs/2307.14306
4. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, G. Schehr, *Run-and-tumble particle in one-dimensional confining potentials: Steady-state, relaxation, and first-passage properties*, Physical Review E 99 (2019), 032132. https://doi.org/10.1103/PhysRevE.99.032132
