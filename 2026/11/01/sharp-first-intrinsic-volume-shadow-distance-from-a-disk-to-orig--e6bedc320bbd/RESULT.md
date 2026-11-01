# Sharp first intrinsic-volume shadow distance from a disk to origin-containing polygons

## Finding
For every integer \(N\ge3\), write \(B\subset\mathbb R^2\) for the closed Euclidean unit disk. Among **all full-dimensional convex polygons** \(P\subset\mathbb R^2\) with \(0\in P\) and at most \(N\) vertices, the first intrinsic-volume shadow metric of Besau and Hoehner has the exact minimum
\[
\boxed{\inf_P\delta_1(B,P)=F_N:=\pi-2N\arcsin\left(\tfrac12\sin\tfrac\pi N\right).}
\]
This minimum is attained **exactly** by rotations about the origin of the regular \(N\)-gon with circumradius
\[
\boxed{R_N=\left(1-\tfrac14\sin^2(\pi/N)\right)^{-1/2}.}
\]
Neither inscribing the polygon in the disk nor circumscribing it about the disk is optimal. The sharp expansion is
\[
F_N=\frac{\pi^3}{8N^2}+\frac{\pi^5}{128N^4}+O(N^{-6}).
\]

## Assumptions and scope
The polygon is compact, full dimensional, convex, contains the disk center, and has at most \(N\) vertices. No central symmetry, perimeter constraint, or regularity is assumed. Put \(u_\theta=(\cos\theta,\sin\theta)\) and \(h_P(u)=\max_{x\in P}\langle x,u\rangle\). Define the metric, using normalized Haar measure on the unoriented line Grassmannian, by
\[
\delta_1(B,P)=\frac\pi2\int_{\operatorname{Gr}(2,1)}\operatorname{length}((B\mid L)\triangle(P\mid L))\,d\nu(L).
\]
Since both projected intervals contain the origin, their symmetric-difference length is the sum of absolute endpoint discrepancies. Thus, for this domain, **with the displayed normalization**, 
\[
\boxed{\delta_1(B,P)=\frac12\int_0^{2\pi}|1-h_P(u_\theta)|\,d\theta.} \tag{1}
\]
The restriction \(0\in P\) is essential to this reduction: no theorem for disjoint projected intervals or arbitrary-position polygons is claimed.

## Proof
**1. Local normal-cone inequality.** Number the \(m\) vertices of \(P\) counterclockwise, where \(3\le m\le N\). Each exposed-vertex normal cone intersects the unit normal circle in an interval \(I_i\) of positive angular length \(\alpha_i\in(0,\pi)\), and
\[\sum_{i=1}^m\alpha_i=2\pi.\]
Choose the midpoint of each cone as angular origin. On \(-\alpha_i/2\le x\le\alpha_i/2\), the support function equals \(a_i\cos x+b_i\sin x\) with real coefficients \(a_i,b_i\). For any \(0<\alpha<\pi\), set
\[
t(\alpha)=\arcsin\left(\tfrac12\sin(\alpha/2)\right),\qquad
s_\alpha(x)=\begin{cases}+1,&|x|<t(\alpha),\\-1,&t(\alpha)<|x|\le\alpha/2.\end{cases}
\]
Direct integration gives
\[
\int_{-\alpha/2}^{\alpha/2}s_\alpha(x)\cos x\,dx=4\sin t-2\sin(\alpha/2)=0,
\quad\int_{-\alpha/2}^{\alpha/2}s_\alpha(x)\sin x\,dx=0.
\]
Use \(|z|\ge-s_\alpha(x)z\) with \(z=1-a\cos x-b\sin x\). The trigonometric terms cancel, leaving
\[
\int_{-\alpha/2}^{\alpha/2}|1-a\cos x-b\sin x|\,dx
\ge\alpha-4\arcsin\left(\tfrac12\sin(\alpha/2)\right)=:g(\alpha).\tag{2}
\]
Equality implies the continuous function \(1-a\cos x-b\sin x\) has a zero at each sign-switch point \(x=\pm t\). Subtracting yields \(b=0\), and then \(a=\sec t\). Conversely this cosine profile has precisely the required sign pattern, so equality holds. Thus (2) has a unique pair of optimizing local coefficients for every \(\alpha\).

