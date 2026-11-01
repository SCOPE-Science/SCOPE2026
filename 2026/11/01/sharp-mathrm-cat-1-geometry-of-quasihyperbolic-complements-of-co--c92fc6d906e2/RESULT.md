# Sharp \(\mathrm{CAT}(1)\) geometry of quasihyperbolic complements of compact convex sets

## Finding

**Theorem.** For every integer \(n\ge3\) and every nonempty compact convex set \(C\subset\mathbb R^n\), equip \(\Omega=\mathbb R^n\setminus C\) with the quasihyperbolic length metric
\[
k_C(x,y)=\inf_{\gamma:x\leadsto y}\int_\gamma\frac{|dz|}{\operatorname{dist}(z,C)}.
\]
Then \((\Omega,k_C)\) is a complete, proper, globally \(\mathrm{CAT}(1)\) geodesic space. No smoothness, interior, or strict-convexity hypothesis on \(C\) is required.

The value \(1\) is the **sharp uniform curvature ceiling**, even among \(C^\infty\) strictly uniformly convex bodies. For these smooth bodies, logarithmic Euclidean obstacle distance is concave along every unit-speed quasihyperbolic geodesic; in fact it satisfies the explicit exact Hessian-deficit identity in Step 3 below.

## Assumptions and scope

A compact convex set is nonempty and bounded, and may be a singleton or have empty interior. The dimension restriction \(n\ge3\) places the result in the higher-dimensional setting of the motivating work. The \(\mathrm{CAT}(1)\) assertion is **global**, including existence and comparison for all geodesic triangles of perimeter less than \(2\pi\). Sharpness means that the class is not uniformly \(\mathrm{CAT}(\kappa)\) for any \(\kappa<1\); it does not assert that each obstacle has a sectional curvature maximum actually attained at a finite point.

For the differential statements assume first that \(C\) is a full-dimensional \(C^\infty\) convex body with strictly positive principal curvatures (all outward principal curvatures \(\kappa_i>0\)). Write \(t(x)=\operatorname{dist}(x,C)\), \(p(x)\) for the unique nearest boundary point, and \(\nu(x)\) for the outward unit normal at \(p(x)\). A tangent principal direction at \(p(x)\), transported along the normal ray, is denoted \(E_i(x)\).

## Proof

**Step 1: curvature calculation.** Outside a smooth strictly convex body, normal coordinates \(x=p+t\nu(p)\) are globally defined for \(t>0\). The Euclidean Hessian of the distance has eigenvalues
\[
\nabla^2t(\nu,\nu)=0,\qquad
\nabla^2t(E_i,E_i)=\frac{\kappa_i}{1+t\kappa_i}.
\]
For the conformal Riemannian metric \(g=t^{-2}g_{\mathrm{Eucl}}\), if \(e_1,e_2\) form a Euclidean-orthonormal basis of a two-plane \(\Pi\), the conformal sectional-curvature formula simplifies, using \(|\nabla t|=1\), to
\[
\operatorname{Sec}_g(\Pi)
=t\bigl(\nabla^2t(e_1,e_1)+\nabla^2t(e_2,e_2)\bigr)-1.
\]
Every eigenvalue of \(t\nabla^2t\) lies in \([0,1)\), so \(-1\le\operatorname{Sec}_g(\Pi)<1\). In particular the smooth complement is *locally* \(\mathrm{CAT}(1)\). This alone would not establish the global property.

