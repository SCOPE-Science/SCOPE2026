# Finite-slew time optimality and a logarithmic resonance in trapped active-particle relaxation

## Finding
For the stationary-to-stationary covariance transfer of an active Ornstein–Uhlenbeck particle in a stiffening harmonic trap, imposing the finite actuator slew constraint \(|\dot a|\le R\) leads to an exact global minimum-time protocol: ramp at the maximal rate, then hold. This protocol simultaneously minimizes the two stationary covariance deficits at every observation time, irrespective of competing admissible nonmonotone controls. The exact minimum arrival time and its weak-tolerance asymptotics are given below. At the final-stiffness resonance \(\mu a_f=\tau^{-1}\), the sharp arrival-time asymptotic contains a genuine additional \(\log\log(1/\varepsilon)\) term.

## Assumptions and scope
Let \(\mu,\tau,D,D_1,R\) be strictly positive and \(0<a_i<a_f\). Let independent Brownian motions drive the linear stochastic differential equations
\[
 dX_t=(-\mu a(t)X_t+V_t)\,dt+\sqrt{2D}\,dB_t,\qquad dV_t=-\tau^{-1}V_t\,dt+\frac{\sqrt{2D_1}}{\tau}\,dW_t.
\]
The initial joint law is the centered stationary Gaussian law for constant stiffness \(a_i\). An admissible protocol on \([0,T]\) is absolutely continuous, satisfies \(a(0)=a_i\), \(a(T)=a_f\), \(a_i\le a(t)\le a_f\) and \(|\dot a(t)|\le R\) almost everywhere. The endpoint restriction necessarily requires \(T\ge t_R=(a_f-a_i)/R\).

Define \(x(t)=\mathbb E[X_t^2]\), \(y(t)=\mathbb E[X_tV_t]\), \(q_i=\mu a_i\), \(q_f=\mu a_f\) and
\[
 y_j=\frac{D_1}{1+\tau q_j},\quad x_j=\frac{D+y_j}{q_j},\qquad j\in\{i,f\}.
\]
For a prescribed tolerance \(0<\varepsilon<E_*(0)\), define the moment-target error \(E_a(t)=\sqrt{(x(t)-x_f)^2+(y(t)-y_f)^2}\). This is the unweighted two-moment Euclidean metric used to assess state-to-state transformations in the cited source; it is not a Wasserstein distance or an energy cost. Let \(a_*(t)=\min(a_i+Rt,a_f)\), and \(E_*=E_{a_*}\).

**Theorem.** For every \(t\ge0\) and every control on \([0,t]\) respecting the initial value, amplitude and slew bounds (whether or not it has yet reached \(a_f\)),
\[
 x_a(t)\ge x_*(t)>x_f,\qquad y_a(t)\ge y_*(t)>y_f,\qquad E_a(t)\ge E_*(t).
\]
Equality in the error at any \(t>0\) requires \(a=a_*\) almost everywhere on \([0,t]\). The function \(E_*\) is continuous, strictly decreasing from \(E_*(0)>0\) to zero. Its unique tolerance-crossing time \(t_\varepsilon\), defined by \(E_*(t_\varepsilon)=\varepsilon\), gives the **exact** minimum duration among endpoint-admissible controls:
\[
 T_\varepsilon=\max\{t_R,t_\varepsilon\}.
\]
The minimizing control is uniquely \(a_*\) up to equality almost everywhere. Exact arrival at the final stationary moment pair cannot occur at finite time.

