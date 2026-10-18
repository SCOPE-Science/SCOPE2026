# Sharp correlation envelope for the stochastic SIRS weak-noise covariance

## Finding
Consider the stable endemic equilibrium of the stochastic SIRS model of Huang, Du, and Liang (2026) at the baseline parameters
\[
(\Lambda,\mu,\beta,\epsilon_d,\gamma,\delta,\alpha,\sigma_1,\sigma_2,\sigma_3)
=(1,0.2,0.1,0.05,0.1,0.25,0.001,0.6,0.8,0.7).
\]
Here \(\epsilon_d\) denotes disease mortality, distinct from the overall small-noise amplitude. For every positive semidefinite three-dimensional Brownian correlation matrix \(R=(\rho_{ij})\) with \(\rho_{ii}=1\), let \(W(R)\) be the first-order stationary covariance of the linearized model, defined by
\[
FW+WF^\top+GRG^\top=0,
\]
where \(F\) is the Jacobian at the stable endemic equilibrium and
\(G=-\operatorname{diag}(\sigma_1S^*,\sigma_2I^*,\sigma_3R^*)\).
Then the total sensitivity variance has the affine representation
\[
\boxed{\operatorname{tr}W(R)
=17.274750562409+5.395303120131\rho_{12}
+0.537604148434\rho_{13}+0.152951296895\rho_{23}},
\]
where the displayed decimals are numerical approximations to uniquely specified analytic Lyapunov solutions, not exact rational constants. The sharp range over **all** correlation matrices is
\[
\boxed{11.494794590740\ \leq\ \operatorname{tr}W(R)\ \leq\ 23.360609127869}.
\]
The unique maximizing correlation pattern is \((\rho_{12},\rho_{13},\rho_{23})=(1,1,1)\). The minimizing pattern is \((-1,-1,1)\); both endpoints are valid rank-one correlation matrices. At fixed marginal noise intensities, the ratio of the two endpoints is approximately \(2.032\).

**Priority boundary.** The correct correlated-noise covariance forcing \(GRG^\top\), and its identification as the correction to a doubled-variance expression in Remark 3.8 of Huang, Du, and Liang, were published earlier as *The correlated-noise sensitivity formula double-counts Brownian variance* (Resultary, 2026-10-04). Neither the general Itô formula nor that correction is claimed as new here. The distinct claim in this note is the **sharp, model-specific, all-correlation trace envelope** for the source's numerical baseline.

## Scope
The result concerns the first-order local stochastic-sensitivity approximation at the model's stable endemic equilibrium. The scalar being optimized is trace, not determinant or individual principal-axis lengths; it is not the true nonlinear stationary covariance under finite-amplitude noise. Singular covariance drivers are permitted, and the extrema are approached by positive-definite correlation matrices if strict positivity is required. This is an exact optimization of the *linearized* covariance for the fixed baseline, not a universal model-independent stochastic epidemic theorem.

## Proof and verification
With the incidence function \(\beta SI/(1+\alpha I^2)\), the deterministic equilibrium satisfies
\[
S^*=\frac{(\mu+\gamma+\epsilon_d)(1+\alpha(I^*)^2)}{\beta},
\qquad R^*=\frac{\gamma}{\mu+\delta}I^*.
\]
Substitution into the susceptible balance yields a scalar polynomial with a unique positive endemic root at this baseline. Direct evaluation gives
\[
(S^*,I^*,R^*)=(3.50361582597,1.01641189180,0.225869309288)+O(10^{-11})
\]
and the drift Jacobian
\[
F\approx \begin{pmatrix}
-0.301536293&-0.349277581&0.25\\
0.101536293&-0.000722419&0\\
0&0.1&-0.45
\end{pmatrix}.
\]
Its eigenvalues have real parts approximately \(-0.166016513,-0.166016513,-0.420225686\), establishing the required Hurwitz property (alternatively, one can check the cubic Routh-Hurwitz inequalities directly at the isolated equilibrium root). Therefore the Lyapunov covariance and the adjoint matrix \(P\) solving
\[
F^\top P+PF+I_3=0
\]
are unique. Cyclicity of trace gives
\[
\operatorname{tr}W(R)=\operatorname{tr}(PGRG^\top)=\operatorname{tr}(HR),
\qquad H=G^\top PG.
\]
Direct linear algebra at the uniquely determined baseline equilibrium gives
\[
H\approx\begin{pmatrix}
9.676088414&2.697651560&0.268802074\\
2.697651560&7.559654500&0.076475648\\
0.268802074&0.076475648&0.039007648
\end{pmatrix},
\]
which proves the affine trace coefficients to the stated precision.