**Step 2: completeness and properness.** Along a path of quasihyperbolic length \(L\), the distance-to-obstacle function is \(1\)-Lipschitz in the Euclidean metric, hence
\[
|\log t(y)-\log t(x)|\le L.
\]
If such a path starts at a fixed point \(o\) and is parametrized by quasihyperbolic arclength, \(|\gamma'(s)|=t(\gamma(s))\le t(o)e^s\). Consequently its Euclidean trace lies within radius \(t(o)(e^L-1)\) of \(o\) and is at Euclidean distance at least \(t(o)e^{-L}\) from \(C\). Closed bounded quasihyperbolic balls are therefore Euclidean compact subsets of \(\Omega\), and the quasihyperbolic metric is locally equivalent to the Euclidean metric on them. This proves properness and completeness by the standard Hopf–Rinow argument for length spaces.

**Step 3: geodesic log-distance concavity and no closed geodesic.** Let \(\gamma(s)\) be a unit-speed \(g\)-geodesic, let \(v=\gamma'(s)\) be its Euclidean velocity, and put \(t=t(\gamma(s))\). Thus \(|v|=t\). Differentiating the conformal geodesic equation gives
\[
\gamma''=2\frac{t'}{t}\gamma'-t\nu.
\]
Define \(h=\log t\). Differentiating again and using the Hessian eigenvalues from Step 1 yields the **exact** identity
\[
\begin{aligned}
h''&=\frac{\nabla^2t(v,v)}{t}+\frac{(t')^2}{t^2}-1\\
&=-\sum_{i=1}^{n-1}
\frac{\langle v,E_i\rangle^2}{t^2(1+t\kappa_i)}\le0.
\end{aligned}
\]
Hence for every geodesic segment of length \(L\) and \(0\le s\le L\),
\[
t(\gamma(s))\ge t(\gamma(0))^{1-s/L}t(\gamma(L))^{s/L}.
\]
If a nonconstant closed local geodesic existed, its periodic twice-differentiable function \(h\) would be concave and thus constant. The exact identity would force all tangential components of \(v\) to vanish, while \(h'=0\) forces its normal component to vanish. This contradicts \(|v|=t>0\). **There are no nonconstant closed local geodesics of any length.**

**Step 4: global comparison for smooth bodies.** In a complete, locally compact, locally \(\mathrm{CAT}(1)\) space, the short-loop/Birkhoff globalization theorem shows that any nontrivial connected component of rectifiable loops of length less than \(2\pi\) has a nonconstant closed local geodesic with length less than \(2\pi\). Indeed minimizing length by Birkhoff shortening within a noncontractible short-loop component, with properness preventing escape on a bounded-length family, produces such a local geodesic. Since Step 3 excludes **every** closed local geodesic, each loop of length less than \(2\pi\) deforms through loops of no greater length to a constant. Therefore the short-loop space is connected, and Bowditch's \(\mathrm{CAT}(1)\) globalization criterion applies. This establishes the smooth case without assuming global comparison from sectional curvature alone.

**Step 5: passage to arbitrary compact convex sets.** Choose smooth strictly positively curved convex bodies \(C_j\) with
\[
C\subset C_j\subset C+\varepsilon_j\mathbb B_2^n,
\qquad\varepsilon_j\downarrow0.
\]
Such outer approximations exist by standard regularization of convex support functions followed by a sufficiently small strictly convex rounding; the construction also covers lower-dimensional \(C\). Put \(\Omega_j=\mathbb R^n\setminus C_j\), \(t_j(x)=\operatorname{dist}(x,C_j)\). Their distance functions obey \(|t_j-t|\le\varepsilon_j\) everywhere. For any fixed \(x,y\in\Omega\), eventually \(x,y\in\Omega_j\). Because \(t_j\le t\) and the domain of admissible paths is smaller, \(k_j(x,y)\ge k_C(x,y)\). Conversely, any fixed path from \(x\) to \(y\) in \(\Omega\) has compact trace and positive minimum obstacle distance, hence eventually lies in \(\Omega_j\); its \(1/t_j\) length converges to its \(1/t\) length. Taking near-minimizing paths yields
\[
k_j(x,y)\longrightarrow k_C(x,y).
\]
On each compact subset of \(\Omega\), local distance comparison yields equicontinuity in both endpoints, so the convergence is locally uniform. For a fixed basepoint, the exponential distance-to-boundary and Euclidean displacement bounds of Step 2 are uniform over \(j\) sufficiently large; consequently every bounded \(k_j\)-ball is trapped in a common compact subset of \(\Omega\). These facts yield pointed Gromov–Hausdorff convergence of the proper spaces \((\Omega_j,k_j,o)\) to \((\Omega,k_C,o)\). The standard closure of \(\mathrm{CAT}(1)\) under pointed Gromov–Hausdorff limits now proves that the full nonsmooth complement is globally \(\mathrm{CAT}(1)\).

**Step 6: sharpness.** For the round ball \(C=a\mathbb B_2^n\) with \(a>0\), both principal curvatures of any tangent two-plane equal \(1/a\). At a point of Euclidean obstacle distance \(t>0\),
\[
\operatorname{Sec}_g(\Pi_{\mathrm{tan}})
=\frac{2t}{a+t}-1=\frac{t-a}{t+a}\xrightarrow[t\to\infty]{}1.
\]
This tangent plane exists since \(n\ge3\). The same asymptotics hold for any smooth strictly positively curved compact obstacle, since \(t\kappa_i/(1+t\kappa_i)\to1\). A smooth Riemannian \(\mathrm{CAT}(\kappa)\) space must have sectional curvatures at most \(\kappa\); hence no uniform constant less than \(1\) is possible. \(\square\)

## Verification

The standalone script `verification/check.py` performs exact-rational tests of the principal-plane curvature formulas, the logarithmic-distance second-derivative identity, and the round-ball sharpness family. Run it with `python3 verification/check.py` from the package root. It checks **510** assertions. Those finite tests do not verify global \(\mathrm{CAT}(1)\), the Birkhoff criterion, or the pointed convergence argument; those parts are justified by the analytic proof and cited metric-geometry theorems.

## Relationship to prior work

Ikonen and Pandey (2026) establish global \(\mathrm{CAT}(2)\) for **all** quasihyperbolic domains in dimensions at least three, and the distinct \(\mathrm{CBB}(-1)\) lower-curvature property for domains with convex complement. Neither implies a global upper bound of \(1\) for convex complements. They also give \(\mathrm{CAT}(0)\) for *convex domains*, an opposite inclusion hypothesis that does not apply here. Their special point-complement example is already known to be \(\mathrm{CAT}(1)\); the present class result extends to any compact convex obstacle and proves the sharp global upper bound, including nonsmooth and lower-dimensional cases. Herron–Martin study planar universal-cover properties, and Hästö studies planar curvature and isometries. Bowditch's 1995 result supplies the general short-loop globalization tool, rather than this quasihyperbolic application. The convex-distance Hessian formula and standard pointed-limit stability are treated as classical inputs, not new theorems.

## Limitations

Compactness of the obstacle is an assumption essential to the formulation proved here; no extension to unbounded convex sets is asserted. The explicit geodesic second-derivative identity is asserted only for smooth uniformly convex bodies, not for nonsmooth obstacles where it need not hold pointwise. The \(\mathrm{CAT}(1)\) statement does not imply global uniqueness of arbitrarily long minimizing geodesics. Historical-priority searches were nonexhaustive, and equivalent results could exist in unindexed work.

## References

1. T. Ikonen and A. Pandey, *Quasihyperbolic domains are CAT(2)*, arXiv:2609.24610v1, first public 2026-09-21; §§1,3,5,7. https://arxiv.org/html/2609.24610
2. B. H. Bowditch, *Notes on locally CAT(1) spaces*, in *Geometric Group Theory*, de Gruyter (1995), pp. 1–48. https://bhbowditch.com/abstracts/lco.html
3. D. Herron and G. Martin, *Quasihyperbolic Metric Universal Covers*, arXiv:2007.00782. https://arxiv.org/abs/2007.00782
4. P. Hästö, *Isometries of the quasihyperbolic metric* (2006), §3. https://www.problemsolving.fi/pp/p50v02.pdf
5. M. Bridson and A. Haefliger, *Metric Spaces of Non-Positive Curvature*, Springer (1999), Chapter II, curvature comparison and GH stability; cited via Ikonen–Pandey, §3.
