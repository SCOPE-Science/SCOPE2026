# Gradient-like boundary and universal period slowdown in a plane-equilibrium quadratic flow

## Finding
Consider the real four-dimensional polynomial differential equation
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=w(y-az),\qquad
\dot w=bxz-y^2+z^2,\qquad a,b\in\mathbb R.
\]
Its equilibrium set is exactly the plane \(E=\{(x,0,0,w):x,w\in\mathbb R\}\). Put \(\Phi(x,y,z,w)=w-bxy\). The following three conclusions hold for the same two-parameter system.

**Gradient-like regime.** If \(b\leq-1\), then \(\Phi\) increases strictly between any two distinct times along every nonstationary solution. Therefore all recurrent points of the polynomial flow are equilibria and there are no nonconstant periodic solutions. Every bounded forward-complete trajectory satisfies \(\operatorname{dist}((x(t),y(t),z(t),w(t)),E)\to0\) and \(w(t)\to w_+\) for some finite real \(w_+\). Every compactly supported invariant probability measure is supported on \(E\). If a nonstationary solution is bounded and defined for all \(t\in\mathbb R\), its past and future limit sets lie in \(E\), its two limiting \(w\)-levels satisfy \(w_-<w_+\), and
\[
 w_+-w_- =\int_{-\infty}^{\infty}\left(z(t)^2-(1+b)y(t)^2\right)\,dt>0.
\]

**Stationary balance.** For arbitrary \(a,b\in\mathbb R\), every compactly supported invariant probability measure \(\mu\) satisfies
\[
\int z^2\,d\mu=(1+b)\int y^2\,d\mu.
\]
In particular, for \(b\leq-1\) the only such measures are probability measures supported on \(E\), and conversely every compactly supported probability measure on \(E\) is invariant.

**Strict period barrier.** If \(b>-1\), every nonconstant periodic orbit of period \(T\), if one exists, obeys
\[
 \boxed{T>\frac{2\pi}{\sqrt{1+b}}}.
\]
Consequently the periods of any family of nonconstant periodic orbits with \(b\downarrow-1\) diverge. No existence assertion for such periodic orbits at general parameters is made.

## Assumptions and scope
Parameters \(a,b\) are arbitrary real constants. Statements involving bounded trajectories refer to solutions that exist for the stated time interval and remain in a compact subset of \(\mathbb R^4\); bounded forward solutions are automatically forward complete for polynomial ODEs. An invariant probability measure is invariant under the ODE flow and has compact support. A recurrent point is one returned arbitrarily closely to its initial state at arbitrarily large positive times. Period denotes a positive return period of a nonconstant solution; the period inequality holds for any such period, in particular the least one. The limit assertions concern full phase-space trajectories and do not assert convergence of \(x(t)\).

The source is the four-dimensional plane-equilibrium flow of Jafari, Sprott and Molaie (2016), equation (6), whose reported chaotic example is \(a=4\), \(b=1/10\). The parameter partition here is intrinsic to an exact global scalar balance and is not a claim that nonstationary recurrence exists for every \(b>-1\).

## Proof
**1. The exact coboundary and equilibrium plane.** Direct differentiation, with no division by any coordinate, gives
\[
\begin{aligned}
\frac{d}{dt}(w-bxy)
&=(bxz-y^2+z^2)-b(y^2+xz)\\
&=z^2-(1+b)y^2.
\end{aligned}
\]
The first two equations show that an equilibrium requires \(y=z=0\), which conversely makes all four derivatives vanish. Thus the equilibrium set is \(E\).

**2. Strict monotonicity for \(b\leq-1\).** In this parameter range \(\dot\Phi\geq0\). If \(\Phi\) were constant throughout a nondegenerate interval, then \(z=0\) on that interval. It follows that \(\dot y=0\), hence \(y\) is constant. If that constant were nonzero, \(\dot z=wy=0\) would force \(w=0\) throughout the interval, contradicting \(\dot w=-y^2<0\) there. Thus \(y=z=0\), and the solution is an equilibrium. Uniqueness of solutions implies every nonstationary solution has \(\Phi(t_2)>\Phi(t_1)\) for \(t_2>t_1\) in its interval of existence. A positively recurrent nonequilibrium point would give arbitrarily late states approaching its initial state, contradicting strict increase and continuity of \(\Phi\).

**3. Bounded-orbit limit sets.** On a bounded forward orbit, \(\Phi\) is bounded above and nondecreasing, hence it has a finite limit. Its compact nonempty \(\omega\)-limit set is invariant and \(\Phi\) is constant on it. Every complete orbit inside this set must therefore be an equilibrium by step 2; hence \(\omega\subseteq E\). Thus \(y(t),z(t)\to0\), and because \(x(t)\) is bounded, \(b x(t)y(t)\to0\); consequently \(w(t)=\Phi(t)+b x(t)y(t)\to w_+\). For a bounded solution defined on the full line, the analogous argument applied to the compact \(\alpha\)-limit set yields \(\alpha\subseteq E\) and \(w(t)\to w_-\) as \(t\to-\infty\). Integrate the identity from step 1 over \([-R,R]\) and let \(R\to\infty\). The nonnegative integrand and the finite endpoint limits give the asserted exact improper integral. It is strictly positive for every nonstationary complete orbit, by step 2.