For an explicit expression, set \(\beta=\mu R\), \(H(t)=(\tau^{-1}+q_i)t+\beta t^2/2\), \(Q(t)=q_it+\beta t^2/2\). During \(0\le t\le t_R\),
\[
 y_*(t)=e^{-H(t)}\left[y_i+\frac{D_1}{\tau}\int_0^t e^{H(u)}\,du\right],
\]
\[
 x_*(t)=e^{-2Q(t)}\left[x_i+2\int_0^t e^{2Q(u)}(D+y_*(u))\,du\right].
\]
Write \(\delta_x=x_*(t_R)-x_f>0\), \(\delta_y=y_*(t_R)-y_f>0\), \(m=2q_f\), \(\ell=\tau^{-1}+q_f\), and \(s=t-t_R\ge0\). After the ramp,
\[
 y_*(t)-y_f=\delta_y e^{-\ell s},
\]
\[
 x_*(t)-x_f=\begin{cases}
\displaystyle\delta_xe^{-ms}+\frac{2\delta_y}{m-\ell}(e^{-\ell s}-e^{-ms}),&m\ne\ell,\\
(\delta_x+2\delta_ys)e^{-ms},&m=\ell.
\end{cases}
\]
In particular the sharp small-tolerance laws, with all physical parameters held fixed, are:
\[
 T_\varepsilon=t_R+\begin{cases}
\displaystyle\frac{1}{m}\log\!\frac{\delta_x+2\delta_y/(\ell-m)}{\varepsilon}+o(1),&q_f<\tau^{-1},\\[7pt]
\displaystyle\frac{1}{\ell}\log\!\frac{\delta_y\sqrt{1+4/(m-\ell)^2}}{\varepsilon}+o(1),&q_f>\tau^{-1},\\[7pt]
\displaystyle\frac{1}{m}\left(L_\varepsilon+\log L_\varepsilon\right)+o(1),&q_f=\tau^{-1},
\end{cases}
\]
where \(L_\varepsilon=\log\![2\delta_y/(m\varepsilon)]\) in the critical case. In particular, at resonance,
\[
 T_\varepsilon=\frac{1}{m}\log(1/\varepsilon)+\frac{1}{m}\log\log(1/\varepsilon)+O(1).
\]

## Proof
**Moment closure.** Itô's formula and independence give \(\dot y=D_1/\tau-(\tau^{-1}+\mu a)y\) and \(\dot x=-2\mu ax+2(D+y)\), with the displayed stationary initial/final values. All relevant moment solutions are finite and strictly positive.

**Global comparison.** The slew bound implies \(a(t)\le a_i+Rt\), while the amplitude bound implies \(a(t)\le a_f\), hence \(a\le a_*\) pointwise. Subtract the scalar \(y\) equations and use variation of constants:
\[
 y_a(t)-y_*(t)=\mu\int_0^t e^{-\int_s^t(\tau^{-1}+\mu a(u))\,du}\,[a_*(s)-a(s)]\,y_*(s)\,ds\ge0.
\]
Next, subtract the \(x\) equations:
\[
 x_a(t)-x_*(t)=2\int_0^t e^{-2\mu\int_s^t a(u)\,du}\left[(y_a(s)-y_*(s))+\mu(a_*(s)-a(s))x_*(s)\right]ds\ge0.
\]
Both inequalities are strict at \(t>0\) if \(a<a_*\) on a positive-measure portion of \([0,t]\). Comparison against the constant-final-stiffness system started from the larger initial steady moments implies \(x_*(t)>x_f\) and \(y_*(t)>y_f\) for each finite \(t\). Since the norm of two nonnegative deficits is increasing in either coordinate, the asserted strict error comparison follows.

**Strict relaxation and minimum-time principle.** On the ramp, differentiate the moment equations: \(\ddot y=-(\tau^{-1}+\mu a)\dot y-\mu R y\) and \(\ddot x=-2\mu a\dot x-2\mu R x+2\dot y\). With \(\dot x(0)=\dot y(0)=0\) and positive moments, their integrating-factor solutions imply \(\dot y<0\), \(\dot x<0\) for all \(0<t\le t_R\). After the ramp the derivatives remain strictly negative because their deviations from final stationarity are positive (equivalently, use the same homogeneous linear derivative equations). Thus \(E_*\) strictly decreases; explicit hold solutions establish its convergence to zero. No protocol can meet the target earlier than \(t_\varepsilon\) by pointwise comparison, nor finish stiffness transfer earlier than \(t_R\). The ramp-then-hold protocol attains both bounds, proving the exact maximum formula. At \(T_\varepsilon>t_R\), equality in the comparator forces \(a=a_*\); at \(T_\varepsilon=t_R\), the endpoint and maximal-slew constraints alone force the ramp almost everywhere. The positive error bound rules out exact finite-time transfer.

