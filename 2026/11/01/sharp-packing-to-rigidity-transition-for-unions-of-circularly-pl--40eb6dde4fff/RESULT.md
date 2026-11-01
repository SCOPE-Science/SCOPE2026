# Sharp packing-to-rigidity transition for unions of circularly placed congruent disks

## Finding
Let \(m\ge3\), \(R>0\), and \(r>0\). Choose \(m\) (possibly repeated) centers \(c_j\) on the radius-\(R\) circle and form the union \(U=\bigcup_{j=1}^m \overline B(c_j,r)\). Put \(\phi=\pi/m\), \(s=\sin\phi\), \(c=\cos\phi\), and \(q=\sqrt{r^2-R^2s^2}\) whenever \(r\ge Rs\). Then the largest possible union area \(A_*(m,R,r)\) is exactly
\[
 A_*=
 \begin{cases}
 m\pi r^2, &0<r\le Rs,\\
 2m\bigl[Rs q+r^2\arcsin(Rs/r)\bigr],&Rs<r<R,\\
 m\bigl[r^2\phi+R^2sc+Rs q+r^2\arcsin(Rs/r)\bigr],&r\ge R.
 \end{cases}
\]
The optimizer undergoes a **sharp rigidity transition** at \(r=R\sin(\pi/m)\). Below this radius, every configuration with all cyclic consecutive center-angle gaps at least \(2\arcsin(r/R)\) is optimal, and these are exactly all optimizers. At the transition and above it, exactly the regular \(m\)-gon center configurations, up to rotation and permutation, are optimal. In particular there is genuine nonuniqueness for \(r<Rs\).

For a near-regular configuration write its consecutive angle gaps as \(g_j=2\phi+\delta_j\), where \(\sum_j\delta_j=0\), and let \(A(\boldsymbol\delta)\) be the union area. At the critical radius \(r=Rs\), its sharp stability law is
\[
 A_*-A(\boldsymbol\delta)
 =\frac43\sqrt{Rs}\,(R\cos\phi)^{3/2}
 \sum_{j=1}^m(-\delta_j)_+^{3/2}
 +O_{m,R}(\|\boldsymbol\delta\|^{5/2})
 \quad(\boldsymbol\delta\to0).
\]
For every fixed \(r>Rs\), it instead has a strictly quadratic expansion
\[
 A_*-A(\boldsymbol\delta)
 =\frac{H}{2}\sum_j\delta_j^2+o_{m,R,r}(\|\boldsymbol\delta\|^2),
 \quad H=\begin{cases}
 \displaystyle \frac{Rs(q^2+R^2c^2)}q,&Rs<r\le R,\\
 \displaystyle \frac{Rs(Rc+q)^2}{2q},&r\ge R.
 \end{cases}
\]
The two displayed expressions for \(H\) agree at \(r=R\). Thus the order of stability changes sharply from flat below the packing threshold, to a \(3/2\)-power contact cusp at it, to quadratic above it.

For every \(r\) and every concentric probe circle of radius \(\rho\), the regular arrangement simultaneously maximizes its covered angular measure. More precisely, when \(|R-r|<\rho<R+r\), put
\[
 \alpha(\rho)=\arccos\frac{R^2+\rho^2-r^2}{2R\rho}.
\]
If the cyclic angular gaps of the centers are \(g_1,\ldots,g_m\), their covered angular measure is exactly
\[
 C_U(\rho)=\sum_{j=1}^m\min\{g_j,2\alpha(\rho)\}
 \le\min\{2\pi,2m\alpha(\rho)\}.
\]
Outside this partial-coverage annulus, coverage is zero when \(\rho>R+r\) or \(r<R\) and \(\rho<R-r\), and it is full when \(r>R\) and \(\rho<r-R\). Hence the regular centers maximize integrals against every nonnegative radial area density, not just ordinary area.

In the large-disk regime, if \(P_m\) is the regular \(m\)-gon formed by the centers, the union's deviation from the area of the Minkowski parallel body satisfies
\[
 \operatorname{Area}(P_m+rB_2)-A_*
 =\frac{mR^3\sin^3(\pi/m)}{3r}+O_{m,R}(r^{-3})
 \quad(r\to\infty).
\]

## Assumptions and scope
All disks have one common positive radius \(r\). Their centers are constrained to the complete circle of fixed radius \(R\) about the origin and may repeat. Only planar Lebesgue area is used. The parameter \(m\) is any integer at least three. At the threshold, tangencies are permitted, and the optimizer is still unique among unordered center multisets up to common rotation. Local gap perturbations must keep every gap positive, which is automatic sufficiently close to the regular arrangement. The term \((x)_+\) means \(\max\{x,0\}\). Error constants keep \(m,R\) (and, for the quadratic statement, \(r\)) fixed.

