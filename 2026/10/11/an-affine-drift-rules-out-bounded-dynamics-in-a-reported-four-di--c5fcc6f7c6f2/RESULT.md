# An affine drift rules out bounded dynamics in a reported four-dimensional Sprott-S extension
## Finding
For the four-dimensional system
\[
\dot x=-x-4y,\qquad
\dot y=x+z^2+a w,\qquad
\dot z=1+x,\qquad
\dot w=-b y,
\]
define
\[
F(x,z,w)=w-\frac{b}{4}(x+z).
\]
For every classical solution,
\[
\dot F=-\frac{b}{4}.
\]
Therefore, if \(b\ne0\), every forward-complete trajectory is unbounded. The flow has no nonempty compact positively invariant set, no periodic orbit, no compact attractor, and no compactly supported invariant probability measure. This includes all positive values of \(b\) used in the 2021 source.

## Assumptions and scope
The claim concerns the exact autonomous polynomial vector field printed as system (2) in Al-hayali and Al-Azzawi (2021). The parameter \(a\) is arbitrary and \(b\ne0\). The source assumes \(a>0\) and \(b>0\), so its parameter range is contained in the theorem. “Forward-complete” means that the classical solution exists for all \(t\ge0\). The conclusion does not assert that every initial condition is forward-complete; finite-time blow-up is logically compatible with the theorem.

The boundary \(b=0\) is excluded because the affine drift vanishes there. The theorem also does not apply to the altered 2022 follow-up model, whose fourth equation contains an additional nonlinear term.

## Proof
Differentiate \(F\) along the printed vector field. Since
\[
\dot x+\dot z=(-x-4y)+(1+x)=1-4y,
\]
one obtains
\[
\begin{aligned}
\dot F
&=\dot w-\frac{b}{4}(\dot x+\dot z)\\
&=-by-\frac{b}{4}(1-4y)\\
&=-\frac{b}{4}.
\end{aligned}
\]
Thus
\[
F(t)=F(0)-\frac{b}{4}t.
\]
If \(b\ne0\), the right-hand side is unbounded as \(t\to\infty\). Because \(F\) is affine in \(x,z,w\), a forward-complete solution with bounded state coordinates would make \(F(t)\) bounded, a contradiction. Hence every forward-complete trajectory is unbounded.

A nonempty compact positively invariant set would contain a forward-complete bounded trajectory, so no such set exists. Periodic orbits and compact attractors are special cases. If a compactly supported invariant probability measure \(\mu\) existed, invariance and the identity above would give, for every \(t>0\),
\[
\int F\,d\mu=\int F\circ\phi_t\,d\mu
=\int F\,d\mu-\frac{b}{4}t,
\]
which is impossible when \(b\ne0\). This proves the measure statement.

## Verification
The accompanying `VERIFY.py` performs an exact rational-coefficient polynomial check of the Lie derivative of \(F\) and confirms that every state-dependent monomial cancels, leaving precisely \(-b/4\). The compactness and invariant-measure consequences use only the displayed affine identity and standard definitions; no finite numerical orbit is used as proof.

As a numerical-scale consistency observation, the source’s Lyapunov calculation uses \(b=0.001\) over \(T=300\), for which the exact change in \(F\) is only \(-0.075\). A finite plot can therefore look slowly drifting even though bounded recurrence is impossible asymptotically. This observation is not needed for the theorem.

## Relationship to prior work
The 2021 source introduces the exact vector field above, states that its parameters are positive, reports hidden chaotic attractors, and reports coexisting attractors for parameter choices including \(b=20\) and \(b=80\). Its analysis discusses equilibria, Lyapunov exponents, divergence, and numerical multistability, but the inspected full text does not state the affine drift identity or its global boundedness consequence.

A 2022 paper by the same authors explicitly constructs a different Sprott-S extension with a single equilibrium point; its leading mathematical classification is 34H10. That follow-up is not covered by the theorem because its fourth equation is modified. A 2023 Mathematics paper reproduces the 2021 vector field and treats it as a bounded hyperchaotic attractor in a network-control example. The exact affine drift shows that such a bounded invariant-attractor interpretation is incompatible with the reproduced autonomous ODE whenever \(b\ne0\).

Searches for the system title, exact affine combination, boundedness consequences, first-integral/coboundary aliases, and implication-equivalent compact-invariance statements did not locate a published statement implying this theorem. Related indexed results for other Sprott extensions use different vector fields and different conserved or balance quantities.

## Limitations
The theorem is about the equations as printed, not about an intended but different implementation. It does not classify finite-time transient geometry, numerical discretizations, controlled/network-coupled systems, or the \(b=0\) boundary. Absence of a compact invariant set does not by itself determine whether a given solution escapes only as \(t\to\infty\) or ceases to exist in finite time. Literature searching is necessarily finite, so an unindexed equivalent statement remains a residual originality risk.

## References
1. M. A. Al-hayali and S. F. Al-Azzawi, “A 4D hyperchaotic Sprott S system with multistability and hidden attractors,” *Journal of Physics: Conference Series* 1879 (2021), 032031. DOI: 10.1088/1742-6596/1879/3/032031.
2. S. F. Al-Azzawi and M. A. Al-Hayali, “Coexisting of self-excited and hidden attractors in a new 4D hyperchaotic Sprott-S system with a single equilibrium point,” *Archives of Control Sciences* 32 (2022), 37–56. DOI: 10.24425/acs.2022.140863.
3. “Outer Synchronization of Two Muti-Layer Dynamical Complex Networks with Intermittent Pinning Control,” *Mathematics* 11 (2023), 3543. DOI: 10.3390/math11163543.
