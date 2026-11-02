# Unique optimal resetting in two random-acceleration level-crossing experiments

## Finding
Consider a randomly accelerated particle with position \(X_t\), velocity \(V_t\), and white-noise acceleration amplitude \(\kappa>0\). At independent Poisson times of rate \(r>0\), *both* position and velocity are returned to a fixed pair. Reset jumps themselves are not counted as crossings. In each of the following two canonical experiments, the stationary intensity of all continuous level crossings is strictly increasing up to exactly one positive resetting rate and strictly decreasing thereafter:

- **Displaced target from rest:** reset to \((X,V)=(0,0)\), count crossings at \(u\ne0\). With \(\tau_u=(|u|/\kappa)^{2/3}\), the unique optimal rate is \(r_* =s_u/\tau_u\), with \(s_u\approx0.520327689493271\) and maximum intensity \(0.104670262107161/\tau_u\).
- **Zero target from a moving start:** reset to \((X,V)=(0,v)\), with \(v\ne0\), and count crossings at zero. With \(\tau_v=v^2/\kappa^2\), the unique optimal rate is \(r_*=s_v/\tau_v\), with \(s_v\approx0.505943004050176\) and maximum intensity \(0.058465882840227/\tau_v\).

The universal numbers above are numerical evaluations of uniquely defined integral roots, not certified numerical enclosures. The exact result is uniqueness and strict unimodality for all admissible physical parameters in both experiments.

## Assumptions and scope
The reset-free excursions satisfy \(dV_t=\kappa\,dW_t\) and \(dX_t=V_t\,dt\), with a standard one-dimensional Brownian motion \(W_t\). After each Poisson reset, a fresh independent excursion starts at the indicated deterministic state. We count total crossings (upward plus downward), not first arrivals, reset discontinuities, or only one crossing orientation. Observation is in the stationary reset-age regime, where the age since the last reset has density \(r e^{-rt}\). In particular, the singular experiment that resets at zero velocity *onto* the counted level is excluded.

## Proof
**1. Reconstruct the exact reset-free crossing kernels.** For a free excursion begun at \((0,v_0)\), the Gaussian pair \((X_t,V_t)\) has means \((v_0t,v_0)\) and covariance data
\[
\operatorname{Var}(X_t)=\frac{\kappa^2t^3}{3},\qquad
\operatorname{Var}(V_t)=\kappa^2t,\qquad
\operatorname{Cov}(X_t,V_t)=\frac{\kappa^2t^2}{2}.
\]
Consequently, at level \(u\), the conditional velocity has mean \(v_0+3(u-v_0t)/(2t)\) and variance \(\kappa^2t/4\). The Kac--Rice crossing intensity is \(h(t)=p_{X_t}(u)\mathbb E[|V_t|\mid X_t=u]\). Using the absolute-Gaussian expectation, put \(C=\sqrt3/(2\pi)\) and obtain
\[
h_u(t)=\frac C t H_u(z),\quad z=\frac{3\tau_u^3}{2t^3},\quad
H_u(z)=e^{-4z}+e^{-z}E_u(z),\quad
E_u(z)=\sqrt{3\pi z}\,\operatorname{erf}(\sqrt{3z}),
\]
for the displaced target, and
\[
h_v(t)=\frac C t H_v(z),\quad z=\frac{\tau_v}{2t},\quad
H_v(z)=e^{-4z}+e^{-3z}E_v(z),\quad
E_v(z)=\sqrt{\pi z}\,\operatorname{erf}(\sqrt z),
\]
for the moving initial state. Both are strictly positive and tend to zero as \(t\downarrow0\) and as \(t\to\infty\); both satisfy \(h(t)\sim C/t\) as \(t\to\infty\).

