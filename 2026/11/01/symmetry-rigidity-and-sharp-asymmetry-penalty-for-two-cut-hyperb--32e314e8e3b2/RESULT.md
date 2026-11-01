# Symmetry rigidity and sharp asymmetry penalty for two-cut hyperbolic balls near the Santaló transition

## Finding

For each real \(C>10/(9\pi)\), there is a number \(\delta_C>0\) such that the following holds. Among **all** truncated balls described below with fixed hyperbolic boundary area \(S=2\pi+\delta\), \(0<\delta<\delta_C\), and independently varying squared cut angles \(0\le u_1,u_2\le C\delta\), there is exactly one minimizer of total mean curvature (up to interchanging the two caps). It has equal positive cut angles:
\[
u_1=u_2=u_*(\delta)=\frac{10}{9\pi}\delta+O_C(\delta^2).
\]
Its total mean curvature relative to the equal-area geodesic sphere satisfies
\[
M_{2\mathrm{cut}}(S)-M_{\mathrm{sphere}}(S)
=-\frac{25\sqrt3}{1458\pi^2}\delta^3+O_C(\delta^4).
\]
Allowing only one active cap yields instead the sharp optimum
\[
M_{1\mathrm{cut}}(S)-M_{\mathrm{sphere}}(S)
=-\frac{25\sqrt3}{2916\pi^2}\delta^3+O_C(\delta^4).
\]
Hence activating two cuts doubles the leading improvement, while making them unequal necessarily costs curvature. More precisely, for each sufficiently small fixed \(\eta>0\), uniformly for \(|h|\le\eta\delta\) and admissible \(u_*\pm h\),
\[
M(S,u_*+h,u_*-h)-M_{2\mathrm{cut}}(S)
=\left(\frac{\sqrt3}{24}\delta+O_C(\delta^2)\right)h^2.
\]
The coefficient \(\sqrt3/24\) is sharp and is the exact leading second variation in the previously unexamined antisymmetric direction.

## Assumptions and scope

Work in hyperbolic three-space of constant sectional curvature \(-1\). In its Beltrami–Klein ball model, a geodesic ball of hyperbolic radius \(r>0\), centered at the model origin, is the Euclidean ball of radius \(\tanh r\). Let \(a,b\in[0,\pi/2)\). Cut it by the two totally geodesic planes of Klein heights \(z=\tanh r\cos a\) and \(z=-\tanh r\cos b\), and retain the central intersection. This is a convex body with one remaining curved spherical zone and two geodesic planar disks, one or both disks possibly degenerate. Count both circular-edge singular curvature measures in the total mean curvature \(M\); define mean curvature as the trace, not half the trace, of the shape operator, in the same normalization as the cited source.

Put \(u_1=a^2\), \(u_2=b^2\), \(v=\sinh^2 r\). After prescribing the area \(S=2\pi+\delta\), the radius \(r\) is determined uniquely and analytically for sufficiently small \(\delta,u_1,u_2\). We minimize over the **full** square \(0\le u_1,u_2\le C\delta\), not just its diagonal or an arbitrary selection of trial values. The bound \(C>10/(9\pi)\) is fixed before taking \(\delta\downarrow0\).

## Proof

**1. Exact independent-cap formulas.** Define
\[
\begin{aligned}
 A(v,\theta)&=v(\cos\theta-1)+\sqrt{1+v\sin^2\theta}-1,\\
 B(v,\theta)&=2\sqrt{v(v+1)}(\cos\theta-1)
 +\sqrt v\sin\theta\arctan(\sqrt{v+1}\tan\theta).
\end{aligned}
\]
Subtracting the two disjoint lost spherical caps and adding each planar disk gives the exact area; adding independently the circular-edge and surviving-sphere curvature gives the exact mean curvature:
\[
\begin{aligned}
 S&=4\pi v+2\pi\bigl(A(v,a)+A(v,b)\bigr),\\
 M&=8\pi\sqrt{v(v+1)}+2\pi\bigl(B(v,a)+B(v,b)\bigr).
\end{aligned}
\]
When \(a=b=\alpha\), these identities agree term-by-term with Fang Hong's formulas (4.1)–(4.2). Thus there is no uncounted edge, and the two individual cut contributions are independent as long as the two planes remain on opposite sides of the center.

**2. Shape expansions and area constraint.** Each cap function is an analytic function of \(u=\theta^2\) near zero. Direct Taylor expansion gives, uniformly for \(v\) in a compact neighborhood of \(1/2\),
\[
\begin{aligned}
 A(v,\sqrt u)&=-\frac{v(v+1)}8u^2
 +\frac{v(v+1)(3v+1)}{48}u^3+O(u^4),\\
 B(v,\sqrt u)&=-\frac{\sqrt{v(v+1)}(4v+1)}{12}u^2
 +\frac{\sqrt{v(v+1)}(36v^2+22v+1)}{180}u^3+O(u^4).
\end{aligned}
\]
Set \(t=S/(4\pi)\). Since the area equation has derivative \(1\) in \(v\) at \(u_1=u_2=0\), the analytic implicit-function theorem gives
\[
v=t-\frac12\sum_{i=1}^{2} A(t,\sqrt{u_i})+O((u_1+u_2)^4).
\]
The same substitution into the mean-curvature identity, including the required first-order response of the sphere term to the area-restoring radius, gives
\[
\begin{aligned}
M(S,u_1,u_2)-M_{\mathrm{sphere}}(S)
=2\pi\sqrt{t(1+t)}\sum_{i=1}^{2}\biggl[
&\frac{1-2t}{24}u_i^2\\
+&\frac{54t^2+13t-11}{720}u_i^3\biggr]
+O((u_1+u_2)^4).
\end{aligned}
\]
Here \(M_{\mathrm{sphere}}(S)=8\pi\sqrt{t(1+t)}\). The remainder is analytic and has uniform derivatives of the required orders for \(t\) near \(1/2\). The leading sum contains **no mixed** monomial of degree at most three because interaction through the area-restoring radius begins at total degree four.

