# Sharp CAT(1) geometry of quasihyperbolic complements of compact convex sets

## Finding

For every integer \(n\ge3\) and every nonempty compact convex set \(C\subset\mathbb R^n\), the complement \(\Omega=\mathbb R^n\setminus C\), with length metric
\[
k_C(x,y)=\inf_{\gamma:x\leadsto y}\int_\gamma\frac{|dz|}{\operatorname{dist}(z,C)},
\]
is a complete, proper, globally \(\mathrm{CAT}(1)\) geodesic space. The curvature ceiling \(1\) is sharp uniformly over the class, even over smooth bodies with strictly positive principal curvatures. For these smooth bodies the log obstacle distance is concave along every quasihyperbolic geodesic, with the exact second-derivative identity below.

## Assumptions and scope

The class includes a singleton or a lower-dimensional compact convex set. Global \(\mathrm{CAT}(1)\) includes comparison for all geodesic triangles of perimeter less than \(2\pi\). The identity for geodesic log distance is asserted for a full-dimensional \(C^\infty\) convex body whose outward principal curvatures \(\kappa_i\) are everywhere positive. Write \(t(x)=\operatorname{dist}(x,C)\); in the smooth setting write \(x=p+t\nu\) for the nearest point \(p\in\partial C\) and its outward normal \(\nu\). No upper bound smaller than \(1\) is valid uniformly; the bound need not be attained at a finite point.

## Proof

**1. Local smooth curvature.** The nearest-point normal parametrization is global outside a smooth convex obstacle. In the normal direction the Euclidean Hessian of \(t\) vanishes, and in the transported principal directions \(E_i\) its eigenvalues are \(\kappa_i/(1+t\kappa_i)\), by differentiating the exterior normal map. For Euclidean orthonormal vectors \(e_1,e_2\) spanning a plane \(\Pi\), the conformal sectional curvature of \(g=t^{-2}g_{\mathrm{Eucl}}\) is
\[
\operatorname{Sec}_g(\Pi)=t\bigl(\nabla^2t(e_1,e_1)+\nabla^2t(e_2,e_2)\bigr)-1.
\]
Indeed the conformal formula with conformal exponent \(-\log t\) cancels the plane components of \(dt\) and leaves \(-|\nabla t|^2=-1\). Each eigenvalue of \(t\nabla^2t\) is in \([0,1)\), so \(-1\le\operatorname{Sec}_g<1\). The smooth exterior is locally \(\mathrm{CAT}(1)\).

