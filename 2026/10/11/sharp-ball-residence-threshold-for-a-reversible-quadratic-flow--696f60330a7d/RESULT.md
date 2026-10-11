# Sharp ball-residence threshold for a reversible quadratic flow

## Finding
Consider the Li–Sprott constant-forced quadratic flow
\[
\dot x=1+yz,\qquad \dot y=-xz,\qquad \dot z=y^2+ayz,
\]
where \(a\in\mathbb R\). Put \(B_R=\{(x,y,z):x^2+y^2+z^2\le R^2\}\) for \(R>0\). Define \(\tau_a(R)\) as the supremum of lengths of solution segments lying entirely in \(B_R\); an equilibrium segment can have arbitrary length.

**Sharp residence theorem.** Exactly when \(a>0\) and \(R\ge\sqrt{a+a^{-1}}\), one has \(\tau_a(R)=+\infty\). In every other case \(\tau_a(R)\) is finite, with explicit bounds
\[
\begin{aligned}
\tau_a(R)&\le\frac{2R\sqrt{1+a^2}}{-a}&& (a<0),\\
\tau_0(R)&\le4R+2R^3,\\
\tau_a(R)&\le\frac{2R\sqrt{(a+a^{-1})^2+(1-a^{-2})^2}}{a+a^{-1}-R^2}&& (a>0,\ R<\sqrt{a+a^{-1}}).
\end{aligned}
\]
Hence the least possible maximum Euclidean norm of a nonempty compact invariant set is exactly \(\sqrt{a+a^{-1}}\) when \(a>0\); when \(a\le0\) there is no nonempty compact invariant set.

For every compactly supported invariant probability measure \(\mu\), necessarily \(a>0\), and
\[
\int y^2\,d\mu=a,\qquad \int yz\,d\mu=-1,\qquad
\int (x^2+y^2+z^2)\,d\mu=a+a^{-1}+\int\left[x^2+(z+y/a)^2\right]d\mu.
\]
Equality in the resulting lower bound \(\int(x^2+y^2+z^2)d\mu\ge a+a^{-1}\) holds if and only if \(\mu\) is a convex combination of the two equilibrium point masses at \(E_\pm=(0,\pm\sqrt a,\mp a^{-1/2})\).

## Assumptions and scope
All statements concern classical maximal solutions of the displayed autonomous polynomial vector field, over real parameters and Euclidean state space. A solution segment may be a restriction of a longer orbit; no global completeness is presupposed. A compact invariant set is nonempty and invariant under the two-sided flow for all time, which is well-defined on it by bounded continuation. The compact support condition on an invariant probability measure ensures all test observables below are integrable and permits differentiation of stationary expectations. The result excludes residence in any *fixed* subcritical ball, not the possibility of large bounded trajectories for positive \(a\).

## Proof
Write \(r^2=x^2+y^2+z^2\). Direct differentiation yields the two identities
\[
P=z-ax,\qquad \dot P=y^2-a,
\]
\[
G=(a+a^{-1})x-(1-a^{-2})z,\qquad
\dot G=(a+a^{-1})-r^2+x^2+(z+y/a)^2 \quad(a\ne0).
\]
Both are pointwise polynomial identities for any solution where the parameter expression is defined.

For \(a<0\), \(\dot P\ge-a>0\). On \(B_R\), Cauchy–Schwarz gives \(|P|\le R\sqrt{1+a^2}\). Integrating \(\dot P\) between any two times of a segment confined to the ball gives \((-a)T\le2R\sqrt{1+a^2}\), proving the first bound.

For \(a=0\), \(\dot z=y^2\), hence confinement gives \(\int_0^T y(t)^2dt\le2R\). Integrating the first equation and using Cauchy–Schwarz,
\[
T=\Delta x-\int_0^T yz\,dt\le2R+R\sqrt{2RT}.
\]
Since \(R\sqrt{2RT}\le T/2+R^3\), this implies \(T\le4R+2R^3\). No assumption on the direction of the segment is needed: translate its initial time to zero.

For \(a>0\), if \(R<\sqrt{a+a^{-1}}\), the second identity gives \(\dot G\ge a+a^{-1}-R^2>0\) at every point of the closed ball. There \(|G|\le R\sqrt{(a+a^{-1})^2+(1-a^{-2})^2}\). Integrating gives the stated third bound.