**2. Strict convexity and vertex count.** Elementary differentiation yields, for \(0<\alpha<\pi\),
\[
g''(\alpha)=\frac{3\sin(\alpha/2)}{8\left(1-\frac14\sin^2(\alpha/2)\right)^{3/2}}>0.\tag{3}
\]
With \(g(0)=0\), strict convexity implies that \(g(x)/x\) increases strictly on \(0<x<\pi\). Combining (1), (2), and Jensen's inequality gives
\[
2\delta_1(B,P)\ge\sum_{i=1}^m g(\alpha_i)
\ge m g(2\pi/m)\ge N g(2\pi/N).\tag{4}
\]
The last inequality is strict unless \(m=N\). Since \(m\ge3\), all relevant equal-gap arguments lie in \((0,\pi)\). The terminal expression is
\[\frac N2 g(2\pi/N)=\pi-2N\arcsin\left(\frac12\sin\frac\pi N\right)=F_N.\]

**3. Equality classification.** If equality holds throughout (4), there must be exactly \(N\) vertices and every normal-cone angle equals \(2\pi/N\). Equality in every local inequality forces each vertex to lie on its cone-midpoint ray at distance
\[
\sec t(2\pi/N)=\left(1-\tfrac14\sin^2(\pi/N)\right)^{-1/2}=R_N.
\]
The successive midpoint normal directions differ by \(2\pi/N\); therefore these are exactly the vertices of a centered regular \(N\)-gon. Conversely a centered regular \(N\)-gon at radius \(R_N\) has the prescribed equal normal-cone cells and realizes local equality, so it realizes the global minimum. This excludes translated, irregular, and fewer-vertex equality cases.

**4. Asymptotic expansion.** Taylor expansion at zero of \(\sin\) followed by \(\arcsin\) in the exact closed form gives
\[
F_N=\frac{\pi^3}{8N^2}+\frac{\pi^5}{128N^4}-\frac{17\pi^7}{15360N^6}+O(N^{-8}),
\]
which implies the claimed expansion.

## Verification
The standalone standard-library script `verify_shadow_polygon.py` evaluates the closed form by independently integrating signed cosine-support cells and by angular quadrature, tests the local dual inequalities on randomized coefficients, and compares against irregular origin-containing polygons. On execution it reported `PASS: 5376 checks`; examples include \(F_3\approx0.454598272016\), \(F_4\approx0.250655662336\), and \(N^2F_N\to\pi^3/8\approx3.875784585037\). The analytic inequalities (2)–(4), not the finite tests, prove the all-integer result. Reproduce using `python3 verify_shadow_polygon.py` with Python 3 and no external dependencies.

## Relationship to prior work
Besau and Hoehner introduced the projection-based intrinsic-volume metric and established broad asymptotic approximation bounds [2]. Hoehner's recent survey [1], first public on 2025-12-02, emphasizes sharp constants for polytopal projection approximation and motivates a finite-vertex planar benchmark. Besau, Hoehner and Kur [3] studied a different intrinsic-volume deviation and included an explicit regular-triangle calculation; that previously known special case is credited and is consistent with \(F_3\) after accounting for normalization. None of the inspected statements in [1]–[3] provides the asserted exact **all-vertex-count lower bound over all origin-containing polygons**, including uniqueness and scale. Classical planar approximation theory may contain an equivalent result under a different metric name; historical priority is not independently established.

## Limitations
The disk center is required to belong to the polygon. The theorem does not classify arbitrary-position polygons, higher-dimensional polytopes, other intrinsic-volume indices, or every possible form of projection loss. The historical-priority assessment is provisional and not an independent audit; earlier polygonal approximation work of Fejes Tóth and McClure–Vitale is a residual priority risk.

## References
[1] Steven Hoehner, *From Circles to Convex Bodies: Approximating Curved Shapes by Polytopes*, arXiv:2512.02379 (first posted 2025-12-02), https://arxiv.org/abs/2512.02379.

[2] Florian Besau and Steven Hoehner, *An intrinsic volume metric for the class of convex bodies in R^n*, arXiv:2208.13927 (first posted 2022-08-29), https://arxiv.org/abs/2208.13927.

[3] Florian Besau, Steven Hoehner and Gil Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, arXiv:1905.08862 (first posted 2019-05-21), https://arxiv.org/abs/1905.08862.

[4] Monika Ludwig, *Asymptotic approximation of smooth convex bodies by general polytopes*, Mathematika 46 (1999), 103–125. (Related historical asymptotic context; not used as an exact theorem.)
