# Global recurrence fold and logarithmic critical slowing in the negative-forcing Sprott M flow

## Finding

**Theorem.** Consider the polynomial flow
\[\dot x=-z,\qquad\dot y=-x^2-y,\qquad\dot z=a+bx+y,\]
with \(b>0\), \(a<0\), and discriminant \(\Delta=b^2+4a\). A nonempty compact, two-sided invariant set exists if and only if \(\Delta\ge0\). For \(\Delta<0\) no bounded forward-complete solution exists. If \(\Delta=0\), the sole compact two-sided invariant set is the equilibrium \(E=(b/2,-b^2/4,0)\), and every bounded forward-complete trajectory converges to \(E\).

At this critical parameter, define the global strong-stable set as those initial states whose forward trajectories exist globally and converge to \(E\) at some exponential rate. Every bounded forward-complete trajectory outside that set eventually has \(x(t)<b/2\) and obeys
\[-\frac{b}{x(t)-b/2}=t+\frac{2}{b}\log t+C+o(1),\qquad t\to\infty,\]
for a finite constant \(C\) depending on the trajectory. The algebraic case is realized by local nonstationary solutions. For \(-b^2/4<a<0\), the two equilibria \(E_\pm=(r_\pm,-r_\pm^2,0)\), \(r_\pm=(b\pm\sqrt\Delta)/2\), consist of a hyperbolic sink \(E_-\) and an index-one hyperbolic saddle \(E_+\).

## Assumptions and scope

Parameters are constant real numbers with \(b>0\) and \(a<0\). A forward-complete solution is defined on \([0,\infty)\); boundedness means its three coordinates remain bounded there. A compact **two-sided invariant** set consists of complete trajectories defined for all real times, and is mapped onto itself by every time map. The theorem does not assert that every forward-invariant compact set consists only of an equilibrium: a bounded transient trajectory together with its closure may be forward invariant.

The asymptotic statement applies only at the fold \(a=-b^2/4\) and only to bounded forward-complete solutions outside the exponentially convergent strong-stable set. The constant \(C\) is not universal, while the coefficient \(2/b\) of the logarithm is universal in this stated family.

## Proof

Set \(Q=y+z\). The vector field gives the exact identity
\[\dot Q=a+bx-x^2=\frac{\Delta}{4}-(x-b/2)^2.\]
When \(\Delta<0\), \(Q(t)\le Q(0)+t\Delta/4\), inconsistent with a bounded forward trajectory. When \(\Delta\ge0\), the equation for equilibria \(x^2-bx-a=0\), with \(z=0\), \(y=-x^2\), has at least one real solution. This proves the sharp existence threshold.

At \(\Delta=0\), \(\dot Q=-(x-b/2)^2\). If a forward orbit is bounded, \(Q\) is bounded and monotone, so \(\int_0^\infty(x-b/2)^2\,dt<\infty\). Because the bounded polynomial vector field bounds \(\dot x\), the square-integrable function \(x-b/2\) is uniformly continuous and tends to zero. Boundedness of \(\ddot x=-\dot z\) and convergence of \(x\) then imply \(\dot x=-z\to0\); finally the stable scalar equation \(\dot y+y=-x^2\) gives \(y\to-b^2/4\). Thus each bounded forward orbit tends to \(E\).

For a bounded complete orbit, boundedness of \(Q\) on the whole real axis yields \(\int_{-\infty}^{\infty}(x(t)-b/2)^2\,dt<\infty\). The uniform-continuity argument applies at both temporal ends, giving \(x(t)\to b/2\), and bounded second derivatives again imply \(z(t)\to0\), as \(t\to\pm\infty\). Moreover, the unique bounded complete solution of the scalar equation is \(y(t)=-\int_{-\infty}^t e^{-(t-s)}x(s)^2\,ds\), which converges to \(-b^2/4\) at both temporal ends by dominated convergence. The monotone function \(Q\) has the same limit \(-b^2/4\) at both ends, hence is constant. Its derivative forces \(x=b/2\), and the equations then force the orbit to equal \(E\). This proves two-sided invariant-set rigidity.