**3. Two-dimensional minimization.** Write \(\delta=S-2\pi>0\), so \(t=1/2+\delta/(4\pi)\), and rescale \(u_i=\delta x_i\). On every fixed compact nonnegative \(x\)-rectangle we obtain convergence, uniformly together with first and second derivatives,
\[
\delta^{-3}\bigl(M(S,\delta x_1,\delta x_2)-M_{\mathrm{sphere}}(S)\bigr)
=F(x_1)+F(x_2)+O_C(\delta),
\]
where
\[
F(x)=-\frac{\sqrt3}{48}x^2+\frac{\pi\sqrt3}{80}x^3.
\]
For \(x\ge0\), the cubic has a unique global minimum at \(x_*=10/(9\pi)\), because \(F'(x)\) changes from negative to positive there, and
\[
F(x_*)=-\frac{25\sqrt3}{2916\pi^2},
\qquad F''(x_*)=\frac{\sqrt3}{24}>0.
\]
Since \(C>x_*\), uniform convergence confines every global minimum on the compact square \([0,C]^2\) to any prescribed neighborhood of \((x_*,x_*)\). There the Hessian is uniformly positive definite; hence the objective is strictly convex, and the implicit-function theorem gives precisely one critical point. Interchanging the cap variables preserves the objective, so uniqueness forces \(x_1=x_2\). Analytic dependence gives \(x_i=x_*+O_C(\delta)\). Evaluating the expansion yields the two-cut optimum. Restricting the same argument to \(x_2=0\) gives the one-cut optimum; its leading negative coefficient is half the two-cut one.

**4. Sharp transverse cost.** At the exact symmetric optimizer, write \(u_1=u_*+h\), \(u_2=u_*-h\). The objective is even in \(h\), and its first derivative vanishes. The scaled second-derivative convergence yields
\[
\frac12\frac{d^2}{dh^2}M(S,u_*+h,u_*-h)\bigg|_{h=0}
=\delta F''(x_*)+O_C(\delta^2)
=\frac{\sqrt3}{24}\delta+O_C(\delta^2).
\]
The analytic even Taylor remainder is \(O(h^4)\) with bounded coefficient on the shrinking square. Since \(h=O(\delta)\), this is absorbed into \(O_C(\delta^2 h^2)\). This proves the uniform claimed penalty and its optimal leading coefficient.

## Verification

`checks/verify_two_cap_symbolic.py` starts from the two exact cap functions, expands them symbolically, independently checks the fixed-area quartic and sextic coefficients, and evaluates the onset stationary equation, curvature, and objective value. `checks/verify_asymmetric_drums.py` solves the exact fixed-area equation at 55-digit precision for three positive values of the area excess; it compares both two-cut and one-cut improvements and tests an independent unequal-cut deformation. Both programs execute successfully using the versions of SymPy and mpmath declared in `requirements.txt`.

The numerical tests are finite consistency checks; the uniform minimization, uniqueness, and sharpness statements are analytic consequences of the stated Taylor expansion and strict positivity of its critical Hessian.

## Relationship to prior work

Fang Hong, *On Santaló's Problem*, arXiv:2606.01771, Section 4, provides the two equal-cap formulas for \(\Gamma(r,\alpha)\) and constructs hyperbolic Santaló counterexamples. It treats a common angle \(\alpha\) at both ends; its equations (4.1) and (4.2) do not determine the response to two independent angles. Related analyses of that diagonal symmetric family already determine the critical area and the leading cubic improvement *along the diagonal*. The present result is the two-variable classification: global minimization over every sufficiently small **unequal** pair of cuts, rigidity of equal depths, the sharp transverse anisotropy penalty, and the quantitative one-cut versus two-cut comparison. Those assertions cannot be inferred solely from a critical-point analysis on the diagonal. General hyperbolic Minkowski inequalities with enclosed-volume terms are not fixed-area optimizations over independently truncated balls.

## Limitations

The result is local as \(S\downarrow2\pi\) and covers squared cap angles bounded by a fixed multiple of \(S-2\pi\). It does not prove a global minimum among arbitrary convex bodies, all possible two-cap angles, off-axis cutting planes, or different ambient curvature normalizations. Priority is conditional on the inspected literature: an older explicit treatment of independently unequal caps may remain unindexed. The singular-edge mean-curvature convention is essential.

## References

1. Fang Hong, *On Santaló's Problem*, arXiv:2606.01771v1 (first publicly posted June 1, 2026), revised as v4 October 9, 2026; Section 4, equations (4.1)–(4.2). https://arxiv.org/html/2606.01771v4
2. The original conjecture and the definitions of hyperbolic curvature measures are discussed with references in Section 1 and Section 2 of the same manuscript.