For \(a>0\) there are exactly two equilibria. Indeed, \(\dot y=0\) implies \(xz=0\); \(z=0\) contradicts \(\dot x=1\), so \(x=0\). Then \(yz=-1\), and \(\dot z=y(y+az)=0\) forces \(y^2=a\) and \(z=-y/a\). Thus they are \(E_\pm=(0,\pm\sqrt a,\mp a^{-1/2})\), each of radius \(\sqrt{a+a^{-1}}\). For \(a\le0\) there is no equilibrium. Each equilibrium produces an arbitrarily long segment in any ball containing it, establishing sharpness including equality. Any compact invariant set fits into some finite centered ball; the previously established uniform finite residence bounds rule out such a set for \(a\le0\), and rule out all compact invariant sets contained in a subcritical ball for \(a>0\).

For compactly supported invariant \(\mu\), stationarity applied to \(x\) and \(P\) yields \(\int yz\,d\mu=-1\) and \(\int y^2\,d\mu=a\). In particular \(a>0\), since the first equality excludes \(a=0\). Stationarity applied to \(G\) and its identity yields the radial-moment equality, with both defect terms nonnegative. If equality holds, continuity and nonnegativity force support in \(x=0\), \(z=-y/a\). Every orbit in the support remains in this closed subset by invariance; along it, \(\dot x=1+yz=1-y^2/a\) must vanish, whence \(y=\pm\sqrt a\). Thus the support is contained in \(\{E_+,E_-\}\). Conversely, any convex combination of their point masses is invariant and attains equality. This proves the stated classification of the minimizers.

## Verification
The accompanying standalone `check.py`, using SymPy, verifies the Lie-derivative identities, the equivalent stationary square decomposition, and ten exact equilibrium substitutions at rational positive parameters. Execute `python check.py` in a Python environment with SymPy. The unbounded-time residence assertion, invariant-set exclusion, and measure equality classification follow from the preceding analytical proof and are **not** asserted on the strength of finite symbolic checks alone.

## Relationship to prior work
Li and Sprott introduced this exact vector field as their constant-forced case B and described its equilibria and numerically observed periodic and chaotic behavior. Sprott's subsequent reversible-flow study analyzed its symmetry, Lyapunov exponents and attractor/repellor pair. Li and Sprott later used the same equations as a seed for a modified flow with a plane of equilibria. None of these inspected sections states the coefficient-uniform sharp Euclidean ball-residence threshold, explicit uniform passage-time bounds, or equality characterization of stationary radial moments. Those conclusions distinguish this result from equilibrium existence or numerical bifurcation plots. Analogous moment identities proved elsewhere for different jerk or quadratic-only vector fields do not imply a bound for this particular constant-forced system.

## Limitations
The theorem is deliberately formulated in terms of residence inside closed **centered Euclidean balls**; it does not give the minimal residence time in arbitrary sets, nor does it establish existence of chaotic invariant sets. For positive parameter, compact invariant sets may have larger radius than the equilibrium radius. No uniform-in-parameter residence bound near zero is claimed: the exact threshold diverges like \(a^{-1/2}\) as \(a\downarrow0\). Numerical statements in the original literature, including a reported cycle emerging near zero parameter, are not treated as rigorous existence claims. Other historical formulations of the same bounds may exist outside the literature inspected here.

## References
1. C. Li and J. C. Sprott, “Chaotic flows with a single nonquadratic term,” *Physics Letters A* **378** (2014), 178–183, DOI: 10.1016/j.physleta.2013.11.004. First available online 2013-11-15. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper411.pdf.
2. J. C. Sprott, “Symmetric Time-Reversible Flows with a Strange Attractor,” *International Journal of Bifurcation and Chaos* **25** (2015), 1550078, DOI: 10.1142/S0218127415500789. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper433.pdf.
3. C. Li and J. C. Sprott, “How to Bridge Attractors and Repellors,” *International Journal of Bifurcation and Chaos* **27** (2017), 1750149, DOI: 10.1142/S0218127417501498. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper478.pdf.
