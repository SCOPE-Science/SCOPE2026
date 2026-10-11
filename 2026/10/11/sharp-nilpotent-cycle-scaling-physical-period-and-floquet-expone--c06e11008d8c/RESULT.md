# Sharp nilpotent-cycle scaling, physical period and Floquet exponent near a cubic center

## Finding
For the cubic vector field
\[
\dot x=y,\qquad \dot y=-x^3+\alpha x^2y+y^3,
\]
let \(\epsilon=-\alpha>0\). For all sufficiently small \(\epsilon\), there exists exactly one nonconstant periodic orbit \(\Gamma_{-\epsilon}\) (the global uniqueness and existence are established in the cited paper). Define the beta integral \(B(p,q)=\int_0^1u^{p-1}(1-u)^{q-1}\,du\), and positive constants
\[
\rho^2=\frac{2B(3/4,3/2)}{B(1/4,5/2)},\qquad
T_*=\frac{\sqrt2}{\rho}B(1/4,1/2),\qquad
J_*=\frac{\rho^3}{\sqrt2}B(1/4,5/2).
\]
The maximum of the absolute horizontal coordinate on the orbit, its minimal period \(\mathcal T\) in the displayed original physical time, and its transverse Floquet multiplier \(\mu\), respectively, obey
\[
\begin{split}
\max_{\Gamma_{-\epsilon}}|x|&=\rho\epsilon^{1/2}+O(\epsilon^{7/2}),\\
\mathcal T(\epsilon)&=T_*\epsilon^{-1/2}+O(\epsilon^{5/2}),\\
\log\mu(\epsilon)&=J_*\epsilon^{3/2}+O(\epsilon^{9/2}).
\end{split}
\]
The multiplier is greater than one, so the cycle is repelling. For \(X=x/\sqrt\epsilon\) and \(Y=y/\epsilon\), the cycle converges as a phase-normalized smooth closed curve to the quartic Hamiltonian oval \(Y^2/2+X^4/4=\rho^4/4\). The leading constants are approximately \(\rho=0.799828239975\), \(T_*=9.272364163377\), and \(J_*=1.084199920792\).

## Assumptions and scope
The parameter approaches zero **from below**, \(\alpha=-\epsilon\uparrow0\) with \(\epsilon>0\). The time variable for \(\mathcal T\) is the time in the original displayed system, rather than time after desingularization. The multiplier is the nontrivial eigenvalue of the monodromy matrix, and equals the derivative of the planar transverse return map. The time exponent and maximum are taken on the unique periodic orbit, not on arbitrary orbits. The \(O\)-terms refer to real \(\epsilon\downarrow0\); the result makes no assertion about continuation to a finite nonzero parameter endpoint. The strict existence/uniqueness of the physical cycle away from zero is credited to Zhuang and Liu; a local cycle is independently reconstructed here for the asymptotic proof.

## Proof
**1. An exact nilpotent blow-up.** Put \(x=\sqrt\epsilon X\), \(y=\epsilon Y\), and \(\tau=\sqrt\epsilon\,t\), and define \(\delta=\epsilon^{3/2}\). The rescaled equation, where primes denote \(d/d\tau\), is exactly
\[
X'=Y,\qquad Y'=-X^3+\delta(Y^3-X^2Y).
\]
At \(\delta=0\), the Hamiltonian \(H=Y^2/2+X^4/4\) is conserved. For each \(R>0\), its regular oval through \((R,0)\) has \(Y=\pm\sqrt{(R^4-X^4)/2}\) and energy \(E=R^4/4\). For \(R\) in a compact neighborhood of a positive value and sufficiently small \(\delta\), the analytic flow has a well-defined analytic first-return map to the positive turning section \(\{Y=0,X>0\}\). Its energy displacement \(\Delta H(R,\delta)\) is analytic and vanishes identically at \(\delta=0\), so the quotient by \(\delta\) extends analytically across zero.

**2. A simple zero of the energy displacement.** The exact identity \(dH/d\tau=\delta(Y^4-X^2Y^2)\) gives, by integration around the unperturbed oval,
\[
\left.\frac{\Delta H(R,\delta)}{\delta}\right|_{\delta=0}
=F(R)=\sqrt2\,R^5(R^2I_3-2I_1),
\]
where
\[
I_1=\int_0^1u^2\sqrt{1-u^4}\,du=\frac14B(3/4,3/2),\qquad
I_3=\int_0^1(1-u^4)^{3/2}\,du=\frac14B(1/4,5/2).
\]
Both integrals are strictly positive. Thus \(F\) has exactly one positive zero, \(R=\rho\), with \(\rho^2=2I_1/I_3\). Its derivative is
\[
F'(\rho)=2\sqrt2\,\rho^6 I_3>0.
\]
The analytic implicit-function theorem therefore gives a unique analytic positive turning radius \(R(\delta)\) near \(\rho\) for all sufficiently small real \(\delta\); the corresponding orbit is nondegenerate and its period \(T(\delta)\) is analytic. The unperturbed minimal \(\tau\)-period equals
\[
T(0)=4\int_0^\rho\frac{dX}{\sqrt{(\rho^4-X^4)/2}}
=\frac{\sqrt2}{\rho}B(1/4,1/2)=T_*.
\]
No formal power series or numerical continuation substitutes for this local implicit-function argument.

