# Finite-amplitude mean–variance shell for delayed predator–prey cycles
## Finding
For the scaled delay system
\[
\dot x(t)=x(t)(1-x(t)-y(t)),\qquad
\dot y(t)=-s y(t)+Y e^{-s\tau}x(t-\tau)y(t-\tau),
\]
with \(s,Y>0\) and \(\tau\ge0\), define
\[
x_*=\frac{s e^{s\tau}}{Y},\qquad y_*=1-x_*.
\]
Every strictly positive nonconstant \(T\)-periodic solution forces \(x_*<1\) and obeys
\[
\bar x+\bar y=1,\qquad \overline{xy}=x_*\bar y,
\]
\[
\operatorname{Var}_T(x)=(\bar x-x_*)(1-\bar x)=\bar y(y_*-\bar y),
\]
and
\[
\operatorname{Cov}_T(x,y)=-\operatorname{Var}_T(x).
\]
Hence
\[
x_*<\bar x<1,\qquad 0<\bar y<y_*,\qquad
\operatorname{Var}_T(y)>\operatorname{Var}_T(x)>0.
\]
Thus every finite-amplitude positive cycle has mean prey density strictly above, and mean predator density strictly below, the corresponding coexistence-equilibrium coordinates. Its prey variance is fixed exactly by either mean, while prey and predator fluctuations have covariance exactly minus the prey variance.

For the numerical parameters used by Fan and Wolkowicz, \(s=0.02\), \(Y=0.6\), and their bistable value \(\tau=81\),
\[
x_*=\frac{e^{81/50}}{30}=0.168436343885462\ldots,
\]
so both stable cycles reported there satisfy \(\bar x>x_*\) and \(\bar y<1-x_*\), despite having very different periods and amplitudes.

## Assumptions and scope
The claim concerns the scaled Holling-I maturation-delay model printed by Fan and Wolkowicz. A periodic solution is assumed continuous, strictly positive, nonconstant, and \(T\)-periodic in both components. Time averages are
\[
\bar f=\frac1T\int_0^T f(t)\,dt,
\]
with \(\operatorname{Var}_T(x)=\overline{x^2}-\bar x^2\) and \(\operatorname{Cov}_T(x,y)=\overline{xy}-\bar x\bar y\). No small-amplitude, near-Hopf, or stability assumption is used. The theorem does not assert existence or uniqueness of a periodic orbit for a given delay.

## Proof
Because \(x(t)>0\), divide the prey equation by \(x(t)\):
\[
\frac{d}{dt}\log x(t)=1-x(t)-y(t).
\]
Averaging over one period gives
\[
\bar x+\bar y=1. \tag{1}
\]
Averaging the predator equation over one period and using periodicity to shift the delayed product gives
\[
0=-s\bar y+Y e^{-s\tau}\overline{x(t-\tau)y(t-\tau)}
  =-s\bar y+Y e^{-s\tau}\overline{xy},
\]
so
\[
\overline{xy}=x_*\bar y. \tag{2}
\]
Averaging the prey equation itself yields
\[
0=\bar x-\overline{x^2}-\overline{xy}.
\]
Using (1) and (2),
\[
\overline{x^2}=(1+x_*)\bar x-x_*.
\]
Therefore
\[
\operatorname{Var}_T(x)=\overline{x^2}-\bar x^2=(\bar x-x_*)(1-\bar x).
\]
Since \(\bar y=1-\bar x\) and \(y_*=1-x_*\), this is also
\[
\operatorname{Var}_T(x)=\bar y(y_*-\bar y). \tag{3}
\]
Moreover,
\[
\operatorname{Cov}_T(x,y)=\overline{xy}-\bar x\bar y=(x_*-\bar x)\bar y=-\operatorname{Var}_T(x). \tag{4}
\]
If the orbit is nonconstant, then \(x\) cannot be constant: constant positive \(x\) in the prey equation would force constant \(y=1-x\). Hence \(\operatorname{Var}_T(x)>0\). Equation (3) then forces \(x_*<\bar x<1\), equivalently \(0<\bar y<y_*\), and in particular \(x_*<1\). Finally Cauchy–Schwarz and (4) give
\[
\operatorname{Var}_T(x)^2=\operatorname{Cov}_T(x,y)^2\le \operatorname{Var}_T(x)\operatorname{Var}_T(y),
\]
so \(\operatorname{Var}_T(y)\ge\operatorname{Var}_T(x)\). Equality would make \(y-\bar y=-(x-\bar x)\) almost everywhere, hence everywhere by continuity, so \(x+y\) would be constant. Equation (1) makes that constant \(1\), and then the prey equation gives \(\dot x=0\), contradicting nonconstancy. Thus the variance inequality is strict.

## Verification
The derivation uses only period integration, positivity of \(x\), delay-shift invariance of an integral over a full period, algebra, and Cauchy–Schwarz. The accompanying checker verifies the algebraic factorization, covariance identity, and the numerical value of \(x_*\) at \(\tau=81\). The source itself reports two orbitally asymptotically stable periodic orbits at \(\tau=81\), with periods approximately \(345\) and \(273.7\), so the theorem constrains two distinct finite-amplitude cycles at the same parameter value.

## Relationship to prior work
Fan and Wolkowicz introduced and analyzed this scaled delayed predator–prey system, gave the coexistence equilibrium \(E_+=(x_*,1-x_*)\), proved persistence in the coexistence regime, and documented Hopf bifurcations, bistability, period doubling, and chaos. Their full text does not state a time-mean, variance, or covariance identity of the form above.

Li, Lin, and Wang studied a broader delayed Lotka–Volterra predator–prey family with both Holling-I and Holling-II responses. Their Holling-I specialization contains the same structural reaction terms after parameter identification, and their work proves global Hopf-branch and multiple-cycle results. Statement-level inspection of the full paper found no corresponding mean, variance, covariance, or period-integral theorem. Thus the present result is not based on a new model; it is a finite-amplitude quantitative law for periodic states of an established delayed model.

## Limitations
The proof does not locate periodic orbits, determine their periods, establish their stability, or extend the identities to arbitrary nonperiodic trajectories without additional hypotheses on limiting time averages. The strict variance dominance is stated in the source's nondimensional variables and should not be transferred unchanged to dimensional variables without applying the scaling. A residual literature risk remains because the identities follow from short period integrations and could have appeared in older work under different notation; targeted full-text and semantic searches did not identify such coverage.

## References
Fan, G. and Wolkowicz, G. S. K., “Chaotic dynamics in a simple predator-prey model with discrete delay,” arXiv:2007.16140v1, first public 31 July 2020; Discrete and Continuous Dynamical Systems - B 26 (2021), 191–216, DOI 10.3934/dcdsb.2020263.

Li, M. Y., Lin, X., and Wang, H., “Global Hopf branches and multiple limit cycles in a delayed Lotka-Volterra predator-prey model,” Discrete and Continuous Dynamical Systems - B 19 (2014), 747–760, DOI 10.3934/dcdsb.2014.19.747.
