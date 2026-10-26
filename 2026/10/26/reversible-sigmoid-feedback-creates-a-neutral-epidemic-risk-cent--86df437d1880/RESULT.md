# Reversible sigmoid feedback creates a neutral collective-risk center and a strict mean-risk premium

## Finding

In the smallest nontrivial collective-risk group, an odd sigmoid environmental response makes the symmetric interior equilibrium a **nonlinear center rather than an attracting Hopf cycle**. Every sufficiently small non-equilibrium state travels on a genuine periodic orbit, and every such cycle has exactly the equilibrium mean cooperation but strictly **higher** mean catastrophe risk. The risk premium is an exact finite-amplitude, risk-weighted variance, not a linear approximation:

\[
\overline{x}=\tfrac12,\qquad \operatorname{Cov}(x,r)=0,\qquad \overline r-r_*=4\overline{r(x-\tfrac12)^2}>0.
\]

## Assumptions and scope

Take the Liu–Chen–Szolnoki collective-risk model with group size \(N=3\), success threshold \(M=2\), exponential/sigmoid environmental response (their Eq. 7), and symmetric risk target \(T=1/2\). Let \(x\in(0,1)\) denote the cooperator fraction and \(r\in(0,1)\) the failure risk. For **all** \(b,\varepsilon,\beta>0\) and \(0<c<b/2\), the governing autonomous planar system is

\[
\varepsilon\dot x=x(1-x)[2brx(1-x)-c],\quad
\dot r=-r(1-r)\tanh\!\left(\frac{\beta(x-1/2)}2\right).
\]

Here \(b\) is endowment, \(c\) is cooperative cost, \(\varepsilon\) is the strategy time-scale ratio, and \(\beta\) is sigmoid steepness. A bar denotes a full physical-time average along one specified periodic orbit. Risk is the model's failure-probability state, not measured realized losses. The interior equilibrium is \(E=(1/2,r_*)\) with \(r_*=2c/b\in(0,1)\).

## Proof

**1. Elliptic linearization.** Define \(F=(F_1,F_2)\) by the right sides. At \(E\), direct differentiation gives

\[
DF(E)=\begin{pmatrix}0 & b/(8\varepsilon)\\
-\beta r_*(1-r_*)/2 & 0\end{pmatrix}.
\]

Its eigenvalues are \(\pm i\omega\), with \(\omega^2=b\beta r_*(1-r_*)/(16\varepsilon)>0\). Pure imaginary eigenvalues alone would *not* establish a center; the following exact symmetry supplies the missing nonlinear step.

**2. Reversible involution and periodic annulus.** Put \(\mathcal R(x,r)=(1-x,r)\). Because \(x(1-x)\) is unchanged under this reflection, and the hyperbolic tangent is odd, \(F(\mathcal R z)=-D\mathcal R\,F(z)\) on the entire unit square. Thus if \(\phi_t\) is the flow, \(\mathcal R\phi_t=\phi_{-t}\mathcal R\). The fixed line of \(\mathcal R\) is \(x=1/2\). Near the elliptic equilibrium, the linearized orbit started at \((1/2,r_*+\delta)\) meets this line again transversely after time \(\pi/\omega\). After scaling the displacement by \(\delta\), smooth dependence of the flow on initial data and the implicit-function theorem give a second transverse intersection at a time \(t_\delta\to\pi/\omega\) for all sufficiently small nonzero \(\delta\). At both intersections the state lies on the fixed line. Reversibility then yields \(\phi_{2t_\delta}(z_\delta)=z_\delta\): reflection of the first trajectory arc is precisely its returning second arc. The derivative of the flow with respect to the initial transverse coordinate is nonsingular, so these orbits fill an annular punctured neighborhood of \(E\). No isolated attracting/repelling limit cycle is asserted.

**3. Exact symmetry averages.** On every such periodic orbit, the reflection maps the orbit to itself as a time reversal: after choosing the initial point on the reflection axis, \(x(t_\delta+t)=1-x(t_\delta-t)\), while \(r(t_\delta+t)=r(t_\delta-t)\). Translation-invariant time averaging gives \(\overline x=1/2\) and \(\overline{(x-1/2)r}=0\), hence \(\operatorname{Cov}(x,r)=0\).

**4. Exact risk excess.** Since \(0<x<1\) throughout, average \(d[\log(x/(1-x))]/dt=[2brx(1-x)-c]/\varepsilon\) over a period to obtain \(2b\overline{r x(1-x)}=c\). Use \(x(1-x)=1/4-(x-1/2)^2\) to get

\[
\bar r-4\overline{r(x-1/2)^2}=\frac{2c}{b}=r_*.
\]

Every nonconstant orbit has \(r(t)>0\) and \(x(t)\not\equiv1/2\), so the variance defect is strictly positive. All quantifiers and endpoint exclusions above are essential; \(\beta=0\) makes the equilibrium non-elliptic, and \(r_*\notin(0,1)\) removes the interior equilibrium.

## Verification

The independent derivative and reflection calculations are reproduced in the embedded `verify.py`. That program checks exact-rational payoff reflection and numerical sigmoid oddness, confirms the risk balance from periodic numerical integration, and compares mean risk to the equilibrium. The analytical symmetry and periodic-orbit argument, not the numerical computations, establish the infinite family of genuine periodic solutions. An unverified numerical orbit is never treated as a proof.

## Relationship to prior work

Liu, Chen and Szolnoki (2023), Eqs. (3), (6) and (7), introduce and analyze this feedback-evolving collective-risk model and report Hopf and oscillatory regimes for general \(N,M,T\). Their Appendix studies local coefficients numerically for a nonminimal parameter example. The present theorem concerns the structurally distinguished minimal symmetric case, where an exact reversing symmetry forces an entire annulus of **neutral** cycles, and derives the resulting finite-amplitude mean-risk premium. Linear feedback has related symmetric center behavior, but that does not imply that the nonlinear sigmoid model retains it. General planar reversibility results motivate the local symmetry argument; no claim is made that the general theory itself is new.

## Limitations

This is a deterministic mean-field result for \(N=3,M=2,T=1/2\), with \(b,\varepsilon,\beta>0\), \(0<c<b/2\), and sufficiently small periodic trajectories near the interior equilibrium. It does not establish global periodicity, attraction, robustness under asymmetric targets or finite stochastic-population effects. The average excess concerns the environmental risk variable, not an independently calibrated public-health outcome. Exact bibliographic priority against all possible equivalent reversible-game formulations remains to be independently checked.

## References

1. L. Liu, X. Chen, and A. Szolnoki, “Coevolutionary dynamics via adaptive feedback in collective-risk social dilemma game,” *eLife* **12**:e82954 (2023), doi:10.7554/eLife.82954; public version May 19, 2023, especially Equations (3), (6), (7) and Appendix 2.
2. Standard local reversibility and implicit-function-theorem facts for planar smooth flows, applied here with their hypotheses verified directly.