## Proof
**1. Radial circle-coverage identity.** At distance \(\rho>0\) from the origin, the intersection of a radius-\(r\) disk centered at argument \(\theta_j\) with the probe circle comprises directions within \(\alpha(\rho)\) of \(\theta_j\), whenever \(|R-r|<\rho<R+r\). This follows from the law of cosines applied to the triangle with sides \(R,\rho,r\). For cyclic center gaps \(g_j\), the uncovered portion of the \(j\)-th gap is \((g_j-2\alpha)_+\). Therefore its covered portion is \(\min(g_j,2\alpha)\), proving the exact formula. The inequality follows from \(\sum_jg_j=2\pi\) and \(\min(g_j,t)\le g_j,t\). Equal gaps attain equality at every \(\rho\). Integrate \(\rho C_U(\rho)\,d\rho\), adding the complete inner disk when \(r>R\), to establish universal radial-area optimality.

**2. Equality classification.** If \(r<R\), the maximal halfwidth among partially covered probe radii is \(\arcsin(r/R)\), attained at \(\rho=\sqrt{R^2-r^2}\). If \(r\ge R\), the halfwidth attains or approaches \(\pi\) near \(\rho=r-R\) (or \(\rho=0\) at equality). If \(r<R\sin\phi\), the regular radius-\(r\) disks are pairwise interior-disjoint; maximal area equals \(m\pi r^2\). A family has this area exactly when every pair of disks is interior-disjoint, equivalent for circular centers to each cyclic gap being at least \(2\arcsin(r/R)\). At equality \(r=R\sin\phi\), the only way \(m\) cyclic gaps can all exceed or equal \(2\phi\) and sum to \(2\pi\) is equality throughout. For \(r>R\sin\phi\), unequal gaps necessarily have one gap shorter than \(2\phi\). Choosing angular coverage thresholds just below \(2\phi\), which occur over a positive-measure set of radii because \(\max\alpha>\phi\), makes the truncated-gap sum strictly smaller than its equal-gap value. Ordinary area is therefore strictly smaller. This proves uniqueness above the threshold as well.

**3. Exact area of the regular union.** In the wedge subtended by \(-\phi\le\theta\le\phi\) around a center on the positive horizontal axis, the only relevant disk is the one centered at \((R,0)\): angular proximity ensures that if a radial point is covered by another disk, it is covered by this one. Its radial intersections solve
\[
 \rho^2-2R\rho\cos\theta+R^2-r^2=0,
 \quad\rho_{\pm}(\theta)=R\cos\theta\pm\sqrt{r^2-R^2\sin^2\theta}.
\]
For \(r\le Rs\), disjointness gives the first branch. For \(Rs<r<R\), both roots are positive for every \(|\theta|\le\phi\), so the union area is
\[
 m\int_{-\phi}^{\phi}\tfrac12(\rho_+^2-\rho_-^2)\,d\theta
 =4mR\int_0^{\phi}\cos\theta\sqrt{r^2-R^2\sin^2\theta}\,d\theta,
\]
which evaluates to the second branch by substituting \(u=R\sin\theta\). For \(r\ge R\), the radial interval starts at zero; the corresponding integral \(m\int_0^\phi\rho_+(\theta)^2\,d\theta\) evaluates to the third branch. Both branches agree continuously at \(r=R\), and the first two agree at \(r=Rs\).

**4. Sharp cusp at first tangency.** At \(r=Rs\), neighboring disks of the regular configuration are externally tangent and all other pairs have positive separation (when \(m=3\), every pair is neighboring). The pairwise contact points are distinct, so there are no triple intersections in a sufficiently small neighborhood of the regular arrangement. For a perturbed gap \(2\phi+\delta_j\), the separation of the corresponding centers is
\[
 d_j=2R\sin(\phi+\delta_j/2)
 =2r+R\cos\phi\,\delta_j+O(\delta_j^2).
\]
The intersection lens area of two disks of radius \(r\) separated by \(d\uparrow2r\) is
\[
 L_r(d)=2r^2\arccos(d/(2r))
 -\frac d2\sqrt{4r^2-d^2}
 =\frac43\sqrt r\,(2r-d)^{3/2}+O_r((2r-d)^{5/2}).
\]
The union deficit equals the sum of precisely these local overlap lenses, proving the displayed cusp with uniform remainder.

