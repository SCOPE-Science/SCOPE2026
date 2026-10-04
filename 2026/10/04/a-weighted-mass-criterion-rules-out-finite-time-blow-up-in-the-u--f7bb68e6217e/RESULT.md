# A weighted-mass criterion rules out finite-time blow-up in the unsaturated age-structured role-reversal model
## Finding
Let \(x(t)>0\) be prey abundance, \(u(t,\tau)\ge0\) the predator age density, \(y(t)=\int_0^\infty u(t,\tau)\,d\tau\), and let \(y_1,y_2\) denote juvenile and adult predator masses split at \(\tau^*\). In the original unsaturated model, assume
\[
g>k,\qquad 2sk\le b(g-k).
\]
Then the source's local positive solution extends to every finite time. More precisely, with \(b/k=+\infty\) when \(k=0\), every
\[
c\in\left[\frac{2s}{g-k},\frac{b}{k}\right]
\]
gives \(V=x+cy\) such that
\[
V'(t)\le C V(t),\qquad C=\max\{r,\|\widetilde B\|_\infty\},
\]
so \(V(t)\le V(0)e^{Ct}\). The displayed parameter condition is exact for the existence of a constant weight that makes all cross-feeding terms nonpositive uniformly over predator ages.

## Assumptions and scope
The source prey equation is
\[
x'=x(r-ax+s y_1-b y_2).
\]
Its predator birth and death rates are
\[
B(x,\tau)=kx\varphi_A(\tau)+\widetilde B(\tau)(1-e^{-\zeta x}),
\qquad
\mu(x,\tau)=gx\varphi_J(\tau)+\mu_B(\tau)+\mu_Me^{-\rho x},
\]
with
\[
\varphi_A(\tau)=\frac{1}{1+e^{-\nu(\tau-\tau^*)}},\qquad
\varphi_J(\tau)=\frac{1}{1+e^{-\nu(\tau^*-\tau)}}=1-\varphi_A(\tau).
\]
The source hypotheses on positive initial prey, nonnegative compactly supported predator age density, bounded \(\widetilde B\), and local regularity are retained. The claim is only a finite-time continuation theorem in the norm \(|x|+\|u\|_1\).

## Proof
Set
\[
Y_A=\int_0^\infty\varphi_A(\tau)u(t,\tau)\,d\tau,
\qquad
Y_J=\int_0^\infty\varphi_J(\tau)u(t,\tau)\,d\tau.
\]
For juvenile ages, \(\varphi_A<1/2\) and \(\varphi_J>1/2\); for adult ages, \(0\le\varphi_A\le1\). Hence
\[
Y_A\le\frac12y_1+y_2,\qquad Y_J\ge\frac12y_1.
\]
Integrating the predator transport equation over age and using the renewal boundary condition gives
\[
y'=kxY_A+(1-e^{-\zeta x})\int_0^\infty\widetilde B(\tau)u(t,\tau)\,d\tau-gxY_J-\int_0^\infty(\mu_B(\tau)+\mu_Me^{-\rho x})u(t,\tau)\,d\tau.
\]
Thus for \(V=x+cy\), positivity yields
\[
V'\le rx-ax^2+x\left[s+\frac c2(k-g)\right]y_1+x(-b+ck)y_2+c\|\widetilde B\|_\infty y.
\]
The two cross coefficients are nonpositive exactly when
\[
c(g-k)\ge2s,\qquad ck\le b.
\]
A positive \(c\) satisfying both exists exactly when \(g>k\) and \(2sk\le b(g-k)\), interpreting the upper bound as absent for \(k=0\). Then
\[
V'\le rx+c\|\widetilde B\|_\infty y\le CV,
\]
and Gronwall gives the finite-horizon bound.

The source proves local existence and local Lipschitz continuity on bounded balls in \(|x|+\|u\|_1\), while age support stays compact on each finite horizon. Since fixed \(c>0\) makes \(V=x+cy\) equivalent to \(x+y\), the finite-horizon estimate prevents norm divergence at a finite maximal time. The usual continuation argument therefore extends the solution to every finite time.

For sharpness within constant weighted masses, the juvenile coefficient can be approached by age profiles concentrated just below \(\tau^*\), and the adult coefficient by profiles concentrated at large adult ages. Therefore a constant \(c\) cannot make all cross terms nonpositive if either coefficient is positive.

## Verification
The proof is analytic. The bundled `verify.py` checks the coefficient algebra using exact rational arithmetic and verifies a nonempty witness \(s=1\), \(k=1\), \(g=2\), \(b=4\), \(c=2\), for which the juvenile coefficient is zero and the adult coefficient is \(-2\). This computation is supplementary; it is not an infinite-dimensional proof.

The source full text was checked for the model equations, smooth maturation functions, local Theorem 1, the operational numerical blow-up rule, and the discussion of saturated replacements. The source calls a simulation a blow-up when a component exceeds 1000 before \(T_{\max}=500\), so the present result concerns mathematical finite-time continuation rather than that numerical label.

## Relationship to prior work
The motivating paper proves only local existence for the original equations and then proposes saturated birth terms, outlining boundedness for the modified system. It does not state the unsaturated weighted-mass criterion above. The Li-Liu-Wei role-reversal predecessor is a finite-dimensional stage ODE; the motivating paper reproduces its equations and reports conditions \(s\le g\) and \(k\le b\), but those do not imply the smooth age-renewal estimate because the logistic maturation functions leak prey-dependent birth and juvenile mortality across the maturation boundary.

Targeted searches of published published-finding corpus findings for the exact source, finite-time blow-up, weighted total population, renewal continuation, and the parameter-balance formulation found no equivalent or stronger covering result. The closest retrieved age-structured finding concerns a different Gurtin-MacCamy threshold model. A prior own-ledger item on the same source concerns an Euler-Lotka predator-invasion threshold; it is implication-incomparable with this nonlinear continuation theorem.

## Limitations
The estimate is exponential and does not prove that populations are uniformly bounded as \(t\to\infty\). It does not prevent crossing the paper's numerical threshold of 1000 and does not contradict reported large-amplitude simulations. Failure of this weighted criterion outside the displayed region is not evidence of finite-time blow-up. The condition is sharp only in the family \(V=x+c\int u\); other nonlinear Lyapunov functionals may work elsewhere.

## References
1. L. C. Suarez, M. K. Cameron, W. F. Fagan, D. Levy, *A predator-prey model with age-structured role reversal*, Journal of Mathematical Biology 92, 73 (2026), DOI 10.1007/s00285-026-02402-5; earliest verified public preprint arXiv:2502.19748, 27 February 2025.
2. J. Li, X. Liu, C. Wei, *The impact of role reversal on the dynamics of predator-prey model with stage structure*, Applied Mathematical Modelling 104 (2022), 339-357, DOI 10.1016/j.apm.2021.11.029.
