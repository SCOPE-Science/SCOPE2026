# Gaussian covariance twins and displacement-only identification of Poisson-rethermalized Ornstein–Uhlenbeck motion

## Finding
Let an equilibrium Gaussian velocity be continuously damped and driven by thermal Brownian forcing, and independently *rethermalized* at Poisson times by an entirely new equilibrium Gaussian draw. Although **all its stationary velocity and displacement second-order correlations agree with those of an ordinary Gaussian Ornstein–Uhlenbeck process of a faster effective relaxation rate**, the displacement has a strictly positive fourth cumulant at every positive observation time. Two displacement variances and one displacement fourth cumulant from a freely chosen pair of windows identify the OU damping rate, the Poisson collision rate, and the thermal velocity scale, with no velocity or collision observations.

For \(\lambda=\gamma+r\), write
\[
B_\lambda(T)=\frac{2(\lambda T-1+e^{-\lambda T})}{\lambda^2},\qquad
J_\lambda(L)=\int_0^L q(L-q)e^{-\lambda q}\,dq
=\frac{\lambda L-2+(\lambda L+2)e^{-\lambda L}}{\lambda^3}.
\]
Then the exact displacement variance and fourth cumulant are
\[
\operatorname{Var}(X_T)=\sigma^2 B_\lambda(T),\qquad
\operatorname{cum}_4(X_T)=48\sigma^4\int_0^T e^{-2\lambda b}(e^{rb}-1)J_\lambda(T-b)\,db.
\]
For \(\gamma,r,\sigma,T>0\), the second expression is strictly positive and, when \(\lambda\) and \(\sigma\) are held fixed, strictly increases with \(r\) on \((0,\lambda)\). The ratio
\[
\lambda\longmapsto\frac{B_\lambda(T_2)}{B_\lambda(T_1)}
\]
is strictly decreasing from \((T_2/T_1)^2\) to \(T_2/T_1\) for every \(0<T_1<T_2\). Consequently, \(\operatorname{Var}(X_{T_1})\), \(\operatorname{Var}(X_{T_2})\), and \(\operatorname{cum}_4(X_{T_1})\) determine \(\lambda\), then \(\sigma\), then \(r\), and finally \(\gamma=\lambda-r\), uniquely.

## Assumptions and scope
On a probability space carrying an independent two-sided Brownian motion, two-sided homogeneous Poisson collision times of rate \(r>0\), and independent centered Gaussian marks of variance \(\sigma^2>0\), define a stationary velocity process. Between collisions it obeys
\[
dV_t=-\gamma V_t\,dt+\sqrt{2\gamma\sigma^2}\,dW_t,\qquad \gamma>0,
\]
and at each collision its velocity is replaced by a *fresh independent* \(\mathcal N(0,\sigma^2)\) variable; its position is never reset. The process is started in its unique equilibrium law, so every fixed-time velocity has distribution \(\mathcal N(0,\sigma^2)\). The measured displacement is \(X_T=\int_0^T V_t\,dt\), with \(T>0\). All stated moments are exact ensemble quantities, not empirical estimates. Poisson clocks and Brownian thermal fluctuations are mutually independent.

## Proof
**1. Gaussian one-time law and covariance concealment.** Both the OU semigroup and the collision kernel preserve the same Gaussian equilibrium law; their stationary concatenation does too. Two distinct times \(s<t\) have correlated velocities only if no Poisson collision lies between them. Conditional on that event the OU covariance is \(\sigma^2 e^{-\gamma(t-s)}\). Hence
\[
\mathbb E[V_sV_t]=\sigma^2e^{-\lambda(t-s)},\qquad \lambda=\gamma+r.
\]
A purely Gaussian stationary OU velocity with relaxation \(\lambda\) and equilibrium variance \(\sigma^2\) therefore has *exactly the same entire covariance function*. Double integration over \([0,T]^2\) gives the stated \(\sigma^2 B_\lambda(T)\). All velocity or displacement quadratic observations, even with arbitrary multiple-time lags, consequently fail to distinguish these processes.

**2. Connected four-time function.** Take \(t_1<t_2<t_3<t_4\) and denote consecutive gaps \(a,b,c>0\). Conditional on collision placements, the velocities form independent centered Gaussian blocks with OU correlations *within* each uninterrupted block. Wick's rule and independence of collision intervals show that the \((12)(34)\) pairing contributes the same unconditional product as in the Gaussian covariance-matched process; the two crossing pairings require an uninterrupted collision-free interval from \(t_1\) to \(t_4\). Each contributes the full OU factor \(\sigma^4 e^{-\gamma(a+2b+c)}e^{-r(a+b+c)}\) instead of the covariance-product factor \(\sigma^4e^{-\lambda(a+2b+c)}\). Subtracting the three pairwise covariance products therefore yields precisely
\[
\operatorname{cum}(V_{t_1},V_{t_2},V_{t_3},V_{t_4})
=2\sigma^4 e^{-\lambda(a+2b+c)}(e^{rb}-1)>0.
\]
Repeated-time identities follow continuously. This exact connected function is zero for its stationary Gaussian covariance twin.

