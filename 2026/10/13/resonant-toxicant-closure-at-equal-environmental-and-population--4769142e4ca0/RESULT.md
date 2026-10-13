# Resonant toxicant closure at equal environmental and population decay rates

## Finding

Mu and Lo use the impulsive toxicant subsystem
\[
\dot T_0=kT_e-gT_0,\qquad \dot T_e=-vT_e,
\]
between pulses, with
\[
\Delta T_0=0,\qquad \Delta T_e=\Lambda
\]
at times \(nT\). Their Lemma 3.2 gives an attracting \(T\)-periodic toxicant solution whose displayed formula divides by \(g-v\). It is therefore undefined at \(g=v\), even though the paper's numerical section takes \(g=v=1\).

The boundary has a removable singularity. If
\[
g=v=c>0,\qquad E=e^{-cT},
\]
and \(\tau\in[0,T)\) is time since the latest pulse, then
\[
T_e^*(\tau)=\frac{\Lambda e^{-c\tau}}{1-E},
\]
and
\[
T_0^*(\tau)
=
e^{-c\tau}
\left(
\frac{k\Lambda T E}{(1-E)^2}
+
\frac{k\Lambda\tau}{1-E}
\right).
\]
In particular,
\[
T_0^*(0)=\frac{k\Lambda T e^{-cT}}{(1-e^{-cT})^2}.
\]

The exact period mean is
\[
\frac1T\int_0^T T_0^*(t)\,dt=\frac{k\Lambda}{c^2T}.
\]
Thus the paper's mean toxicant quantity
\[
\beta_0=\frac{k\Lambda}{vgT}
\]
extends continuously to the equal-rate boundary.

For the numerical values used in Section 6,
\[
k=g=v=T=1,\qquad \Lambda=0.2,
\]
the resonant mean is exactly
\[
\beta_0=0.2.
\]
This agrees with the value used in the paper's threshold calculations.

## Assumptions and scope

Assume \(k,\Lambda,T,c>0\) and \(g=v=c\). The environmental toxicant jumps by \(\Lambda\) at each multiple of \(T\), while \(T_0\) is continuous through the pulse.

The result concerns the toxicant subsystem and the extinction/persistence arguments that depend on its attracting periodic orbit and mean. It does not alter the ecological food-chain equations, re-estimate parameters, or claim that the published numerical trajectories are incorrect.

## Proof

Immediately after a pulse write
\[
T_e(0^+)=Y,\qquad T_0(0^+)=X.
\]
At equal rates,
\[
T_e(\tau)=Ye^{-c\tau}.
\]
The first equation becomes
\[
\frac{d}{d\tau}\left(e^{c\tau}T_0(\tau)\right)=kY,
\]
so
\[
T_0(\tau)=e^{-c\tau}(X+kY\tau).
\]

Let \(E=e^{-cT}\). The post-pulse Poincare map is
\[
\begin{pmatrix}X\\Y\end{pmatrix}
\longmapsto
\begin{pmatrix}E&kTE\\0&E\end{pmatrix}
\begin{pmatrix}X\\Y\end{pmatrix}
+
\begin{pmatrix}0\\\Lambda\end{pmatrix}.
\]
Both multipliers equal \(E\), with \(0<E<1\). Therefore this affine map has a unique globally attracting fixed point.

The fixed-point equations give
\[
Y=EY+\Lambda=\frac{\Lambda}{1-E},
\]
and
\[
X=E(X+kYT)=\frac{k\Lambda T E}{(1-E)^2}.
\]
Substitution proves the periodic formulas.

Integrating the periodic \(T_e\) balance over one pulse interval gives
\[
c\int_0^T T_e^*(t)\,dt=\Lambda,
\]
hence
\[
\int_0^T T_e^*(t)\,dt=\frac{\Lambda}{c}.
\]
Integrating the continuous \(T_0\) equation over a period and using periodicity gives
\[
0=k\int_0^T T_e^*(t)\,dt-c\int_0^T T_0^*(t)\,dt.
\]
Therefore
\[
\int_0^T T_0^*(t)\,dt=\frac{k\Lambda}{c^2},
\]
and the mean is \(k\Lambda/(c^2T)\).

The same branch is obtained by taking \(g\to v=c\) in the nonresonant formulas printed in Lemma 3.2. It is a removable analytic singularity, not a singularity of the differential system.

## Verification

The accompanying checker replays the source's \(k=g=v=T=1,\ \Lambda=0.2\) example. It verifies the fixed-point equations, the pulse periodicity identities, the mean \(0.2\), and convergence of the nonresonant initial-value formula toward the resonant value.

The checker is corroborative only. Existence, uniqueness, attraction, and the mean identity are proved analytically above.

## Relationship to prior work

The closest direct predecessor inspected is the polluted-chemostat model of Meng, Wang, and Zhang. Its toxicant subsystem has decay rates \(h\) and \(g+m\), and its Lemma 2.1 displays a periodic solution with denominator \(h-g-m\). That paper likewise does not state the equal-rate \(h=g+m\) branch, so it does not cover the boundary corrected here.

Targeted searches using the Mu-Lo DOI and title, equal-rate and resonance terminology, the mean-toxicant formula, and correction/erratum terminology did not locate a published repair. The general repeated-rate linear calculation is elementary and is not claimed as a new method. The source-specific contribution is closing the precise boundary used in the motivating paper's numerical examples and showing that its threshold mean survives unchanged there.

## Limitations

The result is limited to \(g=v>0\). It does not provide a new general theory of impulsive systems.

It does not re-evaluate the ecological simulations or persistence thresholds beyond proving that the periodic toxicant orbit and mean used by those arguments remain mathematically well-defined at equal rates.

An unindexed correction or author note could contain the same boundary formula.

## References

1. Y. Mu, W.-C. Lo, “Dynamics of the food-chain population in a polluted environment with impulsive input of toxicant,” Discrete and Continuous Dynamical Systems - B 26 (2021), 4173–4190. DOI: 10.3934/dcdsb.2020279. Early access 21 September 2020.
2. X. Meng, L. Wang, T. Zhang, “Global dynamics analysis of a nonlinear impulsive stochastic chemostat system in a polluted environment,” Journal of Applied Analysis and Computation 6 (2016), 865–875. DOI: 10.11948/2016055.