To calculate the critical approach, introduce \(u=x-b/2\), \(w=z\), and \(h=y+b^2/4+bu\). The shifted equations are exactly
\[\dot u=-w,\qquad\dot w=h,\qquad\dot h=-h-bw-u^2.\]
The equilibrium has one zero eigenvalue and transverse characteristic factor \(\lambda^2+\lambda+b\), whose roots have strictly negative real parts for \(b>0\). On any smooth local center manifold written \(w=W(u)\), \(h=H(u)\), tangency and invariance give
\[W(u)=-u^2/b+2u^3/b^3+O(u^4),\qquad H(u)=-2u^3/b^2+O(u^4).\]
Consequently the reduced scalar equation is \(\dot u=u^2/b-2u^3/b^3+O(u^4)\). Its only nonconstant forward solutions staying near and approaching zero lie eventually on \(u<0\). Standard stable-foliation estimates for an equilibrium with a one-dimensional center and a hyperbolic stable complement imply that every convergent trajectory either belongs to the strong-stable set or exponentially shadows one of these negative-center trajectories. The latter may be chosen to remain near zero for all positive time, proving existence of the algebraic branch.

For \(u<0\) put \(R=-b/u\). Along the reduced center dynamics,
\[\dot R=1+\frac{2}{bR}+O(R^{-2}).\]
It follows first that \(R/t\to1\), then that \(R-t-(2/b)\log t\) converges to a finite constant: after \(R=t+O(\log t)\), its derivative is \(O((\log t)/t^2)\), which is integrable. Exponential tracking changes the expression by \(o(1)\), so the same expansion holds on all non-strong-stable bounded forward trajectories.

For \(-b^2/4<a<0\), put \(s=\sqrt\Delta\). Because \(0<s<b\), the Jacobian at \(E_r=(r,-r^2,0)\) has characteristic polynomial \(\lambda^3+\lambda^2+b\lambda+(b-2r)\). At \(r_-= (b-s)/2\), its constant coefficient is \(s\), and the Routh–Hurwitz conditions \(1>0\), \(b>0\), \(s>0\), \(b>s\) give a hyperbolic sink. At \(r_+=(b+s)/2\), its constant term is \(-s\); it has exactly one positive real root by Descartes' rule, and the remaining roots have negative real parts because their sum is negative and product positive. Hence the upper equilibrium has one unstable direction.

## Verification

The accompanying `verify.py` uses SymPy to check the exact monotonicity identity, both equilibrium characteristic polynomials, the necessary cubic center-manifold coefficients, and the resulting logarithmic coefficient. These algebraic calculations can be reproduced using `python verify.py` with SymPy installed. They do not substitute for the bounded-orbit argument or standard stable-foliation theorem, which are proved or explicitly invoked above. Numerical integrations were used as a diagnostic, not as proof of any infinite-time assertion.

## Relationship to prior work

Sprott's 1994 paper introduced Case M at a specified positive forcing and investigated its chaotic behavior numerically. The 2012 generalized-system synchronization study and Sprott's later parameter-region note discuss related positive-parameter dynamics or controlled errors, not the negative-forcing global recurrence boundary and its explicit logarithmic critical relaxation. General saddle-node theory predicts a leading algebraic scale locally, but not this model's global compact-invariance obstruction or its computed \(2/b\) logarithmic coefficient. This theorem concerns only \(a<0\), not the positive-forcing recurrent regimes.

## Limitations

The result does not classify periodic, chaotic, or homoclinic compact invariant sets when \(-b^2/4<a<0\), nor does it assert that solutions starting outside the bounded basin at the fold are forward complete. No global bound on the number or size of other invariant sets is proved. The full historical literature may contain equivalent normal-form computations not found in the inspected sources; the mathematical novelty comparison is not an independent certification.

## References

1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E **50**, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647, https://sprott.physics.wisc.edu/pubs/paper212.pdf.
2. S. Vaidyanathan, *Global chaos synchronization of Sprott-L and Sprott-M systems by active control*, International Journal of Control Theory and Computer Modelling **2** (2012), DOI: 10.5121/ijctcm.2012.2402, https://airccse.org/journal/ijctcm/papers/2412ijctcm02.pdf.
3. J. C. Sprott, *Dynamic Regions in Simple Chaotic Flows* (2013; revised 2014), https://sprott.physics.wisc.edu/technote/regions.htm.
4. J. Carr, *Applications of Centre Manifold Theory*, Springer (1981), standard reference for local center manifolds and stable foliations.