**3. Integration and positivity.** Integrate the connected four-time function over \([0,T]^4\). Symmetry permits multiplication of the strictly ordered simplex integral by \(4!=24\). With \(q=a+c\), the choices of \((a,c)\) of sum \(q\) have one-dimensional measure \(q\), while the earliest-time location contributes \(T-b-q\). The resulting integral equals
\[
48\sigma^4\int_0^T e^{-2\lambda b}(e^{rb}-1)
\left[\int_0^{T-b}q(T-b-q)e^{-\lambda q}\,dq\right]db.
\]
Both factors involving \(b\) and \(J_\lambda\) are strictly positive on the interior. At fixed \(\lambda\) its integrand is strictly increasing with \(r\), proving positivity and strict monotonicity.

**4. Unique two-window recovery of the covariance decay.** Write
\[
B_\lambda(T)=2\int_0^T (T-h)e^{-\lambda h}\,dh.
\]
The derivative of \(\log B_\lambda(T)\) with respect to \(\lambda\) is minus the mean \(h\) under the density proportional to \((T-h)e^{-\lambda h}\) on \((0,T)\). For \(T_2>T_1\), the density ratio on their shared support is proportional to \((T_2-h)/(T_1-h)\), strictly increasing in \(h\), and the larger-window density has additional positive mass above \(T_1\). The larger-window lag strictly stochastically dominates, so the derivative of \(\log[B_\lambda(T_2)/B_\lambda(T_1)]\) is strictly negative. Its limits at \(\lambda\downarrow0\) and \(\lambda\uparrow\infty\) are \((T_2/T_1)^2\) and \(T_2/T_1\), respectively. Thus a measured variance ratio uniquely fixes \(\lambda\), the first variance uniquely fixes \(\sigma^2\), and the strictly increasing cumulant uniquely fixes \(r\in(0,\lambda)\); subtract to recover \(\gamma>0\).

**5. Sharp scale checks.** Expanding the positive integral at short observation durations gives
\[
\operatorname{cum}_4(X_T)=\frac{2}{5}\sigma^4rT^5+O(T^6),\qquad
\frac{\operatorname{cum}_4(X_T)}{\operatorname{Var}(X_T)^2}
=\frac{2r}{5}T+O(T^2).
\]
For fixed \(\gamma,r,\sigma>0\) and large durations, dominated convergence applied after factoring the linear growth of \(J_\lambda(T-b)\) gives
\[
\operatorname{cum}_4(X_T)\sim\frac{24\sigma^4r}{\lambda^3(2\lambda-r)}T,\qquad
\frac{\operatorname{cum}_4(X_T)}{\operatorname{Var}(X_T)^2}
\sim\frac{6r}{\lambda(2\lambda-r)T}.
\]
These do not imply non-Gaussianity persists after long-time diffusive normalization; rather, they quantify its decay while preserving exact finite-window identifiability.

## Verification
Run `python verify_thermal_refresh.py` with Python 3, NumPy and SciPy. The program verifies 250 four-time cumulants against independent exact enumeration of all eight collision-pattern partitions, the strict two-window variance-ratio ordering at 237 adjacent points, and 80 complete inverse reconstructions. A separate simulation samples the entire random collision partition and the conditional Gaussian displacement variance, without using the four-time cumulant integral; at \((\lambda,r,\sigma,T)=(1.6,0.7,1.3,2.2)\) it obtained a fourth cumulant near \(2.5471\) against exact \(2.5396\) from 150,000 independent histories, with Monte Carlo uncertainty reported by the script. It also checks both leading asymptotic coefficients. These finite checks do not prove the all-parameter result; the analytical steps above do.

## Relationship to prior work
Olsen and Löwen (2024), arXiv:2401.12685, analyze hidden velocity **reset to a fixed value**, developing exact Fourier–Laplace propagators and moment recursions and a long-time effective diffusivity. The present model instead uses fresh *random* Gaussian equilibrium velocity at every collision, thereby maintaining a Gaussian stationary one-time law. Those previous general methods and physical motivations are acknowledged, not claimed as discoveries. Santra, Olsen, and Gupta (2024), arXiv:2408.16643, derive a general renewal switching formulation for **alternating motility phases** and analyze run-and-tumble/passive switching; its formulas may overlap at a broader level but do not state the present Gaussian-covariance-twin, exact connected four-time function, or displacement-only three-moment inverse theorem. Andersen-type thermal velocity redraws are standard. The evaluated fourth-order identity and identifiability assertion, not renewal conditioning or Maxwellian sampling, are the proposed contributions. Published general renewal/thermostat results could potentially imply the formulas after nontrivial specialization; definitive publication priority has not been independently established.

## Limitations
The calculation requires strictly positive OU friction and Poisson rethermalization rate, perfect renewal independence, fresh Gaussian equilibrium draws at collisions, stationary initial conditions, and ideal exact moments. It does not cover deterministic zero-velocity resetting, non-Gaussian draw laws, non-Poisson collision clocks, spatial potentials, measurement noise, or a finite-sample confidence guarantee. Numerical comparisons are corroboration only. The possible existence of a stronger general thermostat/renewal or system-identification theorem remains an originality risk. Independent scientific validation has not been performed.

## References
- K. Stølevik Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (public 23 January 2024), https://arxiv.org/abs/2401.12685 .
- I. Santra, K. Stølevik Olsen, and D. Gupta, *Dynamics of switching processes: general results and applications to intermittent active motion*, arXiv:2408.16643v1 (public 29 August 2024), https://arxiv.org/abs/2408.16643 .
- GROMACS 2021 reference manual, *Molecular Dynamics*, Maxwell–Boltzmann velocity initialization, https://manual.gromacs.org/2021/reference-manual/algorithms/molecular-dynamics.html .