**2. The two free crossing kernels each have exactly one temporal peak.** The elementary integral representations
\[
E_u(z)=6z\int_0^1e^{-3zq^2}\,dq,\qquad E_v(z)=2z\int_0^1e^{-zq^2}\,dq
\]
show, for every \(z>0\), that \(E_j'(z)/E_j(z)\le1/z\). Direct differentiation gives
\[
\frac d{dz}\bigl[z^{1/3}H_u(z)\bigr]
=z^{-2/3}G_u(z),\quad
G_u(z)=\left(\frac13-z\right)e^{-4z}
+\left(\frac56-z\right)e^{-z}E_u(z),
\]
and
\[
\frac d{dz}\bigl[zH_v(z)\bigr]=G_v(z),\quad
G_v(z)=(1-3z)e^{-4z}+
\left(\frac32-3z\right)e^{-3z}E_v(z).
\]
The first \(G_u\) is strictly positive for \(z\le1/3\) and strictly negative for \(z\ge5/6\). Between these endpoints its sign is the sign of \(P_u(z)-1\), where
\[
P_u(z)=\frac{E_u(z)e^{3z}(5/6-z)}{z-1/3}.
\]
On \((1/3,5/6)\),
\[
\frac d{dz}\log P_u(z)
\le3+\frac1z-\frac1{5/6-z}-\frac1{z-1/3}
<6-8<0.
\]
Here the reciprocal sum is at least \(8\), since the two positive denominators add to \(1/2\). Furthermore \(P_u\) drops continuously from infinity to zero, so \(G_u\) changes sign exactly once, from positive to negative as \(z\) increases. The same argument works for \(G_v\): it is positive for \(z\le1/3\), negative for \(z\ge1/2\), and on \((1/3,1/2)\) its sign equals that of
\[
P_v(z)-1,\qquad P_v(z)=\frac{E_v(z)e^z(3/2-3z)}{3z-1}.
\]
In this interval,
\[
\frac d{dz}\log P_v(z)
\le1+\frac1z-\frac1{1/2-z}-\frac1{z-1/3}
<4-24<0,
\]
with \(P_v\) decreasing from infinity to zero. Since the corresponding \(z\) decreases strictly with \(t\), both \(h_u(t)\) and \(h_v(t)\) strictly increase to one maximum and then strictly decrease. The exact peak roots are \(z_u\in(1/3,5/6)\), \(z_v\in(1/3,1/2)\); numerical values are \(z_u\approx0.817916335964687\), \(z_v\approx0.421583690024671\).

**3. A one-peaked free kernel gives a uniquely optimal Poisson clock.** Let \(h\) be either of these free intensities and \(t_0\) its unique peak time. The renewal identity for continuous crossings gives
\[
J(r)=r\int_0^\infty e^{-rt}h(t)\,dt,
\qquad J'(r)=-\int_0^\infty t e^{-rt}h'(t)\,dt.
\]
The integration by parts has vanishing boundary terms because \(h(t)\to0\) as \(t\downarrow0\) and \(h(t)\sim C/t\) as \(t\to\infty\). Define
\[
A(r)=\int_0^{t_0}t h'(t)e^{-rt}\,dt>0,\qquad
B(r)=\int_{t_0}^\infty -t h'(t)e^{-rt}\,dt>0.
\]
Thus \(J'=B-A\). The logarithmic derivative of \(A/B\) equals the difference between the exponentially tilted mean times on \((t_0,\infty)\) and \((0,t_0)\), hence is strictly positive. Also, \(A(r)/B(r)\to0\) as \(r\downarrow0\), since \(A(0)<\infty\) while \(B(r)\to\infty\) logarithmically, using \(-t h'(t)\sim C/t\). As \(r\to\infty\), \(A/B\to\infty\), by bounding a positive contribution from a fixed interval strictly below \(t_0\) against the exponentially smaller whole upper tail above \(t_0\). Therefore \(J'\) changes sign exactly once, from positive to negative. Since \(J\to0\) at both zero and infinite reset rate, this point is the unique strict global maximum.

**4. Fix the optimal dimensionless constants.** The exact roots \(s_u,s_v>0\) are the respective unique zeros of the derivatives of
\[
F_u(s)=Cs\int_0^\infty\frac{e^{-s\theta}}\theta
H_u\left(\frac3{2\theta^3}\right)\,d\theta,
\qquad
F_v(s)=Cs\int_0^\infty\frac{e^{-s\theta}}\theta
H_v\left(\frac1{2\theta}\right)\,d\theta.
\]
The physical stationary intensities are \(J_u(r)=F_u(r\tau_u)/\tau_u\) and \(J_v(r)=F_v(r\tau_v)/\tau_v\). Strict uniqueness already follows analytically; quadrature only supplies the displayed decimal approximations.

## Verification
The analytic sign inequalities establish uniqueness for the complete positive parameter domain. The companion `verify.py` independently reconstructs the two conditional Gaussian crossing rates, differentiates the error-function kernels numerically, checks strict sign changes around the two free-kernel peaks, and solves the two dimensionless Laplace derivative equations with high-precision quadrature. Its numerical checks corroborate the calculations but are not substituted for the global proof.

## Relationship to prior work
Masoliver and Palassini (2023), arXiv:2301.06608, derive the reset-free Gaussian level-crossing intensity. Singh (2020), arXiv:2007.05576, studies joint stationary distributions and first-passage properties under complete or partial resetting, not the present total crossing-rate optimization. Montero, Palassini and Masoliver (first public preprint December 21, 2023; journal 2024), arXiv:2312.13968, derive the Poisson-reset crossing intensity and the scaling integrals in their equations (16), (25), and (33); they numerically exhibit an optimum and discuss asymptotics. Their sections IV.1.1--IV.1.2 and appendices do not present an all-rate uniqueness proof for either scaling integral or the two dimensionless maximizing constants. The present refinement proves the complete global optimizer structure for both cases via explicit one-crossing sign inequalities. General Laplace-transform variation-diminishing principles are established tools; the model-specific one-peak inequalities and their application, not the general principle itself, are the claimed contribution.

## Limitations
The classification is restricted to full Poisson resetting of both position and velocity in the two specified undamped, Gaussian random-acceleration experiments. It does not establish unique optima for arbitrary reset states, damped inertial Brownian motion, directional rather than total crossing counts, non-Poisson clocks, or first-passage-time optimization. Decimal constants are reproducible quadrature approximations and not formal interval certificates. A broader previously published theorem could conceivably subsume the optimization; definitive publication priority and independent validation remain open.

## References
1. M. Montero, M. Palassini, J. Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes*, arXiv:2312.13968 (first public December 21, 2023); Physical Review E **110**, 014116 (2024), https://arxiv.org/abs/2312.13968 , https://doi.org/10.1103/PhysRevE.110.014116 .
2. J. Masoliver, M. Palassini, *Counting of level crossings for inertial random processes: Generalization of the Rice formula*, arXiv:2301.06608 (2023), https://arxiv.org/abs/2301.06608 .
3. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576 (2020), https://arxiv.org/abs/2007.05576 .
