# Neutral strain continua and sharp exchange damping in a delayed two-virus model

## Finding

For the seven-compartment, three-stage-per-virus delayed infection model of Elaiw, Alsaadi and Hobiny [1], restrict to strains with equal kinetic and delay parameters, and retain a common saturation strength \(\psi\geq0\). Define the positive constants \(r,\mu_I,\mu_V,\delta,\theta,\gamma,\eta_H,\phi\), the total maturation delay \(\tau\), the survival factor \(s\), and the effective equilibrium infection scale \(K\) precisely below. Suppose that
\[
\mathcal R=\frac{\phi\gamma}{\eta_HK}>1.
\]

**A neutral continuum at zero saturation.** For \(\psi=0\), all infection-positive equilibria belong to an explicit closed line segment: \(H=K/\gamma\) and \(C+B=T\), where
\[
T=\frac{\phi\gamma-\eta_HK}{\gamma K}>0.
\]
The remaining four infected coordinates are positive constant multiples of their respective viral coordinates \(C\) or \(B\). Every interior point \(0<C<T\), \(B=T-C\), is a two-strain coexistence equilibrium. The segment endpoints are the single-strain equilibria.

**Selection of a single coexistence state by saturation.** For every \(\psi>0\) there is exactly one strictly positive two-strain equilibrium, with
\[
C=B=v_\psi=\frac{\phi\gamma-\eta_HK}{K(2\gamma+\eta_H\psi)},
\qquad H=\frac{K}{\gamma}(1+\psi v_\psi).
\]
As \(\psi\downarrow0\), this equilibrium tends to the midpoint \(C=B=T/2\) of the neutral segment.

**Exact exchange spectrum, monotonicity, and singular rate.** Linearize at this symmetric equilibrium, and restrict to perturbations antisymmetric under interchange of the two virus labels. Their characteristic roots are exactly the zeros of
\[
F(\lambda,\psi)=(\lambda+r)(\lambda+\mu_I)(\lambda+\mu_V)
-\frac{r\mu_I\mu_V}{1+\psi v_\psi}e^{-\lambda\tau}.
\]
For every \(\psi\geq0\), the rightmost antisymmetric characteristic root \(\lambda_\psi\) is real, simple, and unique on its spectral boundary. It equals zero at \(\psi=0\); for every \(\psi>0\) it lies strictly in \((-\min\{r,\mu_I,\mu_V\},0)\), and it is strictly decreasing as a function of \(\psi\). In particular, with \(v_0=T/2\),
\[
\boxed{\lambda_\psi=-\frac{r\mu_I\mu_Vv_0}{r\mu_I+r\mu_V+\mu_I\mu_V+r\mu_I\mu_V\tau}\,\psi+O(\psi^2)
\quad\text{as }\psi\downarrow0.}
\]
Thus the antisymmetric **linear** relaxation time diverges proportionally to \(\psi^{-1}\) as saturation disappears. The explicit coefficient retains the total three-stage delay, rather than replacing the delayed infection chain by an instantaneous one.

## Assumptions and scope

All kinetic constants are strictly positive, delay lengths are nonnegative, and the solution state is nonnegative. The source's compartments are \((H,L,Y,E,Z,C,B)\), where \((L,Y,C)\) and \((E,Z,B)\) denote successive stages for two viral strains. Make the strain-symmetry restrictions
\[
\eta_L=\eta_E=\mu_L,\quad \delta_L=\delta_E=\delta,\quad
\eta_Y=\eta_Z=\mu_I,\quad\eta_C=\eta_B=\mu_V,
\]
\[
\theta_C=\theta_B=\theta,\quad \gamma_{HC}=\gamma_{HB}=\gamma,\quad
\psi_C=\psi_B=\psi,
\]
\[
(\omega_1,\omega_2,\omega_3)=(\omega_4,\omega_5,\omega_6),\qquad
(\alpha_1,\alpha_2,\alpha_3)=(\alpha_4,\alpha_5,\alpha_6).
\]
Put \(r=\mu_L+\delta\), \(\tau=\omega_1+\omega_2+\omega_3\),
\[
s=\exp\left(-\sum_{j=1}^{3}\alpha_j\omega_j\right),\qquad
K=\frac{r\mu_I\mu_V}{s\delta\theta}.
\]
Using a dot for the time derivative and a subscript \(\omega\) for evaluation at \(t-\omega\), the equations are
\[
\begin{aligned}
\dot H&=\phi-\eta_HH-\gamma H\left(\frac{C}{1+\psi C}+\frac{B}{1+\psi B}\right),\\
\dot L&=e^{-\alpha_1\omega_1}\gamma\frac{H_{\omega_1}C_{\omega_1}}{1+\psi C_{\omega_1}}-rL,\\
\dot Y&=e^{-\alpha_2\omega_2}\delta L_{\omega_2}-\mu_IY,\\
\dot C&=e^{-\alpha_3\omega_3}\theta Y_{\omega_3}-\mu_VC,\\
\dot E&=e^{-\alpha_1\omega_1}\gamma\frac{H_{\omega_1}B_{\omega_1}}{1+\psi B_{\omega_1}}-rE,\\
\dot Z&=e^{-\alpha_2\omega_2}\delta E_{\omega_2}-\mu_IZ,\\
\dot B&=e^{-\alpha_3\omega_3}\theta Z_{\omega_3}-\mu_VB.
\end{aligned}
\]
These equations are exactly the pairwise-identical-parameter specialization of [1, (2.1)–(2.7)]; the zero-saturation case is permitted in [1, p. 13774]. All statements above concern equilibrium geometry and **linearized exchange modes**, not the global convergence rate or full stability spectrum of the seven-component system.