**3. Reversibility eliminates the first perturbative terms.** For every real \(\delta\), if \((X(\tau),Y(\tau))\) solves the rescaled system, then \((X(-\tau),-Y(-\tau))\) solves that same system with parameter \(-\delta\). This involution fixes the section point \((R,0)\). Local uniqueness of the analytic periodic orbit consequently gives the exact identities \(R(-\delta)=R(\delta)\) and \(T(-\delta)=T(\delta)\). Analyticity then improves the generic \(O(\delta)\) remainders to \(R(\delta)=\rho+O(\delta^2)\) and \(T(\delta)=T_*+O(\delta^2)\). Moreover, the symmetry \((X,Y)\mapsto(-X,-Y)\) of the vector field gives the paired negative turning point, so \(\max|X|=R(\delta)\), not merely the positive turning coordinate.

**4. Floquet exponent and its parity.** The divergence of the rescaled field is \(\delta(3Y^2-X^2)\). Liouville's formula gives the exact logarithm of the nontrivial Floquet multiplier,
\[
L(\delta)=\log\mu(\delta)
=\delta\int_0^{T(\delta)}(3Y(\tau)^2-X(\tau)^2)\,d\tau.
\]
The leading integral is equal to the derivative of the first energy displacement with respect to energy, evaluated at the simple zero of the displacement: \(dE/dR=R^3\), so
\[
L'(0)=\frac{F'(\rho)}{\rho^3}
=2\sqrt2\rho^3 I_3
=\frac{\rho^3}{\sqrt2}B(1/4,5/2)=J_*>0.
\]
This identity also follows by direct integration of \(3Y^2-X^2\) over the quartic oval. Reversing time conjugates the positive- and negative-parameter return maps as inverse local diffeomorphisms, giving \(\mu(-\delta)=\mu(\delta)^{-1}\). Hence the analytic function \(L\) is odd, so \(L(\delta)=J_*\delta+O(\delta^3)\), with no quadratic term. In particular the positive-parameter blown-up cycle is repelling.

**5. Undoing the blow-up.** The coordinate and positive time changes preserve periodic orbits and their Floquet multipliers. Since \(\delta=\epsilon^{3/2}\), \(\max|x|=\sqrt\epsilon R(\delta)\), and \(\mathcal T=\epsilon^{-1/2}T(\delta)\), the claimed powers \(7/2,5/2,9/2\) follow. Analytic dependence of the phase-normalized periodic solution on \(\delta\) gives smooth convergence of the rescaled curve to the quartic oval. The global uniqueness from the cited work identifies this local branch with the uniquely existing cycle in the stated small-parameter regime.

## Verification
The companion standard-library program `verify_cycle.py` evaluates the beta constants, integrates the rescaled differential equation by fourth-order Runge–Kutta, locates return crossings, and tests the positive and negative perturbations \(\delta\in\{0.16,0.08,0.04\}\). It checks the evenness of turning radius and period, oddness of the computed logarithmic multiplier, and the predicted leading scales. A successful run prints `CHECK_OK`. This finite diagnostic verifies implementation and signs; the analytic displacement/implicit-function/reversibility argument proves the asymptotics for all sufficiently small parameters.

## Relationship to prior work
Zhuang and Liu (arXiv:2201.08107, first posted January 20, 2022) prove uniqueness of the cycle of exactly this quasi-homogeneous cubic system, building on Gasull's limit-cycle problem and earlier uniqueness criteria. Their existence and uniqueness are used, not rediscovered. The present theorem isolates the previously unquantified nilpotent collision at \(\alpha=0\), gives explicit beta-function constants for the shrinking amplitude, diverging **original-time** period, and weak transverse repulsion, and derives the missing lower-order term cancellations by exact parameter-reversing dynamics. General results on cubic centers and first-order averaging establish broader qualitative machinery but do not, in the inspected material, supply this triple quantitative law for this equation.

## Limitations
The result is a local parameter asymptotic as \(\alpha\uparrow0\) from negative values; it does not describe other parameter thresholds, nonperiodic solutions, or exact finite-parameter cycle shapes. The asymptotic remainders are not uniform beyond a sufficiently small parameter neighborhood and do not provide explicit numerical error constants. Publication-priority comparison with historical works whose complete texts could not be accessed remains incomplete; the stated scientific conclusion rests on the displayed direct proof, not on absence of search hits. Numerical samples do not establish the asymptotic theorem. Independent external validation has not been performed.

## References
1. Ziwei Zhuang and Changjian Liu, *A proof of the uniqueness of the limit cycle of a quasi-homogeneous system*, arXiv:2201.08107v1 (2022-01-20), later in *Qualitative Theory of Dynamical Systems*, DOI: 10.1007/s12346-024-00991-4.
2. Armengol Gasull, *Some open problems in low-dimensional dynamical systems*, arXiv:2012.02524v1 (2020-12-04), Problem 3.
3. W. Aziz, J. Llibre, and C. Pantazi, *Centers of quasi-homogeneous polynomial differential equations of degree three*, *Advances in Mathematics* **254** (2014), 233–250, DOI: 10.1016/j.aim.2013.12.006.
4. A. Cima, A. Gasull, and F. Mañosas, *Cyclicity of a family of vector fields*, *Journal of Mathematical Analysis and Applications* (1995), DOI: 10.1006/jmaa.1995.1451 (historical comparison; complete text not inspected).
