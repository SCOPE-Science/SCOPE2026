# Complete bounded-orbit classification at the critical Sprott-R forcing plane

## Finding
Consider the two-parameter Sprott-R differential system
\[
\dot x=a-y,\qquad \dot y=b+z,\qquad \dot z=xy-z,
\]
with \((x,y,z)\in\mathbb R^3\) and \((a,b)\in\mathbb R^2\). On the natural zero-restoring plane \(a=0\), define
\[
H=y+z+\frac{x^2}{2}.
\]
Then \(\dot H=b\). In particular, if \(a=0\) and \(b\ne0\), no forward-complete bounded orbit and no nonempty compact invariant set exist.

At \(a=b=0\), every leaf \(H=h\), for real \(h\), has the following **complete bounded-dynamics classification**:

1. If \(h<0\), there is no bounded forward orbit and no bounded complete orbit.
2. If \(h=0\), the origin is the only bounded complete orbit; every bounded forward orbit on the leaf converges to it.
3. If \(h>0\), put \(u=\sqrt{2h}\). The only bounded complete orbits on that leaf are the two equilibria \((u,0,0)\) and \((-u,0,0)\), and **exactly one nonconstant heteroclinic orbit up to time translation**, which connects \((u,0,0)\) in backward time to \((-u,0,0)\) in forward time. Every bounded forward orbit on the leaf converges to one of these two equilibria.

For that unique heteroclinic orbit the dissipated transverse action has the exact value
\[
\int_{-\infty}^{\infty}y(t)^2\,dt=\frac{2}{3}(2h)^{3/2}.
\]
Every compactly supported invariant probability measure for \(a=b=0\) is supported on the equilibrium line \(\{(x,0,0):x\in\mathbb R\}\), and every probability measure supported on that line is invariant.

## Assumptions and scope
The vector field is the polynomial field displayed above, without perturbations or external forcing, and solutions are considered on their maximal intervals of existence. "Bounded forward orbit" means a solution defined for all nonnegative time whose image is bounded. "Bounded complete orbit" means a solution defined on all of \(\mathbb R\) whose image is bounded. A compact invariant set is invariant under the full flow wherever defined, hence consists of bounded complete trajectories. The classification concerns the entire parameter plane \(a=0\) (all real \(b\)) and all real levels \(h\) when \(b=0\); it does not classify dynamics for \(a\ne0\).

## Proof
**1. Drift obstruction.** Direct differentiation, without restricting parameters, gives
\[
\dot H=(a-y)x+(b+z)+(xy-z)=b+ax.
\]
Thus when \(a=0\), \(H(t)=H(0)+bt\) throughout every solution's interval. If \(b\ne0\), a forward-complete orbit cannot stay in a bounded subset of \(\mathbb R^3\), because the polynomial \(H\) is bounded on bounded sets. A compact invariant set would contain bounded complete orbits, so none exists. Any compactly supported invariant measure would likewise give \(0=\int\dot H\,d\mu=b\), a contradiction.

**2. Exact leaf reduction.** Set \(a=b=0\), so \(H=h\) is constant. Put \(v=\dot x=-y\). Solving for the third coordinate gives
\[
y=-v,\qquad z=h+v-\frac{x^2}{2}.
\]
The restricted flow is exactly the planar damped equation
\[
\dot x=v,\qquad \dot v=\frac{x^2}{2}-h-v,
\]
or \(\ddot x+\dot x=x^2/2-h\). Define the cubic potential and energy
\[
U_h(x)=hx-\frac{x^3}{6},\qquad
E_h(x,v)=\frac{v^2}{2}+U_h(x).
\]
A complete differential identity is
\[
\frac{d}{dt}E_h(x(t),v(t))=-v(t)^2.
\]
The same identity holds directly in the original variables with the polynomial \(E=y^2/2+xH-x^3/6\) on the \(a=b=0\) field.

**3. Limit sets and convergence.** For a bounded forward trajectory, the decreasing energy has a finite limit. Its compact, nonempty omega-limit set lies in the largest invariant subset of \(\{v=0\}\) by the standard invariance principle: on \(v=0\), remaining there requires \(\dot v=x^2/2-h=0\). Consequently, if \(h<0\), bounded forward trajectories are impossible. If \(h=0\), the omega-limit set is the origin; if \(h>0\), it is contained in the two equilibria \((x,v)=(\pm u,0)\), where \(u=\sqrt{2h}\). The omega-limit set of a continuous bounded trajectory is connected, so it is one equilibrium, proving convergence. The same argument in backward time applies to alpha-limit sets of bounded complete trajectories, because the energy has a finite limit in each temporal direction and its derivative is nonpositive.

For \(h=0\), a nonstationary bounded complete trajectory would have the origin as both alpha- and omega-limit, and hence equal limiting energy at both ends. Integrating \(\dot E_h=-v^2\) over the full orbit forces \(v\equiv0\), a contradiction. Therefore only the origin is bounded and complete.