## Proof

**Equilibrium elimination.** For any equilibrium with viral concentration \(v>0\), the associated latent and infected stages satisfy
\[
L_v=\frac{e^{-\alpha_1\omega_1}K}{r}v,
\qquad Y_v=\frac{e^{-\alpha_2\omega_2}\delta}{\mu_I}L_v,
\qquad v=\frac{e^{-\alpha_3\omega_3}\theta}{\mu_V}Y_v.
\]
The final equality follows from the definition of \(K\), and the first follows because the infection flux equals \(Kv\) at equilibrium. Multiplying the three stage balances and cancelling the positive viral concentration yields
\[
\gamma H/(1+\psi v)=K. \tag{1}
\]
When both strains are positive, (1) holds for \(v=C\) and \(v=B\). If \(\psi>0\), equality of the right-hand sides forces \(C=B\); if \(\psi=0\), it forces only \(H=K/\gamma\). Substituting the flux identity \(\gamma H v/(1+\psi v)=Kv\) into the \(H\)-balance gives
\[
\phi-\eta_HH-K(C+B)=0. \tag{2}
\]
Equations (1)–(2) prove the asserted continuum and the unique positive symmetric equilibrium, including all its remaining stage coordinates. Conversely, substituting any listed equilibrium into each of the seven right-hand sides gives zero, so no candidate is merely formal. For \(\psi=0\), a positive pair \((C,B)\) exists because \(T>0\), and its closure includes the two endpoints. For \(\psi>0\), the explicit \(v_\psi\) is positive because \(\mathcal R>1\).

**Exchange-mode linearization.** At the symmetric equilibrium write \(u=L-E\), \(w=Y-Z\), \(z=C-B\). Interchanging strain labels preserves the vector field; hence the antisymmetric tangent subspace has zero \(H\)-perturbation and is invariant under linearization. On this subspace,
\[
\dot u=-ru+e^{-\alpha_1\omega_1}\frac{\gamma H}{(1+\psi v_\psi)^2}z_{\omega_1},\quad
\dot w=-\mu_Iw+e^{-\alpha_2\omega_2}\delta u_{\omega_2},\quad
\dot z=-\mu_Vz+e^{-\alpha_3\omega_3}\theta w_{\omega_3}.
\]
A nonzero exponential mode has characteristic equation
\[
(\lambda+r)(\lambda+\mu_I)(\lambda+\mu_V)
=\frac{s\gamma H\delta\theta}{(1+\psi v_\psi)^2}e^{-\lambda\tau}
=\frac{r\mu_I\mu_V}{1+\psi v_\psi}e^{-\lambda\tau},
\]
using (1) and the definition of \(K\).