**2. Properness, completeness and geodesics.** This step does not require smoothness. The complement is path connected: rays from a fixed point in \(C\) through exterior points stay exterior beyond those points and can be joined by an arc on a large sphere. The distance function is Euclidean 1-Lipschitz. Along a path from \(o\) parametrized by quasihyperbolic arclength \(s\), it follows that \(|\log(t(\gamma(s))/t(o))|\le s\) and \(|\gamma'(s)|=t(\gamma(s))\le t(o)e^s\) almost everywhere. Thus a path of length \(L\) stays within Euclidean distance \(t(o)(e^L-1)\) of \(o\) and at distance at least \(t(o)e^{-L}\) from \(C\). Using paths whose length approaches the metric distance gives the corresponding bounds for the closed metric balls. The local Euclidean and quasihyperbolic topologies agree, from short Euclidean segments away from \(C\) and the same displacement estimate. The closed balls are therefore compact. This proper length space is complete and geodesic.

**3. Exact smooth geodesic identity.** For a unit-speed \(g\)-geodesic let \(v=\gamma'\), so \(|v|=t\) in Euclidean norm. The conformal geodesic equation reads \(\gamma''=2(t'/t)v-t\nu\). Hence, along the geodesic,
\[
\begin{aligned}
(\log t)'' &=t^{-1}\nabla^2t(v,v)+(t'/t)^2-1\\
 &=-\sum_{i=1}^{n-1}\frac{\langle v,E_i\rangle^2}{t^2(1+t\kappa_i)}\le0.
\end{aligned}
\]
In particular \(t(\gamma(s))\ge t(\gamma(0))^{1-s/L}t(\gamma(L))^{s/L}\) for \(0\le s\le L\), \(L>0\). A closed local geodesic would make \(\log t\) periodic and constant. The identity forces the tangential velocity to vanish and \(t'=0\) forces the normal velocity to vanish, contradicting unit speed.

**4. Global smooth comparison via an explicit short-loop contraction.** The inverse Gauss map \(p(\omega)\), \(\omega\in\mathbb S^{n-1}\), is smooth; identify the tangent spaces perpendicular to \(\omega\) in Euclidean space. Its differential \(B_\omega\) is positive definite and self-adjoint, with the principal radii \(1/\kappa_i\) as eigenvalues. In coordinates \((\omega,t)\mapsto p(\omega)+t\omega\) the metric is
\[
g=d(\log t)^2+\bigl|(I+B_\omega/t)d\omega\bigr|^2.
\]
In particular the spherical projection has speed no greater than the quasihyperbolic speed. The map \((\omega,t)\mapsto(\omega,\max(t,T))\) does not increase path lengths: in the log coordinate it cuts off downward excursions without increasing radial speed, and whenever height increases each positive eigenvalue of \(I+B_\omega/t\) decreases. This applies almost everywhere to arclength-parametrized rectifiable paths. A loop can be homotoped through these maps up to a level \(T\) larger than its greatest height, starting with a cutoff below its smallest height. This is a continuous homotopy through loops of no greater length.

Consider a loop of quasihyperbolic length \(L<2\pi\) whose spherical projection has round length \(\ell\). If \(\ell=0\), the level loop is constant. Otherwise the spherical projection stays in an open hemisphere: select two points \(a,b\) separated by half the projected arclength. For any point \(x\) on either projected subarc, \(d_{\mathbb S}(a,x)+d_{\mathbb S}(b,x)\le\ell/2<\pi\). Consequently \(x\cdot(a+b)>0\), by the cosine sum identity; also \(a+b\ne0\). In that hemisphere the homotopy that multiplies radial distance from the unit center \((a+b)/|a+b|\) by a factor in \([0,1]\) is round length nonincreasing. In polar coordinates this follows from \(dr^2+\sin^2r\,d\xi^2\) for \(r<\pi/2\), including the center by continuity.

On the level \(T\), a curve of round length at most \(\ell\) has quasihyperbolic length at most \((1+M/T)\ell\), where \(M=\sup_\omega\|B_\omega\|<\infty\). For \(\ell>0\) one has \(\ell<L\): on the compact initial loop the height is bounded above and the least eigenvalue of \(B_\omega\) is bounded away from zero, so the speed inequality integrated on the projected curve is uniformly strict in ratio. Choose \(T\) large enough that \((1+M/T)\ell\le L\). Lift the spherical contraction to this level. Every loop of length less than \(2\pi\) has thus been deformed to a constant through loops of length less than \(2\pi\); the constant loops also lie in one component. Bowditch’s short-loop criterion applies to this complete, locally compact, locally \(\mathrm{CAT}(1)\) space and proves global \(\mathrm{CAT}(1)\).

**5. Arbitrary compact convex obstacles.** Take outer approximants \(C\subset C_j\subset C+\epsilon_j\mathbb B_2^n\), \(\epsilon_j\to0\), smooth with strictly positive principal curvatures. For example, average the support function of \(C\) with a smooth approximate identity of rotations. The smoothed support functions are smooth and converge uniformly on the sphere, and their spherical Hessian plus the function times the identity is positive semidefinite. Adding positive constants tending to zero and at least as large as the errors of uniform approximation gives support functions of the required outer approximants with positive definite spherical Hessian-plus-function tensors. This also treats lower-dimensional \(C\).

Write \(t_j=\operatorname{dist}(\cdot,C_j)\); then \(0\le t-t_j\le\epsilon_j\). Every compact path trace in \(\Omega\) stays a positive distance from \(C\), so it eventually lies in each approximating exterior and its weighted length converges. Conversely, \(k_j\ge k_C\) on the approximating exterior. Using a fixed near-minimizing path for the upper bound gives \(k_j(x,y)\to k_C(x,y)\) for fixed exterior points. On any compact subset of \(\Omega\) short Euclidean segments between nearby endpoints stay uniformly away from \(C_j\) for all large \(j\), making the distance functions uniformly equicontinuous in both endpoints. Thus convergence is uniform on compact subsets of \(\Omega\) in both variables. For a fixed exterior basepoint and radius \(R>0\), all the approximating closed balls of radius \(R\) lie in the compact limit ball, since \(k_j\ge k_C\). Every point in the limit ball can be moved by at most any prescribed \(\delta\in(0,R)\) toward the basepoint along a limit geodesic to radius at most \(R-\delta\). Such points lie in the approximating ball for large \(j\), uniformly by compact convergence. This gives pointed Gromov–Hausdorff convergence. Stability of \(\mathrm{CAT}(1)\) under this convergence gives the global assertion also for \(C\).

**6. Sharpness.** For \(C=a\mathbb B_2^n\), \(a>0\), a two-plane tangent to a distance level exists since \(n\ge3\), and has curvature \(2t/(a+t)-1=(t-a)/(t+a)\to1\) as \(t\to\infty\). A smooth Riemannian \(\mathrm{CAT}(\kappa)\) space has sectional curvatures at most \(\kappa\). No smaller ceiling works uniformly even for smooth strictly positively curved obstacles. The tangent-plane asymptotic is also valid along a fixed normal ray of any such body, by the two principal eigenvalues in Step 1.

## Verification

The auxiliary script `verification/check.py` checks finitely many exact-rational instances of the principal curvature, log-Hessian and round-ball formulas. The proof of global comparison uses the short-loop contraction and the limit argument, not computation. The example of the round ball verifies sharpness analytically for all \(n\ge3\).

## Relationship to prior work and limitations

Ikonen–Pandey give the weaker global upper bound \(\mathrm{CAT}(2)\) for general quasihyperbolic domains, and the lower bound \(\mathrm{CBB}(-1)\) for convex complements. Their point-complement example is already globally \(\mathrm{CAT}(1)\). The result here treats the entire nonempty compact convex obstacle class at the sharp upper bound. Bowditch supplies the general globalization criterion; the contraction through high distance levels verifies that criterion for this class without a compactness assumption on the space of free loops. No extension to unbounded obstacles, pointwise log-Hessian identity at nonsmooth obstacles, or uniqueness of all long geodesics is asserted. Historical priority is not claimed exhaustively.

## References

1. T. Ikonen and A. Pandey, *Quasihyperbolic domains are CAT(2)*, arXiv:2609.24610v1, especially Theorems 1.1 and 1.6–1.8. https://arxiv.org/html/2609.24610
2. B. H. Bowditch, *Notes on locally CAT(1) spaces*, in *Geometric Group Theory*, de Gruyter (1995), pp. 1–48. https://bhbowditch.com/abstracts/lco.html
3. M. Bridson and A. Haefliger, *Metric Spaces of Non-Positive Curvature*, Springer (1999), Chapter II, curvature comparison and limit stability.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, expanded second ed., Cambridge University Press (2014), support functions and smooth approximation.