**4. Unique heteroclinic at each positive level.** Fix \(h>0\) and \(u=\sqrt{2h}\). The equilibrium \((u,0)\) is a hyperbolic saddle, since its linearization has characteristic polynomial \(\lambda^2+\lambda-u\); \((-u,0)\) is asymptotically stable, since its polynomial is \(\lambda^2+\lambda+u\). The unstable manifold of the saddle has two local branches. On one branch \(x<u\), \(v<0\), while on the other \(x>u\), \(v>0\).

On the left branch the strict energy inequality \(E_h<U_h(u)=u^3/3\) holds at every finite time, because the energy tends to \(U_h(u)\) backward and strictly decreases forward. The orbit therefore cannot cross \(x=u\), where the potential already equals \(U_h(u)\). It stays in \(x<u\); moreover \(U_h(x)\to+\infty\) as \(x\to-\infty\). The energy bound thus restricts \(x\) to a compact interval, and the kinetic term bounds \(v\). This branch exists globally forward and its omega-limit cannot be the saddle (its energy has strictly decreased); it converges to \((-u,0)\). It is the desired heteroclinic.

Any other nonstationary bounded complete trajectory would have equilibria as its two temporal limits and strictly decreasing energy. Since \(U_h(u)=u^3/3>U_h(-u)=-u^3/3\), its alpha-limit must be the saddle and its omega-limit the sink. It therefore belongs to the saddle's one-dimensional unstable manifold. The right branch cannot be bounded complete: its energy is strictly below \(U_h(u)\), so it cannot cross \(x=u\), while the leaf has no equilibrium at \(x>u\) that could be its omega-limit. Thus the left branch is the **only** nonconstant bounded complete orbit, up to time translation.

**5. Exact dissipation and stationary states.** The heteroclinic tends to its two endpoints, so integration of the energy identity gives
\[
\int_{\mathbb R}v(t)^2\,dt
=U_h(u)-U_h(-u)=\frac{2u^3}{3}
=\frac23(2h)^{3/2}.
\]
Since \(y=-v\), this is the claimed action law. For a compactly supported invariant probability measure at \(a=b=0\), integration of the global polynomial identity \(\dot E=-y^2\) gives \(\int y^2\,d\mu=0\). Its invariant support lies in \(y=0\); invariance under \(\dot y=z\) then forces \(z=0\). Conversely all points on the line \(y=z=0\) are equilibria, so arbitrary probability distributions on that line are invariant.

## Verification
The standalone standard-library script `VERIFY.py` symbolically checks coefficient-by-coefficient, over exact rational arithmetic, the identities \(\dot H=b+ax\) and
\[
\dot E=-y^2+b(x+y)+a\left(H+\frac{x^2}{2}\right),
\qquad E=\frac{y^2}{2}+xH-\frac{x^3}{6},
\]
and the exact endpoint potential difference \(U_h(u)-U_h(-u)=2u^3/3\) when \(h=u^2/2\). Run `python3 VERIFY.py` to reproduce these algebraic checks. The global classification and uniqueness are analytic deductions in the proof, **not** consequences of finite numerical experiments or of the script alone.

## Relationship to prior work
Sprott's 1994 introducing article, *Some simple chaotic flows*, displays case R at nonzero parameters and reports a chaotic numerical trajectory. Sprott and Linz (2000), *Algebraically Simple Chaotic Flows*, derive its third-order jerk equation \(\dddot x+\ddot x-x\dot x+ax+b=0\) and show the nonzero-parameter attractor. Sprott's 2013 *Dynamic Regions in Simple Chaotic Flows* presents numerical two-parameter regions including case R. These sources motivate examination of the otherwise neglected zero-restoring and zero-forcing boundary; none of the inspected relevant passages establishes the complete bounded-leaf separatrix classification or its exact action. The jerk representation is algebraically equivalent to the present system and is not claimed as new.

## Limitations
This theorem makes no claim about the existence or uniqueness of attractors away from \(a=0\). It does not provide a closed elementary time parametrization for the heteroclinic. Its assertion about nonzero \(b\) excludes bounded forward-complete orbits but does not assert global existence of every unbounded orbit, nor does it classify finite-time escape. Other algebraically equivalent presentations or unindexed historical studies may contain the same zero-boundary classification; the literature comparison does not amount to a proof of absolute priority. Independent mathematical audit has not been performed.

## References
1. J. C. Sprott, *Some simple chaotic flows*, Physical Review E **50** (1994), R647–R650, DOI: 10.1103/PhysRevE.50.R647. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper212.pdf.
2. J. C. Sprott and S. J. Linz, *Algebraically Simple Chaotic Flows*, International Journal of Chaos Theory and Applications **5** (2000), 3–22. Author-hosted manuscript: https://sprott.physics.wisc.edu/pubs/paper250.pdf.
3. J. C. Sprott, *Dynamic Regions in Simple Chaotic Flows*, technical note dated April 27, 2013 (updated September 1, 2014): https://sprott.physics.wisc.edu/technote/regions.htm.
