# Correct characteristic factor and first delay crossing in an awareness-mediated epidemic model
## Finding
For the positive endemic equilibrium of the delayed SEQIJR epidemic model studied by Maji, Al Basir, Mukherjee, Nisar and Ravichandran, the incidence term depends simultaneously on the current infectious population and the delayed infectious population. Writing
\[
C=c+\mu,\qquad G=\gamma+\mu,\qquad L=\lambda+\mu+d_1,
\]
\[
u=\beta e^{-mI_*}I_*,\qquad v=\beta e^{-mI_*}S_*,
\]
the endemic equilibrium identities imply \(cp\gamma v=CGL\). A direct linearization of the printed nonlinear model gives the exact nontrivial characteristic factor
\[
F(\xi,\tau)=(\xi+C)(\xi+G)(\xi+L)(\xi+\mu+u)+CGL(\xi+\mu)\bigl(mI_*e^{-\xi\tau}-1\bigr).
\]
The removed compartment contributes only the stable factor \(\xi+d_2+\mu\).

For the source's parameter set
\[
(r,\beta,m,\mu,d_1,d_2,c,p,\gamma,\lambda)=(40,0.0025,0.2,0.01,0.1,0.1,0.6,0.6,0.02,0.1),
\]
the corrected endemic equilibrium has
\[
I_*=13.646976755456900\ldots,\qquad S_*=3271.592615677488\ldots.
\]
The corrected characteristic equation is Hurwitz at zero delay. It has one positive imaginary-axis frequency,
\[
\theta_*=0.06652293610984329\ldots,
\]
and its first positive-delay crossing is
\[
\tau_*=18.59248621759530\ldots.
\]
At the crossing,
\[
\operatorname{Re}\left(\frac{d\xi}{d\tau}\right)=0.001262757946267497\ldots>0,
\]
so the endemic equilibrium first loses linear stability there.

The published linearization places the current-infectious derivative of the incidence into the delayed matrix. That merger is valid after setting \(\tau=0\), but not for a positive delay. Consequently the paper's displayed characteristic equation and its subsequent analytic delay-crossing formulas do not follow from the printed nonlinear model. The corrected threshold nevertheless agrees qualitatively with the paper's numerical bifurcation transition near delays \(18\)--\(19\).

## Assumptions and scope
All parameters are positive and the calculation concerns the positive endemic equilibrium of the exact delay system printed in the source. The delay \(\tau\) occurs only through the awareness factor \(e^{-mI(t-\tau)}\). The claim is local and spectral: it identifies the characteristic equation and the first loss of linear stability. It does not prove existence, direction, or orbital stability of a nonlinear Hopf branch, and it does not assert instability for every larger delay.

## Proof
Let \(s,e,q,i\) denote perturbations of \(S,E,Q,I\). Differentiating the incidence \(\beta e^{-mI(t-\tau)}S(t)I(t)\) at the endemic equilibrium gives the three independent first-order contributions
\[
u s(t)+v i(t)-m v I_* i(t-\tau).
\]
Therefore the current-state linearization in the first four coordinates is
\[
A=\begin{pmatrix}
-(u+\mu)&0&0&-v\\
u&-C&0&v\\
0&c&-G&0\\
0&0&p\gamma&-L
\end{pmatrix},
\]
and the delayed matrix has only
\[
B_{14}=m v I_*,\qquad B_{24}=-m v I_*.
\]
The endemic chain gives \(cp\gamma v=CGL\). Expanding \(\det(\xi I-A-e^{-\xi\tau}B)\) and using that balance yields
\[
(\xi+C)(\xi+G)(\xi+L)(\xi+\mu+u)-CGL(\xi+\mu)+CGLmI_*(\xi+\mu)e^{-\xi\tau},
\]
which is the stated factor.