**4. Compact invariant measures.** If \(\mu\) is compactly supported and invariant, stationarity of the bounded-on-support differentiable function \(\Phi\) gives \(\int \dot\Phi\,d\mu=0\). The identity in step 1 proves the stated moment balance for all parameters. When \(b<-1\), its nonnegative integrand forces \(y=z=0\) on the support. At \(b=-1\), it forces \(z=0\) on the support. That support is invariant; hence any orbit contained in it with \(z=0\) has constant \(y\), and \(x(t)=x(0)+ty\). Compact support for all positive and negative times forces \(y=0\). Thus, in both cases, \(\operatorname{supp}\mu\subseteq E\). Conversely, every measure supported on the equilibrium plane is invariant.

**5. Period inequality and strictness.** Let \(b>-1\) and suppose a nonconstant solution has period \(T\). Since \(\dot x=y\), integration yields \(\int_0^T y(t)\,dt=0\). Moreover \(\dot y=z\), and integrating the scalar coboundary over one period gives
\[
\int_0^T \dot y(t)^2\,dt=(1+b)\int_0^T y(t)^2\,dt.
\]
The right integral is positive, since \(y\equiv0\) would imply \(z\equiv0\) and an equilibrium. Wirtinger's periodic zero-mean inequality therefore yields
\[
1+b=\frac{\int_0^T\dot y^2\,dt}{\int_0^T y^2\,dt}
\geq\left(\frac{2\pi}{T}\right)^2.
\]
If equality held, the equality case of Wirtinger's inequality would force \(y(t)=A\cos(\omega t)+B\sin(\omega t)\) with \(\omega=2\pi/T=\sqrt{1+b}\) and \(A^2+B^2>0\), so \(z=\dot y\) and \(\dot z=-\omega^2y\). If \(a\ne0\), a zero of the nonzero sinusoid \(y-az\) occurs at a time where \(y\ne0\). At that time the differential equation forces \(\dot z=w(y-az)=0\), contradicting \(\dot z=-\omega^2 y\ne0\). If \(a=0\), the equation \(\dot z=wy\) forces \(w=-\omega^2\) wherever \(y\ne0\), and hence identically by continuity. At an extremum of the sinusoid \(y\ne0\) and \(z=0\), however, \(\dot w=bxz-y^2+z^2=-y^2<0\), a contradiction. Equality is impossible, proving strictness.

## Verification
The accompanying standalone `verify.py` checks the polynomial identity \(\dot\Phi=z^2-(1+b)y^2\), the boundary specializations at \(b=-1\) and \(b=-2\), the equilibrium-plane substitution, and the auxiliary extremal identities using exact symbolic algebra. Run `python verify.py` with SymPy installed. The dynamical conclusions require the independent analytic limit-set and Wirtinger arguments in the proof; the script does not claim to certify them. The proof is not based on finite trajectory sampling or numerical simulations.

## Relationship to prior work
Jafari, Sprott and Molaie introduce this exact four-dimensional system and numerically study chaotic attraction and parameter scans for positive \(b\) (equation (6), figures 1–4 of the six-page original article). Their linearized equilibrium-plane analysis and numerical evidence do not supply the exact scalar coboundary, global recurrence exclusion for \(b\leq-1\), compact invariant-measure rigidity, or the strict universal period barrier. These statements also do not follow from the generic periodic Wirtinger inequality alone without first identifying the system-specific exact balance.

A later plane-equilibrium numerical study by Bayani and collaborators (2019) is topically plausible, but its complete text could not be obtained from lawful public sources; its abstract discusses numerical coexistence, bifurcation and offset boosting, not the particular analytical inequalities above. It is explicitly an unresolved literature-coverage risk, not evidence that its uninspected sections do not cover the result. General results about monotone Lyapunov functions or Wirtinger inequalities remain standard ingredients, not new claims.

## Limitations
The sign boundary \(b=-1\) is exact for nonnegativity of the displayed coboundary, not proved to be the precise threshold for existence of periodic or chaotic solutions. The lower bound for periods is strict but need not be sharp as an infimum. No claim is made about unbounded trajectories, about the convergence of the \(x\)-coordinate of every bounded orbit, or about uniqueness of invariant measures on the equilibrium plane. Historical equivalent formulas not indexed or not accessible remain possible. Independent audit has not been performed.

## References
1. S. Jafari, J. C. Sprott and M. Molaie, *A Simple Chaotic Flow with a Plane of Equilibria*, International Journal of Bifurcation and Chaos **26** (2016), article 1650098, DOI: 10.1142/S021812741650098X. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper443.pdf (equation (6), full six-page article; document records a publisher copy downloaded on 2016-06-29).
2. A. Bayani et al., *Dynamical analysis of a new multistable chaotic system with hidden attractor: Antimonotonicity, coexisting multiple attractors, and offset boosting*, Physics Letters A **383** (2019), 1450–1456, DOI: 10.1016/j.physleta.2019.02.005 (bibliographic data and abstract inspected; full text not available).
3. Periodic Wirtinger inequality and its equality characterization (classical, standard analytic ingredient, not claimed original).