For sharpness, represent an arbitrary correlation matrix as the Gram matrix of three unit vectors \(u_1,u_2,u_3\). Set \(x=u_1\cdot u_2\), \(y=u_1\cdot u_3\), \(z=u_2\cdot u_3\), and write the positive off-diagonal coefficients as \(a,b,c\), respectively, where
\[
(a,b,c)\approx(5.395303120131,0.537604148434,0.152951296895).
\]
All three dot products are at most one, and all simultaneously equal one, proving the maximum \(\operatorname{tr}H+a+b+c\). For the minimum, fixing \(u_1,u_2\) with dot product \(x\), optimization over \(u_3\) reduces the off-diagonal term to
\[
 a x-\sqrt{b^2+c^2+2bcx},\qquad -1\le x\le1.
\]
Its derivative is \(a-bc/\sqrt{b^2+c^2+2bcx}\). Here the certified strict inequality \(a>bc/(b-c)\) applies because \(b>c>0\); thus the derivative is positive throughout the interval. The minimizing \(x=-1\) forces \(u_2=-u_1\). As \(b>c\), the optimal third unit vector is \(u_3=-u_1\), giving \((x,y,z)=(-1,-1,1)\) and minimum \(\operatorname{tr}H-a-b+c\). This also certifies attainability rather than just bounds.

An independent calculation reconstructs the equilibrium, Jacobian and Hurwitz eigenvalues from the model drift, solves the two continuous Lyapunov equations, and checks the exact Gram-vector reduction and strict coefficient ordering; the displayed equations independently determine all coefficients and inequalities. The numerical constants are approximate; the analytic construction and inequalities constitute the mathematical claim.

## Relationship to earlier literature
Huang, Du, and Liang, *Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model* (AIMS Mathematics 11 (2026), 6720--6743; DOI 10.3934/math.2026278), formulate independent-noise stochastic sensitivity and state a correlated-noise extension in Remark 3.8. Their Eq. (4.4) gives the baseline independent covariance, but they do not optimize trace over the correlation elliptope.

*The correlated-noise sensitivity formula double-counts Brownian variance* (Resultary/2026, published 2026-10-04) already establishes that the correlated covariance forcing is \(GRG^\top\) and that the printed source expression duplicates the independent marginal forcing. Those parts are **prior work**; the present contribution neither rediscovers nor claims independent priority for them. The earlier note does not calculate the present baseline's affine trace law, coefficient inequalities, extrema, or range.

Cai, Cai and Mao (2019), DOI 10.1007/s11071-019-05114-2, examine a different correlated-noise SIS epidemic model; Yuan, Wu, Lan and Wang (2020), DOI 10.1007/s11538-020-00733-y, present stochastic-sensitivity covariance for a producer-grazer model. Neither source supplies this fixed SIRS trace optimization. General linear-SDE covariance identities and the Gram representation of correlations are standard inputs, not novel conclusions.

## Limitations
The fixed-baseline trace optimization is model-specific, is not a general-purpose theorem on all stochastic epidemiological systems, and does not optimize ellipsoid orientation. Other correlation-sensitive quantities can have different extremizers. The dependence on a rounded numerical parameter baseline gives scientifically useful exact optimization with numerically reported coefficients; it does not establish inference accuracy outside the small-noise regime. An unindexed same-baseline numerical analysis remains a residual literature risk.

## References
1. J. Huang, J. Du, H. Liang, *Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model*, AIMS Mathematics **11** (2026), 6720--6743. DOI: 10.3934/math.2026278.
2. *The correlated-noise sensitivity formula double-counts Brownian variance*, Resultary/2026, publication date 2026-10-04, `2026/10/4/SCOPE-the-correlated-noise-sensitivity-formula-double-counts-brownian--645774f4d661/RESULT.md`.
3. S. Cai, Y. Cai, X. Mao, *A stochastic differential equation SIS epidemic model with two correlated Brownian motions*, Nonlinear Dynamics **97** (2019), 2175--2187. DOI: 10.1007/s11071-019-05114-2.
4. S. Yuan, D. Wu, G. Lan, H. Wang, *Noise-Induced Transitions in a Nonsmooth Producer--Grazer Model with Stoichiometric Constraints*, Bulletin of Mathematical Biology **82** (2020), 55. DOI: 10.1007/s11538-020-00733-y.