Write it as
\[
P(\xi)+e^{-\xi\tau}(q_1\xi+q_0),
\]
where
\[
P(\xi)=\xi^4+p_1\xi^3+p_2\xi^2+p_3\xi+p_4,\qquad q_1=CGLmI_*,\qquad q_0=\mu q_1.
\]
At the source parameters,
\[
(p_1,p_2,p_3,p_4)=(0.8622264611456573\ldots,0.1630924919738087\ldots,0.001866980616941863\ldots,0.000008556290182760837\ldots),
\]
\[
(q_1,q_0)=(0.01048906633424417\ldots,0.0001048906633424417\ldots).
\]
If \(\xi=i\theta\) and \(z=\theta^2\), eliminating the phase gives
\[
z^4+(p_1^2-2p_2)z^3+(p_2^2+2p_4-2p_1p_3)z^2+(p_3^2-2p_2p_4-q_1^2)z+(p_4^2-q_0^2)=0.
\]
Its coefficient signs are \(+,+,+,-,-\), so Descartes' rule gives at most one positive root; the negative constant term and positive leading coefficient give at least one. Hence there is exactly one positive frequency. Numerically,
\[
z_*=0.004425301028674292\ldots,\qquad \theta_*=\sqrt{z_*}=0.06652293610984329\ldots.
\]
Writing
\[
R_1=p_1\theta^3-p_3\theta,\qquad R_2=-\theta^4+p_2\theta^2-p_4,
\]
the phase equations give
\[
\cos(\theta\tau)=\frac{q_1\theta R_1+q_0R_2}{q_1^2\theta^2+q_0^2},\qquad
\sin(\theta\tau)=\frac{-q_0R_1+q_1\theta R_2}{q_1^2\theta^2+q_0^2}.
\]
For \(\theta=\theta_*\), these are \(0.3277958316911819\ldots\) and \(0.9447485870462503\ldots\), giving the first phase \(1.236826772776234\ldots\) and therefore \(\tau_*=18.59248621759530\ldots\).

At zero delay the quartic coefficients satisfy the strict Routh--Hurwitz inequalities. There is no zero root for any delay, and the unique positive imaginary frequency has no crossing before \(\tau_*\). Standard continuity of the retarded spectrum therefore gives linear asymptotic stability up to that first crossing. Implicit differentiation of \(F(\xi,\tau)=0\) gives
\[
\frac{d\xi}{d\tau}=\frac{\xi e^{-\xi\tau}(q_1\xi+q_0)}{4\xi^3+3p_1\xi^2+2p_2\xi+p_3+e^{-\xi\tau}\left[q_1-\tau(q_1\xi+q_0)\right]},
\]
whose real part at \((i\theta_*,\tau_*)\) is strictly positive as stated.

## Verification
A standalone numerical checker accompanies this result. It reconstructs the endemic equilibrium from the printed parameters, derives the corrected coefficients, verifies the one-sign-change frequency polynomial, checks the zero-delay Routh--Hurwitz determinants, evaluates \(F(i\theta_*,\tau_*)\), and recomputes the crossing derivative. The direct characteristic residual is below \(10^{-12}\) in ordinary double precision.

The source's own numerical bifurcation figure places the transition between approximately \(18\) and \(19\), which is consistent with the corrected \(18.592486\ldots\) value even though its displayed analytic characteristic construction is not the linearization of the printed delay model.

## Relationship to prior work
The motivating paper introduces the delayed awareness-modulated SEQIJR model, prints the current/delayed matrices, develops a characteristic equation and Hopf-delay calculation, and supplies the numerical bifurcation plot. Direct comparison shows that its matrix decomposition merges the current \(I(t)\) derivative with the delayed \(I(t-\tau)\) derivative. The result here replaces that step by the exact linearization and derives the first crossing from the corrected factor.

A closely related earlier paper by Basir, Ray and Venturino studies awareness/media delays in a different SIS-type epidemic system. Its full model and stability setup were inspected. It neither has the same SEQIJR infection chain nor implies the characteristic factor above.

Targeted searches by exact title, DOI, characteristic-equation terminology, Hopf terminology, and correction/erratum terminology found the source and citing literature but no source-specific correction of this current-versus-delayed derivative merger. This negative search evidence is not a proof of exhaustive novelty.

## Limitations
The calculation is a local spectral correction, not a nonlinear bifurcation theorem. It does not determine the first Lyapunov coefficient, the stability of any periodic orbit, or the global epidemic dynamics. It also does not claim that the equilibrium remains unstable for all delays above \(\tau_*\); only the first stability loss is proved. The numerical constants are reproducible certificates for the source parameter set, while the characteristic factor itself is symbolic and parameter-exact.

## References
1. C. Maji, F. Al Basir, D. Mukherjee, K. S. Nisar, C. Ravichandran, “COVID-19 propagation and the usefulness of awareness-based control measures: A mathematical model with delay,” *AIMS Mathematics* 7 (2022), 12091–12105. DOI: 10.3934/math.2022672.
2. F. A. Basir, S. Ray, E. Venturino, “Role of media coverage and delay in controlling infectious diseases: A mathematical model,” *Applied Mathematics and Computation* 337 (2018), 372–385. DOI: 10.1016/j.amc.2018.05.042.