**Explicit hold and resonance.** The ramp formulas follow from scalar integrating factors. For constant final stiffness the two deficit equations are \(\dot{\delta y}=-\ell\delta y\) and \(\dot{\delta x}=-m\delta x+2\delta y\), which yield the stated nonresonant and resonant forms. If \(m<\ell\), \(\delta x\) has a strictly positive coefficient multiplying the slow \(e^{-ms}\) mode; if \(m>\ell\), both deficits have nonzero coefficients multiplying \(e^{-\ell s}\). Taking the Euclidean norm gives the first two logarithmic laws. When \(m=\ell\), the positive term \(2\delta_y s e^{-ms}\) dominates the norm, giving \(\varepsilon=2\delta_y s e^{-ms}(1+o(1))\). Writing \(u=ms\) and \(L=\log[2\delta_y/(m\varepsilon)]\), inversion of \(u-\log u=L+o(1)\) yields \(u=L+\log L+o(1)\). This is the additional logarithmic resonance.

## Verification
The standalone `verification/check.py` independently propagates the closed moment equations using an adaptive ODE solver and compares them to numerical quadrature of the closed ramp integrals, checks pointwise moment dominance against 60 randomly sampled admissible bounded-slew protocols over 21 times, computes the finite-tolerance optimum, and tests all three spectral regimes. Running `python verification/check.py` with NumPy and SciPy installed prints `ALL CHECKS PASSED`. For \(D=\mu=\tau=1\), \(D_1=2\), \(a_i=1\), \(a_f=5\), \(R=4\), \(\varepsilon=10^{-3}\), the minimum duration is \(1.715820331569\) (rounded). The mathematical proof does not rely on randomized tests, floating-point quadrature, or their stopping tolerances.

## Relationship to prior work
Casert and Whitelam (2024) introduce the same active Ornstein–Uhlenbeck moment equations and a Euclidean state-to-state tolerance, study heat-minimizing protocols, and numerically discuss fastest finite-tolerance transfers without a finite slew bound. Their article and supplementary section S3B already evaluate the **instantaneous initial stiffness jump**, its step-response threshold, and model-parameter effects; none is claimed here as new. This result instead proves the exact optimizer within a physically different, Lipschitz **finite-slew** control class, including the endpoint constraint, and identifies its sharp high-accuracy three-regime behavior and resonant double-logarithm. Davis, Proesmans and Fodor (2024) optimize dissipation in a weak/slow-driving response framework, rather than this global duration objective with an actuator slew ceiling. Gupta, Klapp and Sivak (2023) optimize approximate excess work when moving a trap in a bistable landscape, not the stiffness-transfer problem. The two-dimensional covariance closure and scalar comparison methods are standard tools; the claim is their sharp evaluation for this new constrained reachability problem, not discovery of the moment equations or a general control theorem.

## Limitations
Only stationary covariance-state transfer of a noninteracting, centered, Gaussian active Ornstein–Uhlenbeck particle is covered. The theorem does not minimize heat or work, cover joint control of activity, impose a lower-bound slew speed, address inertial or interacting models, or prove robustness to measurement noise or imprecise physical parameters. The near-resonance formulas hold in three fixed-parameter cases and do not furnish a uniform crossover when final stiffness approaches resonance at a tolerance-dependent rate. External publication-priority verification remains incomplete: a broader reachability theorem not identified in the literature could imply this special case. Independent mathematical review has not been performed.

## References
1. C. Casert and S. Whitelam, “Learning protocols for the fast and efficient control of active matter,” arXiv:2402.18823 (first public 2024-02-29); *Nature Communications* **15**, 9128 (2024), doi:10.1038/s41467-024-52878-2. Primary full text and supplementary sections S3B/S4.
2. L. K. Davis, K. Proesmans and É. Fodor, “Active Matter under Control: Insights from Response Theory,” arXiv:2305.11078; *Physical Review X* **14**, 011012 (2024), doi:10.1103/PhysRevX.14.011012.
3. D. Gupta, S. H. L. Klapp and D. A. Sivak, “Efficient control protocols for an active Ornstein–Uhlenbeck particle,” arXiv:2304.12926; *Physical Review E* **108**, 024117 (2023), doi:10.1103/PhysRevE.108.024117.