**Rightmost-root and strict damping proof.** Set \(m=\min\{r,\mu_I,\mu_V\}\), \(g(\psi)=r\mu_I\mu_V/(1+\psi v_\psi)\), and for real \(x>-m\) write
\[
q_\psi(x)=(x+r)(x+\mu_I)(x+\mu_V)-g(\psi)e^{-x\tau}.
\]
All three factors are positive there, and \(q'_\psi(x)>0\). Moreover \(q_\psi(-m)<0\), whereas \(q_\psi(0)=r\mu_I\mu_V-g(\psi)\ge0\), with equality only at \(\psi=0\). Thus there is exactly one simple real root \(\lambda_\psi\) in \((-m,0]\), and it is zero exactly when \(\psi=0\). If a complex characteristic root \(z\) has \(\operatorname{Re}z>-m\), take absolute values to obtain
\[
\prod_{a\in\{r,\mu_I,\mu_V\}}(\operatorname{Re}z+a)
\le\prod_a|z+a|=g(\psi)e^{-\tau\operatorname{Re}z},
\]
which implies \(\operatorname{Re}z\le\lambda_\psi\). Equality is impossible when \(\operatorname{Im}z\ne0\). Roots with real part at most \(-m\) are automatically further left. Therefore \(\lambda_\psi\) is the unique rightmost characteristic root, even for arbitrary finite delays.

Finally \(\psi v_\psi=(\phi\gamma-\eta_HK)\psi/[K(2\gamma+\eta_H\psi)]\) is strictly increasing in \(\psi\ge0\). Consequently \(g(\psi)\) strictly decreases, and strict monotonicity of \(q_\psi\) implies that \(\lambda_\psi\) strictly decreases. The implicit-function theorem at \((\lambda,\psi)=(0,0)\), where
\[
\partial_\lambda F=r\mu_I+r\mu_V+\mu_I\mu_V+r\mu_I\mu_V\tau>0,
\qquad \partial_\psi F=r\mu_I\mu_Vv_0>0,
\]
gives the displayed expansion, with a genuinely positive coefficient. This also proves that the eigenvalue zero is simple at zero saturation and its eigenvector is tangent to the neutral equilibrium segment.

## Verification

The algebraic identities (1)–(2) and the characteristic determinant admit direct substitution checks, and the strict rightmost-root comparison above does not rely on a finite-dimensional approximation of the delay equation. The accompanying `CHECK.py` evaluates all seven equilibrium residuals for a delayed sample, checks several characteristic residuals and the strict ordering of their real roots, and confirms the leading small-saturation coefficient numerically. Execute `python CHECK.py`; the expected final line is `CHECK_OK`. These finite numerical checks serve only as reproducibility aids; the proof for all positive parameters and arbitrary nonnegative delays is analytic.

## Relationship to prior work

Elaiw, Alsaadi and Hobiny [1] introduced the seven-state delayed saturated-incidence model, derived explicit equilibria, and proved global stability in parameter regions. Their Section 2.3 and concluding discussion emphasize a finite equilibrium list and coexistence induced by saturation, but do not give the neutral zero-saturation continuum on the symmetry surface or the exact delayed exchange characteristic root and its \(\psi\)-dependent asymptotics. Our result neither disputes their nondegenerate saturated coexistence theorem nor reclaims that theorem. Kogan et al. [2] already analyze neutral coexistence lines in different stochastic SIS/SIR strain-competition systems; the *general concept* of neutral competition is consequently not claimed as new. Their models have neither this three-stage delayed viral chain nor this exact saturation-controlled exchange spectrum. Nurtay et al. [3] treat mutation-mediated coexistence and complicated bifurcations in a different viral-strain model, rather than the no-mutation, delayed weak-saturation limit here.

## Limitations

The strict parameter symmetry is essential for exact decoupling of the exchange mode; near-symmetric unequal strains are not analyzed. The \(\psi^{-1}\) statement concerns a **linearized antisymmetric relaxation time**, not the nonlinear equilibration time of an arbitrary initial condition, nor stochastic fixation. No new global stability assertion is made. The neutral line at \(\psi=0\) is non-hyperbolic, so it has no isolated asymptotically stable equilibrium in the full space; the proof does not classify global basins or all characteristic roots of the symmetric sector. The first source's threshold and coexistence conclusions away from the equal-strain boundary are not contradicted.

## References

1. A. M. Elaiw, G. S. Alsaadi and A. D. Hobiny, *Global co-dynamics of viral infections with saturated incidence*, AIMS Mathematics **9** (2024), 13770–13818, DOI: 10.3934/math.2024671. Source equations (2.1)–(2.7), equilibrium Section 2.3, p. 13774 admissible zero saturation, and concluding Section 6. https://www.aimspress.com/aimspress-data/math/2024/6/PDF/math-09-06-671.pdf
2. O. Kogan, M. Khasin, B. Meerson, D. Schneider and C. R. Myers, *Two-strain competition in quasineutral stochastic disease dynamics*, Physical Review E **90** (2014), 042149, DOI: 10.1103/PhysRevE.90.042149. https://cac.cornell.edu/myers/papers/PhysRevE.90.042149.pdf
3. A. Nurtay, M. G. Hennessy, J. Sardanyés, L. Alsedà and S. F. Elena, *Theoretical conditions for the coexistence of viral strains with differences in phenotypic traits: a bifurcation analysis*, Royal Society Open Science **6** (2019), 181179, DOI: 10.1098/rsos.181179.
