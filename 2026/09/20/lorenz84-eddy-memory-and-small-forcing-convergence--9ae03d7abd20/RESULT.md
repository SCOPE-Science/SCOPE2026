# Stationary eddy-energy law and a small-forcing convergence criterion for Lorenz-84

## System and notation

Consider the autonomous Lorenz-84 system
\[
\dot X=-Y^2-Z^2-aX+aF,
\qquad
\dot Y=XY-bXZ-Y+G,
\qquad
\dot Z=bXY+XZ-Z,
\]
with \(a>0\) and \(b,F,G\in\mathbb R\). Write
\[
R=Y^2+Z^2,\qquad U=F-X,\qquad W=Y+iZ.
\]
The quantity \(R\) is the squared eddy amplitude (and is proportional to the eddy-energy/heat-transport variable in the physical interpretation of the model).

## Main result

### Theorem

1. **Exact past-memory law on recurrent dynamics.** Every bounded complete trajectory satisfies
   \[
   \boxed{F-X(t)=\int_0^\infty e^{-as}R(t-s)\,ds.}
   \]
   Hence every compact invariant set is contained in \(X\le F\). If \(G\ne0\), every compact invariant set in fact satisfies \(\sup X<F\).

2. **Exact stationary conditional law.** For every compactly supported invariant probability measure \(\mu\),
   \[
   \boxed{\mathbb E_\mu[R\mid X]=a(F-X)}\qquad \mu\text{-a.s.}
   \]
   Equivalently, for every continuous \(h\),
   \[
   \int h(X)R\,d\mu
   =a\int h(X)(F-X)\,d\mu.
   \]
   In particular,
   \[
   \langle R\rangle=a(F-\langle X\rangle),
   \qquad
   \operatorname{Cov}(X,R)=-a\operatorname{Var}(X),
   \]
   and
   \[
   \operatorname{Var}(R)\ge a^2\operatorname{Var}(X).
   \]
   More generally, conditional Jensen gives
   \[
   \int \Phi(R)\,d\mu\ge
   \int \Phi(a(F-X))\,d\mu
   \]
   for every convex \(\Phi\) on an interval containing the support of \(R\).

3. **Explicit recurrent slab for \(F<1\).** If \(F<1\), let \(\delta=1-F\). Every bounded complete trajectory obeys
   \[
   |W(t)|\le \frac{|G|}{\delta},
   \qquad
   F-\frac{G^2}{a\delta^2}\le X(t)\le F.
   \]
   Thus every compact invariant set lies in the same explicit slab and eddy disk.

4. **A nonzero-forcing global convergence criterion.** If \(F<1\) and
   \[
   \boxed{2\sqrt{1+b^2}\,G^2<a(1-F)^3,}
   \]
   then the global attractor consists of a single equilibrium. Consequently every forward trajectory converges to that equilibrium. The equilibrium is therefore unique. This criterion includes the unforced case \(G=0\) for every \(F<1\), but it also gives a genuinely nonzero-forcing region.

## Proof

The first equation is
\[
\dot X=a(F-X)-R,
\]
so \(U=F-X\) obeys the stable scalar filter
\[
\dot U=R-aU.
\]
Along a bounded complete trajectory, variation of constants over a backward interval of length \(T\) gives
\[
U(t)=e^{-aT}U(t-T)+\int_0^T e^{-as}R(t-s)\,ds.
\]
Boundedness and \(a>0\) allow \(T\to\infty\), proving the memory formula. Since \(R\ge0\), it follows that \(U\ge0\), hence \(X\le F\). If \(G\ne0\) and \(U(t_0)=0\), the nonnegative integral forces \(R(t_0-s)=0\) for all \(s\ge0\); thus \(Y=Z=0\) throughout a past interval, contradicting \(\dot Y=G\). Compactness then upgrades the pointwise strict inequality to \(\sup X<F\).