**5. Strict quadratic stability.** Let \(F(g)=\int\rho\min\{g,2\alpha(\rho)\}\,d\rho\), where the integral ranges over partial-coverage probe radii and the full-inner-disk area is independent of gaps. Then \(\operatorname{Area}(U)=\mathrm{constant}+\sum_jF(g_j)\). At a gap \(g\) near \(2\phi\), the superlevel set \(2\alpha(\rho)\ge g\) is the radial interval between the quadratic roots
\[
 R\cos(g/2)\pm\sqrt{r^2-R^2\sin^2(g/2)},
\]
with the lower endpoint clipped to zero for \(r\ge R\). Differentiating under the integral gives
\[
 F'(g)=\tfrac12\left[\bigl(R\cos(g/2)+q_g\bigr)^2-
 \bigl(\max\{0,R\cos(g/2)-q_g\}\bigr)^2\right],
 \quad q_g=\sqrt{r^2-R^2\sin^2(g/2)}.
\]
One more differentiation at \(g=2\phi\) yields \(-F''(2\phi)=H\) in the two branches of the finding; \(H>0\). Taylor expansion in the gaps, using \(\sum\delta_j=0\), eliminates the first-order term and yields the quadratic law.

**6. Parallel-body comparison.** The Steiner formula for the regular center polygon is \(\operatorname{Area}(P_m+rB_2)=\pi r^2+2mRsr+mR^2sc\). Expanding the third exact-area branch with \(q=r-R^2s^2/(2r)+O(r^{-3})\) and \(\arcsin(Rs/r)=Rs/r+R^3s^3/(6r^3)+O(r^{-5})\) proves the asserted deficit.

## Verification
The accompanying `verify.py`, executable with Python 3 and no third-party dependencies, directly intersects rays with each disk, merges intervals, and numerically integrates their squared-radius contributions. It compares independently computed union areas with all three exact branches across four polygon orders and five radii each, including threshold cases, checks dozens of nonregular configurations against the sharp optimum, tests the contact-cusp coefficient at multiple perturbation scales, and checks the finite-difference quadratic curvature. The performed run printed `ALL_CHECKS_PASSED`. These finite numerical diagnostics do not establish the universal or asymptotic assertions; the proofs above do.

## Relationship to prior work
Finch, *Union of n Disks: Remote Centers, Common Origin* (2015), develops union-area expressions under simultaneous remote-center and common-boundary-origin assumptions. In particular the common-origin condition corresponds to the special radius equality \(r=R\) for equal circularly placed disks; the present claim does not assert that arbitrary union-area evaluation is new. Neither the sharp all-radius optimizer-family transition nor the contact stability law follows from that restriction. Basit and Lángi (2023) study disk-polygons constructed by **intersections**, rather than the unions here. Existing exact circular-gap laws for **intersections** of congruent disks with centers on a circle are likewise opposite set operations and do not supply this union rigidity threshold. Existing radial-coverage inequalities for unions of co-centered rotated regular polygons have a related angular-coverage principle but different geometric inputs; those inequalities alone do not yield the closed disk-union area branches and the nonquadratic contact law. The originality claim is restricted to their combined sharp, radius-dependent classification and stability, not to elementary arc truncation by itself.

## Limitations
The disks must have equal radii and their centers must lie on the fixed circle. No claim is made for arbitrary center domains, unequal disks, higher dimensions, or weighted densities that vanish on all radii where an optimizer is distinguishable. The cusp and quadratic expansions fix \(m,R\) and concern sufficiently small angular-gap perturbations; no global quantitative stability bound is claimed. Historical novelty is assessed against the materially inspected sources rather than proved exhaustively, and no independent audit has been performed.

## References
1. Bushra Basit and Zsolt Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026v1, first public 2023-07-08. https://arxiv.org/html/2307.04026v5
2. Steven Finch, *Union of n Disks: Remote Centers, Common Origin*, arXiv:1511.04968v1, 2015-11-16. https://arxiv.org/html/1511.04968v1
3. Viktor Kiss and Zoltán Vidnyánszky, *Unions of regular polygons with large perimeter-to-area ratio*, arXiv:1402.5452v1, 2014-02-21. https://arxiv.org/abs/1402.5452
4. *Universal radial coverage by concentric regular-polygon unions*, publicly available mathematical result, identifier 4705952c9b28.
5. *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*, publicly available mathematical result, identifier 1c25b18e16e8.