For an invariant probability measure \(\mu\) with compact support, the generator identity \(\int L\psi\,d\mu=0\) applies to every \(C^1\) test function. Taking \(\psi=H(X)\), with \(H'=h\), yields
\[
0=\int h(X)[a(F-X)-R]\,d\mu.
\]
As this holds for every continuous \(h\), it is exactly the conditional-expectation identity \(\mathbb E[R\mid X]=a(F-X)\). The mean relation is the case \(h=1\). With \(h=X\),
\[
\mathbb E[XR]=a(F\mathbb E[X]-\mathbb E[X^2]),
\]
and subtraction of \(\mathbb E[X]\mathbb E[R]\) gives \(\operatorname{Cov}(X,R)=-a\operatorname{Var}(X)\). Finally, the law of total variance gives
\[
\operatorname{Var}(R)\ge \operatorname{Var}(\mathbb E[R\mid X])=a^2\operatorname{Var}(X),
\]
and conditional Jensen gives the stated convex-moment hierarchy.

Now suppose \(F<1\), and set \(\delta=1-F>0\). The complex eddy variable satisfies
\[
\dot W=[(X-1)+ibX]W+G.
\]
On a bounded complete trajectory the memory law already gives \(X\le F\), hence the real part of the coefficient of \(W\) is at most \(-\delta\). Backward variation of constants therefore gives
\[
W(t)=G\int_0^\infty
\exp\!\left(\int_{t-s}^t[(X(\tau)-1)+ibX(\tau)]\,d\tau\right)ds,
\]
so
\[
|W(t)|\le |G|\int_0^\infty e^{-\delta s}ds=\frac{|G|}{\delta}=:M.
\]
Substituting \(R=|W|^2\le M^2\) into the first memory formula gives
\[
0\le U(t)\le \frac{M^2}{a}=\frac{G^2}{a\delta^2},
\]
which proves the slab.

For the final assertion, take two bounded complete trajectories and denote their variables by \((U_j,W_j)\), \(j=1,2\). Put
\[
p=U_1-U_2,\qquad v=W_1-W_2,
\]
and let \(P=\sup_{t\in\mathbb R}|p(t)|\), \(V=\sup_{t\in\mathbb R}|v(t)|\). From the two scalar memory formulas,
\[
P\le \frac{1}{a}\sup_t\big||W_1|^2-|W_2|^2\big|
\le \frac{2M}{a}V.
\]
Writing
\[
q_j(t)=(X_j(t)-1)+ibX_j(t),
\]
we have \(\operatorname{Re}q_j\le-\delta\) and
\[
\dot v=q_1v-(1+ib)pW_2.
\]
Backward variation of constants gives
\[
V\le \frac{\sqrt{1+b^2}\,M}{\delta}P.
\]
Combining the last two inequalities,
\[
V\le
\frac{2\sqrt{1+b^2}\,M^2}{a\delta}V
=
\frac{2\sqrt{1+b^2}\,G^2}{a\delta^3}V.
\]
Under the displayed strict parameter condition the factor is less than one, so \(V=0\), hence also \(P=0\). Thus there is at most one bounded complete trajectory.

For completeness, the system is globally dissipative. With
\[
E=\frac12(X^2+Y^2+Z^2)
\]
one has the exact identity
\[
\dot E=-aX^2-R+aFX+GY,
\]
and Young's inequality gives
\[
\dot E\le-cE+\frac{aF^2+G^2}{2},
\qquad c=\min(a,1)>0.
\]
Hence all forward solutions are global and enter a bounded absorbing set; in finite dimension the system has a compact global attractor, consisting of the states on bounded complete trajectories. The preceding uniqueness therefore makes this attractor a singleton. Autonomy forces its unique complete trajectory to be stationary, so it is the unique equilibrium and every forward trajectory converges to it.

## Context and direction of improvement

Lorenz introduced the model in 1984 and already used its energy balance to establish boundedness. Later work has emphasized bifurcations, multistability, attractor geometry, dissipation/energy transfer, non-autonomous attractors, and statistical comparison of invariant measures. The result here is aimed at a different layer: exact constraints obeyed by *every* compact recurrent statistical state, plus an explicit sufficient region where recurrent dynamics collapses globally to one equilibrium despite nonzero longitudinal forcing.

The conditional law is stronger than a single time-average balance: it determines the mean eddy energy at every zonal-flow level in the invariant-measure sense. Its covariance and variance consequences therefore provide exact diagnostics for numerically estimated invariant measures and for reduced or parametrized versions of Lorenz-84. The small-forcing criterion is global, whereas the commonly quoted equilibrium criteria are local; it rules out coexistence of periodic, quasiperiodic, or chaotic compact invariant sets throughout the stated parameter region.

## Scientific limitations

- The stationary conditional law is stated for compactly supported invariant probability measures. The autonomous Lorenz-84 flow is dissipative for \(a>0\), so its physical invariant measures on the global attractor satisfy this hypothesis, but the statement is not formulated for arbitrary noncompact invariant measures.
- The global convergence inequality is sufficient, not claimed necessary or sharp. It requires \(F<1\).
- The result concerns the autonomous Lorenz-84 equations. Seasonally forced, stochastic, and coupled variants require separate arguments.
- The auxiliary scalar and energy identities are elementary consequences of the equations and are not claimed to be novel in isolation. The originality claim concerns the combined past-memory/support result, the invariant-measure conditional law and its covariance/variance hierarchy, the explicit recurrent slab, and the nonzero-forcing global convergence criterion.
- Pelino and Pasini (2001) explicitly study dissipation and energy transfer in Lorenz-84, but their full article was not inspected; it is the strongest identified prior-coverage risk for an equivalent energy-transfer identity.
- Yu (2006), cited by Wang et al. for the simpler \(G=0\) dynamics, was not available in full. It may cover part or all of the unforced specialization, so no originality is claimed for the \(G=0\) corollary by itself.
- Naser, Abdel Aal and Gumah (2026) study global stability for generalized non-autonomous Lorenz systems. The accessible abstract specifically emphasizes attractivity under vanishing forcing and stability of unforced forms; the full theorem text was not inspected, so it remains a coverage risk for nearby global-stability statements.
- Gallo, Anselmi and Lazzari (2026) use an invariant-measure moment matrix for Lorenz-84 system identification. The accessible abstract was inspected, but the full preprint could not be inspected through the available route; it remains the main current-literature risk for moment identities.

## Reproducibility

`artifacts/verify_lorenz84_identities.py` symbolically checks the scalar-filter identity, the exact total-energy balance, the eddy-energy derivative, the divergence, and the algebraic covariance consequence. `artifacts/verification.txt` records the zero residuals obtained from that script.

## References

1. E. N. Lorenz, "Irregularity: a fundamental property of the atmosphere", Tellus A 36 (1984), 98--110. https://doi.org/10.1111/j.1600-0870.1984.tb00230.x
2. V. Pelino and A. Pasini, "Dissipation in Lie-Poisson systems and the Lorenz-84 model", Physics Letters A 291 (2001), 389--396. https://doi.org/10.1016/S0375-9601(01)00764-2
3. J. G. Freire, C. Bonatto, C. C. DaCamara and J. A. C. Gallas, "Multistability, phase diagrams, and intransitivity in the Lorenz-84 low-order atmospheric circulation model", Chaos 18 (2008), 033121. https://doi.org/10.1063/1.2953589
4. H. Wang, Y. Yu and G. Wen, "Dynamical Analysis of the Lorenz-84 Atmospheric Circulation Model", Journal of Applied Mathematics (2014), 296279. https://doi.org/10.1155/2014/296279
5. M. Anguiano and T. Caraballo, "Asymptotic behaviour of a non-autonomous Lorenz-84 system", Discrete and Continuous Dynamical Systems 34 (2014), 3901--3920. https://doi.org/10.3934/dcds.2014.34.3901
6. G. Vissio and V. Lucarini, "Evaluating a stochastic parametrization for a fast-slow system using the Wasserstein distance", Nonlinear Processes in Geophysics 25 (2018), 413--427. https://doi.org/10.5194/npg-25-413-2018
7. M. Rosalie and S. Mangiarotti, "Structure analysis of the Lorenz-84 chaotic attractor", Chaos 35 (2025), 103101. https://doi.org/10.1063/5.0287725
8. M. F. M. Naser, M. Abdel Aal and G. Gumah, "Global stability analysis of two nonautonomous generalized Lorenz systems with time-varying parameters", SeMA Journal (2026). https://doi.org/10.1007/s40324-026-00429-8
9. M. Gallo, F. Anselmi and P. Lazzari, "Attractor Geometry Determines the Identifiability Limits of System Discovery", arXiv:2607.18490 (2026). https://arxiv.org/abs/2607.18490
